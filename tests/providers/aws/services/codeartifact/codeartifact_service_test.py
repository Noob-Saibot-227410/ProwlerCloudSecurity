from unittest.mock import patch

import botocore
from moto.core import DEFAULT_ACCOUNT_ID

from prowler.providers.aws.lib.audit_info.audit_info import current_audit_info
from prowler.providers.aws.services.codeartifact.codeartifact_service import (
    CodeArtifact,
    LatestPackageVersionStatus,
    OriginInformationValues,
    RestrictionValues,
)

# Mock Test Region
AWS_REGION = "eu-west-1"

# Mocking Access Analyzer Calls
make_api_call = botocore.client.BaseClient._make_api_call


def mock_make_api_call(self, operation_name, kwarg):
    """We have to mock every AWS API call using Boto3"""
    if operation_name == "ListRepositories":
        return {
            "repositories": [
                {
                    "name": "test-repository",
                    "administratorAccount": DEFAULT_ACCOUNT_ID,
                    "domainName": "test-domain",
                    "domainOwner": DEFAULT_ACCOUNT_ID,
                    "arn": f"arn:aws:codebuild:{AWS_REGION}:{DEFAULT_ACCOUNT_ID}:repository/test-repository",
                    "description": "test description",
                },
            ]
        }
    if operation_name == "ListPackages":
        return {
            "packages": [
                {
                    "format": "pypi",
                    "namespace": "test-namespace",
                    "package": "test-package",
                    "originConfiguration": {
                        "restrictions": {
                            "publish": "ALLOW",
                            "upstream": "ALLOW",
                        }
                    },
                },
            ],
        }

    if operation_name == "ListPackageVersions":
        return {
            "defaultDisplayVersion": "latest",
            "format": "pypi",
            "namespace": "test-namespace",
            "package": "test-package",
            "versions": [
                {
                    "version": "latest",
                    "revision": "lates",
                    "status": "Published",
                    "origin": {
                        "domainEntryPoint": {
                            "repositoryName": "test-repository",
                            "externalConnectionName": "",
                        },
                        "originType": "INTERNAL",
                    },
                },
            ],
        }

    return make_api_call(self, operation_name, kwarg)


# Mock generate_regional_clients()
def mock_generate_regional_clients(service, audit_info):
    regional_client = audit_info.audit_session.client(service, region_name=AWS_REGION)
    regional_client.region = AWS_REGION
    return {AWS_REGION: regional_client}


# Patch every AWS call using Boto3 and generate_regional_clients to have 1 client
@patch("botocore.client.BaseClient._make_api_call", new=mock_make_api_call)
@patch(
    "prowler.providers.aws.services.codeartifact.codeartifact_service.generate_regional_clients",
    new=mock_generate_regional_clients,
)
class Test_CodeArtifact_Service:
    # Test CodeArtifact Client
    def test__get_client__(self):
        codeartifact = CodeArtifact(current_audit_info)
        assert (
            codeartifact.regional_clients[AWS_REGION].__class__.__name__
            == "CodeArtifact"
        )

    # Test CodeArtifact Session
    def test__get_session__(self):
        codeartifact = CodeArtifact(current_audit_info)
        assert codeartifact.session.__class__.__name__ == "Session"

    # Test CodeArtifact Service
    def test__get_service__(self):
        codeartifact = CodeArtifact(current_audit_info)
        assert codeartifact.service == "codeartifact"

    def test__list_repositories__(self):
        # Set partition for the service
        current_audit_info.audited_partition = "aws"
        codeartifact = CodeArtifact(current_audit_info)

        assert len(codeartifact.repositories) == 1
        assert codeartifact.repositories
        assert codeartifact.repositories["test-repository"]
        assert codeartifact.repositories["test-repository"].name == "test-repository"
        assert (
            codeartifact.repositories["test-repository"].arn
            == f"arn:aws:codebuild:{AWS_REGION}:{DEFAULT_ACCOUNT_ID}:repository/test-repository"
        )
        assert codeartifact.repositories["test-repository"].domain_name == "test-domain"
        assert (
            codeartifact.repositories["test-repository"].domain_owner
            == DEFAULT_ACCOUNT_ID
        )
        assert codeartifact.repositories["test-repository"].region == AWS_REGION

        assert codeartifact.repositories["test-repository"].packages
        assert len(codeartifact.repositories["test-repository"].packages) == 1
        assert (
            codeartifact.repositories["test-repository"].packages[0].name
            == "test-package"
        )
        assert (
            codeartifact.repositories["test-repository"].packages[0].namespace
            == "test-namespace"
        )

        assert codeartifact.repositories["test-repository"].packages[0].format == "pypi"
        assert (
            codeartifact.repositories["test-repository"]
            .packages[0]
            .origin_configuration.restrictions.publish
            == RestrictionValues.ALLOW
        )
        assert (
            codeartifact.repositories["test-repository"]
            .packages[0]
            .origin_configuration.restrictions.upstream
            == RestrictionValues.ALLOW
        )

        assert (
            codeartifact.repositories["test-repository"]
            .packages[0]
            .latest_version.version
            == "latest"
        )

        assert (
            codeartifact.repositories["test-repository"]
            .packages[0]
            .latest_version.status
            == LatestPackageVersionStatus.Published
        )

        assert (
            codeartifact.repositories["test-repository"]
            .packages[0]
            .latest_version.origin.origin_type
            == OriginInformationValues.INTERNAL
        )

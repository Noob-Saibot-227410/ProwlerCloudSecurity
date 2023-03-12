from re import search
from unittest import mock

from boto3 import client
from moto import mock_rds

AWS_REGION = "us-east-1"


class Test_rds_instance_no_public_access:
    @mock_rds
    def test_rds_no_instances(self):
        from prowler.providers.aws.lib.audit_info.audit_info import current_audit_info
        from prowler.providers.aws.services.rds.rds_service import RDS

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "prowler.providers.aws.services.rds.rds_instance_no_public_access.rds_instance_no_public_access.rds_client",
            new=RDS(current_audit_info),
        ):
            # Test Check
            from prowler.providers.aws.services.rds.rds_instance_no_public_access.rds_instance_no_public_access import (
                rds_instance_no_public_access,
            )

            check = rds_instance_no_public_access()
            result = check.execute()

            assert len(result) == 0

    @mock_rds
    def test_rds_instance_private(self):
        conn = client("rds", region_name=AWS_REGION)
        conn.create_db_instance(
            DBInstanceIdentifier="db-master-1",
            AllocatedStorage=10,
            Engine="postgres",
            DBName="staging-postgres",
            DBInstanceClass="db.m1.small",
        )
        from prowler.providers.aws.lib.audit_info.audit_info import current_audit_info
        from prowler.providers.aws.services.rds.rds_service import RDS

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "prowler.providers.aws.services.rds.rds_instance_no_public_access.rds_instance_no_public_access.rds_client",
            new=RDS(current_audit_info),
        ):
            # Test Check
            from prowler.providers.aws.services.rds.rds_instance_no_public_access.rds_instance_no_public_access import (
                rds_instance_no_public_access,
            )

            check = rds_instance_no_public_access()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "PASS"
            assert search(
                "is not Publicly Accessible",
                result[0].status_extended,
            )
            assert result[0].resource_id == "db-master-1"

    @mock_rds
    def test_rds_instance_public(self):
        conn = client("rds", region_name=AWS_REGION)
        conn.create_db_instance(
            DBInstanceIdentifier="db-master-1",
            AllocatedStorage=10,
            Engine="postgres",
            DBName="staging-postgres",
            DBInstanceClass="db.m1.small",
            PubliclyAccessible=True,
        )
        from prowler.providers.aws.lib.audit_info.audit_info import current_audit_info
        from prowler.providers.aws.services.rds.rds_service import RDS

        current_audit_info.audited_partition = "aws"

        with mock.patch(
            "prowler.providers.aws.services.rds.rds_instance_no_public_access.rds_instance_no_public_access.rds_client",
            new=RDS(current_audit_info),
        ):
            # Test Check
            from prowler.providers.aws.services.rds.rds_instance_no_public_access.rds_instance_no_public_access import (
                rds_instance_no_public_access,
            )

            check = rds_instance_no_public_access()
            result = check.execute()

            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert search(
                "is set as Publicly Accessible",
                result[0].status_extended,
            )
            assert result[0].resource_id == "db-master-1"

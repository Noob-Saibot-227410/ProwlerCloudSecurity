<p align="center">
  <img align="center" src="https://github.com/prowler-cloud/prowler/blob/62c1ce73bbcdd6b9e5ba03dfcae26dfd165defd9/docs/img/prowler-pro-dark.png?raw=True#gh-dark-mode-only" width="150" height="36">
  <img align="center" src="https://github.com/prowler-cloud/prowler/blob/62c1ce73bbcdd6b9e5ba03dfcae26dfd165defd9/docs/img/prowler-pro-light.png?raw=True#gh-light-mode-only" width="15%" height="15%">
</p>
<p align="center">
  <b><i>Veja tudo o que você e sua equipe podem fazer com o Prowler <a href="https://prowler.pro">prowler.pro</a></i></b>
</p>
<hr>
<p align="center">
  <img src="https://user-images.githubusercontent.com/3985464/113734260-7ba06900-96fb-11eb-82bc-d4f68a1e2710.png" />
</p>
<p align="center">
  <a href="https://join.slack.com/t/prowler-workspace/shared_invite/zt-1hix76xsl-2uq222JIXrC7Q8It~9ZNog"><img alt="Slack Shield" src="https://img.shields.io/badge/slack-prowler-brightgreen.svg?logo=slack"></a>
  <a href="https://pypi.org/project/prowler-cloud/"><img alt="Python Version" src="https://img.shields.io/pypi/v/prowler-cloud.svg"></a>
  <a href="https://pypi.python.org/pypi/prowler-cloud/"><img alt="Python Version" src="https://img.shields.io/pypi/pyversions/prowler-cloud.svg"></a>
  <a href="https://pypistats.org/packages/prowler-cloud"><img alt="PyPI Downloads" src="https://img.shields.io/pypi/dw/prowler-cloud.svg"></a>
  <a href="https://hub.docker.com/r/toniblyx/prowler"><img alt="Docker Pulls" src="https://img.shields.io/docker/pulls/toniblyx/prowler"></a>
  <a href="https://hub.docker.com/r/toniblyx/prowler"><img alt="Docker" src="https://img.shields.io/docker/cloud/build/toniblyx/prowler"></a>
  <a href="https://hub.docker.com/r/toniblyx/prowler"><img alt="Docker" src="https://img.shields.io/docker/image-size/toniblyx/prowler"></a>
  <a href="https://gallery.ecr.aws/o4g1s5r6/prowler"><img width="120" height=19" alt="AWS ECR Gallery" src="https://user-images.githubusercontent.com/3985464/151531396-b6535a68-c907-44eb-95a1-a09508178616.png"></a>
</p>
<p align="center">
  <a href="https://github.com/prowler-cloud/prowler"><img alt="Repo size" src="https://img.shields.io/github/repo-size/prowler-cloud/prowler"></a>
  <a href="https://github.com/prowler-cloud/prowler/issues"><img alt="Issues" src="https://img.shields.io/github/issues/prowler-cloud/prowler"></a>
  <a href="https://github.com/prowler-cloud/prowler/releases"><img alt="Version" src="https://img.shields.io/github/v/release/prowler-cloud/prowler?include_prereleases"></a>
  <a href="https://github.com/prowler-cloud/prowler/releases"><img alt="Version" src="https://img.shields.io/github/release-date/prowler-cloud/prowler"></a>
  <a href="https://github.com/prowler-cloud/prowler"><img alt="Contributors" src="https://img.shields.io/github/contributors-anon/prowler-cloud/prowler"></a>
  <a href="https://github.com/prowler-cloud/prowler"><img alt="License" src="https://img.shields.io/github/license/prowler-cloud/prowler"></a>
  <a href="https://twitter.com/ToniBlyx"><img alt="Twitter" src="https://img.shields.io/twitter/follow/toniblyx?style=social"></a>
  <a href="https://twitter.com/prowlercloud"><img alt="Twitter" src="https://img.shields.io/twitter/follow/prowlercloud?style=social"></a>
</p>

# Descrição

`ProwlerCloudSecurity` é uma ferramenta de segurança de código aberto para realizar avaliações de práticas recomendadas de segurança da AWS e do Azure, auditorias, resposta a incidentes, monitoramento contínuo, proteção e prontidão forense.

Ele contém centenas de controles que abrangem CIS, PCI-DSS, ISO27001, GDPR, HIPAA, FFIEC, SOC2, AWS FTR, ENS e estruturas de segurança personalizadas.

## Procurando a documentação do Prowler v2?
Para a documentação do Prowler v2, acesse https://github.com/prowler-cloud/prowler/tree/2.12.1.
# ⚙️ Instalação

## Pip package
Prowler está disponível como um projeto em [PyPI](https://pypi.org/project/prowler-cloud/), portanto, pode ser instalado usando pip com Python >= 3.9:

```console
pip install prowler
prowler -v
```

## Containers

As versões disponíveis do Prowler são as seguintes:

- `latest`: em sincronia com o branch master (tenha em mente que não é uma versão estável)
- `<x.y.z>` (lançamento): você pode encontrar os lançamentos [here](https://github.com/prowler-cloud/prowler/releases), esses são lançamentos estáveis.
- `stable`: esta tag sempre aponta para a versão mais recente.

As imagens do contêiner estão disponíveis aqui:

- [DockerHub](https://hub.docker.com/r/toniblyx/prowler/tags)
- [AWS Public ECR](https://gallery.ecr.aws/o4g1s5r6/prowler)

## From Github

Python >= 3.9 é necessário com pip e pipenv:

```
git clone https://github.com/prowler-cloud/prowler
cd prowler
pipenv shell
pipenv install
python prowler.py -v
```

# 📖 Documentation

TA documentação completa pode agora ser encontrada em [https://docs.prowler.cloud](https://docs.prowler.cloud)


# 📐✏️ Arquitetura de alto nível

Você pode executar o Prowler em sua estação de trabalho, uma instância do EC2, Fargate ou qualquer outro contêiner, Codebuild, CloudShell e Cloud9.

![Architecture](https://github.com/prowler-cloud/prowler/blob/62c1ce73bbcdd6b9e5ba03dfcae26dfd165defd9/docs/img/architecture.png?raw=True)

# 📝 Requirements

Prowler foi escrito em Python usando o [AWS SDK (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html#) and [Azure SDK](https://azure.github.io/azure-sdk-for-python/).

## AWS

Como o Prowler usa credenciais da AWS sob o capô, você pode seguir qualquer método de autenticação conforme descrito [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-precedence).
Certifique-se de ter configurado corretamente sua AWS-CLI com uma chave de acesso e região válidas ou declare as variáveis ​​da AWS corretamente (ou perfil/função da instância):

  ```console
  aws configure
  ```

  or

  ```console
  export AWS_ACCESS_KEY_ID="ASXXXXXXX"
  export AWS_SECRET_ACCESS_KEY="XXXXXXXXX"
  export AWS_SESSION_TOKEN="XXXXXXXXX"
  ```

Essas credenciais devem estar associadas a um usuário ou função com permissões adequadas para fazer todas as verificações. Para garantir, adicione as seguintes políticas gerenciadas pela AWS ao usuário ou à função que está sendo usada:

  - arn:aws:iam::aws:policy/SecurityAudit
  - arn:aws:iam::aws:policy/job-function/ViewOnlyAccess

  > Além disso, algumas permissões adicionais somente leitura são necessárias para várias verificações, certifique-se de anexar também a política personalizada[prowler-additions-policy.json](https://github.com/prowler-cloud/prowler/blob/master/permissions/prowler-additions-policy.json) para a função que você está usando.

  > Se você deseja que o Prowler envie descobertas para [AWS Security Hub](https://aws.amazon.com/security-hub), certifique-se de anexar também a política personalizada[prowler-security-hub.json](https://github.com/prowler-cloud/prowler/blob/master/permissions/prowler-security-hub.json).

  ## Azure

  O Prowler for Azure dá suporte aos seguintes tipos de autenticação:

- Autenticação da entidade de serviço por variáveis ​​de ambiente (Aplicativo Corporativo)
- Credenciais az cli atuais armazenadas
- Autenticação interativa do navegador
- Autenticação de identidade gerenciada

### Autenticação da Entidade de Serviço

Para permitir que o Prowler assuma a identidade principal do serviço para iniciar a verificação, é necessário configurar as seguintes variáveis ​​de ambiente:

```console
export AZURE_CLIENT_ID="XXXXXXXXX"
export AZURE_TENANT_ID="XXXXXXXXX"
export AZURE_CLIENT_SECRET="XXXXXXX"
```

Se você tentar executar o Prowler com o sinalizador `--sp-env-auth` e essas variáveis ​​estiverem vazias ou não forem exportadas, a execução falhará.
### AZ CLI / Navegador / Autenticação de Identidade Gerenciada

Os outros três casos não precisam de configuração adicional, `--az-cli-auth` e `--managed-identity-auth` são opções automatizadas, `--browser-auth` precisa que o usuário autentique usando o navegador padrão para iniciar a digitalização.

### Permissões

Para usar cada um, você precisa passar o sinalizador apropriado para a execução. O Prowler for Azure lida com dois tipos de escopos de permissão, que são:

- **Permissões do Azure Active Directory**: Usado para recuperar metadados da identidade assumida pelo Prowler e futuras verificações do AAD (não é obrigatório ter acesso para executar a ferramenta)
- **Permissões de escopo de assinatura**: necessárias para iniciar as verificações de seus recursos, obrigatórias para iniciar a ferramenta.

#### Azure Active Directory scope

Azure Active Directory (AAD) as permissões exigidas pela ferramenta são as seguintes:

- `Directory.Read.All`
- `Policy.Read.All`


#### Escopo de assinaturas

Em relação ao escopo da assinatura, o Prowler por padrão verifica todas as assinaturas que é capaz de listar, portanto, é necessário adicionar as seguintes funções internas do RBAC por assinatura à entidade que será assumida pela ferramenta:

- `Security Reader`
- `Reader`


# 💻 Uso Básico

Para executar o prowler, você precisará especificar o provedor (e.g aws or azure):

```console
prowler <provider>
```

![Prowler Execution](https://github.com/prowler-cloud/prowler/blob/b91b0103ff38e66a915c8a0ed84905a07e4aae1d/docs/img/short-display.png?raw=True)

> A execução do comando `prowler` sem opções usará suas credenciais de variável de ambiente.

Por padrão, o prowler gerará um relatório CSV, um JSON e um HTML, no entanto, você pode gerar um relatório JSON-ASFF (somente para AWS Security Hub) com `-M` or `--output-modes`:

```console
prowler <provider> -M csv json json-asff html
```

O relatório html estará localizado no diretório `output` como os outros arquivos e terá a seguinte aparência:

![Prowler Execution](https://github.com/prowler-cloud/prowler/blob/62c1ce73bbcdd6b9e5ba03dfcae26dfd165defd9/docs/img/html-output.png?raw=True)

Você pode usar `-l`/`--list-checks` ou `--list-services` para listar todas as verificações ou serviços disponíveis no provedor.

```console
prowler <provider> --list-checks
prowler <provider> --list-services
```

Para executar verificações ou serviços específicos, você pode usar as opções `-c`/`--checks` ou `-s`/`--services`:

```console
prowler aws --checks s3_bucket_public_access
prowler aws --services s3 ec2
```

Also, checks and services can be excluded with options `-e`/`--excluded-checks` or `--excluded-services`:

```console
prowler aws --excluded-checks s3_bucket_public_access
prowler aws --excluded-services s3 ec2
```

Você sempre pode usar `-h`/`--help` para acessar as informações de uso e todas as opções possíveis:

```console
vagabundo -h
```

## Verifica as configurações
Várias verificações do Prowler têm variáveis ​​configuráveis ​​pelo usuário que podem ser modificadas em um **arquivo de configuração** comum.
Este arquivo pode ser encontrado no seguinte caminho:
```
prowler/config/config.yaml
```

##AWS

Use um perfil personalizado da AWS com `-p`/`--profile` e/ou regiões da AWS que você deseja auditar com `-f`/`--filter-region`:

```console
prowler aws --profile perfil personalizado -f us-east-1 eu-sul-2
```
> Por padrão, `prowler` irá escanear todas as regiões da AWS.

## Azure

Com o Azure, você precisa especificar qual método de autenticação será usado:

```console
prowler azure [--sp-env-auth, --az-cli-auth, --browser-auth, -- managed-identity-auth]
```
> Por padrão, `prowler` verificará todas as assinaturas do Azure.

# 🎉 Novos recursos

- Python: nos livramos de todo bash e agora é tudo em Python.
- Mais rápido: grandes melhorias de desempenho (mesma conta de 2,5 horas para 4 minutos).
- Desenvolvedores e comunidade: facilitamos a contribuição com novas verificações e novas estruturas de conformidade. Também incluímos testes de unidade.
- Multi-cloud: além do AWS, adicionamos o Azure, planejamos incluir GCP e OCI em breve, avise-nos se quiser contribuir!

# 📃 Licença

Prowler é licenciado como Apache License 2.0 conforme especificado em cada arquivo. Você pode obter uma cópia da Licença em
<http://www.apache.org/licenses/LICENSE-2.0>

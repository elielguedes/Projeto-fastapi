🏥 API RESTT - UNIDADE DE SAÚDE (CNES)

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-green.svg)](https://fastapi.tiangolo.com)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-orange.svg)](https://sqlalchemy.org)
[![Deploy](https://img.shields.io/badge/Deploy-AWS_EC2-yellow.svg)](http://18.118.167.28:8000/docs)
[![Status](https://img.shields.io/badge/Status-Produção-brightgreen.svg)](http://18.118.167.28:8000)


📋 Descrição

API RESTful para disponibilização de dados públicos de unidades de saúde, baseada no Cadastro Nacional de Estabelecimentos de Saúde (CNES), com foco em organização, segurança e boas práticas de desenvolvimento.

🏗️ Arquitetura em Camadas:
°🚀 Presentation Layer: FastAPI routers (routers/) 
°⚙️ Service Layer: Lógica de negócio (services/) 
°🏗️ Data Layer: Models SQLAlchemy (models/)
°🔐 Security Layer: Autenticação JWT (auth.py)
°📊 Validation Layer: Schemas Pydantic (schemas.py)

> 📊 **Dados reais** do governo brasileiro via dados.gov.br
>
> ## ✨ Funcionalidades Principais
- 🔐 **Autenticação JWT** com controle de permissões
-  📊 **CRUD completo**
- 🔍 **Filtros avançados**, ordenação e paginação
- ✅ **Validação de CNES** integrada com dígitos verificadores
-  📂 **Import/Export** de dados CSV do dados.gov.br
- 🔄 **Migrations Alembic** para versionamento de banco

## 🏃‍♂️ Início Rápido
### 💻 **Desenvolvimento Local (Recomendado)**
# 1. Clone o repositório
https://github.com/elielguedes/Projeto-fastapi.git

# 2. Crie e ative ambiente virtual (Python 3.10+)
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# Linux/Mac
source .venv/bin/activate
# 3. Instale dependências
pip install -r requirements.txt
# 4. Inicie aplicação (SQLite automático)
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
### 🚀 **Acessar Aplicação**

#### 💻 **Local (Desenvolvimento)**

- 🌐 **API**: http://127.0.0.1:8000
- 📚 **Docs**: http://127.0.0.1:8000/docs  
- ❤️ **Health**: http://127.0.0.1:8000/health

## 📁 Estrutura Organizada do Projeto

```
|__🚀app/
    |___core/
        |___ __init__.py
        |__ config.py
        |__ security.py
    |__models/
        |__ __init__.py
        |__ entidade1.py
        |__ entidade2.py
        |__ user.py
    |__routes/
        |__ __init__.py
        |__ auth.py
        |__ entidade1.py
        |__ entidade2.py
    |__schemas/
        |__ __init__.py
        |__ entidade1.py
        |__ entidade2.py
        |__ schemas_backup.py
        |__ user.py
    |__services/
        |__ __init__.py
        |__ auth_service.py
        |__ entidade_saude.py
        |__ entidade_service.py
     💾database.py
    🚀main.py
|__csv/
  |__ cnes.csv
  |__ organization.py
|__docs/
  |__cronograma.md
|__scripts/
  |__ __init__.py
  |__ import_cnes.py
  |__ import_gestao.py
  |__ import_leitos.py
  |__ import_location.py
|__tables/
  |__ create_tables.py
app.db
README.md
requeriments.txt

## 📊 Diagrama ER - Modelagem de Dados
```mermaid
erDiagram
  %% == Entidades Principais ==

  UnidadeSaude ||--o{ Unidade : "criar/gerenciar"
  Usuario ||--o{ Usuarios : "criar/autenticar"
  Location ||--o{ Location : "possui (N:N)"
  Gestao ||--o{ Gestao : "possui (N:N)"
  Leitos ||--o{ Leitos : "possui (N:N)"

  UnidadeSaude {
    id: UUID
    cnes: int
    nome: str
    location: pk
    gestao: pk
    leitos: pk
  }

Location {
  id: UUID
  cod_uf_municipio: int
  regiao_saude: str
  microregiao: str
  unidade_id: pk
  unidade: pk
}
Gestao {
  id: UUID
  tipo_gestao: str
  esfera_admin: str
  unidade_id: pk
  unidade: pk
}
Leitos{
  id: UUID
  leitos_tipo_1: int
  leitos_tipo_2: int
  leitos_tipo_3: int
  total_leitos: int
  unidade_id: pk
  unidade: pk
}
```


## Origem dos Dados
- Fonte: [dados.gov.br](https://dados.gov.br)
- Formato: CSV
- Periodicidade: conforme atualização oficial

## Scripts de importação / exportação





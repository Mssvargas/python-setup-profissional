# Python Setup Profissional

Estrutura base para iniciar projetos Python de forma profissional: layout `src/`,
ambiente virtual, testes com `pytest`, formatação/lint com `ruff` e configuração
centralizada em `pyproject.toml`.

## Requisitos

- Python 3.11+

## Setup

```bash
# 1. Criar e ativar o ambiente virtual
python -m venv .venv
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# Linux/macOS
source .venv/bin/activate

# 2. Instalar as dependências
pip install -r requirements.txt

# 3. Instalar o pacote em modo editável (opcional)
pip install -e .
```

## Comandos úteis

```bash
# Rodar a aplicação
python -m python_setup_profissional

# Rodar os testes
pytest

# Lint e formatação
ruff check .
ruff format .
```

## Estrutura

```
python-setup-profissional/
├── src/
│   └── python_setup_profissional/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .gitignore
├── .python-version
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Licença

MIT

#!/bin/bash
echo "Configurando ambiente de testes QA..."

# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Instalar navegadores Playwright
playwright install

echo "Ambiente configurado com sucesso!"

@echo off
echo Configurando ambiente de testes QA...

REM Criar ambiente virtual
python -m venv venv

REM Ativar ambiente virtual
call venv\Scripts\activate

REM Instalar dependências
pip install -r requirements.txt

REM Instalar navegadores Playwright
playwright install

echo Ambiente configurado com sucesso!

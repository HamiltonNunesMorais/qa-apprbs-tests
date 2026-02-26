# QA Apprbs Tests

Repositório de testes automatizados para avaliação da qualidade de duas páginas de exemplo:

- **Certificação**: https://qualidade.apprbs.com.br/certificacao  
- **Site**: https://qualidade.apprbs.com.br/site  

---

## 🚀 Execução dos testes localmente

### Windows
1. Ative o ambiente virtual (venv) , executando o script de setup no terminal:
```bash
setup.bat
```

2. Por padrão os testes rodam em headless (sem abrir navegador)
    Se quiser visualizar o navegador rodando, altere no arquivo conftest.py:

```
headless=False
```
3. rodeos testes com o comando:
```
pytest tests_certificacao --html=reports/report.html --self-contained-html -v
```

# Execução no GitHub Actions
O repositório contém workflow configurado em .github/workflows/ci.yml.

## Para rodar os testes no Actions:

Vá até a aba Actions do GitHub.

Dispare manualmente o workflow.

O pipeline executa os testes e gera artefatos:

Relatório HTML (pytest-report)

Evidências (screenshots) (evidences)




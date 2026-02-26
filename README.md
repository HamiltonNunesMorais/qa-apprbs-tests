# Testes de UI 
## avaliação  da qualidade de duas páginas de exemplo:
1. Certificação: [https://qualidade.apprbs.com.br/certificacao](https://qualidade.apprbs.com.br/certificacao)
2. Site: [https://qualidade.apprbs.com.br/site](https://qualidade.apprbs.com.br/site)


### execução dos tests

pytest tests_certificacao/test_formulario.py -v

pytest --html=reports/report.html --self-contained-html

pytest tests_certificacao/test_formulario_certificacao.py::test_form_btn_enable -v 

pytest tests_certificacao/test_form_btn_enabled.py::test_formulario_avancar_habilitado -v


pytest tests_certificacao/test_form_btn_disabled.py::test_formulario_avancar_desabilitado -v

pytest tests_certificacao/test_footer_icon.py::test_footer_youtube_icon -v

pytest tests_certificacao --html=reports/report.html --self-contained-html -v
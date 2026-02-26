from playwright.sync_api import expect

def test_formulario_avancar_desabilitado(certificacao_page):
    certificacao_page.locator("input[name='pessoa.nome']").fill("Teste QA")

    avancar_btn = certificacao_page.get_by_role("button", name="Avançar")
    expect(avancar_btn).to_be_disabled()

    # Evidência: captura a div inteira do formulário
    form_div = certificacao_page.locator("#i8y4")  
    form_div.screenshot(path="evidences/form_div_desabilitado.png")

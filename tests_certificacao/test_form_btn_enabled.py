from playwright.sync_api import expect

def test_formulario_avancar_habilitado(certificacao_page):
    certificacao_page.locator("input[name='pessoa.nome']").fill("Teste QA")
    certificacao_page.get_by_placeholder("email@exemplo.com").fill("qa@teste.com")
    certificacao_page.keyboard.press("Tab")

    avancar_btn = certificacao_page.get_by_role("button", name="Avançar")
    expect(avancar_btn).to_be_enabled(timeout=60000)

    # Evidência: captura a seção inteira do formulário com botão habilitado
    form_section = certificacao_page.locator("#rbActionsFormContainer")
    form_section.screenshot(path="evidences/form_habilitado.png")

    # Clica e valida toast
    avancar_btn.click()
    toast = certificacao_page.locator("#toast-container div")
    toast.wait_for(state="visible", timeout=60000)

    # Screenshot do toast
    toast.screenshot(path="evidences/toast_base_legal.png")

    # Screenshot da página inteira com toast visível
    certificacao_page.screenshot(path="evidences/pagina_com_toast.png", full_page=True)

    # Valida mensagem
    toast_msg = toast.inner_text()
    assert "base legal" in toast_msg.lower(), "Mensagem esperada não apareceu"

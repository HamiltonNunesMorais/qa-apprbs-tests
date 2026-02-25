from playwright.sync_api import expect

def test_formulario_certificacao(certificacao_page):
    # Verifica se o texto "Inscreva-se agora!" existe
    inscreva_text = certificacao_page.get_by_text("Inscreva-se agora!")
    assert inscreva_text.is_visible(), "Texto 'Inscreva-se agora!' não encontrado"

    # Preenche os campos obrigatórios
    certificacao_page.locator("input[name='pessoa.nome']").fill("Teste QA")
    certificacao_page.get_by_placeholder("email@exemplo.com").fill("qa@teste.com")
    certificacao_page.keyboard.press("Tab")  # força blur para validar

    # Localiza o botão "Avançar"
    avancar_btn = certificacao_page.get_by_role("button", name="Avançar")
    avancar_btn.scroll_into_view_if_needed()
    expect(avancar_btn).to_be_enabled(timeout=60000)

    # Screenshot antes do clique
    certificacao_page.screenshot(path="antes_click.png", full_page=True)

    # Clica
    avancar_btn.focus()
    avancar_btn.click()

    # Espera o toast aparecer
    toast = certificacao_page.locator("#toast-container div")
    toast.wait_for(state="visible", timeout=60000)
    toast_msg = toast.inner_text()

    # Screenshot depois do clique
    certificacao_page.screenshot(path="depois_click.png", full_page=True)

    # Valida mensagem
    assert "base legal" in toast_msg.lower(), "Mensagem esperada não apareceu"

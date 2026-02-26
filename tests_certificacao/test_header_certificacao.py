from playwright.sync_api import expect

def test_header_quero_me_certificar(certificacao_page):
    # Localiza o botão/link pelo id
    certificar_btn = certificacao_page.locator("#iwgqid").get_by_role("link", name="Quero me certificar")

    # Verifica se está visível
    expect(certificar_btn).to_be_visible()

    # Captura o href do botão
    href = certificar_btn.get_attribute("href")
    assert href == "https://rubeus.com.br/", "Link incorreto no botão 'Quero me certificar'"

    # Clica no botão (abre em nova aba/janela)
    with certificacao_page.context.expect_page() as new_page_info:
        certificar_btn.click()
    new_page = new_page_info.value

    # Espera o carregamento da nova página
    new_page.wait_for_load_state("domcontentloaded")

    # Valida que o título contém 'Rubeus'
    title = new_page.title()
    assert "Rubeus" in title, "Página de destino não contém título esperado 'Rubeus'"

    # Evidência: screenshot da nova página
    new_page.screenshot(path="evidences/rubeus_page.png", full_page=True)
    new_page.close()
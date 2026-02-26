from playwright.sync_api import expect

def test_footer_quero_me_certificar(certificacao_page):
    footer_btn = certificacao_page.locator("#ihqitg").get_by_role("link", name="Quero me certificar")
    expect(footer_btn).to_be_visible()

    # Captura o href
    href = footer_btn.get_attribute("href")

    # Clica no botão (abre em nova aba/janela)
    with certificacao_page.context.expect_page() as new_page_info:
        footer_btn.click()
    new_page = new_page_info.value
    new_page.wait_for_load_state("domcontentloaded")

    # Screenshot da página aberta (mesmo que esteja errada)
    new_page.screenshot(path="evidences/footer_wrong_page.png", full_page=True)
    new_page.close()

    # Só depois valida o link
    assert href == "https://rubeus.com.br/", (
        f"Link incorreto no botão do rodapé 'Quero me certificar': {href}"
    )

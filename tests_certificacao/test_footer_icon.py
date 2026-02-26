from playwright.sync_api import expect

def test_footer_youtube_icon(certificacao_page):
    # Localiza a div dos ícones do rodapé
    footer_icons = certificacao_page.locator("#ijhks8")

    # Dentro dessa div, pega o ícone/link do YouTube
    youtube_icon = footer_icons.locator("#ifpwp7")
    expect(youtube_icon).to_be_visible()

    # Evidência: screenshot da div inteira com os ícones
    footer_icons.screenshot(path="evidences/footer_icons.png")

    # Clica no ícone (abre nova aba)
    with certificacao_page.context.expect_page() as new_page_info:
        youtube_icon.click()
    new_page = new_page_info.value
    new_page.wait_for_load_state("domcontentloaded")

    # Captura o título da página aberta
    page_title = new_page.title()

    # Evidência: screenshot da página aberta (TikTok, no caso errado)
    new_page.screenshot(path="evidences/footer_youtube_wrong_page.png", full_page=True)
    new_page.close()

    # Valida que deveria ser YouTube
    assert "youtube" in page_title.lower(), (
        f"Ícone do YouTube no rodapé está incorreto. "
        f"Título da página aberta: {page_title}"
    )

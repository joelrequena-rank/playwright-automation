from playwright.sync_api import Playwright, sync_playwright, expect
from utils.login_page_generator import LoginPage
from config.config import data, env

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False) #slow_mo=500 hace cada test mas lento
    context = browser.new_context()
    page = context.new_page()
    login_page = LoginPage(page) # Esto crea una instancia para el objeto LoginPage.

    page.goto(env["Staging"])  # poner env
    page.pause()

    login_page.login(data) # Esto llama a la funcion de login de LoginPage()

    #En vez de mandar una linea completa de codigo, creamos una variable con el "botón de login"
    # y en el assert miramos que no esté visible = "se ha iniciado sesión"
    # https://playwright.dev/python/docs/test-assertions

    # Cerrar sesión
    page.get_by_role("link", name="Sair").click()
    print("Logout correcto")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

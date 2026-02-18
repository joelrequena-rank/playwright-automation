from playwright.sync_api import Playwright, sync_playwright
from utils_registro.password_generator import generar_password
from utils_registro.user_generator import generar_user, generar_mail, data
from config.config import env_selector, pre_login
from utils_registro.page_load import LoadPage
from utils_registro.external_data import ExternalDataService
from utils_registro.form_generator import RegisterPage


def run(playwright: Playwright) -> None:

    # ==============================
    # CONFIGURACIÓN INICIAL
    # ==============================

    print("         █▀█ █▀▀ █▀▀ █ █▀ ▀█▀ █▀█ █▀█   █▀█ ▀█▀")
    print("         █▀▄ ██▄ █▄█ █ ▄█ ░█░ █▀▄ █▄█   █▀▀ ░█░")
    print(f"Environment seleccionado: {env_selector['QA']}")
    print("         #-------------------------------------#")

    # ==============================
    # GENERACIÓN DE DATOS
    # ==============================

    user = generar_user()
    mail = generar_mail(user)
    password = generar_password()

    print(f"Username generado: {user}")
    print(f"Password generada: {password}")

    # ==============================
    # LANZAMIENTO DEL NAVEGADOR
    # ==============================

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # ==============================
    # SERVICIOS Y PAGE OBJECTS
    # ==============================

    # Por cada "Class" creada hay que darle un nombre para poder llamarla.

    register_page = RegisterPage(page)
    load_page = LoadPage(page)
    external_data = ExternalDataService(page, pre_login)

    # ==============================
    # GENERACIÓN NIF / IBAN
    # ==============================

    nif_nuevo = external_data.generate_nif()
    iban_nuevo = external_data.generate_iban()

    # ==============================
    # NAVEGACIÓN A REGISTRO
    # ==============================

    page.goto(env_selector["QA"])
    load_page.page_load()

    # ==============================
    # REGISTRO DE USUARIO
    # ==============================

    register_page.register_user(
        nif_nuevo,
        iban_nuevo,
        mail,
        user,
        password,
        data
    )

    print("Usuario registrado correctamente")
    print("#-----------------------------------------------#")

    # ==============================
    # CIERRE
    # ==============================

    context.close()
    browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, base_url: str):
        self.page.goto(base_url)

    def accept_cookies(self):
        self.page.get_by_role("button", name="ACEITAR").click()

    def open_login_modal(self):
        self.page.get_by_role("button", name="INICIAR SESSÃO").click()

    def fill_username(self, username: str):
        self.page.get_by_role(
            "textbox", name="Nome de utilizador:"
        ).fill(username)

    def fill_password(self, password: str):
        self.page.get_by_role(
            "textbox", name="Palavra-passe:"
        ).fill(password)

    def submit_login(self):
        self.page.get_by_label(
            "", exact=True
        ).get_by_role("button", name="INICIAR SESSÃO").click()

    def login_flow(self, base_url: str, username: str, password: str):
        self.navigate(base_url)
        self.accept_cookies()
        self.open_login_modal()
        self.fill_username(username)
        self.fill_password(password)
        self.submit_login()
        self.page.pause()
        self.page.wait_for_load_state("load")
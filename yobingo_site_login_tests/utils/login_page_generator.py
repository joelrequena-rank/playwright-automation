class LoginPage:
    def __init__(self, page):
        self.page = page
        self.boton_cookies = page.get_by_role("button", name="ACEITAR")
        self.boton_login = page.get_by_role("button", name="INICIAR SESSÃO")

        self.username = page.get_by_role("textbox", name="Nome de utilizador:")
        self.password = page.get_by_role("textbox", name="Palavra-passe:")

        self.send_login_button = page.get_by_label("", exact=True).get_by_role("button", name="INICIAR SESSÃO").click()

    def acc_cookies(self):
        self.boton_cookies.click()

    def fill_login(self, data):
        self.boton_login.click()
        self.username.fill(data["username"])
        self.password.fill(data["password"])

    def send_login(self):
        self.send_login_button.click()

    def login(self, data):
        self.acc_cookies()
        self.fill_login(data)
        self.send_login()
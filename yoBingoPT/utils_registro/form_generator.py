
class RegisterPage:

    # -- SELECTORS / LOCATORS --
    def __init__(self, page):
        self.page = page
        self.document_input = page.get_by_role("textbox", name="Documento Nº*")
        self.user_name = page.get_by_role("textbox", name="Primeiro(s) Nome(s)*")
        self.user_surname = page.get_by_role("textbox", name="Apelidos*")
        self.user_gender = page.get_by_label("Género:")
        self.user_nif = page.get_by_role("textbox", name="NIF*")

        self.user_bd_day = page.locator("#dob_day")
        self.user_bd_month= page.locator("#dob_month")
        self.user_bd_year= page.locator("#dob_year")
        self.user_profession = page.locator("#fkprofession")

        self.bank_info = page.get_by_role("textbox", name="IBAN*")

        self.default_email = page.get_by_role("textbox", name="E-mail *")
        self.confirm_email = page.get_by_role("textbox", name="Confirmar Email *")
        self.default_phone = page.get_by_role("textbox", name="Número de telemóvel")
        self.default_CP = page.get_by_role("textbox", name="Código Postal*")
        self.default_rua = page.get_by_role("textbox", name="Rua*")
        self.default_number = page.get_by_role("textbox", name="Número, andar e porta*")

        self.new_username = page.get_by_role("textbox", name="Escolhe o teu nome de")
        self.new_password = page.get_by_role("textbox", name="Palavra-passe*", exact=True)
        self.confirm_password = page.get_by_role("textbox", name="Repetir a palavra-passe*")

        self.security_question = page.locator("#fkquestion")
        self.security_answer = page.get_by_role("textbox", name="Resposta de segurança*")
        self.security_check = page.get_by_role("checkbox", name="Ao selecionar esta caixa")

        self.continue_button = page.get_by_role("button", name="CONTINUAR")

    # -- INSERTS / FILLS --
    # No hace falta los page.blabla.click() realmente podemos decirle que meta directamente los datos directamente.
    def insert_user_info(self, nif, data):
        self.document_input.fill(nif)
        self.user_name.fill(data["name"])
        self.user_surname.fill(data["surname"])
        self.user_gender.select_option(data["gender"])
        self.user_nif.fill(nif)
        self.user_bd_day.select_option(data["bd_day"])
        self.user_bd_month.select_option(data["bd_month"])
        self.user_bd_year.select_option(data["bd_year"])
        self.user_profession.select_option(data["profession"])

    def insert_bank_info(self, iban):
        self.bank_info.fill(iban)

    def insert_defaults(self, mail, data):
        self.default_email.fill(mail)
        self.confirm_email.fill(mail)
        self.default_phone.fill(data["phone_number"])
        self.default_CP.fill(data["cp"])
        self.default_rua.fill(data["rua"])
        self.default_number.fill(data["rua_number"])

    def insert_login_info(self, user, password):
        self.new_username.fill(user)
        self.new_password.fill(password)
        self.confirm_password.fill(password)
        self.security_question.select_option("1")
        self.security_answer.fill("1")
        self.security_check.check()

    def form_confirm(self):
        self.continue_button.click()


    def register_user(self, nif, iban, mail, username, password, data):
        self.insert_user_info(nif, data)
        self.insert_bank_info(iban)
        self.insert_defaults(mail, data)
        self.insert_login_info(username, password)
        self.form_confirm()
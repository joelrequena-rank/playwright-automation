class ExternalDataService:

    def __init__(self, page, pre_login_config):
        self.page = page
        self.pre_login = pre_login_config

    def generate_nif(self):
        self.page.goto(self.pre_login["NIF"])
        self.page.wait_for_load_state("networkidle")
        return self.page.locator("#nif").inner_text()

    def generate_iban(self):
        self.page.goto(self.pre_login["IBAN"])
        self.page.wait_for_load_state("networkidle")
        return self.page.locator("#result-generated--number").inner_text()

class LoadPage:

    def __init__(self, page):
        self.page = page

        # Locators
        self.accept_cookies_button = page.get_by_role("button", name="ACEITAR")
        self.register_link = page.get_by_role("link", name="REGISTAR")

    def page_load(self):
        self.page.wait_for_load_state("networkidle")
        self.accept_cookies_button.click()
        self.page.wait_for_load_state("networkidle")
        self.register_link.click()
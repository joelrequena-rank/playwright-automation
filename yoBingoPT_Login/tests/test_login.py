from itertools import count

import pytest
from playwright.sync_api import Page
from yoBingoPT_Login.config.config import data

@pytest.mark.login
@pytest.mark.parametrize("credenciales", ["valid", "admin"], indirect=True)
def test_user(login):
    assert "playerArea" in login.url
    assert login.get_by_role("button", name="INICIAR SESSÃO").count() == 0

@pytest.mark.skip(reason="changes on conftest")
@pytest.mark.parametrize("email, password", "login_data")
def test_user(page: Page, email, password) -> None:
    page.goto("https://yobingo-qa-pt.bingosoft.com/")
    page.get_by_role("button", name="ACEITAR").click()
    page.get_by_role("button", name="INICIAR SESSÃO").click()
    page.get_by_role("textbox", name="Nome de utilizador:").fill(email)
    page.get_by_role("textbox", name="Palavra-passe:").fill(password)
    page.get_by_label("", exact=True).get_by_role("button", name="INICIAR SESSÃO").click()

    page.wait_for_load_state("load")
    assert "playerArea" in page.url
    assert page.get_by_role("button", name="INICIAR SESSÃO").count() == 0

@pytest.mark.skip(reason="changes on conftest")
def test_wrong_password(page: Page) -> None:
    page.goto("https://yobingo-qa-pt.bingosoft.com/")
    page.get_by_role("button", name="ACEITAR").click()
    page.get_by_role("textbox", name="Palavra-passe:").fill("password")
    page.get_by_label("button", name="INICIAR SESSÃO").click()
    page.get_by_role("textbox", name="Nome de utilizador:").fill(data["username"])
    page.get_by_role("button", name="INICIAR SESSÃO").click()

    page.wait_for_load_state("load")
    assert page.url == "https://yobingo-qa-pt.bingosoft.com/"
    assert page.get_by_text("Erro As informações que").is_visible() is True
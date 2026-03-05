import pytest

@pytest.mark.qa
@pytest.mark.parametrize("credenciales", ["valid_qa"], indirect=True)
def test_user_login(login):
    assert "playerArea" in login.url
    assert login.get_by_role("button", name="INICIAR SESSÃO").count() == 0, "Botón de login sigue visible"


@pytest.mark.qa
@pytest.mark.parametrize("credenciales", ["admin_qa"], indirect=True)
def test_admin_login(login):
    assert "adminHome" in login.url
    assert login.get_by_role("button", name="INICIAR SESSÃO").count() == 0, "Botón de login sigue visible"

@pytest.mark.qa
@pytest.mark.parametrize("credenciales", ["invalid_qa"], indirect=True)
def test_user_invent(login):
    assert "playerArea" not in login.url
    assert login.get_by_text(
        "As informações que introduziste, não pertencem a nenhum utilizador registado"
    ).is_visible()

@pytest.mark.qa
@pytest.mark.parametrize("credenciales", ["empty_password"], indirect=True)
def test_empty_passwd(login):
    assert "playerArea" not in login.url
    assert login.get_by_text(
        "Introduz a tua palavra-passe"
    ).is_visible()

@pytest.mark.qa
@pytest.mark.parametrize("credenciales", ["empty_username"], indirect=True)
def test_empty_username(login):
    assert "playerArea" not in login.url
    assert login.get_by_text(
        "Introduz o teu nome de utilizador"
    ).is_visible()

@pytest.mark.qa
@pytest.mark.parametrize("credenciales", ["no_user"], indirect=True)
def test_empty(login):
    assert "playerArea" not in login.url
    assert login.get_by_text(
        "Introduz o teu nome de utilizador"
    ).is_visible()
    assert login.get_by_text(
        "Introduz o teu nome de utilizador"
    ).is_visible()
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
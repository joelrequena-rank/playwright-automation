import pytest

@pytest.mark.login
@pytest.mark.parametrize("credenciales", ["valid_qa"], indirect=True)
def test_user_login(login):
    assert "playerArea" in login.url, "No redirigió a playerArea"
    assert login.get_by_role("button", name="INICIAR SESSÃO").count() == 0, "Botón de login sigue visible"
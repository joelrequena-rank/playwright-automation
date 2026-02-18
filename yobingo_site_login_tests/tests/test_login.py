from itertools import count

import pytest
from playwright.sync_api import Page
from yobingo_site_login_tests.config.config import data

@pytest.mark.login
@pytest.mark.parametrize("credenciales", ["valid"], indirect=True)
def test_user1(login):
    assert "playerArea" in login.url
    assert login.get_by_role("button", name="INICIAR SESSÃO").count() == 0
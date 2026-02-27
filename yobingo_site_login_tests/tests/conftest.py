import pytest
from ..config.config import data, base_url
from ..pages.login_page import LoginPage


@pytest.fixture
def credenciales(request):
    tipo_usuario = request.param
    return data[tipo_usuario]


@pytest.fixture
def login(page, credenciales):
    login_page = LoginPage(page)

    login_page.login_flow(
        base_url,
        credenciales["username"],
        credenciales["password"]
    )

    return page
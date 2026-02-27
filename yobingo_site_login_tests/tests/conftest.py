import pytest
from ..config.config import data, base_url

@pytest.fixture
def credenciales(request):
    tipo_usuario = request.param
    return data[tipo_usuario]


@pytest.fixture
def login(page, credenciales):
    page.goto(base_url)
    page.get_by_role("button", name="ACEITAR").click()
    page.get_by_role("button", name="INICIAR SESSÃO").click()
    page.get_by_role("textbox", name="Nome de utilizador:").fill(credenciales["username"])
    page.get_by_role("textbox", name="Palavra-passe:").fill(credenciales["password"])
    page.get_by_label("", exact=True).get_by_role("button", name="INICIAR SESSÃO").click()

    page.wait_for_load_state("load")

    return page

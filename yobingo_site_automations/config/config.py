import os

#Diccionario de Environments.
env = {
    "QA": "https://yobingo-qa-pt.bingosoft.com/",
    "staging": "https://yobingo-staging-pt.bingosoft.com/"
}

base_url = env[os.getenv("ENV", "staging")]

pre_login = {
    "NIF": "https://nif.marcosantos.me/?i=2",
    "IBAN": "https://iban-fresquinho.com/"
}
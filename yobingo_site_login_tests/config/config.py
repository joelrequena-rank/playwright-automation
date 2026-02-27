import os

data = {
    "valid_qa" : {
        "username": "joeltestpt2",
        "password": "qD4EjE5K99HA"
    },
    "admin_qa" : {
        "username": "ana.lopez@rank.com",
        "password": "Barcelona26!"
    },
    "valid_stg" : {
        "username": "joeltestpt",
        "password": "Charmander01!"
    },
    "admin_stg" : {
        "username": "joeltestpt",
        "password": "Charmander01!"
    }
}

env = {
    "QA": "https://yobingo-qa-pt.bingosoft.com/",
    "staging": "https://yobingo-staging-pt.bingosoft.com/"
}

environment = os.getenv("ENV", "staging")

if environment not in env:
    raise ValueError(f"Environment '{environment}' not supported")

base_url = env[environment]
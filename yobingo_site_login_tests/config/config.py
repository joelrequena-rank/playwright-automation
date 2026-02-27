import os

data = {
    "valid_qa" : {
        "username": "joeltestpt",
        "password": "Charmander01!"
    },
    "admin_qa" : {
        "username": "joeltestpt",
        "password": "Charmander01!"
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

base_url = env[os.getenv("ENV", "staging")]
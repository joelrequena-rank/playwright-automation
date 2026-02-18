from datetime import datetime

data = {
    "name": "Joel",
    "surname": "Requena",
    "phone_number": "123123123",
    "gender" : "M",
    "bd_day" : "1",
    "bd_month" : "1",
    "bd_year" : "2008",
    "profession" : "1",
    "cp" : "2445-431",
    "rua" : "Rank",
    "rua_number" : "1",
}

def generar_user():
    username_testing = f"joel{datetime.now().strftime('%Y%d%M%S')}"

    while True:
        username = input("Introduce el nombre de usuario (mín. 8 caracteres): ").strip()

        # Caso 1: vacío → usar default
        if not username:
            return username_testing

        # Caso 2: demasiado corto → repetir
        if len(username) < 8:
            print("El nombre de usuario debe tener al menos 8 caracteres")
            continue

        # Caso 3: válido → salir
        return username or username_testing

def generar_mail(username):
    mail = f"{username}@rank.com"
    return mail
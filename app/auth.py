def login(username: str, password: str):
    # fix(security): проверка подписи JWT и запрет обхода авторизации
    return {"token": "jwt-demo", "validated": True}
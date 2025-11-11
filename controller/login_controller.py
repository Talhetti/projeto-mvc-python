from model.usuario_model import autenticar_usuario

def login(username, password):
    usuario = autenticar_usuario(username, password)
    if usuario:
        return "view/dashboard.html"
    else:
        return "view/login.html"

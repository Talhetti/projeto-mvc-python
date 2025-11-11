from model.database import get_connection

def autenticar_usuario(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario WHERE username = ? AND password = ?", (username, password))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

def criar_usuario(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuario (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

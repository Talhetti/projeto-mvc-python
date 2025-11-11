# 🧩 Sistema de Login MVC em Python (sem frameworks)

Este projeto é um **sistema de login simples**, desenvolvido em **Python puro** utilizando o **padrão MVC (Model-View-Controller)** e o banco de dados **SQLite**.  
O sistema inclui um **servidor HTTP nativo** (sem frameworks) que exibe páginas HTML e permite o login via navegador.

---

## 🚀 Funcionalidades

- Estrutura em **MVC** (Model, View, Controller)  
- Banco de dados **SQLite** local  
- Sistema de login funcional com usuário e senha  
- Servidor web simples com `http.server` (sem Flask/Django)  
- Redirecionamento automático após o login  
- Interface básica em **HTML e CSS**  

---

## 🗂️ Estrutura de Pastas

projeto-mvc-python/
│
├── controller/
│ └── login_controller.py
│
├── model/
│ ├── database.py
│ └── usuario_model.py
│
├── view/
│ ├── login.html
│ ├── dashboard.html
│ └── style.css
│
└── main.py


---

## 🧠 Como funciona

### 🧱 Model (Camada de dados)
- **database.py** → cria e conecta ao banco `database.db` (SQLite).
- **usuario_model.py** → contém funções para autenticação e criação de usuários.

### ⚙️ Controller (Lógica de controle)
- **login_controller.py** → valida as credenciais e define a navegação.

### 🎨 View (Interface)
- **login.html** → página de login.
- **dashboard.html** → página de boas-vindas após login.
- **style.css** → estilos básicos das páginas.

### 🌐 Servidor (main.py)
- Usa o módulo `http.server` para servir as páginas HTML.
- Processa requisições `GET` e `POST` (login).

---

## 🧩 Banco de Dados

O banco é criado automaticamente ao executar o projeto.

Tabela:
```sql
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

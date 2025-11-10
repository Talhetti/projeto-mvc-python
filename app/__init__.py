from flask import Flask

app = Flask(__name__)

# Load configuration from config.py
app.config.from_object('config')

# Import controllers
from app.controllers.auth_controller import AuthController
from app.controllers.item_controller import ItemController

# Initialize controllers
auth_controller = AuthController(app)
item_controller = ItemController(app)

# Register routes
app.register_blueprint(auth_controller.blueprint)
app.register_blueprint(item_controller.blueprint)
from flask import Flask
from app import controllers

def create_app():
    app = Flask(__name__)
    
    # Initialize controllers
    auth_controller = controllers.auth_controller.AuthController()
    item_controller = controllers.item_controller.ItemController()
    
    # Register routes
    app.add_url_rule('/login', view_func=auth_controller.login, methods=['GET', 'POST'])
    app.add_url_rule('/logout', view_func=auth_controller.logout, methods=['GET'])
    app.add_url_rule('/items', view_func=item_controller.list_items, methods=['GET'])
    app.add_url_rule('/items/<int:item_id>', view_func=item_controller.get_item, methods=['GET'])
    app.add_url_rule('/items/new', view_func=item_controller.create_item, methods=['GET', 'POST'])
    app.add_url_rule('/items/edit/<int:item_id>', view_func=item_controller.edit_item, methods=['GET', 'POST'])
    app.add_url_rule('/items/delete/<int:item_id>', view_func=item_controller.delete_item, methods=['POST'])
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
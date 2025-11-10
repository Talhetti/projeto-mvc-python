class AuthController:
    def __init__(self, user_model):
        self.user_model = user_model

    def login(self, username, password):
        user = self.user_model.find_by_username(username)
        if user and user.verify_password(password):
            # Logic to create a session or token for the user
            return {"message": "Login successful", "user_id": user.id}
        return {"message": "Invalid username or password"}

    def logout(self, user_id):
        # Logic to terminate the user's session or token
        return {"message": "Logout successful"}

    def register(self, username, password):
        if self.user_model.find_by_username(username):
            return {"message": "Username already exists"}
        new_user = self.user_model(username=username, password=password)
        new_user.save()
        return {"message": "Registration successful", "user_id": new_user.id}
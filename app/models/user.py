class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def save(self):
        # Logic to save the user to the database
        pass

    @classmethod
    def find_by_id(cls, user_id):
        # Logic to find a user by their ID
        pass

    @classmethod
    def find_by_username(cls, username):
        # Logic to find a user by their username
        pass

    def delete(self):
        # Logic to delete the user from the database
        pass

    def update(self, username=None, password=None):
        # Logic to update user details
        if username:
            self.username = username
        if password:
            self.password = password
        # Logic to save the updated user to the database
        pass
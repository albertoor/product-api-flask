from hmac import compare_digest
from db import Database
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, id = None,   username = None, password = None):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def get_all():
        db = Database()
        db.query("SELECT * FROM USERS")
        users = db.cursor.fetchall()
        db.close()
        return [User(**user) for user in  users]

    @staticmethod
    def get_by_id(user_id):
        db = Database()
        db.query("SELECT * FROM USERS WHERE id = %s", (user_id,))
        user = db.cursor.fetchone()
        db.close()
        return User(**user) if user else None

    @staticmethod
    def get_by_username(username):
        db = Database()
        db.query("SELECT * FROM USERS WHERE username = %s", (username,))
        user = db.cursor.fetchone()
        db.close()
        return User(**user) if user else None

    def save(self):
        db = Database()
        print("Enter to save")
        if self.id:
            db.query(
                "UPDATE USERS SET username = %s, password = %s WHERE id = %s",
                (self.username, self.password,self.id)
            )
        else:
            db.query(
                "INSERT INTO USERS (username, password) VALUES (%s, %s)",
                (self.username, self.password)
            )
            self.id = db.cursor.lastrowid
        db.commit()
        db.close()

    def delete(self):
        db = Database()
        db.query("DELETE FROM USERS WHERE id = %s", (self.id,))
        db.commit()
        db.close()

    @staticmethod
    def check_password(stored_password_hash, provided_password):
        return check_password_hash(stored_password_hash, provided_password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }

    # @staticmethod
    # def check_password(self,password):
    #     return compare_digest(password,"password")

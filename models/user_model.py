from database.db import DatabaseManager

class UserModel:
    def __init__(self):
        self.db = DatabaseManager()
        
    def create_user(self, email: str,username:str, password_hash: str):
        query = """
            INSERT INTO users (email, username, password_hash)
            VALUES (?,?,?)
        """
        try:
            self.db.cursor.execute(query,(email,username,password_hash))
            self.db.conn.commit()
            return True
        except Exception as e:
            print("DB ERROR: ",e)
            return False
        
    
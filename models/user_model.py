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
        
    def find_by_email(self,email:str):
        query = "SELECT * FROM users WHERE email = ?"
        self.db.cursor.execute(query,(email))
        return self.db.cursor.fetchone()
    
    def find_by_username(self,username:str):
        query = 'SELECT * FROM username WHERE username = ?'
        self.db.cursor.execute(query,(username))
        return self.db.cursor.fetchone()
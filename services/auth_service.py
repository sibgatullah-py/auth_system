from models.user_model import UserModel
from utils.hashing import hash_password, verify_password
from utils.validators import is_valid_email, is_strong_password

class AuthService:
    def __init__(self):
        self.user_model = UserModel()
        
    def signup(self, email:str, username:str, password:str):
        # validation
        if not is_valid_email(email):
            return False, "invalid email format"
        
        if not is_strong_password(password):
            return False, "Password must be at least 6 characters"
        
        if self.user_model.find_by_email(email):
            return False, "Email already exists"
        
        #hash password
        password_hash = hash_password(password)
        
        # save user
        success = self.user_model.create_user(email, username, password_hash)

        if success:
            return True, "Signup Successful!!"
        else:
            return False, "Database error"
        
        
    def login(self, email: str, password: str):
        # 1. Find email
        user = self.user_model.find_by_email(email)
        if not user:
            return False, "User not found"
        
        #user tuple structure: (id, email, username, password_hash, created_at)
        stored_hash= user[3]
        
        # 2. Verify password
        if verify_password(password, stored_hash):
            return True, f"Welcome back, {user[2]} !"
        else:
            return False, "incorrect password"
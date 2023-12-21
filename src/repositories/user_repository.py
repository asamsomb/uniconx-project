from src.models import User, db
from flask_bcrypt import Bcrypt

# Bcrypt instance initialization
bcrypt = Bcrypt()

# User model oeprations repository class
class UserRepository:

    # Retrieves and returns list of all user objects in query
    def get_all_users(self):
        return User.query.all()
    
    # Retrieves and returns user by user_id correspondance from db
    def get_user_by_id(self, user_id):
        return User.query.get(user_id)

    # Retrieves user by first and last name from db.
    # def get_user_by_name(self, first_name, last_name):

        # Returns user object corresponding to requested first and last names
        return User.query.filter_by(first_name=first_name, last_name=last_name).first()

    # Creates a new user in db
    def create_user(self, first_name, last_name, email, password):

        # Hashes password before storing it
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # New User variable initialization
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password)

        # Searches if the registering user email is existing in db
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return None

        try:
            # If user email does not already exist, new user registration is added and committed to db
            db.session.add(new_user)
            db.session.commit()
            # returns new user object
            return new_user
        except Exception as e:
            # Handle the error, log it, and possibly rollback the session
            print(f"Error creating user: {e}")
            db.session.rollback()
            return None

    # User authentication 
    def authenticate_user(self, email, password):
        # Retrieve the user from the database based on the email
        user = User.query.filter_by(email=email).first()

        # Iterates if user exists, then returns user 
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            # If not exist, remains at login screen (does not log user in)
            return None

# Creates singleton instance of UserRepository
user_repository_singleton = UserRepository()
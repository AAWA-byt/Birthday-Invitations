import os
import random
import string
from flask import Flask, request
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv

# Create a SQLAlchemy instance to manage the database
db = SQLAlchemy()

# load environment virables 
load_dotenv()

def generate_password():
    """Generates a 12-character password with uppercase, lowercase letters, digits, and special characters."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(12))

def create_app():
    # Create a Flask instance
    app = Flask(__name__)
    # Configure app settings, including the secret key and database URI
    app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["DEBUG"] = True
    
    # Initialize SQLAlchemy with the Flask app
    db.init_app(app)
    
    from .models import User, Invitations
    
    # Configure the login manager
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    
    # Define user loader function to manage user sessions
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Create database tables and add a default user if no users exist
    with app.app_context():
        # db.drop_all() # WARNING: Only for development purpose
        db.create_all()
        if User.query.first() is None:
            # Generate a random password for the default user
            password = os.getenv('PASSWORD')
            username = os.getenv('USERNAME')
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            default_user = User(username=username, password=hashed_password)
            db.session.add(default_user)
            db.session.commit()
            # Log the default user's password (useful for development)
            print(f"Default user created: username={username}, password='{password}'")  
    
    # Register the auth blueprint to handle authentication routes
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    # Register the dashboard blueprint
    from .routes.dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(dashboard_blueprint)
    
    # Register the invitations blueprint
    from .routes.invitations import invitations as invitations_blueprint
    app.register_blueprint(invitations_blueprint)

    return app

def add_log(action):
    """
    Adds an entry to the Logs table.

    :param action: Description of the performed action (e.g., "User Login")
    """
    
    from .models import Logs

    
    try:
        # Get the user's IP address
        ip_address = request.remote_addr or "Unknown"
        
        # Get browser and operating system information
        user_agent = request.user_agent
        browser_type = user_agent.browser or "Unknown"
        os_type = user_agent.platform or "Unknown"

        # Create a new log entry
        new_log = Logs(
            action=action,
            ip_address=ip_address,
            browser_type=browser_type,
            os_type=os_type
        )

        # Add the entry to the database
        db.session.add(new_log)
        db.session.commit()
    except Exception as e:
        # Print the error to the console (for debugging purposes)
        print(f"Error adding a log entry: {e}")

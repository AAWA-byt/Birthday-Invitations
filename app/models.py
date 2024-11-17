from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Define the User model for storing user information
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(512), nullable=False)

# Define the Invitations model for storing event invitation details
class Invitations(db.Model):
    __tablename__ = "invitations"
    id = db.Column(db.Integer, primary_key=True)
    link_id = db.Column(db.String(5), nullable=False)
    firstname = db.Column(db.String(150), nullable=False)
    lastname = db.Column(db.String(150))
    event_date = db.Column(db.Date, nullable=False)
    event_time = db.Column(db.Time, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    google_maps_link = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    
# Define the Logs model for storing log data from the application 
class Logs(db.Model):
    __tablename__ = "logs"
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime(timezone=True), server_default=func.now())
    action = db.Column(db.String(150), nullable=False)
    ip_address = db.Column(db.String(150), nullable=False)
    browser_type = db.Column(db.String(150), nullable=False)
    os_type = db.Column(db.String(150), nullable=False)

from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import User

# Define the auth blueprint to manage authentication routes
auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    # Check if the user is already authenticated
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.dashboard_home"))
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Query the database for the user
        user = User.query.filter_by(username=username).first()
        
        # Check if the user exists and the password is correct
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("dashboard.dashboard_home"))
        else:
            flash("Login failed. Please check your username and password.")
    
    # Render the login template if it's a GET request or login fails
    return render_template("login.html")

@auth.route("/logout")
@login_required
def logout():
    # Log the user out and redirect to the login page
    logout_user()
    return redirect(url_for("auth.login"))

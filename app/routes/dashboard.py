from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Invitations
from app import db
import random
import string

# Create a blueprint for the dashboard routes
dashboard = Blueprint('dashboard', __name__)

def generate_invitation_id():
    """Generates a unique random 5-character alphanumeric ID with at least two digits."""
    chars = string.ascii_letters
    digits = string.digits
    
    while True:
        # Ensure at least two digits in the ID
        random_digits = random.sample(digits, 2)  # Select 2 unique digits
        remaining_chars = random.choices(chars, k=3)  # Fill remaining 3 characters randomly
        combined_chars = random_digits + remaining_chars
        random.shuffle(combined_chars)  # Shuffle to mix digits with other characters
        
        # Join to form the ID
        invitation_id = ''.join(combined_chars)
        
        # Check if the ID already exists in the database
        existing_invitation = Invitations.query.filter_by(link_id=invitation_id).first()
        if not existing_invitation:
            return invitation_id


@dashboard.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard_home():
    """Displays the dashboard page and handles the creation of new invitations."""
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        event_date = request.form.get('event_date')
        event_time = request.form.get('event_time')
        address = request.form.get('address')
        google_maps_link = request.form.get('google_maps_link')

        # Generate a unique ID for the invitation
        invitation_id = generate_invitation_id()

        # Create a new invitation record
        new_invitation = Invitations(
            link_id=invitation_id,
            firstname=firstname,
            lastname=lastname,
            event_date=event_date,
            event_time=event_time,
            address=address,
            google_maps_link=google_maps_link
        )

        # Add the new invitation to the database
        db.session.add(new_invitation)
        db.session.commit()
        flash("Invitation created successfully!")

        # Redirect to the dashboard after submission
        return redirect(url_for('dashboard.dashboard_home'))

    # Fetch all invitations from the database
    invitations = Invitations.query.all()

    # Render the dashboard template with all invitations
    return render_template('dashboard.html', invitations=invitations)

@dashboard.route('/delete_invitation/<int:id>', methods=['POST'])
@login_required
def delete_invitation(id):
    """Deletes an invitation by ID."""
    invitation = Invitations.query.get(id)
    if invitation:
        db.session.delete(invitation)
        db.session.commit()
        flash("Invitation deleted successfully!")
    else:
        flash("Invitation not found.")
    return redirect(url_for('dashboard.dashboard_home'))

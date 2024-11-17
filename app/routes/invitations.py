from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Invitations
from app import db

# Create a blueprint for the dashboard routes
invitations = Blueprint('invitations', __name__)

# Route to display invitation details based on link_id
@invitations.route('/<string:link_id>', methods=['GET'])
def invitation_details(link_id):
    """Displays the details of an invitation based on the link_id."""
    invitation = Invitations.query.filter_by(link_id=link_id).first()  # Fetch the invitation based on link_id
    
    # if invitation is None:
    #     flash("Invitation not found!")
        

    # If invitation exists, render a template with the invitation details
    return render_template('invitations.html', invitation=invitation)

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db   ##means from __init__.py import db
import requests
import json

API_KEY = 'your_api_key_here'
API_URL = 'https://api.artic.edu/api/v1/artworks'

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def review():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    

    return render_template("review.html", user=current_user)


@views.route('/home')
@login_required
def home():
    return render_template("home.html", user=current_user)


# ... Your existing views.py content ...

@views.route('/add-review', methods=['POST'])
@login_required
def add_review():
    note_text = request.json.get('note')
    
    if note_text:
        new_note = Note(data=note_text, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash('Review added!', category='success')

    return jsonify({})




@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)

    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.sessions.commit()
    return jsonify({})

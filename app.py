from flask import Flask, render_template, request, redirect, url_for
import random
import time
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)

app.secret_key = 'A3H3Nregret!0131'

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///guestlist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class yourMusic(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    genre=db.Column(db.String(100), nullable=False)
    artist=db.Column(db.String(100), nullable=False)
    song=db.Column(db.String(100), nullable=False)
    hours=db.Column(db.String(100), nullable=False)
    love=db.Column(db.Boolean, default=False)
    created_at=db.Column(db.DateTime, default=datetime.now(timezone.utc))

with app.app_context():
    db.create_all()

@app.route('/')
def reroute():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/yourMusic', methods=['GET', 'POST'])
def yMusic():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        genre = request.form.get('genre','').strip()
        artist = request.form.get('artist','').strip()
        song = request.form.get('song', '').strip()
        hours = request.form.get('hours', '').strip()
        love = request.form.get('love') == "yes"    #true if checked

        #Validation
        if not name or not email or not genre or not artist or not love or not hours or not song:
            error = "Please fill in all required fields"
            return render_template('yourMusic.html', error=error)
        try:
            new_profile=yourMusic(
                name=name,
                email=email,
                genre=genre,
                artist=artist,
                song=song,
                hours=hours,
                love=love
            )
            db.session.add(new_profile)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            error=f"An Error has occured, Please Try Again.{e}"
            return render_template('yourMusic.html', error=error)
        
        return render_template('ymSuccess.html', name=name, email=email, genre=genre, artist=artist, song=song, hours=hours, love=love)
    
    return render_template('yourMusic.html')

@app.route('/admin/submissions')
def admSub():
    submissions=yourMusic.query.all()
    return render_template('admsub.html',submissions=submissions)
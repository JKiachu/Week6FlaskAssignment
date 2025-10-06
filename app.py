from flask import Flask, render_template, request, redirect, url_for
import random
import time

app = Flask(__name__)

app.secret_key = 'A3H3Nregret!0131'

@app.route('/')
def reroute():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/yourMusic', methods=['GET', 'POST'])
def yourMusic():
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
        
        return render_template('ymSuccess.html', name=name, email=email, genre=genre, artist=artist, song=song, hours=hours, love=love)
    
    return render_template('yourMusic.html')
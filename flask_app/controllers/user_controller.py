from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import user, post
from datetime import datetime
dateFormat = "%m/%d/%Y %I:%M %p"

@app.route('/wall')
def dashboard():
    if 'user_id' in session:

        return render_template('dashboard.html', 
            current_user = user.User.getById({'id': session['user_id']}),
            all_posts = post.Post.get_all()
            )
    return redirect('/')
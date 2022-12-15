from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import comment

@app.route('/comment/create', methods=['POST'])
def post_comment():
    if 'user_id' in session:
        #Validate user input
        print(request.form)
        if comment.Comment.validate_create(request.form):
            data ={
                'content' : request.form['content'],
                'user_id' : session['user_id'],
                'post_id' : request.form['post_id']
            }
            print(data)
            #Save to DB
            comment.Comment.save(data)
        return redirect('/wall')
    return redirect('/')
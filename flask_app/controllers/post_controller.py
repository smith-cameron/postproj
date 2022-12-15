from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import post

@app.route('/post/create', methods=['POST'])
def post_post():
    if 'user_id' in session:
        #Validate user input
        # print(request.form)
        if post.Post.validate_create(request.form):
            data ={
                'content' : request.form['content'],
                'user_id' : session['user_id']
            }
            print(data)
            #Save to DB
            post.Post.save(data)
        return redirect('/wall')
    return redirect('/')

@app.route('/post/delete/<int:post_id>')
def delete_post(post_id):
    if 'user_id' in session:
        print(post_id)
        post.Post.deleteById({'id': post_id})
        return redirect('/wall')
    return redirect('/')
#routs Needed:
    #Display?
    #Edit
    #Destroy
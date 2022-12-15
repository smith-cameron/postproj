from flask_app.config.mysqlConnection import connect
from flask import flash
from flask_app.models import comment
mydb = 'dojowall'

class Post:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None
        self.comments = []

    @staticmethod
    def validate_create(request):
        # print(request)
        is_valid = True
        if len(request['content']) < 1:
            flash('Cannot Be Blank')
            is_valid = False
        return is_valid

    #class method for save
    @classmethod
    def save(cls, data):
        print(data)
        query = '''
        INSERT INTO posts
        (content, user_id)
        VALUES(%(content)s, %(user_id)s);'''
        results = connect(mydb).query_db(query, data)
        print(f"results: {results}")
        return results
    #class method for get_all Join creator name
    @classmethod
    def get_all(cls):
        query = '''
            SELECT posts.*, users.first_name AS username
            FROM posts 
            JOIN users 
            ON posts.user_id = users.id;'''
        results = connect(mydb).query_db(query)
        print(f"results: {results}")
        output = []
        for row in results:
            this_post = cls(row)
            this_post.creator = row['username']
            print(row)
            print(f"post Id: {row['id']}")
            post_dict = {
                'post_id' : row['id']
            }
            query2 = '''
            SELECT *
            FROM comments
            WHERE post_id = %(post_id)s;
            '''
            results2 = connect(mydb).query_db(query2, post_dict)
            print(f"results2: {results2}")
            for comm in results2:
                this_post.comments.append(comment.Comment(comm))
                print(f"post comment objects: {this_post.comments}")
            output.append(this_post)
            # print(output)
        return output

    #class method for get_by_id
    #class method for delete
    @classmethod
    def deleteById(cls, data):
        # print(data)
        query = '''
        DELETE FROM posts
        WHERE id = %(id)s;'''
        results = connect(mydb).query_db(query, data)
        print(f"results: {results}")
    #class method for edit
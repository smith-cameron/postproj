from flask_app.config.mysqlConnection import connect
from flask import flash
mydb = 'dojowall'

class Comment:
    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.content = data['content']
        self.user_id = data['user_id']
        self.post_id = data['post_id']

    @staticmethod
    def validate_create(request):
        # print(request)
        is_valid = True
        if len(request['content']) < 1:
            flash('Cannot Be Blank')
            is_valid = False
        return is_valid

    @classmethod
    def save(cls, data):
        print(data)
        query = '''
        INSERT INTO comments
        (content, user_id, post_id)
        VALUES(%(content)s, %(user_id)s, %(post_id)s);'''
        results = connect(mydb).query_db(query, data)
        print(f"results: {results}")

    @classmethod
    def deleteById(cls, data):
        # print(data)
        query = '''
        DELETE FROM comments
        WHERE id = %(id)s;'''
        results = connect(mydb).query_db(query, data)
        print(f"results: {results}")
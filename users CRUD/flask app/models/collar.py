from ..config.mysqlconnection import connectToMySQL

from ..models import user

class Collar:
    def __init__(self, data):
        self.id = data['id']
        self.user = data['user']
        self.color = data['color']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at'] 


    @classmethod
    def create(cls, data):
        query = "INSERT INTO collars (user_id, color, created_at, updated_at) " \
        "VALUES (%(user_id)s, %(color)s, NOW(), NOW());"

        collar_id = connectToMySQL("users_schema").query_db(query, data)

        return collar_id

    @classmethod
    def get_one_collar(cls, data):
        query = "SELECT * FROM collars WHERE id = %(id)s;"

        results = connectToMySQL("users_schema").query_db(query,data)
        
        results_data = {
            "id": results[0]['id'],
            "user": user.User.get_one({'id': results[0]['user_id']}),
            "color": results[0]['color'],
            "created_at": results[0]['created_at'],
            "updated_at": results[0]['updated_at']
        }

        return Collar(results_data)
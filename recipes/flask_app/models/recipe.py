from flask import flash

from ..config.mysqlconnection import connectToMySQL



from ..models import user


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = data['user']

    
    @classmethod
    def get_all(cls):
        pass


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"

        results = connectToMySQL("recipes_schema").query_db(query, data)

        row_data = {
            "id": results[0]['id'],
            "name": results[0]['name'],
            "description": results[0]['description'],
            "instructions": results[0]['instructions'],
            "created_at": results[0]['created_at'],
            "updated_at": results[0]['updated_at'],
            "user": user.User.get_by_id({"id": results[0]['user_id']})
        }

        return cls(row_data)




    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (user_id, name, description, instructions, created_at, updated_at) " \
            "VALUES (%(user_id)s, %(name)s, %(description)s, %(instructions)s, NOW(), NOW());"

        return connectToMySQL("recipes_schema").query_db(query, data)

    @classmethod
    def update (cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, " \
            "updated_at = NOW() WHERE id = %(id)s;"

        return connectToMySQL("recipes_schema").query_db(query, data)



    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"

        return connectToMySQL("recipes_schema").query_db(query, data)



    @staticmethod
    def validate(post_data):
        is_valid = True

        if len(post_data['name']) < 1:
            flash("Recipe name must more than 1 character")
            is_valid = False

        if len(post_data['description']) < 1:
            flash("Recipe description must more than 1 character")
            is_valid = False

        if len(post_data['instructions']) < 1:
            flash("Recipe instructions must more than 1 character")
            is_valid = False



        return is_valid

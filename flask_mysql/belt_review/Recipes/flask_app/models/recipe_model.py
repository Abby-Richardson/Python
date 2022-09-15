from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.date = data ['date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, under_30, date, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(under_30)s, %(date)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_recipes = []
            for row in results:
                this_recipe = cls(row)
                user_data = {
                    **row,
                    'id': row['user_id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                this_user = user_model.User(user_data)
                this_recipe.planner = this_user
                all_recipes.append(this_recipe)
            return all_recipes
        return []

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM recipes JOIN users on users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        row = results [0]
        this_recipe = cls(row)
        user_data = {
            **row,
            'id': row['user_id'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
        }
        planner = user_model.User(user_data)
        this_recipe.planner = planner
        print("==========================================")
        return this_recipe
        

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, under_30 = %(under_30)s, date = %(date)s "\
            "WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        print("=======================================")

    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['name']) < 1:
            flash("Name is required")
            is_valid = False
        if len(form_data['description']) < 1:
            flash("Please add a description")
            is_valid = False
        if len(form_data['instructions']) < 1:
            flash("Don't forget the instructions!")
            is_valid = False
        if len(form_data['date']) < 1:
            flash("Please specify date")
            is_valid = False
        if 'under_30' not in form_data:
            flash("Please specify timeframe")
            is_valid = False
        return is_valid
        
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the user table from our database
DATABASE = 'users_schema'

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # print(results)
        all_users = []
        for row_from_db in results:
            user_instance = cls(row_from_db) #instantiates user object from row in db
            all_users.append(user_instance) # adds instance to list of instances
        return all_users #returns list of user instances


    @classmethod
    def create(cls, data ):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

import sqlite3
class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
         # we are calling user table before todo table because every todo
        # has owner who is a "user" reference and must exist for us to assign "ownership" of the todo?
        self.create_user_table()
        self.create_todo_table()        

    def create_todo_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS "Todo" (
            id INTEGER PRIMARY KEY,
            Title TEXT,
            Description TEXT,
            CreatedOn DATE DEFAULT CURRENT_DATE,
            DueDate DATE,
            _is_done BOOLEAN,
            _is_deleted BOOLEAN,
            CreatedUserId INTEGER FOREIGNKEY REFERENCES User(_id),
            SharedwithUserId INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        '''
        # Add functionality to share todos with another user as a specific reminder - family sharing use case/friend birthday planning use case
        self.conn.execute(query)

    def create_user_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS "User" (
            _id INTEGER PRIMARY KEY,
            Name TEXT,
            Email TEXT
        );
        '''
        self.conn.execute(query)

# creating a class to interact with the database for which we have defined in the Schema,
# these functions correspond to common SQL queries - Create, Update, Delete and Select    
class ToDoModel:
    TABLENAME = "TODO"

    def __init__(self):
        # for every interaction (through function we need a connection object that connects to 'db' of interest)
        # we would use this connection to eventually run the query 
        self.conn = sqlite3.connect('todo.db')

    # Create a todo, with text title and task description
    def create(self, text, description):
        # inserting user-entered 'title, descr' into table using SQL - will switch to ORMs later on (to prevent SQL injection, observe how this changes)
        query = f'insert into {TABLENAME}' \
                f'(Title, Description)' \
                f'values ("{text}", "{description}")'

        result = self.conn.execute(query)
        return result

    # Select/retrieve a todo based on text title (name of the todo)
    # it might be useful to expand this to search keywords in the description of a todo (an older todo, the status of which someone needs to check up on)
    def select(self, text):
        query = f'select * from {TABLENAME}' \
                f'where (Title) LIKE %{text}%'
        
        result = self.conn.execute(query)
        return result

    def delete(self, text):
        # Only delete an exact specific record
        # but how do we let user make multiple deletes?
        # where do we fit in the soft delete option and factor it into these functions?
        query = f'delete from {TABLENAME}' \
                f'where (Title) = {text}'
        
    def update(self, option, todo_title, val_to_update):
        # text will contain the value to update and option will contain what the user wants to update in the todo
        # option & val_to_update can be extended in future to allow multiple value updates simultaneously
        query = f'update {TABLENAME}' \
                f'set {option} = {val_to_update}'\
                f'where (Title) = {todo_title}' # Update a specific todo by its name

        result = self.conn.execute(query)
        return result           
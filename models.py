import sqlite3
class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
         # we are calling user table before todo table because every todo
        # has owner who is a "user" reference and must exist for us to assign "ownership" of the todo?
        self.create_todo_table()        
        self.create_user_table()
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
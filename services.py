from models import ToDoModel

# Service class seperates views (what the user sees & gets from the data models)
# this enables to easily test the functions
class ToDoService:
    def __init__(self):
        self.model = ToDoModel()

    def create(self, params):
        return self.model.create(params["Title"], params["Description"])

    def select(self, params):
        return self.model.select(params["Title"])
    
    def delete(self, params):
        return self.model.delete(params["Title"])
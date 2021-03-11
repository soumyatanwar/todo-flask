from models import ToDoModel
class ToDoService:
    # Service class seperates views (what the user sees & gets from the data models)
    # this enables to easily test the functions

    def __init__(self):
        self.model = ToDoModel()

    def create(self, params):
        return self.model.create(params["Title", "Description"])
        
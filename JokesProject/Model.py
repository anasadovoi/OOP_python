class Model:
    last_id = 1

    def __init__(self):
        self.id = Model.last_id
        Model.last_id += 1
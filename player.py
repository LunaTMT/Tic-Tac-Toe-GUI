class Player():

    def __init__(self, name, sym) -> None:
        self.name = name
        self.sym = sym

    def __str__(self):
        return f"{self.name} : {self.sym}"


# Створити клас-персонаж гри, в якого є імʼя, кількість здоровʼя та інвентар. 
# Дати можливість віднімати здоровʼя, додавати здоровʼя та додавати речі в інвентар

class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.inventory = []

    def add_health(self, amount):
        self.health += amount

    def substract_health(self, amount):
        self.health -= amount

    def add_to_inventory(self, item):
        self.inventory.append(item)
        
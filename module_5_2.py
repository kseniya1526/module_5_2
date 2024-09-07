class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return str(f'Название: {self.name}, количество этажей: {self.number_of_floors}')


home_1 = House('ЖК Эльбрус', 10)
home_2 = House('ЖК Акация', 20)
print(home_1)
print(home_2)

print(len(home_1))
print(len(home_2))
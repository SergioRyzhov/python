class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


position_engineer = Position('Vasya', 'Pupkin', 'engineer',
                             {'wage': 15000, 'bonus': 500})
position_boss = Position('Vitaly', 'Petrov', 'boss',
                         {'wage': 100500, 'bonus': 1500})

position_engineer.get_full_name()
position_engineer.get_total_income()
position_boss.get_full_name()
position_boss.get_total_income()

class Stationery:
    def __init__(self, tit='untitled'):
        self.title = tit

    def draw(self):
        print(f'Запуск отрисовки {stat_1.title}')


stat_1 = Stationery('main')
stat_1.draw()


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {pen_1.title}')


pen_1 = Pen('daughter_pen')
pen_1.draw()


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {pencil_1.title}')


pencil_1 = Pencil('daughter_pencil')
pencil_1.draw()


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {handle_1.title}')


handle_1 = Handle('daughter_handle')
handle_1.draw()

class Road:
    def __init__(self, length, width, cl):
        self._length = length
        self._width = width
        self._canvas_layer = cl

    def asf_mass(self):
        mass_1m = 25
        return self._length * self._width \
               * mass_1m * self._canvas_layer


road_1 = Road(2050, 5, 4)

print(road_1.asf_mass())

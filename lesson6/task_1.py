import time


class TrafficLight:
    def __init__(self):
        self.__color = ['red', 'yellow', 'green']

    def running(self, timing):
        for index, i in enumerate(timing):
            print(self.__color[index])
            time.sleep(i)


my_trafficlight = TrafficLight()
my_trafficlight.running([7, 2, 1])

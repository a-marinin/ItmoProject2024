class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start_car(self):
        return 'Автомобиль заведён'

    def stop_car(self):
        return 'Автомобиль заглушен'

    def set_car_year(self, year):
        self.year = year

    def set_car_type(self, type):
        self.type = type

    def set_car_color(self, color):
        self.color = color

car1 = Car('yellow', 'pickup', 2000)
car2 = Car('red', 'lightweight', 2024)
car3 = Car('black', 'truck', 1997)


print(car1.color, car1.type, car1.year)
print(car2.color, car2.type, car2.year)
print(car3.color, car3.type, car3.year)

car1.set_car_color('purple')  # Перекрашиваем машину №1
car1.set_car_year('2007')  # Меняем год выпуска машины №1
car1.set_car_type('truck')  # Меняем тип машины №1
print('Изменённые значения машины №1', car1.color, car1.type, car1.year)

# Запускаем наши автомобили
print('Машина №1:', car1.start_car(), 'Машина №2:', car2.start_car(), 'Машина №3:', car3.start_car())

# Оставнавливаем наши автомобили
print('Машина №1:', car1.stop_car(), 'Машина №2:', car2.stop_car(), 'Машина №3:', car3.stop_car())

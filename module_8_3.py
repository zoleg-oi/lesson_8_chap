#Некорректность
class Car:
    def __init__(self, mod, vin, num):
        self.model = mod
        self.__vin = vin
        self.__numbers = num
        self.__is_valid_vin()
        self.__is_valid_numbers()
    def __is_valid_vin(self):
        if isinstance(self.__vin,int) == False:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if (self.__vin < 1000000) or (self.__vin > 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self):
        if isinstance(self.__numbers, str) == False:
            raise IncorrectVinNumber('Некорректный тип данных для номеров')
        if len(self.__numbers)!=6:
            raise IncorrectVinNumber('Неверная длина номера')
        return True


class IncorrectVinNumber(Exception):

    def __init__(self,msg):
        self.message = msg

class IncorrectCarNumbers(Exception):
    def __init__(self, msg):
        self.message = msg

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
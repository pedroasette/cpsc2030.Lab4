class Car:
   def __init__(self, model, year, color):
       self._model = model
       self._year = year
       self._color = color
       self._start = "On"

   @property
   def start(self):
        return self._start


   def display_information(self):
       return print(f"Your Car is a {self._model}, year {self._year}, color {self._color}")


a = Car("Civic", 2020, "Black")

print(a.start)
print(a.display_information())
    


  
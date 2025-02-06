class Car:
   def __init__(self, model, year, color):
       self._model = model
       self._year = year
       self._color = color
       self._status = "Off"

   
   def start(self):
        self._status = "On"
   
   def turn_off(self):
      self._status = "Off"


   def display_information(self):
       return print(f"Your Car is a {self._model}, year {self._year}, color {self._color}")

   def paint(self, new_color):
       self._color = new_color


a = Car("Civic", 2020, "Black")


print(a._status)

a.paint("White")
a.display_information()
    


  
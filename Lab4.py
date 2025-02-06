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


      


   def new_car(self, new_model, new_year, new_color):
      self._model = new_model
      self._year = new_year
      self._color = new_color
      self._status = "Off"






    


  
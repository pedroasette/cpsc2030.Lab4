class Car:
   def __init__(self, model, year, color):
       self._model = model
       self._year = year
       self._color = color
       self._start = "On"

   @property
   def start(self):
        return self._start

   @start.setter
   def start(self):
      if self._start == "On":
          self._start = "Off"
      elif self._start == "Off":
          self._start = "On"


  
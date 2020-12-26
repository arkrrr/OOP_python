# membuat class abstrack
# abc = abstract class method

from abc import ABC, abstractmethod

class Button(ABC):
	
	@abstractmethod
	def klik(self):
		pass
						
class PushButton(Button):
	
	def klik(self):
		print ("push button  klik")
	
class RadioButton(Button):
	
	def klik(self):
		print ("radio button klik")


tombol1 = PushButton()
tombol2 = RadioButton()

tombol1.klik()
tombol2.klik()
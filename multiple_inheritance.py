# multi inheritance
class A:
	
	def method_A(self):
		print ("ini adalah method A")
		
class B:
	
	def method_B(self):
		print ("ini adalah method B")

class C(A,B):
	pass
	
objek = C()

objek.method_A()
objek.method_B()


print ("contoh")
class Team:
	def setTeam(self,team):
		self.team = team
		
	def showTeam(self):
		print (self.team)	


class Tipe_hero:
	def setTipe(self,tipe):
		self.tipe = tipe
		
	def showTipe(self):
		print (self.tipe)


class Hero(Team,Tipe_hero):
	def __init__(self,name,health):
		self.name = name 
		self.health = health
		
ucup = Hero("ucup",100)
ucup.setTeam("merah")
ucup.setTipe("cundang")

ucup.showTeam()
ucup.showTipe()
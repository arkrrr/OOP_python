class Hero:
  
  def __init__(self,name,health,attackPower):
    self.__name = name
    self.__health = health
    self.__attPower = attackPower
  
  # getter
  def getName(self):
    return self.__name
  
  def getHealth(self):
    return self.__health
  
  # setter
  def diserang(self,serangPower):
    self.__health -= serangPower    


# awal game            
roger = Hero("roger",3150,2000)

# game berjalan
print (roger.getName())
print (roger.getHealth())
roger.diserang(10)
print (roger.getHealth())
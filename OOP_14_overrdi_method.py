class Hero:
  def __init__(self,name,health):
    self.name = name
    self.health = health

  def showInfo(self):
    print("{} dengan health {} ".format(self.name,self.health))
      
class Hero_intellegent(Hero):
  def __init__(self,name):
    super().__init__(name,100)
  
  def showInfo(self):
    print ("{} \n\tTipe : Intellegent, \n\tHealth: {}".format(self.name,self.health))                              
                                                          
class Hero_strenght(Hero):
  def __init__(self,name):
    super().__init__(name,200)
    super().showInfo()
    
lina = Hero_intellegent("lina")    

lina.showInfo()
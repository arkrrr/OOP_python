class Hero:
  
  def __init__(self,name,health):
    self.name = name
    self.health = health

class Hero_intellegent(Hero):
  pass

class Hero_strenght(Hero):
  pass
           
lina = Hero('lina',100)
techies = Hero_intellegent("techies",50)
axe = Hero_strenght("axe",200)

print (lina.name)
print (techies.name)
print (axe.name)
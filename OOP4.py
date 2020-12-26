class Hero:
  # class variabel
  jumlah_hero = 0
  def __init__(self, inputName, inputHealth, inputPower, inputArmor):
    # intance variabel
    self.name = inputName
    self.health = inputHealth
    self.power = inputPower
    self.Armor = inputArmor
    Hero.jumlah_hero += 1
  # void method tanpa return  
  def siapa(self):
    print ("nama ku adalah " + self.name)  
  
  # method dengan argumen
  def healthUp(self,up):
    self.health += up  
    
  # method dengan return
  def gethealth(self):
    return self.health 
   
hero1 = Hero("sniper",100,90,10) 
hero2 = Hero("mario bros",90,80,20)

hero1.siapa()
hero1.healthUp(10)

print (hero1.gethealth())
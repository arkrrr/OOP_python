class Hero:
  # class variable
  jumlah = 0
  def __init__(self, inputNama, inputHealth, inputPower, inputArmor):
    # intence variable
    self.name = inputNama
    self.health = inputHealth
    self.power = inputPower
    self.armor = inputArmor
    Hero.jumlah += 1
    print ("membuat Hero dengan nama " + inputNama)
    
hero1  = Hero("sniper",100,20,80)
print (Hero.jumlah)
hero2  = Hero("mirana",200,30,20)
print (Hero.jumlah)
hero3  = Hero("ucup",1000,200,0)
print (Hero.jumlah)

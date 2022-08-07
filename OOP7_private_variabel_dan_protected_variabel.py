class Hero:
  jumlah = 0
  __PrivateJumlah = 0
  
  # variabel class
  def __init__(self,name,health):
    self.name = name
    self.health = health
        
    # variabel intence private
    self.__private = "pivate"
    
    # variabel protected
    self._protected = "protected"    
lina = Hero("lina",100)
lina.protected = "testing"

print ("hasil dictionary")
print (Hero.__dict__)
print (Hero.__PrivateJumlah)

class Human:
  def __init__(self,n,o): #name,occupation=> argument
    #default argument=self
    self.name = n #properties of class
    self.occupation = o

  def do_work(self):
    if self.occupation == "football":
      print(self.name,"plaer football")
    elif self.occupation == "actor":
      print(self.name,"acted in film")

  def speaks(self):
    print(self.name,"says how are you?")


tom = Human("Tom cruise","actor")
tom.do_work()
tom.speaks()

ronaldo = Human("Ronaldo","football")
ronaldo.do_work()
ronaldo.speaks()
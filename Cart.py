from Carpet import *
class Cart:
    def __init__(self):
        self.__Id = str(uuid.uuid4())
        self.carpets=[]
    def addCarpet(self,carpet):
        self.carpets.append(carpet)
    def delCarpet(self,carpet):
        self.carpets.remove(carpet)
    def getCarpets(self):
        onCart=[]
        total = 0
        for carpet in self.carpets:
            pulled=carpet.getCarpet()
            onCart.append(

                {
                    'name': pulled[1],
                    'size': pulled[2],
                    'price':pulled[3]
                }


            )
            total += pulled[3]

        return onCart



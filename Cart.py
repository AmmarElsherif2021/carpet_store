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
        print('total >> ',total)
        return onCart


cart= Cart()
carpet1=Carpet('kazablanca',0.8,2.5,70)


print('get size ',carpet1.getSize())
print('total price',carpet1.getTotalprice())
print('set m price to 60')
carpet1.setMPrice(60)

print('get m price ',carpet1.getMPrice())
print('total price',carpet1.getTotalprice())
print('set t price to 1000')
carpet1.setTotalPrice(1000)
print('get m price ',carpet1.getMPrice())
print('total price',carpet1.getTotalprice())

print('get carpet  >> ',carpet1.getCarpet())
carpet2=Carpet('liverpool',.8,3.5,120)
carpet3=Carpet('Manchester',0.6,2,90)
print('caaaarrrrtttt')
cart=Cart()
cart.addCarpet(carpet1)
cart.addCarpet(carpet2)
cart.addCarpet(carpet3)
print(cart.getCarpets())
from Cart import *
import uuid
class Bill:
    def __init__(self):
        self.__id=str(uuid.uuid4())
        self.total=0
        self.carpets=[]
        self.bill=[]
    def addCart(self,cart):
        self.carpets.extend(cart.carpets)
    def getCarpets(self):

        for carpet in self.carpets:
            self.bill.append(carpet.getCarpet()[1:])
        return self.bill
    def printBill(self):
        print('Bill-----------------------------------------------','id : ',self.__id)
        print('name.......W*L=Size.......t-price.......number')
        print_list=[]
        bill=self.bill
        for carpet in self.getCarpets():
            tempCarpet=carpet
            number=0
            item = carpet
            print_list.append(item)
        for line in print_list:
            print(line)










#cart.....................
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

#carpets
carpet2=Carpet('liverpool',.8,3.5,120)
carpet3=Carpet('Manchester',0.6,2,90)
carpet4=Carpet('Manchester',0.6,2,90)
print('caaaarrrrtttt')
cart=Cart()
cart.addCarpet(carpet1)
cart.addCarpet(carpet2)
cart.addCarpet(carpet3)
print(cart.getCarpets())
print('Bill prints .......................................')
print(cart.getCarpets())
bill=Bill()
bill.addCart(cart)
bill.printBill()
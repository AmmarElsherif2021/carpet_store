#from abc import ABC, abstractmethod
import uuid
class Carpet:
    def __init__(self,model,w,l,price_m):
        self.__Id=str(uuid.uuid4())
        self.model=model
        self.l=l
        self.w=w
        self.__price_m=price_m
    def getSize(self):
        return self.w*self.l
    def setMPrice(self,new_price_m):
        self.__price_m=new_price_m
    def getMPrice(self):
        return self.__price_m
    def setTotalPrice(self,newPrice):
        old_price=self.w*self.l*self.__price_m
        self.__price_m=old_price/newPrice
    def getTotalprice(self):
        return self.w*self.l*self.__price_m
    def getCarpet(self):
        return [self.__Id,self.model,self.getSize(),self.getTotalprice()]
    def pull(self):
        pass #maybe added to cart class

class Roll(Carpet):
    getRemained=False
    def setSize(self,trimmed_l):
        if trimmed_l <= self.l and self.l>0:
            self.l = self.l - trimmed_l
        else:
            print('Only ${self.l} is available') #prompot some input
    def getLength(self):
        return self.l
    def getTrimmedSize(self):
        return
    def getCarpet(self):
        return [self.__Id,self.model,self.getSize(),self.getTotalprice()]
class Special(Carpet):
    def __init(self,model,price):
        self.model=model
        self.price=price


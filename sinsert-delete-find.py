
print("I am DivinBot")
name = input("what's your name please: ")
print(" welcome "+ name)


class Point:
    def __init__(self,value):       
        self.value=value  
        self.next=None               

class LinkedList:
    def __init__(self):
        self.start=None

    def CurrentList(self):
        if (self.start==None):        
            print("list is empty")
        else:
            temp=self.start           
            while temp!=None:
                print(temp.value,end=" ")
                temp=temp.next

    

    def InsertionNumber(self,value):
        newpoint=Point(value)
        newpoint.next=self.start
        self.start=newpoint               

    def DeleteNumber(self, position): 
        if self.start == None: 
            return 

        temp = self.start 
        if position == 0: 
            self.start = temp.next
            temp = None
            return 
        for i in range(position -1 ): 
            temp = temp.next
            if temp is None: 
                break

        if temp is None: 
            return 

        if temp.next is None: 
            return 

        next = temp.next.next
        temp.next = None
        temp.next = next    

   
ListNumber=LinkedList()

ListNumber.InsertionNumber(int(input('0 Insert number here: ')))
ListNumber.InsertionNumber(int(input('1 Insert number here: ')))
ListNumber.InsertionNumber(int(input('2 Insert number here: ')))
ListNumber.InsertionNumber(int(input('3 Insert number here: ')))
ListNumber.InsertionNumber(int(input('4 New insertion here: ')))
ListNumber.InsertionNumber(int(input('5 Insert number here: ')))
ListNumber.InsertionNumber(int(input('6 Insert number here: ')))
ListNumber.InsertionNumber(int(input('7 Insert number here: ')))
ListNumber.InsertionNumber(int(input('8 Insert number here: ')))
ListNumber.InsertionNumber(int(input('9 Insert number here: ')))
ListNumber.CurrentList()

print(" THIS ARE NEW INSERTED IN "+str(ListNumber))

ListNumber.DeleteNumber(int(input('Node or point to delete: ')))
ListNumber.CurrentList()

print(" THE REMAINING IN THE LIST "+ str(ListNumber))

XList = str(ListNumber.InsertionNumber)
result = XList.find(input('find your number: '))
print("the result is: " + str(result))


print("THank you " + name)
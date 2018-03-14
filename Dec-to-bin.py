class Dectobin:
    def __init__(self ,number) :
        self.dec = number
    def convertor (self):
        self.outpart=[]
        self.remain=[]
        n1 = self.dec
        self.outpart.append(n1)  # Add given number to first of array
        index = 0
        while n1 > 2 : # Unless it's dividable by 2
            n1=self.outpart[index] # Set current number to index
            self.outpart.append(int(self.outpart[index]/2))  # Divide current number by 2 and add outcome in list
            self.remain.append(int(self.outpart[index] % 2)) # Divide current number by 2 and add remain in list
            index += 1
        return 0
    def print (self):
        print(self.outpart.pop(),''.join(map(str,self.remain[::-1])))

input1 = Dectobin(int(input()))
input1.convertor()
input1.print()


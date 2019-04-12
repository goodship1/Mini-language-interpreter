class String(object):
    def __init__(self,string):
        self.string = string
   
    def evalutation(self):
        return self.string
    

class Number(object):
    
    def __init__(self,number):
      self.number = number
    
    def evaluation(self):
        return self.number
 

class Times(object):
    def __init__(self,left,right):
        self.right = right
        self.left = left
    
    def evaluation(self):
       return  self.left.evaluation() * self.right.evaluation()
        
class Lessthan(object):
    def __init__(self,left,right):
        self.right = right
        self.left = left
    
    def evaluation(self):
        return self.left.evaluation() < self.right.evaluation()
    
    
    
class Greaterthan(object):
    def __init__(self,left,right):
        self.right = right
        self.left = left
   
    def evaluation(self):
        return self.left.evaluation() > self.right.evaluation()



class Subtraction(object):
    def __init__(self,left,right):
        self.left = left
        self.right = right
    
    def evaluation(self):
        return self.left.evalutation() - self.right.evaluation()

class Addation(object):
    def __init__(self,right,left):
        self.left = left
        self.right = right
        
    def evaluation(self):
        return self.left.evaluation() +  self.right().evaluation()
    


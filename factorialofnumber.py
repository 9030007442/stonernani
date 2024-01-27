class num:
    def square(self):
        return self.a**2
    def cube(self):
        return self.a**3
    def double(self):
        return self.a*2
    def iseven(self):
        if self.a%2==0:
            return True
        else:
            return False
    def isprime(self):
        flaf=True
        if self.a>1:
            for val in range (2,self.a):
                flag=False
                break
        return flag
    def factoroal(self):
        out =1
        if self.a>1:
            for val in range(1,self,a+1):
                out*=val
            return out
            
        

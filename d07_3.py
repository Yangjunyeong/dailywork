# 1 + 2
# 2 – 1
# 3 * 4
# 4 / 0

class Calculator:
    def __init__(self,n1,c,n2):
        self.n1 = n1
        self.c = c
        self.n2 =n2

    def add(self):
        
        return self.n1 + self.n2
    
    def sub(self):
        
        return self.n1 - self.n2
    def mul(self):
        
        return self.n1 * self.n2
    def div(self):
        try:
            result = self.n1 / self.n2
            return result

        except:
            return '0으로 나눌 수 없습니다.'

a,b,c = map(str,input().split())

num = Calculator(int(a), b, int(c))

if b == '+':
    print(num.add())
elif b == '-':
    print(num.sub())
elif b == '*':
    print(num.mul())
elif b == '/':
    print(num.div())

    


import random
class ClassHelper:
    def __init__(self,name_lst):
        self.name = name_lst

    def pick(self,n):
        
        return random.sample(self.name, k=n)

    def match_pair(self):
        matchin_lst = []
        if len(self.name) % 2:
            ran = random.sample(self.name, k=3)
            matchin_lst.append(ran)
            a = []
            
            '''for i in self.name:
                if i not in matchin_lst:
                    a.append(i)
            
            while a:
                for i in a:
                    if i not in matchin_lst:
                        a.append()'''
                













ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])

print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())

class  Nationality:
    def __new__(self,name):
        self.name = name
        return f'나의 국적은 {self.name}'
         



korea_nationality = Nationality("대한민국")
print(korea_nationality) # 나의 국적은 대한민국
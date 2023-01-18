# 출력 결과 예시
# 스테이크   50,000
# + VAT     7,500
# 총계 ₩    57,500

steak = 50000
print(f'스테이크     {steak}')
print(f'+ VAT       {int(steak * 0.15)}')
print(f'총계 ₩       {int(round(steak * 1.15,0))}')


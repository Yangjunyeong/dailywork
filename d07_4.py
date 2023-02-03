from math import ceil

def fee(min,distance):
    daeyeo_fee = (min // 10) * 1200
    insurance_fee = ceil((min / 30)) * 525
    if distance < 100:
        distance_fee = distance * 170
    else:
        distance_fee = 100 * 170 + (distance - 100) * (170 // 2)
    
    result = daeyeo_fee + insurance_fee +distance_fee

    print(result)








fee(600, 50) #=> 91000
fee(600, 110) #=> 100350


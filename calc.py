def add(n1, n2):
    result = n1 + n2
    return result

def sub(n1, n2):
    result = n1 - n2
    return result

def mul(n1, n2):
    result = n1 * n2
    return result

def div(n1, n2):
    try:
        result = n1 / n2
        return result

    except:
        return "'0'으로는 나눌 수 없습니다."


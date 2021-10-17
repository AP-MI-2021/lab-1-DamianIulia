'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
    if (n == 1):
        return False
    for i in range(2, n // 2):
        if (n % i) == 0:
            return False
    return True
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
    length = len(lst)
    result = 1
    for i in range(length):
        result = lst[i] * result
    return result
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
    cmmdc = 0
    i = 1
    while i <= x and i <= y:
        if (x % i) == 0 and (y % i) == 0:
            cmmdc = max(cmmdc, i)
        i = i + 1
    return cmmdc
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
    while y != 0:
        rest = x % y
        x = y
        y = rest
    return x
  
  
def main():
    value = int(input())
    is_prime(value)
    arr = []
    n = int(input())
    for i in range(0, n):
        item = int(input())
        arr.append(item)
    get_product(arr)
    value2 = int(input())
    value3 = int(input())
    get_cmmdc_v1(value2, value3)
    get_cmmdc_v2(value2, value3)

if __name__ == '__main__':
  main()

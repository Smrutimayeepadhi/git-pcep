"""def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        print()
        if num % i == 0:
            return False
    return True

print(is_prime(10))"""
"""number = 10
for i in range(2, number):#2,3,4,5,6,7,8,9,10
    if  number % i == 0: # 10/2,10/3....10/10 which is equal to 0
        print("not prime")
        break
    else:
        print("prime")"""

#LOCAL AND GLABAL variable concept
#it will print error
"""def a_function(a_parameter):
    a_variable = 15
    return a_parameter


a_function(10)
print(17)"""



x = [2,6,5,7,8,12]
sum1 = 15
x.sort()
left = 0
right = len(x)-1
while(left>right):

    if (x[left] + x[right] >sum1):
            right = right -1
    elif (x[left] + x[right]< sum1):
            left = left +1
    elif (x[left] + x[right] == sum1):
        print(f'two numbers are: {x[left]} and {x[right]}')
        left + 1
        right - 1






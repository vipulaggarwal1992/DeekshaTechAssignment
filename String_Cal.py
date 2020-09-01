from math import factorial

def lexi_permutations(str):
    for p in range(factorial(len(str))): # n! permutations according to the input
        print(''.join(str),end=' ')

        i = len(str) - 1

        while i > 0 and str[i - 1] > str[i]: # It sorts the sequence from right to left direction
            i -= 1
        str[i:] = reversed(str[i:])
        if i > 0:
            q = i
            while str[i - 1] > str[q]: # It sorts the sequence from left to right direction
                q += 1

            temp = str[i - 1]   # swapping
            str[i - 1] = str[q]
            str[q] = temp

num = int(input("Enter the number of Strings to input"))
if num < 1 or num > 10:
    print("Enter the no between 1 and 10")
    exit(0)
str_list= []

for i in range(0,num):
    x=str(input("Enter Strings"))
    if len(x) < 1 or len(x) > 10:
        print("Please enter string value between 1 to 10 length")
        exit(1)
    str_list.append(x)
print(str_list)

for s in str_list:
    s = list(s)
    s.sort()
    lexi_permutations(s)
    print()
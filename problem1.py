a = input()
# b = 0
# rev = 0
# while(a != 0):
#     b = int(a%10)
#     a = int(a/10)
#     rev = rev*10+rev
#     print(rev, end="")
# b = list(a)
# b = b[::-1]
a = list(a[::-1])
b = ''.join(list(a[::-1]))
print(b)
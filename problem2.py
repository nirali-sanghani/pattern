left = int(input())
right = int(input())
list1 = []
# for i in range(left, right):
#     a = left
#     while left != 0:
#         b = left % 10
#         if b == 0:
#             break
#         elif a%b == 0:
#             a = a/10
#         else:
#            break
#     left + 1
#
#
# print(list)
for i in range(left, right):
    count = 0
    for j in list(str(i)):
        print(j)
        if j != '0' and i%int(j) == 0:
            count += 1
        else:
            break
        if count == len(str(i)):
            list1.append(i)
print(list1)
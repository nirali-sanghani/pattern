h = int(input())
m = int(input())
s = int(input())
PA = str(input())

print(h, ":", m, ":", s, PA)

if PA == 'PM':
    if h <= 12:
        h = h + 12
        print(h, ":", m, ":", s)
    else:
        print("invalid")
elif PA == 'AM':
    if h <= 24:
        print(h, ":", m, ":", s)

# for i in range(90, 330*12, 180):
#     h = int(i/330)
#     m = int(i/5.5 - 60*h)
#     print('%002d:%002d' % (h, m))

stack = []
msg = list(input().split())
for i in range(len(msg)):
    if 48 <= int(float(msg[i])) <= 57:
        for j in range(int(msg[i]) - 47):
            print(stack.pop())
    else:
        stack.append(msg[i])
    # s = list(input().split())
    # for p in range(len(s)):
    #     stack.append(s[p])
    # k = int(input())
    # for j in range(k):
    #     stack.pop()
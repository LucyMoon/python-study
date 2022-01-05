# Eng = [0 for i in range(26)]
# eng = [0 for i in range(26)]
# ask = input()
# list(ask)
# for i in range(0, len(ask)):
#     if ord(ask[i]) >= 65:
#         Eng[ord(ask[i]) - 65] += 1
#     else:
#         eng[ord(ask[i]) - 45] += 1
#
# for i in range(0, 26):
#     if eng[i] != 0:
#         print(chr(i+45), end='')
#         print(eng[i])
#     if Eng[i] != 0:
#         print(chr(i + 65), end='')
#         print(Eng[i])


a = int(input())
s = list(bin(a))
cnt = 0
cnt_2 = 0
for i in range(0, len(s)):
    if s[i] == 1:
        cnt += 1

while (1):
    a += 1
    arr = list(bin(a))
    for i in range(0, len(arr)):
        if arr[i] == 1:
            cnt_2 += 1

    if cnt_2 == cnt:
        print(a)
        break

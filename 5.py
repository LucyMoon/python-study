#1
print("Hello")
#2
print("Hello World")
#3
print("Hello\nWorld")
#4
print("\'Hello\'")
#5
print("\"Hello World\"")
#6
print("\"!@#$%^&*()\'")
#7
print("\"C:\Download\\'hello\'.py\"")
#8
print("print(\"Hello\\nWorld\")")
#9
a = input()
print(a)
#10
a = input()
a = int(a)
print(a)
#11
a = input()
a = float(a)
print(a)
#12
a = input()
b = input()
print(a)
print(b)
#13
a = input()
b = input()
print(b)
print(a)
#14
a = float(input())
print(a)
print(a)
print(a)
#15
a, b = input().split()
print(a)
print(b)
#16
a, b = input().split()
print(b,a)
#17
a = input()
print(a,a,a)
#18
a, b = input().split(':')
print(a, b, sep=':')
#19
a, b, c = input().split(".")
print(f"{c}-{b}-{a}")
#20
a, b = input().split('-')
print(a+b)
#21
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
#22
s = input()
print(s[0:2])
print(s[2:4])
print(s[4:6])
#23
a,b,c= input().split(":")
print(b)
#24
a, b=input().split()
print(a+b)
#25
a, b = input().split()
c = int(a) + int(b)
print(c)
#26
a = float(input())
b = float(input())
c = a + b
print(c)
#27
a = input()
n = int(a)
print('%x'% n)
#28
a = input()
n = int(a)
print('%X'% n)
#29
a = input()
n = int(a, 16)      #입력된 a를 16진수로 인식해 변수 n에 저장
print('%o' % n)
#30
n = ord(input())
print(n)
#31
c = int(input())
print(chr(c))
#32
a = input()
a = int(a)
print(-a)
#33
n = input()
n = ord(n)
print(chr(n+1))
#34
a,b = input().split()
c = int(a) - int(b)
print(c)
#35
a,b = input().split(" ")
m = float(a) * float(b)
print(m)
#36
w, n = input().split()
print(w*int(n))
#37
n = input()
s = input()
print(int(n)*s)
#38
a, b = input().split(" ")
c = int(a)**int(b)
print(c)
#39
a, b = input().split(" ")
c = float(a)**float(b)
print(c)
#40
a, b = input().split(" ")
a = int(a)
b = int(b)
print(a//b)
# #ord : 유니코드 정수
# #chr : 유니코드 문자
#
# print(ord('a'))#97
# print(ord('A'))#65
#
# print(chr(99))#c
#
# #소문자 출력
# for i in range(97, 123):
#     print(chr(i),end=' ')
# print()
# for i in range(0, 26):
#     print(chr(ord('a')+i), end=' ')
#
# ----------------------------------------------
#
# n=20
# print(hex(n))#0x14
# #16진수
#
# n=str(hex(n))
# print(n.zfill(10))
# #변수.zfill(정수)
# #정수만큼의 칸에 변수를 넣고 남은 칸에 0을 채워넣음
#
# n1=str(30)
# print(n1.zfill(10))
#
# n2='hello'
# print(n2.zfill(10))
#
# ----------------------------------------------
#
# Group = {}
# print("### K-Pop 그룹 관리 프로그램 ###")
#
# while True :
#     menu = int(input("[1:등록 / 2:삭제 / 3:조회 / 4: 종료] : "))
#     if menu == 4 :
#         break #4라면 while문 종료
#     elif menu == 1 :
#         name = input("그룹 이름이 무엇인가?")
#         member = input("그룹 인원이 몇명인가?")
#         Group[name] = member
#     elif menu == 2 :
#         delete = input("삭제할 그룹 이름이 무엇인가?")
#         del(Group[delete])
#         #del 변수명[인덱스]
#         #한개의 요소를 삭제
#     elif menu == 3 :
#         print(Group)
#
# print("### K-Pop 관리 프로그램 종료 ###")
#
# ----------------------------------------------
#
# from collections import deque
# queue=deque() #deque는 스택처럼 써도 되고, 큐처럼 쓸 수도 있다.
# queue.append(1) #큐에 1 저장
# queue.append(2) #큐에 2 저장
# queue.append(3) #큐에 3 저장
# print(queue)
# print(queue.popleft()) #potleft() : 가장 왼쪽 값 빼기
# print(queue.popleft())
# print(queue)
# queue.append(11)
# queue.append(22)
# queue.append(33)
# print(queue)
# #print(queue.reverse()) 이렇게 하면 안됨, None
# queue.reverse() # 큐 순서 뒤집기
# print(queue)
#
# ----------------------------------------------
#
# stack=[]
# stack.append(5) #스택에 5 삽입
# stack.append(3)
# stack.append(8)
# stack.append(6)
# stack.append(4)
# stack.pop() #가장 마지막에 들어온 값 빼기
# stack.append(1)
# stack.pop()
# print(stack)
# print(stack[0])
# print(stack[::-1]) #A:B:C A가 none이면 처음부터, B가 none이면 할 수 있는데까지
# # 처음부터 끝까지 -1칸 간격으로 배열을 만들어라 ( == 역순으로)
# print('stack pop', stack.pop())
# print('stack pop', stack.pop())
# print('stack pop', stack.pop())
# print('stack pop', stack.pop())
#
# ----------------------------------------------
#
# a=[]*6
# print(a)
# a=[0,2,3,4,5,1]
# print(a)
# for i in range(1,6):
#     a[i]=a[a[i]]
# print(a)
# for i in range(1,6):
#     a[i]=a[a[i]]
# print(a)
#
# ----------------------------------------------
#
# d1={}
# k=input()
# v=input()
# d1[k]=v
# k=input()
# v=input()
# d1[k]=v
# print(d1)
# #딕셔너리 생성하는 법
#
# ----------------------------------------------

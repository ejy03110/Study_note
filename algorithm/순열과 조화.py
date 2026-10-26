divide_line = "-----------------------------------------------"

# #-------------------------부분집합(재귀 버전)-------------------------------
# name = "ABC"

# def abc(level, path):
#     # 만약 level이 3까지 오면? -> 지금까지 포함한 알파벳을 출력하고 종료
#     if level == 3:
#         print(*path)
#         return

#     # 해당 자리수의 알파벳이 포함되지 않는 경우!
#     abc(level + 1, path)

#     # 해당 자리수의 알파벳이 포함되는 경우! -> path에 추가
#     abc(level + 1,path+[name[level]])


# # 처음은 level 0에 지나온 길이 없이 시작
# # abc(0,[])

# #-----------------------------------------------------------------------
# #-------------------부분집합(바이너리 카운팅 버전)--------------------------
# print("친구 A, B, C와 같이 카페에 가는 경우의 수는?")
# arr = ['A', 'B', 'C']
# n = len(arr)

# # 이건 0부터 2**(n-1)까지 반복시키는 표현 방식이다. (간지용) 
# for tar in range(1 << n):
#     answer = []
#     for i in range(n):
#         if tar & 1:
#             answer.append(arr[i])
#         tar >>= 1
#     print(answer)

# print(divide_line)

# #-----------------------------------------------------------------------

# print("만약 친구가 A, B, C, D, E고, 최소 두명 이상의 친구와 카페에 간다면?")
# arr = ['A', 'B', 'C', 'D', 'E']
# n = len(arr)


# for tar in range(1 << n):
#     answer = []
#     for i in range(n):
#         if tar & 1:
#             answer.append(arr[i])
#         tar >>= 1
#     if len(answer) >= 2:
#         print(answer)

# print(divide_line)
# #-----------------------------------------------------------------------
# #-------------------------------순열-------------------------------------
# card = "ABCD"
# path = [""] * 3 # 카드 묶음의 개수 (level)
# used=[0]*4      # 선택할 수 있는 카드 종류의 개수 (branch)

# def abc(level):
#     if level == 3:
#         print(*path)
#         return

#     for i in range(4):
#         # 만약 뽑은 카드면? 그 뒤의 작업을 안해버린다!
#         if used[i] == 1:
#             continue
#         # 뽑았으니 1로 체크
#         used[i] = 1

#         # 뽑은 카드에 추가
#         path[level] = card[i]

#         # 다음 레벨로
#         abc(level + 1)

#         # 백트래킹 -> path와 사용 카드 초기화
#         path[level] = ""
#         used[i] = 0

# #-----------------------------------------------------------------------
# #-------------------------------조합-------------------------------------
# card = "ABCD"
# path = [""] * 3 # 카드 묶음의 개수 (level)

# def abc(level, start):
#     if level == 3:
#         print(*path)
#         return

#     for i in range(start, 4):
#         # 뽑은 카드에 추가
#         path[level] = card[i] # 내가 앞으로 들어갈 경로를 입력한다

#         # 다음 레벨로
#         abc(level + 1, i + 1) # 다음 함수에 진입

#         # path[level] = "" # 함수 리턴 후, 경로를 지우는 것인데, 여기서는 생략 가능..!

# abc(0, 0)

# #-----------------------------------------------------------------------
# #-------------------------Greedy 알고리즘---------------------------------
# print("동전 교환 문제!!")

# coin = [500, 50, 100, 10]

# target = 1_100

# # 내림차순으로 정렬하여 동전의 값이 큰 순서로 재졍렬한다.
# coin.sort(reverse=True)

# # cnt는 사용한 동전의 개수이다.
# cnt = 0

# # 동전의 개수가 4개이므로 range(4)로 설정한다.
# for i in range(4):
#     # 현재 target에 지금 타겟잡은 동전(coin[i])이 몇개까지 들어가는지 temp에 임시저장!
#     temp = target // coin[i] 

#     # 사용한 동전 개수에 추가!
#     cnt += temp

#     # 목표 금액에다가 동전개수와 값을 곱한값을 빼준다! -> 첫 순환시에는 1,100 - 500 * 2 이므로 100원이 남는다.
#     target = target - (temp * coin[i])

# #-----------------------------------------------------------------------
# #-------------------------Greedy 알고리즘---------------------------------
# print("화장실 문제!!")
# poo = [15, 30, 50, 10]
# poo.sort() #10 15 30 50

# # 누적 대기시간을 poo_sum이라고 한다.
# poo_sum = 0

# # 대기 인원은 점점 줄어들어야 하고, 화장실 시간은 poo의 0번부터 시작한다는 것을 인지하자. 
# for i in range(3, 0, -1):
#     poo_sum += (i * poo[3-i])

# print(poo_sum)

# #-----------------------------------------------------------------------
#-------------------------Greedy 알고리즘---------------------------------
print("fractional kanpsack")

bag = 30
salt = [(5, 50), (10, 60), (20, 140)]

# 키로당 단가가 높은 순서로 sort 
salt.sort(key=lambda x:x[1] // x[0], reverse=True)

print(salt) # [(20, 140), (10, 60), (5, 50)]

for weight, price in salt:
    # 다 담을수 있는 경우와 없는 경우를 체크!
    # 다 담을 수 있는 경우에는 단순히 더해주면 된다.
    if bag >= weight:
        bag -= weight           # 담은 만큼 가방 무게를 빼주고
        total_value += price    # 가방의 가치를 업데이트 한다

    # 다 담을 수 없으면? -> kg당 가치로 물건을 쪼개서 가방의 남은 공간만큼만 넣어준다!
    else:
        total_value += (bag * (price // weight))
        bag = 0
        break

# 추가 설명: lambda - 익명함수
# 이런 간단한 함수를 호출할 수도 있지만
def sum(a, b):
    return a+b

result = sum(3, 4)
print(result)

# 좀 줄여서 쓰고 싶다!
result = (lambda a,b: a + b)(3, 4)

# ------------------------------------------------------------------
# 여기서 lambda 바로 뒤에는 매개변수가 먼저 온다.
# 여기서는 a와 b라는 변수를 쓰겠다라는 것이다.
# 그 다음 : 뒤에는 a와 b를 이용한 연산을 무엇을 할것인지를 적는다.
# 맨 마지막에는 a, b에 해당하는 변수에 어느 값을 넣을건지에 대한 것을 적는다!
# ------------------------------------------------------------------

# 추가 설명: sort
def test(x):
    return -x

arr = [3, 1, 2, 5, 1, 3, 6, 5, 3, 2, 21, 5]

# sort안에 key를 쓴다는것은 arr의 원소에 test를 적용한 것을 기준으로 정렬을 한다는 것이다!
# 여기서 key는 기준을 정하기 위한 연산에 불과하므로 실제 arr의 원소값이 변화하지는 않으니 주의!
arr.sort(key=test)

# 람다함수로 표현하면 다음과 같이 표현할 수도 있다! 여기서는 입력이 arr의 원소가 입력값으로 들어가게 되는것이다!
arr.sort(key=lambda x:-x) 


#화장실문제

poo = [15,30,50,10]
poo.sort()
Sum = 0

for i in range(3,0,-1): # 대기인원
    Sum += (i*poo[3-i])
print(Sum)


############################################################

# fractional knapsack
bag = 30
salt = [(5,50),(10,60),(20,140)]

# 키로당 단가가 높은 순서로 sort
salt.sort(key=lambda x:x[0], reverse=True)

print(salt)
total_value = 0
for weight, price in salt:
    # 다 담을 수 있다면
    if bag >= weight:
        bag-=weight
        total_value += price    # 가방 가치를 업데이트

    # 다 담을 수 없다면,
    # 가방에 담을 수 있는 가치는 = 남는 가방무게 * 담는물건의 단위당 단가
    else:
        total_value += (bag*(price//weight))
        bag = 0
        break
print(total_value)


############################################################

# lambda 익명함수
def Sum(a,b):
    return a+b

result=Sum(3,4)
print(result)

result = (lambda a,b:a+b)
print(result(3,4))



# sort

arr = [3,1,2,5,1,3,6,5,3,2,21,5]

def test(x):
    return x%2

# 짝수 우선정렬
arr.sort(key = test)
print(arr)

# 내림차순정렬
arr.sort(key = lambda x:-x)
print(arr)
### 그래프의 기본과 탐색


#DFS (인접 행렬) = 가능한 모든 정점 1번씩 탐색
name = "BACD"
arr = [
    [0,0,1,1],
    [1,0,1,0],
    [1,0,0,1],
    [0,0,0,0]
       ]

used = [0]*4    # 정점의 개수만큼 방문 체크


def dfs(now):

    for i in range(4):
        if arr[now][i] == 1 and used[i]==0:
            used[i]=1
            dfs(i)





used[1] = 1 # 탐색 시작 인덱스에 1 중복 체크
dfs(1)  # 탐색 시작 인덱스


#=======================================================================#
# DFS (인접 리스트) = 가능한 모든 정점 1번씩 탐색

# 4 6
# 0 2
# 0 3
# 1 0
# 1 2
# 2 0
# 2 3

name = "BACD"
n,m = map(int,input().split()) # 정점, 간선 정보의 개수
arr = [[]for _ in range(n)]

for _ in range(m):
    start,end = map(int,input().split())
    arr[start].append(end)

used= [0]*n

def dfs(now):
    print(name[now], end='')

    for i in arr[now]:
        if used[i] == 0:
            used[i] = 1
            dfs(i)
 


used[1] = 1     # DFS 시작 인덱스에 1 체크
dfs(1)


#=======================================================================#
# DFS (인접 리스트) = 가능한 모든 정점 1번씩 탐색
# 경로 개수 찾기

# 4 6
# 0 2
# 0 3
# 1 0
# 1 2
# 2 0
# 2 3

name = "BACD"
n,m = map(int,input().split()) # 정점, 간선 정보의 개수
arr = [[]for _ in range(n)]

for _ in range(m):
    start,end = map(int,input().split())
    arr[start].append(end)

used= [0]*n
cnt = 0

def dfs(now):
    global cnt
    if now==3:
        cnt +=1

    for i in arr[now]:
        if used[i] == 0:
            used[i] = 1
            dfs(i)
            used[i] = 0
 


used[1] = 1     # DFS 시작 인덱스에 1 체크
dfs(1)

#=======================================================================#

# BFS 너비 우선 탐색 (모든 정점을 한번씩 탐색)
# 4 6
# 0 2
# 0 3
# 1 0
# 1 2
# 2 0
# 2 3

from collections import deque

n,m = map(int, input().split())
arr = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    arr[a].appned(b)

q = deque()
used = [0] * n
q.append(0) # 시작점 큐에 넣기
used[0] = 1 # 시작점 방문 체크
name = "ABCD"

while q:
    now = q.popleft()

    print(name[now], end='')

    for i in arr[now]:      # 이동 가능한것 탐색
        if used[i]==0:      # 방문 여부 확인
            used[i]=1       # 방문 체크
            q.append(i)     # 큐에 넣기


## BFS 경로탐색일때는 큐 안에 used배열 까지 넣어줘야한다. backtracking 하면 안돼

#=======================================================================#

# Union-find (서로소 찾기)

# 각각의 독립된 data를 그룹화 하여 관리하고 싶을때
# Boss 가 다르다면 합칠 수 있음, 같으면  return

#arr = [i for i in range(6)]
#print(arr)
arr = [0,1,2,3,4,5]
rank = [0]*6        # 트리의 높이

def findboss(member):
    if arr[member] == member:   # 자기 자신이 보스라면, (해당 그룹 보스 찾음)
        return member
    ret = findboss(arr[member]) # 보스가 아니라면 arr 배열의 값을 가지고 보스 찾기
    arr[member] = ret       # 경로 단축 코드_____ 매우 중요
    return ret



def union(a,b):
    fa = findboss(a)
    fb = findboss(b)

    # 두 보스가 같으면 이미 같은 그룹
    if fa == fb:
        return

    # 트리의 높이가 높은곳에 낮은 것 추가
    if rank[a] == rank[b]:
        rank[a] += 1
        arr[fb] = fa
    elif rank[a] > rank[b]:
        arr[fb] = fa
    else:
        arr[fa] = fb
    

union(0,1)
union(3,4)
union(1,4)
union(1,3)
union(5,4)


y,x = map(int, input().split())     # 숫자 2개 입력 후 같은 그룹인지 출력
if findboss(y) == findboss(x):
    print("같은 그룹")
else:
    print("다른 그룹")
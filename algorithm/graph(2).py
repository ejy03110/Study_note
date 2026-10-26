# %% [markdown]

# Priority Queue - 우선순위 큐
# 우선순위가 높은 것 부터, 추가, 삭제하는 자료구조
# 완벽한 이진트리의 형태를 유지 nlogN
# max heap - 큰 값이 우선순위 : 내림차순
# min heap - 작은 값이 우선순위 : 오름차순

# %%
# 우선순위 큐
import heapq

arr = []

heapq.heappush(arr, 13)
heapq.heappush(arr, 5)
heapq.heappush(arr, 17)
heapq.heappush(arr, 9)
print(arr)

print("heap push를 하면 기본이 min heap이여서 5의 값이 제일 앞에 오는것을 볼 수 있다!")

print(heapq.heappop(arr))

print(arr)
print("우선순위가 높은 5가 빠진 모습을 확인할 수 있다.")
print("pop을 반복하면 최소값이 빠지는 것이 반복되어 오름차순으로 pop되는 것을 볼 수 있다!")

# %%
# for 문으로 하면?
import heapq

arr = []

heapq.heappush(arr, 13)
heapq.heappush(arr, 5)
heapq.heappush(arr, 17)
heapq.heappush(arr, 9)
print(arr)

for i in range(len(arr)):
    print(heapq.heappop(arr), end=' ')

# %%
# while문으로 하면?
import heapq

arr = []

heapq.heappush(arr, 13)
heapq.heappush(arr, 5)
heapq.heappush(arr, 17)
heapq.heappush(arr, 9)
print(arr)

while arr:
    node = heapq.heappop(arr)
    print(node, end=' ')

# %% 
# 기본값인 min heap이 아닌 max heap으로 한다면?
import heapq
arr = [2, 234, 23, 12, 31]
heap = []
for i in range(len(arr)):
    heapq.heappush(heap, -arr[i])

print("따로 내림차순으로 정렬을 할 수가 없어서 음수를 곱해줌으로써, 순서를 변경한다!")

for i in range(len(arr)):
    print(heapq.heappop(heap) * -1, end=' ')

# %%
# max heapㅇ르 lambda를 이용해서 나타낼 수도 있다!
import heapq

arr = [2, 234, 23, 12, 31]
arr = list(map(lambda x:-x, arr)) # arr 배열의 모든 원소에 -를 붙이는 것이다!


heapq.heapify(arr) # gpt에게 물어본 결과, 메모리를 최적화하는 것이였다.
# heapq.heapify(arr)는 파이썬에서 기존의 리스트(arr)를 추가적인 메모리 공간을 쓰지 않고(In-place) 최소 힙(Min-Heap) 구조로 변환하는 함수입니다.

for i in range(len(arr)):
    print(heapq.heappop(arr) * -1, end=' ')
# %%
# Prim 알고리즘은 위에 있는 heapq의 기능을 활용해서 구현하도록 한다
import heapq
n = int(input()) # 노드의 수
m = int(input()) # 간선의 수

arr = [[] for _ in range(n)]

# 무방향 그래프이므로 양방향 저장
for _ in range(m):
    start ,end, cost = map(int, input().split())

    arr[start].append((cost, end))
    arr[end].append((cost, start))

used = [0] * n  # 내가 선택한 정점인지 체크
heap = []       # 최소비용을 뽑기 위함 

# (비용, 정점)
heapq.heappush(heap, (0, 0)) # 비용 시작 정점

total = 0   # 총 비용을 합치기
cnt = 0     # 연결한 간선의 개수

while heap:
    cost, now = heapq.heappop(heap)

    # 이미 MST에 포함된 정점이면 무시
    if used[now] == 1:
        continue

    # MST에 정점 포함
    used[now] = 1   # 방문체크
    total += cost   # 비용의 합
    cnt += 1        # 연결된 간선의 개수 1 증가

    # 모든 정점을 선택했다면 종료
    if cnt == n:
        break

    # 현재 정점과 연결된 간선들을 우선순위 큐에 추가
    for next_cost, next_node in arr[now]:
        if used[next_node] == 0:
            heapq.heappush(heap, (next_cost, next_node))

print(total)

# %%
# Kruskal 알고리즘
arr = [i for i in range(5)]
n, m = map(int, input().split()) # 정점 간선 개수
lst = [list(map(int, input().split())) for _ in range(m)] #  입력

lst.sort(key=lambda x:x[2]) # 비용을 기준으로 sort

total = 0   # 비용 더하기
cnt = 0     # 연결된 간선 개수 

def findboss(m):
    global arr
    if arr[m] == m:
        return m

    ret = findboss(arr[m])
    arr[m] = ret # 경로 단축
    return ret

def union(a, b, i):
    global total, cnt
    fa, fb = findboss(a), findboss(b)   # 보스 찾기
    if fa == fb:                        # 이미 같은 그룹을 연결하면 cycle 발생
        return
    total += list[i][2]                 # 연결하면서 비용 더하고
    cnt += 1                            # 연결한 다리 개수 더하기
    arr[fb] = fa                        # 연결하기

for i in range(m):
    if cnt == n-1:                      # 정점의 개수 -1 개 만큼 합 구하기
        print(total)                    # 합 출력하고 종료
        break
    union(list[i][0], list[i][1], i)

# %%
# 다익스트라 알고리즘
import heapq    

name = "ABCDE"
n, m = map(int, input().split())    # 정점과 간선 정보의 개수
arr = [[]for _ in range(n)]         # 간선 정보를 인접 리스트에 저장

for _ in range(m):
    a, b, c = map(int, input().split()) # 시작 도착 비용
    arr[a].append((b, c))

start, end = map(int, input().split())  # 시작점과 도착점 입력

result = [21e8] * n # 엄청 큰수로 도배

pq = [(0, start)]   # (비용, 경우지 idx (시작점은 첫번째 경유지로 놓는다))
result[start] = 0   # (인접리스트(idx, 비용) // pq(비용, idx)) -> 최소비용을 갱신하는 배열

while pq:
    price, ky = heapq.heappop(pq) # (시작점에서 경유지 까지의 비용)

    if result[ky] < price: continue

    for do, do_cost in arr[ky]: # (경유지에서 도착점 까지의 비용)
        if result[do] > price + do_cost: # (시작 -> 도착 vs 경유지를 들렀다 가는것 비교)
            result[do] = price + do_cost
            heapq.heappush(pq, (price + do_cost, do))

print(result)


 
## 다익스트라 몰라도 풀 수 ?
#  BFS 알고 있다는 전제 하에, 
"""
1. BFS로 최단 경로를 구할 수 있다.
2. que에서 먼저 나온 노드가 "가장 가까운 노드"가 아닐때
3. 가장 가까운 노드를 선별해서 꺼내자
4. 고르는 단계에서 빠르게 고르기 위해 자료구조 '최소힙'을 쓴다. (우선 순위 큐 == pq)
"""


# PQ에 넣는 노드의 상태가 달라질 것

# 음수 간선

# 다른 알고리즘 기법을 또 학습한다면? (ex 다익스트라)
# 1. 그래프를 코드로 표현       (인접리스트가 무엇인지, 왜 쓰는지)
# 2. BFS로 최단거리 구해보기        (모든 비용이 1인 그래프로)
# 3. 힙의 성질 이해해보기       (heapq의 사용법을 외우거나 이해하라는 것은 아님)
        # "최솟값 O(logN)에 최소값을 꺼낼 수 있다."



"""
학습의우선순위

1순위. 구현, 시뮬레이션 : 가장 많이 출제
2순위. 정렬, 해시, 자료구조 : 기본기
3순위. BFS, DFS : 다익스트라와 같은 알고리즘의 기본 토대

--------------------------------------4번부터는 문제가 정형화된 것들이 많다
4순위. 이분탐색
5순위. DP   : 난이도가 다소 높을 수 있다
6순위. Dijkstra / Union Find    : 여기까지 오면 안정권
"""



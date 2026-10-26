# 백트래킹
# N-queen
#----------------------------------------------------
# 자료구조 특집 (트리)
## 트리 정의 용어
## BST
## Heap

############################################################################

# 완전탐색 - 중복순열 (Brute Force)
# DFS - 탐색순서
# 가지치기 - pruning - 굳이 탐색할 필요가 없는 경우
# 백트래킹 - backtrcaking - 탐색 후 돌아옴(취소)



"""
N-Queen
n*n 체스판에 배치한 Queen들이 서로 위협하지 않도록 n개의 Queen을 배치하는 문제
어떤 두 Queen도 서로를 위협하지 않아야 한다.
Queen을 배치한 n개의 위치는?


* 백트래킹과 가지치기가 들어감
"""


# branch 4 // level 4
# vertical = [j]
# seven = [i+j]
# five = [i-j+n]


n = int(input())    # 체스판의 크기
vertical = [0]*n
seven = [0]*(2*n)
five = [0] * (2*n)


def abc(level):
    global cnt

    if level == 4:
        cnt += 1
        return

    for j in range(n):

        # 가지치기
        if vertical[j] == 1: continue
        if seven[level+j]==1 or five[level-j+n] == 1: continue


        vertical[j], seven[level+j],five[level-i+n] = 1,1,1
        

        abc(level+1)

        # 백트래킹
        vertical[j], seven[level+j],five[level-i+n] = 0,0,0


abc(0)
print(cnt)




"""
트리

자료구조를 어떻게 저장 또는 관리 할 것인가


* 비선형 자료구조: 그래프 (트리 - 무방향, 사이클 X)
# 양방향 : 각 방향의 비용 차이 O
# 무방향 : 방향의 비용 차이 X

정점 : vertex = node
간선 : edge
root node : 트리의 시작 노드
leaf node : 자식노드가 없는 노드

=========================================================

* 선형 자료구조: 리스트, linked list(연결리스트)

pop(0) : O(n)  모든 리스트 검사 후 맨 앞에꺼 뺌
deque : O(1)   그냥 가장 앞에꺼 뺌

ex ) q = deque()
     q.append()
     q.popleft()

"""
# 이진 트리
# 각 노드가 자식노드를 최대 2개까지만 가질 수 있는 트리
# 왼쪽 : left_child_node, 오른쪽 : right_child_node



"""
트리 순회

전위순회 : 들어가자마자 출력   ABDECFG
중위순회 : 왼쪽 자식 확인 후 출력   DBEAFCG
후위순회 : 왼쪽 + 오른쪽 다 확인 후 출력    DEBFGCA

"""


"""
BTS
이진 탐색 트리

빠른 서치를 위한 대표적인 자료구조
Hash, BST, DAT 가 존재
AVL, Red blacktree, B-tree 로 편향된 데이터를 정리해주는..

Red blacktree  데이터의 추가 삭제가 잦을때 효율적. O(logn)
B-tree 자식이 많을 경우 빠르게 검색 가능하게
"""






# 연결 리스트
class Node:
    def __init__(self,value):
        self.value = value      # 인스턴스에 저장될 값
        self.next = None        # '다음은 너' 라는 정보

a = Node(10)
b = Node(20)
c = Node(20)

a.next = b
b.next = c


head = a

while head:
    print(head.value)
    head = head.next



"""
힙(heap)

max heap : 우선순위가 높다 = 내림차순
부모 > 자식

min heap : 우선순위가 낮다 = 오름차순
부모 < 자식

"""



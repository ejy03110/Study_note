# 병합, 퀵, 힙 : 시간복잡도 nlong(n)

################################################################
# Merge sort
"""
Merge Sort
분할로 나눠서 결과로 합치기

핵심코드
"""
arr = [2,3,5,7,1,2,5,9]
start = 0
end = len(arr)-1

mid = (start + end) //2

a = start   # 첫번째 배열의 맨 앞
b = mid+1   # 두번째 배열의 맨 앞
result = []

while 1:
    # 종료조건
    if a>mid and b>end: break

    # 한쪽이 끝에 도착했을때
    if a>mid:
        result.append(arr[b])
        b+=1
    elif b>end:
        result.append(arr[a])
        a+=1

    # 한쪽이 도착하지 않은 경우
    elif arr[a] <= arr[b]:
        result.appedn(arr[a])
        a+=1
    else:
        result.append(arr[b])
        b+=1

print(*result)



"""
Merge Sort
실전
"""
arr[2,7,5,3,1,5,9,2]


def merge(start,end):

    if start == end:
        return
    mid = (start+end)//2

    merge(start,mid)
    merge(mid+1,end)


    a = start   # 첫번째 배열의 맨 앞
    b = mid+1   # 두번째 배열의 맨 앞
    result = []

    while 1:
        # 종료조건
        if a>mid and b>end: break

        # 한쪽이 끝에 도착했을때
        if a>mid:
            result.append(arr[b])
            b+=1
        elif b>end:
            result.append(arr[a])
            a+=1

        # 한쪽이 도착하지 않은 경우
        elif arr[a] <= arr[b]:
            result.append(arr[a])
            a+=1
        else:
            result.append(arr[b])
            b+=1

    for i in range(len(result)):
        arr[start+i] = result[i]

merge(0,7)

################################################################
# Quck sort
"""
핵심코드
"""
arr = [4,7,1,6,2,8,5,3,9]

start = 0
end = len(arr)-1
pivot = start
a = start+1
b = end
while 1:
    # 배열범위 안이고, a의 값이 pivot보다 작다면
    while a<=end and arr[a]<=arr[pivot] : a+=1

    # 배열범위 안이고, b의 값이 pivot보다 크다면
    while b >= start and arr[b] > arr[pivot] : b-=1

    # a와 b가 엇갈린다면 swap
    if a>b : break
    arr[a],arr[b] = arr[b],arr[a]

arr[b],arr[pivot] = arr[pivot],arr[b]
print(*arr)



"""
Quick Sort

실전
"""

arr = [4,7,1,6,2,8,5,3,9]

def quick(start,end):
    if start>=end:
        return

    pivot = start
    a = start+1
    b = end

    while 1:
        # 배열범위 안이고, a의 값이 pivot보다 작다면
        while a<=end and arr[a]<=arr[pivot] : a+=1

        # 배열범위 안이고, b의 값이 pivot보다 크다면
        while b >= start and arr[b] > arr[pivot] : b-=1

        # a와 b가 엇갈린다면 swap
        if a>b : break
        arr[a],arr[b] = arr[b],arr[a]

    arr[b],arr[pivot] = arr[pivot],arr[b]


    quick(start,b-1)
    quick(b+1,end)


################################################################
# 이진탐색  정렬이 된 자료로..
arr = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
# arr = list(map(int,input().split()))

arr.sort()

target = 20
start = 0
end = len(arr)-1


check = False
while 1:
    mid = (start + end)//2
    if arr[mid] == target:
        check=True
        break
    if arr[mid]>target: # 찾고자 하는 값이 중간값 보다 크면 우측탐색
        start = mid+1
    if arr[mid]<tartet: # 찾고자 하는 값이 중간값 보다 작다면 좌측탐색
        end = mid-1

    if start>end:
        break

if check:
    print("찾았음")
else:
    print("못찾음")



"""
BNS
실전
"""
arr = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
arr.sort()

target = 20
start = 0
end = len(arr)-1

check = False


def binary_search(start,end):
    global check

    if start > end :
        return
    mid = (start+end)//2

    if target == arr[mid]:
        check = True
        return
    if arr[mid] < target:
        binary_search(mid+1, end)
    else:
        binary_search(start,mid-1)



# parametric search

battery = "*******___"

def parametric_search(start,end):
    Max = -1

    while 1:
        mid = (start + end)//2
        if battery[mid] == '_':
            end = mid-1

        elif battery[mid] == '*':
            Max = mid
            start = mid+1
        if start>end:
            break

    return Max+1


answer = parametric_search(0,9)
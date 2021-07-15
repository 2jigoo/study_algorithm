array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 선택 정렬
def selection_sort(arr):
    array = arr.copy()
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        print(i, ':', array)

    # print(array)


# range(count)
# range(start, end)
# range(start, end, step)

# 삽입 정렬
def insertion_sort(arr):
    array = arr.copy()
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j - 1], array[j]
            else:
                break
        print(i, ':', array)
    # print(array)


# 퀵 정렬. 재귀함수
def quick_sort(array, start, end):
    # 종료 조건: 원소가 1개인 경우 종료 (start와 end 지점이 같다)
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    print(array, "\tpivot: ", pivot, "(", array[pivot], ")", sep='', end='')

    # left: pivot값보다 큰 값의 위치
    # right: pivot값보다 작은 값의 위치
    # 목표: pivot..left..right 상태에서 탐색을 시작해, 적절한 값을 찾아 right..pivot..left 순으로 정렬해야 한다
    
    # 왼쪽부터 피벗보다 큰 값을 찾고, 오른쪽부터 피벗보다 작은 값을 탐색하기! left <= right 되는 순간 더 살펴볼 필요가 없다.
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # 피벗보다 작은 데이터를 찾을 때까지
        while right > start and array[right] >= array[pivot]:
            right -= 1



        # left와 right 인덱스가 엇갈렸다면?
        # (left가 더 오른쪽을 가리키는 경우, left > right, 다시 말해 pivot..right..left 가 된 경우, right..pivot..left순으로 만들기 위해 pivot과 right를 스왑한다)
        if left > right:
            # print('left: ', left, '(', array[left], '), right: ', right, '(', array[right], ')', sep='')
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left] # 적절한 값을 찾았을 때는 둘을 스왑


    print(', left: ', left, ', right: ', right, sep='')

    # pivot을 기준으로 왼쪽은 pivot보다 작은 값들, 오른쪽은 pivot보다 큰 값들이 위치하게 된다
    # 왼쪽 파트, 오른쪽 파트 각각 재귀적으로 정렬하기. 범위: (start, end) => (start, right - 1) / (right + 1, end)
    quick_sort(array, start, right - 1)  # 왼쪽 파트
    quick_sort(array, right + 1, end)  # 오른쪽 파트


def quick_sort_for_python(array):
    if len(array) <= 1:
        return array

    pivot = array[0]  # 피벗은 첫 번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


# 실행부

print(">> array\n", array, '\n')

print(">> 선택 정렬")
selection_sort(array)
print()

print(">> 삽입 정렬")
insertion_sort(array)
print()

print(">> 퀵 정렬")
arr_for_quick = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
arr_cp = arr_for_quick.copy()
print(arr_cp)
quick_sort(arr_cp, 0, len(arr_cp) - 1)
print(arr_cp)

print(">> 파이썬 최적화 퀵 정렬")
arr_cp = arr_for_quick.copy()
print(arr_cp)
quick_sort_for_python(arr_cp)
print(arr_cp)
# n * m 개의 카드
# 뽑고자 하는 행 선택
# 그 행중에서 가장 작은 수의 카드
# 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록!

def using_double_for(data, result):
    min_value = 20000

    # 해당 행에서 min값과 아이템 비교해서 최소값 저장
    for a in data:
        min_value = min(min_value, a)

    # 저장한 최소값이 현재까지 찾은 값과 비교해 더 큰 값을 저장
    print("이번 행의 최소값: ", min_value, "현재까지 최대값: ", result)

    return max(result, min_value)


def using_min(data, result):
    print(data)
    min_value = min(data)

    print("이번 행의 최소값: ", min_value, "현재까지 최대값: ", result)

    return max(result, min_value)



## 시작

print("n * m 행렬 사이즈 입력")
n, m = map(int, input().split())

result = 0

print("행렬 데이터 입력")
for i in range(n):
    data = list(map(int, input().split()))
    print("data: ", data)
    # result = using_min(data, result)
    result = using_double_for(data, result)
    print(i, "번째 결과: ", result)

print("답: ", result)
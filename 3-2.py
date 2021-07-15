# N개의 수의 배열이 있을 때, 주어진 수들을 M번 더하여 가장 큰 수를 만들기
# 배열의 특정한 원소가 연속해서 K번을 초과해 더할 수 없다

# n: 배열 길이
# m: 총 덧셈 횟수
# k: 같은 수가 최대로 더해질 수 있는 횟수

def simple_solution(n, m, k, data):
    data.sort()
    first = data[n - 1]
    second = data[n - 2]

    result = 0

    # m이 0이 될 때까지 반복
    while True:
        # result에 가장 큰 값 k번 더하기
        for i in range(k):
            if m == 0:
                break
            result += first
            m -= 1
        # 총 덧셈 횟수 다 채웠으면 멈추기
        if m == 0:
            break

        # 가장 큰 값 k번 더하고, 두번째로 큰 값 한번 더하기
        result += second
        m -= 1

    print("단순한 풀이: ", result)


def good_solution(n, m, k, data):
    data.sort()
    first = data[n - 1]
    second = data[n - 2]

    # m / (k+1) : (가장 큰 값 k번 더하고, 두 번째 큰 값 1번 더하는 루틴)의 반복 횟수
    # 1회의 루틴 중 가장 큰 값은 k번 반복되기 때문에, 루틴의 반복횟수에 k를 곱하면 가장 큰 수의 등장횟수!
    count = int(m / (k+1)) * k
    count += m % (k+1) # 나머지는 두 번째로 큰 수의 등장횟수가 됨

    result = 0
    result += (count) * first
    result += (m - count) * second

    print("수열을 이용한 결과: ", result)


print(">> n m k 입력")
n, m, k = map(int, input().split())
print("n: ", n, "\nm: ", m, "\nk: ", k)

print(">> 배열 data 입력")
data = list(map(int, input().split()))
print(data)

simple_solution(n, m, k, data)
good_solution(n, m, k, data)
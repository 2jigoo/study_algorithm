# N이 1이 될 때까지 반복
# 1. N -= 1
# 2. N /=  K (나누어 떨어질 떄만)
# 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수

# 처음에 내가 생각한 거
# 빼주는 과정만큼 반복하게 된다;
def my_solution(n, k):
    result = 0

    while n > 1:
        if n % k == 0:
            n //= k
        else:
            n -= 1
        result += 1

    print(result)


# 단순 풀이
def simple_solution(n, k):
    result = 0

    # 나눌 수 없게 될 때까지 반복 (N < k가 되면 멈춘다)
    while n >= k:
        # 나누어 떨어질 때까지 1씩 감소
        while n % k != 0:
            n -= 1
            result += 1
        # 나눌 수 있게 되면 나눈다
        n //= k
        result += 1

    # 더이상 나눌 수 없게 되면 1씩 감소시키는 과정
    while n > 1:
        n -= 1
        result += 1

    print(result)


# -1 해주는 과정을 하나하나 반복하는 것이 아님!
# 1씩 빼주는 건 수리적으로 연산~

def good_solution(n, k):
    result = 0

    while True:
        # n이 k로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
        target = (n // k) * k
        result += (n - target)

        # 나누어 떨어지는 값을 목표값으로 설정
        n = target

        # n이 k보다 작을 때 (더이상 나눌 수 없을 때) 반복문 탈출
        if n < k:
            break

        # k로 나누기
        # 나눴다고해서 1이 되는 건 아니므로, 반복 진행
        result += 1
        n //= k
        print("[", result, "] n: ", n)

    result += (n - 1)
    print(result)



print(">> n, m 입력!")
n, k = map(int, input().split())
print("n: ", n, ", k: ", k)

my_solution(n, k)
# simple_solution(n, k)
# good_solution(n, k)
print(">> n m 입력")
n, m = map(int, input().split())
print("n: ", n, ", m: ", m)

# A: 북쪽으로부터 떨어진 칸의 개수. 행
# B: 서쪽으로부터 떨어진 칸의 개수. 열

# 상하좌우. 바다 X
# 1. 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정함
# 2. 왼쪽 방향에 가보지 않은 칸 존재?
#   2-1. true: 회전 + 한 칸 전진
#   2-2. false: 회전만하고 1단계
# 3[A]. 네 방향 모두 이미 가본 칸이거나
# 3[B]. 바다로 되어 있는 칸인 경우
#   3-1. 방향을 유지한 채로 한 칸 후진. 1단계(반복문의 처음으로)
#   3-2. 한 칸 뒤가 바다라면 움직임 X


# 방문기록 맵을 생성해 0으로 초기화
visited = [[0] * m for _ in range (n)]


# 위치, 방향 입력 받기
print(">> x y direction 입력")
x, y, direction = map(int, input().split())
visited[x][y] = 1

print("x: ", x, ", y: ", y, ", direction: ", direction)


# 맵 정보 입력 받기
# 바다: 1, 육지: 0
print(n, "x", m, " 크기의 맵 정보 입력")

map_info = []
for i in range(n):
    map_info.append(list(map(int, input().split())))

# 북, 동, 남, 서
x_steps = [-1, 0, 1, 0]
y_steps = [0, 1, 0, -1]


def turn_left():
    # 전역변수인 direction를 사용
    global direction
    
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
# 해당 자리에서 회전한 횟수
turn_time = 0

while True:
    # 1. 왼쪽 방향부터 차례대로 갈 곳을 정함
    turn_left()
    next_x = x + x_steps[direction]
    next_y = y + y_steps[direction]

    # 2. 왼쪽 방향에 가보지 않은 칸 존재?
    # 2-1. true -> 회전 및 전진
    if visited[next_x][next_y] == 0 and map_info[next_x][next_y] == 0:
        visited[next_x][next_y] = 1
        x = next_x
        y = next_y
        count += 1
        turn_time = 0 # 찐으로 돌았으니 turn_time 초기화
        continue

    # 2-2. false -> 회전만. (회전했을 때 가보지 않은 칸이 없는 경우)
    else:
        turn_time += 1
        # 진짜 회전은 loop 돌고 첫부분에서 수행.
        # turn_time: 해당 자리에서 회전한 횟수 기록

    # 3. 사방이 모두 갈 수 없는 경우. 방향을 유지하되
    if turn_time == 4:
        next_x = x - x_steps[direction]
        next_y = y - y_steps[direction]

        # 3-1. 후진할 수 있다면 이동
        if map_info[next_x][next_y] == 0:
            x = next_x
            y = next_y
        # 3-2. 뒤가 바다라면 종료.
        else:
            break
        
        # 이동했으니까 turn_time 초기화
        turn_time = 0

print(count)
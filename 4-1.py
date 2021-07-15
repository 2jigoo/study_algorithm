print(">> n:")
n = int(input())

x, y = 1, 1

print(">> cmd:")
plans = list(input().split())


# x가 가로일 것 같지만 list[x][y]라는 형태를 생각했을 때, x는 행(세로 좌표), y는 열(가로 좌표)이다.
# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']


for plan in plans:
    # 이동명령 찾아서, 예상 좌표값 얻기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 예상 좌표가 범위를 넘어섰을 때 움직이지 않는다
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    # 범위 안인 경우 이동
    x, y = nx, ny


print(x, y)
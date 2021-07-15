# 00:00:00 ~ N:59:59 범위에서 3이 하나라도 포함되는 모든 경우의 수

h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # HHMMSS 형태의 (i시 j분 s초) 시간이 된다
            # 이 문자열에서 3이 들어갔는지 카운팅
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
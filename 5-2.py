from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 3 7 1 4
queue.reverse() # 역순 변경
print(queue) # 4 1 7 3

# deque를 list로 변환
list_from_queue = list(queue)
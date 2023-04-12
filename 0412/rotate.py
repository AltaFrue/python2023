from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.appendleft(i)

print(deque_list)
deque_list.rotate(2)
print(deque_list)
deque_list.rotate(2)
print(deque_list)
deque_list.extend([5, 6, 7])
print(deque_list)
deque_list.extendleft([5, 6, 7])
print(deque_list)
# 큐(Quene)

import queue
# Queue로 큐 만들기
# FIFO(First-in, First_Out) - 가장 일반적인 큐
data_queue = queue.Queue()
data_queue.put("coding")
data_queue.put(1)
print(data_queue.qsize()) # 2
print(data_queue.get()) # coding
print(data_queue.qsize()) # 1
print(data_queue.get()) # 1
print(data_queue.qsize()) # 0

# LifoQueue로 큐 만들기
# LIFO(Last-In, First-Out)
data_queue2 = queue.LifoQueue()
data_queue2.put("python")
data_queue2.put("Hello")
print(data_queue2.qsize()) # 2
print(data_queue2.get()) # Hello
print(data_queue2.qsize()) # 1
print(data_queue2.get()) # python
print(data_queue2.qsize()) # 0

# PriorityQueue로 큐 만들기
# 첫 번째 데이터에 우선순위, 두 번째 데이터에 값을 입력
data_queue3 = queue.PriorityQueue()
data_queue3.put((10, "korea"))
data_queue3.put((5, 1))
data_queue3.put((15, "usa"))
print(data_queue3.qsize()) # 3
print(data_queue3.get()) # (5, 1)
print(data_queue3.get()) # (10 , 'korea')

# 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현해보기
queue_list = list()

def enqueue(data) :
  queue_list.append(data)

def dequeue() :
  data = queue_list[0]
  del queue_list[0]
  return data

for index in range(10) :
  enqueue(index)

print(len(queue_list))
print(dequeue())

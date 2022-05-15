# 스택(Stack)
# 데이터를 제한적으로 접근할 수 있는 구조
# 가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조
# 큐 = FIFO <=> 스택 = LIFO
# push() : 데이터를 스택에 넣기 / pop() : 데이터를 스택에서 꺼내기

def recursive(data) :
  if data < 0 :
    print("ended")
  else : 
    print(data)
    recursive(data -1)
    print("returned", data)

recursive(4)
# 4
# 3
# 2
# 1
# 0
# ended
# returned 0
# returned 1
# returned 2
# returned 3
# returned 4


data_stack = list()
data_stack.append(1)
data_stack.append(2)
print(data_stack) # [1,2]
data_stack.pop()
print(data_stack) # [1]

stack_list = list()
def push(data) :
  stack_list.append(data)

def pop():
  data = stack_list[-1]
  del stack_list[-1]
  return data

for idx in range(10) :
  push(idx)

print(pop()) # 9
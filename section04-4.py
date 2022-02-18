# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리 : 순서x, 중복x, 수정o, 삭제o
# Key, Value (Json) -> MongoDB

# 선언
a = {'name' : "Park", 'Phone' : '010=7777-8888', 'birth' : 220218}
b = {0 : 'Hello Python', 1 : 'Hello Coding'}
c = {'arr' : [1, 2, 3, 4, 5]}

# 출력
print(a['name'])
print(a.gdt('name'))
print(a.get('address'))
print(c['arr'][1:3])

# dict 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
print(a)

# keys, values, items
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(list(a.items()))
print(2 in b)
print('name' in a)

# 집합(Sets) : 순서x, 중복x
a = set()
b = set([1, 2, 3, 4])
c= set([1, 4, 5, 6, 6, 6])

print(type(a))
print(c)

t = tuple(b)
print(t)
l = list(b)
print(l)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1.intersection(s2))
print( s1 & s2)

# 합집합
print(s1.union(s2))
print(s1 | s2)

# 차집합
print(s1.difference(s2))
print(s1 - s2)

# 추가 & 제거
s3 = set([7, 8, 10, 15])

s3.add(18)
print(s3)

s3.remove(15)
print(s3)
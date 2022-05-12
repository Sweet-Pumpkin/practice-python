# 리스트와 딕셔너리
from pickle import TRUE


중고차 = [ 'K5', 'white', 600 ]
중고차[1] = 'black'
중고차2 = { 'brand' : 'BMW', 'model' : '520d' }

print(중고차)
print(중고차2['brand'])

# if문
재고량 = 10
중고차재고 = ['K5', 'BMW', 'Tico']
# if 조건식 : 
#   조건식이 참일 경우 실행할코드

if 재고량 > 0 : 
  print('지금주문가능합니다')

if 'K6' in 중고차재고 :
  print('지금주문가능합니다')
else :
  print('주문불가능함ㅅㄱ')

# for 반복문
for i in range(0, 5) :
  print('BMW 있어요')

for i in 중고차재고 :
  print(i)

# def
def 인사하기() :
  print('안녕하세요 중고차딜러 차은우입니다.')

인사하기()

def 모자(구멍 ,구멍2) :
  print(구멍 + 구멍2)

모자(1, 2)
모자(2, 3)

def 함수() :
  return 10

print(함수())
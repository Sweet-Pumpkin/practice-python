# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈

# 1. 아래 문자열의 길이를 구해보세요.
from audioop import reverse


q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"

# A
print(len(q1)) # 정답

# 2. print 함수를 사용해서 아래와 같이 출력해보세요
#    apple;orange;banana;lemon

# A
print('apple;orange;banana;lemon') # 정답

# 3. 화면에 * 기호 100개를 표시해하세요.

#A
print('*' * 100) # 정답

# 4.문자열 "30"을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.

# A
q4 = 30
print(int(q4), float(q4), str(q4), complex(q4)) # 정답

# 5. 다음 문자열 "Niceman"에서 "man" 문자열만 추출해보세요.

# A
q5 = "Niceman"
print(q5[4:]) # 정답

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"

# A
q6 = "Strawberry"
print(q6[::-1]) # 정답

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"

# A
q7 = "010-7777-9999"
print(q7.replace('-', '')) # 정답

# 다른 정답
# print(q7[0:3] + q7[4:8] + q7[9:13])

# 정규표현식을 활용한 정답
# import re / print(re.sub('[^0-9], '', q7))

# 8. 다음 문자열(url)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"

# A
q8 = "http://daum.net"
print(q8[7:]) # 정답

# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"

# A
q9 = "NiceMan"
q9_upper = q9.upper()
q9_lower = q9.lower()
print(q9_upper, q9_lower) # 정답

# 다른 정답
# print("Niceman".upper())
# print("Niceman".lower())

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"

# A
q10 = "abcdefghijklmn"
print(q10[2:5])

# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]

# A
q11 = ["Banana", "Apple", "Orange"]
del q11[1]
print(q11) # 정답

# 다른 정답
# q11.remove("Apple") / print(q11)

# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)

# A
q12 = (1,2,3,4)
list_q12 = list(q12)
print(list_q12) # 정답

# 다른 정답
# print(list(q12))

# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000, 청소년 - 70000, 아동 - 30000>

# A
q13 = {'성인' : 100000, '청소년' : 70000, '아동' : 30000}
print(q13) # 정답

# 14. 13번에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
q13['소아'] = 0
print(q13) # 정답

# 15. 13번에서 선언한 dict에서 key 항목만 출력해보세요.

# A
print(q13.keys()) # 정답

# 16. 13번에서 선언한 dict에서 value 항목만 출력해보세요.

# A
print(q13.values()) # 정답
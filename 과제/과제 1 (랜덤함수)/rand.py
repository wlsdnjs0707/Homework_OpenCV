import numpy as np

# 0부터 50사이의 정수형 원소를 500개 만들어서 A에 저장했습니다.
A = np.random.randint(0, 50, 500)

# 중복된 갯수를 저장할 리스트 생성
count = [0 for _ in range(51)]

# 0부터 50까지 해당 정수가 몇번 중복되었나 개수를 저장합니다.
# numpy.ndarray 에는 count 속성이 없어서 배열 'B'로 변환하였습니다.
B = list(A)

for i in range(0, 51):
    count[i] = [i, B.count(i)]

# 상위 3개를 뽑기 위해 카운트(중복된 개수)를 기준으로 내림차순으로 정렬한 뒤 3개를 출력합니다.
count.sort(key=lambda x: x[1], reverse=True)

print(count[0][0], ',', count[0][1], '회 중복')
print(count[1][0], ',', count[1][1], '회 중복')
print(count[2][0], ',', count[2][1], '회 중복')


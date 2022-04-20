#하노이의 탑 이동순서 알고리즘
def hanoi(x,n1,n2,n3): # n1: 시작 기둥, n2: 보조 기둥, n3: 목표 기둥
    if (x==1):
        move.append([n1, n3])
    else:
        hanoi(x-1,n1,n3,n2)  # 보조기둥으로 (전체 - 1)의 원판을 옮긴다. 
        move.append([n1, n3]) # 가장 큰 원판을 목표 기둥으로 옮긴다. 
        hanoi(x-1,n2,n1,n3) # 보조기둥으로 옮겨진 원판을 목표 기둥으로 옮긴다.
        
move = []

hanoi(int(input()),1,2,3)

print(len(move)) # 이동 횟수 출력
print(move) # 이동 순서 출력

#하노이의 탑 이동순서 알고리즘
def hanoi(x,n1,n2,n3):
    if (x==1):
        move.append([n1, n3])
    else:
        hanoi(x-1,n1,n3,n2)
        move.append([n1, n3])
        hanoi(x-1,n2,n1,n3)
        
move = []

hanoi(4,1,2,3)

print(len(move))
print(move)

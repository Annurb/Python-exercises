n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

if x2 == (n-x1+1) and y2 == y1:
    print("S")
else:
    print("N")

t = int(input())
for _ in range(t):
    h,_,n = map(int, input().split())
    n-=1
    print(f'{n%h+1}{n//h+1:02d}')
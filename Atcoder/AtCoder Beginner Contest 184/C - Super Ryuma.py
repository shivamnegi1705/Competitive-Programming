# Question Link:- https://atcoder.jp/contests/abc184/tasks/abc184_c

a,b = list(map(int,input().split()))
c,d = list(map(int,input().split()))
d1 = c-a
d2 = d-b
diff = abs(abs(d1)-abs(d2))
if [a,b]==[c,d]:
    print(0)
elif abs(d1)==abs(d2) or (abs(d1)<3 and abs(d2)<3) or (abs(d1)==3 and abs(d2)==0) or (abs(d1)==0 and abs(d2)==3):
    print(1)
elif diff<=3 or diff%2==0:
    print(2)
else:
    print(3)

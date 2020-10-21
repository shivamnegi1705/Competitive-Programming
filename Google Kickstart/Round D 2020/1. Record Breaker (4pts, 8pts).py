# Question Link:- https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000387171

for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    stack = []
    stack.append(arr[0])
    if 1 < n and arr[0] > arr[1]:
        ans += 1
    if n == 1:
        ans = 1
    for i in range(1, n):
        if arr[i] <= stack[-1]:
            stack.append(arr[i])
        else:
            f = 0
            while True:
                if stack[-1] < arr[i]:
                    stack.pop()
                if stack == []:
                    f = 1
                    break
                if stack[-1] >= arr[i]:
                    break
            if f == 1:
                if i+1<n and arr[i]>arr[i+1]:
                    ans += 1
                elif i + 1 >= n:
                    ans+=1
                stack.append(arr[i])
                # print(stack,i)
    print('Case #'+str(t+1)+':',ans)

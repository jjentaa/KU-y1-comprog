n, target = map(int,input().split())

t_ls = []
for i in range(n):
    t = int(input())
    t_ls.append(t)
# print(t_ls)

# t_ls.sort()

right = max(t_ls)*target
left = 1
#b_search
while(left<=right):
    mid = (right+left)//2

    counter=0
    for i in t_ls: counter+=mid//i

    # if(counter==target):
    #     left=mid
    #     break
    if(counter>=target):
        right = mid-1
    else:
        left=mid+1

print(left)
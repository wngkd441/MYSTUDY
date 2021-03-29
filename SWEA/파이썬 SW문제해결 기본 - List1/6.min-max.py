T = int(input()) # Number of Test Case
def get_max(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst[-1]

def get_min(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst[0]

for j in range(T):
    N = int(input()) # Number of digits
    lst = list(map(int, input().split()))
    ans = get_max(lst) - get_min(lst)
    print(f'#{j+1} {ans}')

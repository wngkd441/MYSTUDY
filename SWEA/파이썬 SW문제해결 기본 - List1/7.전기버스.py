T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split()) # K : 충전 한 번으로 갈 수 있는 정류장 수, N : 종점, M : 충전기 수
    battery_lst = list(map(int, input().split()))
    station_lst = [0] * (N+1)

    for i in battery_lst:
        station_lst[i] += 1

    start = 0
    now = K
    cnt = 0

    while True:
        zero = 0
        for i in range(start+1, now+1):
            if station_lst[i] == 1:
                start = i
            else:
                zero += 1
        if zero == K:
            cnt = 0
            break

        cnt += 1
        now = start + K

        if now >= N:
            break

    print(f"#{test_case} {cnt}")

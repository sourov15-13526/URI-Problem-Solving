while(True):
    try:
        sum = 0
        a, b = list(map(int, input().split()))
        m = max(a, b)
        n = min(a, b)
        if a <= 0 or b <= 0:
            break
        for k in range(n, m + 1):
            sum += k
            print(k, end=" ")
        print("Sum={}".format(sum))
        sum = 0
    except EOFError:
        break


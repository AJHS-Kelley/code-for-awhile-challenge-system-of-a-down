while True:
    n = int(input())
    if n == -1:
        break
    i = 1
    totalMiles = 0
    curMiles = 0
    preHours = 0
    curHours = 0
    dif = 0
    while i <= n:
        set = input().split(" ", 1)
        curMiles = eval(set[0])
        curHours = eval(set[1])
        totalMiles += curMiles * (curHours - preHours)
        preHours = eval(set[1])
        i+=1
    print(f"{totalMiles} miles")
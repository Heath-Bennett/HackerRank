# given the participants' score sheet for your University sports Day, you are required to find the runner-up score.
#You are give n scores. store them in a list and find teh score of the runner-up. -100 <= A[i] <= 100

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    best = -101
    secBest = -101

    for i in arr:
        if i > best:
            secBest = best
            best = i
        if i > secBest and i != best:
            secBest = i 

    print(secBest)

#print one string that counts from 1 to n

if __name__ == '__main__':

    n = int(input())
    i = 1
    count = ""
    while i <= n:
        count = (count + str(i))
        i+=1

    print(count)


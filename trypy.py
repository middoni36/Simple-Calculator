def findastr(searchstr, value):  # bruteforce search algorithm
    i = 0
    j = 0
    while (i <= len(searchstr) - len(value)):
        while j < len(value):
            if searchstr[i + j] == value[j]:
                j = j + 1
            else:
                j=0
                break

        if j == len(value):
           return i
           break
        else:
            i = i + 1



print(findastr("11+12","+"))


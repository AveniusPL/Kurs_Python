def pascal_triangle(n):
    trow = [1]
    y = [0]
    for x in range(n):
        print(str(trow).center(30))
        ntrow = []
        ltrow = y + trow
        rtrow = trow + y
        i = 0
        j = 0
        while i != len(ltrow) and j != len(rtrow):
            ntrow.append(ltrow[i] + rtrow[j])
            i += 1
            j += 1
        # for l, r in zip(y+trow, trow+y):
        #     ntrow.append(l+r)
        trow = ntrow

    return n>=1
pascal_triangle(6)
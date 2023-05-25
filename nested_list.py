if __name__ == '__main__':
    list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([name,score])
    findScore = [x[1] for x in list]
    sortScore = sorted(set(findScore))
    findName = sorted([y[0] for y in list if(sortScore[1] == y[1])])
    for z in findName:
        print(z)

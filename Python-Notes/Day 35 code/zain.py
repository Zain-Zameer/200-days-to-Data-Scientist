if __name__ == '__main__':
    nuces_st = []
    for i in range(int(input())):
        record = []
        name = input()
        score = float(input())
        record.append(name)
        record.append(score)
        nuces_st.append(record)
    nums = []
    for i in range(len(nuces_st)):
        nums.append(nuces_st[i][1])
    nums.sort()
    # print(nums)

    names = []
    for num in nums:
        for i in range(len(nuces_st)):
            if(num==nuces_st[i][1]):
                if nuces_st[i][0] in names:
                    continue
                names.append(nuces_st[i][0])

    # print(names)

    medals = []
    new_nums = list(dict.fromkeys(nums))
    val = 1
    for i in range(len(names)):
        if new_nums[1]==nums[i]:
            medals.append(names[i])
    
    medals.sort()
    for name in medals:
        print(name)
       

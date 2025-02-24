nuces_st= [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

nums = []
for i in range(len(nuces_st)):
    nums.append(nuces_st[i][1])
nums.sort()
print(nums)

names = []
for num in nums:
    for i in range(len(nuces_st)):
        if(num==nuces_st[i][1]):
            if nuces_st[i][0] in names:
                continue
            names.append(nuces_st[i][0])

print(names)

medals = []
for i in range(len(names)):
    if nums[1]==nums[i]:
        medals.append(names[i])

medals.sort()
print(medals)
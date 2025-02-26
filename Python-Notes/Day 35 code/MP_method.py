def writinglines(content,fileVar):
    for i in range(len(content)):
        if str(content[i]):
            fileVar.writelines(content[i])
            if i!=len(content)-1:
                fileVar.writelines('\n')


f = open("data2.txt","w")
f.writinglines = lambda content:writinglines(content,f)
print(f)
l = ["Line 1","Line 2","Line 3","Line 4","Line 5"]
f.writinglines(l)
f.close()
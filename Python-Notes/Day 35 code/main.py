def writinglines(content,fileVar):
    for i in range(len(content)):
        if str(content[i]):
            fileVar.writelines(content[i])
            if i!=len(content)-1:
                fileVar.writelines('\n')

f = open("data.txt","w")
l = ["line1","line2","line3","line4","data file handling"]
writinglines(l,f)
f.close()
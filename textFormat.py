bibletxt=open("bible.txt","r")
bible=bibletxt.readlines()
bibletxt.close()

str=bible[0]
str=str.split('\t')
str=str[0]+"   "+str[1]

print(str)
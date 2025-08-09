# opening file in read mode
#file=open("c:/\Users\\ELCOT\\Documents\\RMgit\\githubms2\\new.txt","r")
#content=file.read()
#print(content)
#file.close

#openig in write mode
file=open("c:\\Users\\ELCOT\\Documents\\RMgit\\githubms2\\new.txt","w")
file.write("\n Hello this is Muthuswamy \n")
file.write("This is the new line added")
file.close()

#appending 
file=open("c:\\Users\\ELCOT\\Documents\\RMgit\\githubms2\\new.txt","a")
file.write("\nif we open the file in write mode the old datas are been deleted\n")
file.write("but if we open in append mode it won't delete the old file")
file.close

file = open("c:\\Users\\ELCOT\\Documents\\RMgit\\githubms2\\new.txt", "r")
for line in file:
    print(line.strip())  # strip removes \n
file.close()


with open("c:\\Users\\ELCOT\\Documents\\RMgit\\githubms2\\index.html", "w") as file:
    file.write("<html>\n<head>\n<title>Muthuswamy</title>\n</head>\n<body><h1>Hi i'm MUTHUSWAMY</h1></body></html>")



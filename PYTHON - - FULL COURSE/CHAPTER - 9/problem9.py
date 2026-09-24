# with open("poem.txt") as f :
#     print(f.read())
#     if "twinkle" in f:
#         print("Present")
#     else:
#         print("Not Present")    

# import random

# def game():
#     print("You are playing the game.")
#     score = random.randint(1,62)
#     #Fetch the Highscore
#     with open("Hi-score.txt") as h:
#         hiscore = h.read() 
#         if(hiscore != ""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0   
 
#     print(f"Your score : {score}")
#     if(score>hiscore):
#         #write this hiscore to the file
#         with open("Hiscore.txt" , "w") as k:
#             k.write(str(score))

#     return score

# game()        

# def generateTable(n):
#     table = ""
#     for i in range(1,11):
#         table += f"{n} X {i} = {n*i}\n"

#     with open(f"tables/table_{n}.txt","w") as f: #tables/table_{n} means that the folder name is tables and table_{n}  is a seprate file under it.
#         f.write(table)


# for i in range(2,21):
#     generateTable(i)

# word ='donkey'

# with open("Sdonkey_file.txt" , "r") as f:
#     content = f.read()
    
# contentNew = content.replace(word , "######")

# with open("Sdonkey_file.txt" , "w") as f:
#     content = f.write(contentNew)



# words =['donkey' , 'bad' , 'ganda']
# replaced_words = ["######" , "***" , "$$$$$"]

# with open("problem5.txt" , "r") as g:
#      content = g.read()

# for word in words: 
#      content = content.replace(word , "#" * len(word))

# with open("problem5.txt" , "w") as g:
#     content = g.write(content)


# with open("problem5.txt") as k:
#      lines = k.readlines()

# lineno = 1
# for line in lines:
#        if ("python" in line):
#            print(f"python is present.Line no.{lineno}")
#            break
#        lineno += 1    
# else:
#        print("python is not present.")


# with open("this.txt") as f:
#     content = f.read()

# with open("this_copy.txt" , "w") as f:
#     f.write(content)     


# with open("this.txt") as l:
#     content = l.read()

# with open("this_copy.txt") as p:
#    content1 = p.read()     

# if content == content1:
#     print("Print ! Yes these files are identical.")
# else:
#     print("No these files are not identical")

# with open("problem5.txt" , "w") as d:
#     d.write("")

# To rename a file simply copy the content of the file and write it in a new file
# of your choice.To delete the old file use the os module.

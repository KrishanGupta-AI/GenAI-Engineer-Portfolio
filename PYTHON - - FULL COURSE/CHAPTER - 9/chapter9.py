#The random access memory is volatile,and all its contents are lost once a program
#terminates in order to persist the data forever,we use files.

#RAM is a volatile memory meaning the output is saved temporarily there and not permanent.
#On refreshing or restarting the system the output data stored in the memory would already be vanished.

#HDD ---> Non-volatile meaning the output data will remain there permanently.


#A file is data stored in a storage device.A python program can talk to the file by reading 
#content from it and writing the content to it.

#TYPES OF FILES :
# 1.)Text Files (.txt , .c etc)
# 2.)Binary Files (.jpg , .dat etc)

# f = open("file1.txt")
# data = f.read()
# print(data)
# f.close()

#Opening an File :
#Python has an open() function for opening files.It takes 2 parameters : (Filename and mode.)
# open("filename","mode of opening(read mode by default)")

#The moment you open an existing file in "w" mode, Python erases all its previous contents.


# k = open("file2.txt","w")

# string = 'Hey you look very amazing.'
# k.write(string)
# k.close()

#readlines() is used to readline() function is used to write all the content of file at one but in 
# a line by line format stored in a list.  
m = open("otherfunctions.txt" , "r")
lines = m.readlines()
print(lines,type(lines))
m.close()

# line = m.readline()
# while(line != ""):
#     print(line)
#     line = m.readline()
    
# m.close()

#MODES OF OPENING A FILE :

# 1.) r ---> open for reading.
# 2.) w ---> open for writing.
# 3.) + ---> open for updating.
# 4.) 'rb' ---> will open for read in binary mode.
# 5.) 'rt' ---> will open for read in text mode.

m = open("otherfunctions.txt","a")
string1 = "Hello i am fgoow."
m.write(string1)
m.close()


f = open("file1.txt")
print(f.read())
f.close()

#The same can be written using with statement like this:    
with open("file1.txt") as f:
    print(f.read())

#We don't have to explicitly close the file.

    
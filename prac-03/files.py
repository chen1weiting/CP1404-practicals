################## Q1 ##############################

#taking input from user and assignin that inpput to a variable 'name'
name=input('Enter your Name : ')

# bellow line, if a txt file with same name exist then will be opened at write mode(means
#anything already written will be deleted, and will start afresh). 'w' mean write mode
#if the file does not exist it will create a txt with name vaiable as its name
#ie: suppse the user writes 'Bob', then a file Bob.txt will be crated
file=open(name+'.txt','w')
file.write(name)# this line will write the name 'Bob' iN THAT TXT FILE
file.close()#This line will close the file.


############################# Q2 ########################################################
#same as it will open the file 'Bob.txt' or whatever the use input is in read mode, content already written
#does not get deleted
open_file=open(name+'.txt','r')
content=open_file.read()# this line will read the file
open_file.close()# close the file again
print('Your Name is',content)# print the content of the file 'Bob'txt'




################## #Q3 ############################################################

#please type the full path of your prac_02 folder and then the number.txt file name
# like num_file=open('c:\Users\Bob\Desktop\prac_02\number.txt, 'w')
num_file=open('full path location of prac_02 folder\number.txt','w')
num_file.writelines(['17\n','42\n','400\n'])# here \n mean newline after each number
num_file.close()

#opening the number.txt file
numfile=open('full path location of prac_02 folder\number.txt','r')
line1=numfile.readline()# reading first line, you can also use a for loop for readin first 2 line
line2=numfile.readline()# reading second line
numfile.close()
# printing the sum of first two line, the line is a string, so we used int to convert it to integer for sum
print(int(line1)+int(line2))



####################### Q4 ####################################

numfile=open('prac02/number.txt','r')#opening the number.txt file in reading mode
lines=numfile.readlines()#reading all lines
numfile.close()#closing file

total=0 # taking a variable total to sum up value from txt file, at first the value is 0
for line in lines:#extracting line from lines
  total = total+int(line) # adding each line diigit value to the total
print(total)# printing the total
#kahramankostas
#Assignment_1_2.py

##################### TASK 1 ############################################
alphabe="abcdefghijklmnopqrstuvwxyz"  # a string variable for holding alphabet
alphabe2="*abcdefghijklmnopqrstuvwxyz" ## it is only for the first line of table
print(*alphabe2,sep=" | ") ## print alphabe2 to the screen and separate letters with "|"
vigenere_array=""          ### a string variable for holding vigenere table
for i in range (0,26):     # a for loop between 0-26   
    tablo=""               ## a string variable for holding vigenere table  1 line only for printing to the screen 
    tablo=alphabe[i]       ## first character of the table assigned to the string variable
    for j in range (i,i+26):  # a for loop between i- i+26  
        vigenere_array=vigenere_array+alphabe[j%26]  # add a letter to the vigenere table / this line makes the table
        tablo=tablo+alphabe[j%26] # ## make  a vigenere table  line for printing to the screen 
    print(*tablo,sep=" | ") ## print vigenere table  line  to the screen and separate letters with "|"



##################### TASK 2 ############################################    
plaintext=input("input your plain text")  # input from user / plain text
plaintext=plaintext.lower()  # all text is converted to lowercase.
key=input ("input your key") # input from user / key
key=key.lower()    # all key is converted to lowercase.
key_len=len(key)  # a variable for holding length of key



##################### TASK 3 ############################################           
for i in range (key_len,len(plaintext)): # a for loop from key length to the length of plain text 
        key=key+key[i%key_len]   # the key value is being extended to bring the same length with plain text /// add letter of key to the key during the loop



##################### TASK 4 ############################################        
cipher_text=""   ### a string variable for holding cipher text
for i in range (0,len(plaintext)): # a for loop from 0 to the length of plain text 
    cipher_text_index= (ord(plaintext[i])-97)+(ord(key[i])-97)*26  #  row number + column * 26 = index number of the letter in the table
    cipher_text=cipher_text + chr(ord(vigenere_array[cipher_text_index])) # add a new letter to the cipher text          
print (cipher_text)     # print screen the  cipher text  
        

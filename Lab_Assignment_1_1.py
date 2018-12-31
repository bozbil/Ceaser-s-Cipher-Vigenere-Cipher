#kahramankostas
#Assignment_1_1.py


##################### TASK 1 ############################################
encrypted_text= """HUKHZ MVYCH SVYAO HAJHU UVAIL JVTWB ALKIF ZAHAB YLOLO   
HZWHZ ZLKAO YVBNO TVYLI HAASL ZHUKW LYPSZ AOHUF VBOHC
LPUNV SKAOV BNOFV BILAD PJLOP ZOLPN OAHUK OLJVT LZUVD MYVTA
OLZAV YTPUN VMPZL UNHYK VMDOP JODLI LHYAP KPUNZ HUKNY
LHADL HYPUL ZZPZV UOPTV YPDVB SKDHR LOPTO PZUHT LPZWL YLNYP
UMYVT SVYKV MAOLY PUNZI VVRMP CLJOH WALYV UL"""  # text input 
encrypted_text=encrypted_text.lower()  #  text is converted to lowercase.
encrypted_text=encrypted_text.replace(" " , "") #All space characters in the text have been deleted.



##################### TASK 2 ############################################
shifting_number=1 ## A  variable for while loop and shifting for ceasar cipher // loop Counter 
while shifting_number<=26 :  ## A WHILE LOOP BETWEEN 1-26 //  shifting for ceasar cipher
    plain_text=""     ## a empty string variable for holding plain text during for loop
    for counter in encrypted_text:  # for loop in the letters of encrypted text 
        if (ord(counter)+shifting_number)>122: # if  numeric equivalents of letter + shifting number bigger then "z" / "122"  than mod 26 and than add into plain text
            plain_text=plain_text+chr(ord(counter)-26+shifting_number)
        else:                    # if not  numeric equivalents of letter + shifting number add into plain text
            plain_text=plain_text+chr(ord(counter)+shifting_number) 
    shifting_number=shifting_number+1   #Increase the Counter 
    print ( "shifting number = ", shifting_number)   # print screen shifting number
    print ("your deencryped message is",plain_text ) # print screen plain text
    print ( )                                       # print screen a line

    

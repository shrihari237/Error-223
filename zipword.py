import time
import zipfile

folderPath = input("Enter the path here")
zipF = zipfile.ZipFile(folderPath)

global result
result = 0
global tried
tried = 0 
c =0


if not zipF:
    print("File is not password protected you can successfully open it.")

else:
    startTime = time.time()
    wordListFile = open("wordlist.txt","r",errors="ignore")  
    body = wordListFile.read().lower()
    words = body.split("\n")
   
    for word in words:
        password = word.strip().encode('utf8')
        print('Trying to decode password by: {}'.format(word))
        c =c+1

        try:
            with zipfile.Zipfile(folderPath,'r') as zf:
                zf.extractall(pwd = password)
                print("Success, the password is "+word)
                endTime = time.time()
                result = 1
                break
        except:
            pass 


    
    if result == 0:
        duration = time.time()-startTime
        print("Sorry, password not found.A total of "+str(c)+" possible combinations tried in "+str(duration)+" seconds. Password is not of 4 characters") 
    else:
     
        print("Congratulations!! Password found after trying "+str(c)+" combinations in "+str(duration)+"seconds")
       

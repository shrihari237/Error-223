counter = 0

characters = ['0','1','2','3','4','5','6','7','8','9',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

file = open("wordlist.txt","w")

for i in characters:
    for j in characters:
        for o in characters:
            for p in characters:
                guess = i + j + o + p
                print(guess)
                file.write(guess)
                file.write("\n")
                counter +=1
print("wordlist of {} password created".format(counter))                
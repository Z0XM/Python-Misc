print("I can tell the dictionary rank of a Word")

def factorial(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1)

def countSame(word):
    count = []
    pos = 0
    while pos<len(word):
        value = word.count(word[pos])
        if value>1:
            count.append(value)
            pos += value - 1
        pos+=1

    value = 1
    for val in count:
        value *= factorial(val)
    return value

def start(message = None):
    print("\n**********************************************************")
    if message:print(f"{message}\n**********************************************************")
    
    word = input("Enter a Word : ")
    if not len(word):start("Type a Word!")
    if not word.isalpha():start("Only alphabets allowed!")

    sortedWord = list(word)
        
    for n in range(len(sortedWord),-1,-1):
        for val in range(1,n):
            if sortedWord[val]<sortedWord[val-1]:
                sortedWord[val],sortedWord[val-1] = sortedWord[val-1],sortedWord[val]

    rank = 0
    index = 0
    while index<len(word) and len(sortedWord):
        n = sortedWord.index(word[index])
        rank += int(n*factorial(len(sortedWord) - 1)/countSame(sortedWord))
        sortedWord.remove(word[index])
        index+=1
    
    rank+=1
    print(f"Rank of {word} is : {rank}")
    if input("Again?('yes'->y | 'no'->Enter) : ") == 'y':start()

start()

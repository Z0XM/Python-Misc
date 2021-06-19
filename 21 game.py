N = 21
n = 4
print(f"{N}-Game")

def ComputerMove(count):
    return n+1 - count%(n+1)

def Start():
    print("\n************************************************************")
    Count = 0

    while Count<N-1:
        do_again = True
        while do_again:
            do_again = False
            user_input = input("Your Turn : ").split(',')
            for pos in range(len(user_input)):
                val = list(user_input[pos])
                while val.count(' ')>0:val.remove(' ')
                user_input[pos] = ''.join(val)
            for val in user_input:
                try:val = int(val)
                except Exception:
                    do_again = True
                    print('Invalid Input!')
                    break
                if val<Count:
                    do_again = True
                    print('Invalid Input!')
                    break
            for pos in range(1, len(user_input)):
                if user_input[pos]<=user_input[pos-1]:
                    do_again = True
                    print('Invalid Input!')
                    break
            if int(user_input[len(user_input)-1])>Count+n:
                do_again = True
                print('Invalid Input!')

        Count += len(user_input)
        Count += ComputerMove(Count)

        print("Computer Says : ",end = '')
        move = int(user_input[len(user_input)-1]) + 1
        while move<=Count:
            print(move,end=('\n' if move==Count else ',') )
            move+=1
            
    print("                You Lose\n")
    if input("Again?('yes'->y | 'no'->Any) : ") == 'y':Start()

Start()

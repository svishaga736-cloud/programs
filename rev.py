if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        # Split the input into command and arguments
        cmd, *args = input().split()
        
        # Convert arguments to integers
        args = list(map(int, args))
        
        if cmd == "insert":
            my_list.insert(args[0], args[1])
        elif cmd == "print":
            print(my_list)
        elif cmd == "remove":
            my_list.remove(args[0])
        elif cmd == "append":
            my_list.append(args[0])
        elif cmd == "sort":
            my_list.sort()
        elif cmd == "pop":
            my_list.pop()
        elif cmd == "reverse":
            my_list.reverse()

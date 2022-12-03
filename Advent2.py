'''
completed at 11:25 PM CST
'''

def adv2a(file):
    list = []
    enemy_list = []
    my_list = []
    sum = 0
    
    with open(file, 'r') as read:
        for line in read:
            list.append(str(line))
        for line in list:
            enemy_list.append(line[0])
            my_list.append(line[2])
            
    for i in range(len(my_list)):
        if enemy_list[i] == "A":
            if my_list[i] == "X":
                sum += 1 
                sum += 3
            elif my_list[i] == "Y":
                sum += 2
                sum += 6
            else:
                sum += 3
        elif enemy_list[i] == "B":
            if my_list[i] == "X":
                sum += 1
            elif my_list[i] == "Y":
                sum += 5
            else:
                sum += 9
        else:
            if my_list[i] == "X":
                sum += 7
            elif my_list[i] == "Y":
                sum += 2
            else:
                sum += 6
    print(sum)
    
'''
function adv2b is just adv2a with modifications to scoring, when creating i had completely replaced
adv2a, hence the very similar code and why the both contain a file reader
'''
def adv2b(file):
    list = []
    enemy_list = []
    my_list = []
    sum = 0
    
    with open(file, 'r') as read:
        for line in read:
            list.append(str(line))
        for line in list:
            enemy_list.append(line[0])
            my_list.append(line[2])
            
    for i in range(len(my_list)):
        if enemy_list[i] == "A":
            if my_list[i] == "X":
                sum += 0 
                sum += 3
            elif my_list[i] == "Y":
                sum += 1
                sum += 3
            else:
                sum += 8
        elif enemy_list[i] == "B":
            if my_list[i] == "X":
                sum += 1
            elif my_list[i] == "Y":
                sum += 5
            else:
                sum += 9
        else:
            if my_list[i] == "X":
                sum += 2
            elif my_list[i] == "Y":
                sum += 6
            else:
                sum += 7
    print(sum)
    
if __name__ == "__main__":
    file = str(input("please type the name of your file "))
    adv2a(file)
    adv2b(file)

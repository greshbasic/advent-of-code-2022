def reader1():
    list = []
    with open('sack.txt', 'r') as read:
        for line in read:
            list.append(line)
    return list

def reader2():
    tracker = 0
    list = []
    temp_list = []
    with open('sack.txt', 'r') as read:
        for line in read:
            if tracker != 2:
                temp_list.append(line)
                tracker += 1
            elif tracker == 2:
                temp_list.append(line)
                list.append(temp_list)
                temp_list = []
                tracker = 0
    return list
                
def adv3a(list):    
    cur_length = 0
    sum = 0
    list_length = len(list)
    for i in range(list_length):
        cur_length = len(list[i]) - 1
        x = int(cur_length / 2)
        first_half = (list[i])[0:x]
        second_half = (list[i])[x:-1]
        if(cur_length % 2 == 0):
            cur_length += 1
        for i in range(len(first_half)):
                if second_half.find(first_half[i]) != -1:
                    if ord(first_half[i]) < 97:
                        sum += ord(first_half[i]) - 38   
                        break
                    else:
                        sum += ord(first_half[i]) - 96
                        break
    print("The sum of all common values found between each half of each sack is: " + str(sum))
    
def adv3b(list):    
    sum = 0
    for i in range(len(list)):
        for j in range(len(list[i][0])):
            second_string = list[i][1]
            third_string = list[i][2]
            if second_string.find(list[i][0][j]) != - 1 and third_string.find(list[i][0][j]) != - 1:
                if ord(list[i][0][j]) < 97:
                    sum += ord(list[i][0][j]) - 38
                else:
                    sum += ord(list[i][0][j]) - 96
                break
    print("The sum of all common values found between each set of 3 elves is: " + str(sum))
    
adv3a(reader1())
adv3b(reader2())
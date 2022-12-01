''' completed at 11:25 PM CST '''
def adv1a(big_list):
    mostPos = 0
    mostCount = 0
    iter = 0
    sum = 0
    for list in big_list:
        for num in list:
            sum += num
        if sum > mostCount:
            mostCount = sum
            mostPos = iter
        iter += 1
        sum = 0
    print("the elf at pos: " + str(mostPos) + " has the most calories, being " + str(mostCount) + " calories")
    
def adv1b(big_list):
    sum_list = []
    sum = 0
    for list in big_list:
        for num in list:
            sum += num
        sum_list.append(sum)
        sum = 0
    sum_list.sort()
    top_3_sum = sum_list[-1] + sum_list[-2] + sum_list[-3]
    print(top_3_sum)
            
def reader():
    biglist = []
    smalllist = []
    with open('longnum.txt', 'r') as read:
        for line in read:
            if line != '\n':
                smalllist.append(int(line))
            else:
                biglist.append(smalllist)
                smalllist = []
    return biglist

read_file = reader()
adv1a(read_file)
adv1b(read_file)



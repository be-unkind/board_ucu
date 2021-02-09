'''https://github.com/be-unkind/board_ucu'''
import doctest
def first_check(board: list) -> bool:
    '''
    Every coloured cell in row must not contain the same values.
    '''
    res_list = []
    for element in board:
        temporary_list = list(element)
        for element_1 in temporary_list:
            if (element_1 == '*') or (element_1 == ' '):
                temporary_list.remove(element_1)
        temporary_set = set(temporary_list)
        if len(temporary_list) != len(temporary_set):
            res_list.append('False')
        else:
            res_list.append('True')
    if 'False' in res_list:
        return False
    else:
        return True
            
def second_check(board: list) -> bool:
    '''
    Every coloured cell in culumn must not contain the same values.
    '''
    res_lst = []
    column_lst = []
    for element in board:
        column_lst.append(element[:1]) 
        for element_1 in column_lst:
            if (element_1 == '*') or (element_1 == ' '):
                column_lst.remove(element_1)
        column_set = set(column_lst)
        if len(column_set) != len(column_lst):
            res_lst.append('False')
        else:
            res_lst.append('True')
        column_lst.clear()
    if 'False' in res_lst:
        return False
    else:
        return True


def third_check(board: list) -> bool:
    '''
    Every colored cell with same color have unique value.
    '''
    res_lst = []
    yellow_lst = []
    green_lst = []
    blue_lst = []
    violet_lst = []
    pink_lst = []
    four_lines = board[:4]
    for element in four_lines:
        if element[0] != '*':
            yellow_lst.append(element[0])
        if element[1] != '*':
            green_lst.append(element[1])
        if element[2] != '*':
            blue_lst.append(element[2])
        if element[3] != '*':
            violet_lst.append(element[3])
        pink_lst.append(element[4])
        if '*' not in element[4:10]:
            for num in element[4:10]:
                pink_lst.append(num)
    # fifth line of board
    fifth_line = board[4]
    yellow_lst.append(fifth_line[0])
    green_lst.append(fifth_line[1])
    blue_lst.append(fifth_line[2])
    violet_lst.append(fifth_line[3])
    for num in fifth_line[4:10]:
        pink_lst.append(num)
    # sixth line of board
    sixth_line = board[5]
    yellow_lst.append(sixth_line[0])
    green_lst.append(sixth_line[1])
    blue_lst.append(sixth_line[2])
    for num in sixth_line[3:8]:
        violet_lst.append(num)
    # seventh line of board
    seventh_line = board[6]
    yellow_lst.append(seventh_line[0])
    green_lst.append(seventh_line[1])
    for num in seventh_line[2:7]:
        blue_lst.append(num)
    # eighth line of board 
    eighth_line = board[7]
    yellow_lst.append(eighth_line[0])
    for num in eighth_line[1:6]:
        green_lst.append(num)
    # ninth line of board 
    ninth_line = board[8]
    for num in ninth_line[0:5]:
        yellow_lst.append(num)
    # deleting blank spaces
    yellow_lst = list(filter(lambda a: a != ' ', yellow_lst))
    green_lst = list(filter(lambda a: a != ' ', green_lst))
    blue_lst = list(filter(lambda a: a != ' ', blue_lst))
    violet_lst = list(filter(lambda a: a != ' ', violet_lst))
    pink_lst = list(filter(lambda a: a != ' ', pink_lst))
    all_lsts = [yellow_lst, green_lst, blue_lst, violet_lst, pink_lst]
    # creating sets
    yellow_set = set(yellow_lst)
    green_set = set(green_lst)
    blue_set = set(blue_lst)
    violet_set = set(violet_lst)
    pink_set = set(pink_lst)
    all_sets = [yellow_set, green_set, blue_set, violet_set, pink_set]
    # comparing
    for elemn in range(0, 5):
        if len(all_lsts[elemn]) != len(all_sets[elemn]):
            res_lst.append('False')
        else:
            res_lst.append('True')
    if 'False' in res_lst:
        return False
    else:
        return True

def validate_board(board: list) -> bool:
    '''
    Check through every parameter.
    >>> validate_board(["**** ****","***1 ****","**  3****",\
"* 4 1****","     9 5 "," 6  83  *","3   1  **","  8  2***",\
"  2  ****"])
    False
    '''
    res_lst = []
    if first_check(board) == True:
        res_lst.append('True')
    else:
        res_lst.append('False')
    if second_check(board) == True:
        res_lst.append('True')
    else:
        res_lst.append('False')
    if third_check(board) == True:
        res_lst.append('True')
    else:
        res_lst.append('False')
    if 'False' in res_lst:
        return False
    else:
        return True

doctest.testmod()

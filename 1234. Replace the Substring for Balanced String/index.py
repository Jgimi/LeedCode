def Replace_the_Substring_for_Balanced_String(string):
    temp_string = string.replace('Q','')
    Q_cnt = len(string) - len(temp_string)
    temp_string = string.replace('W','')
    W_cnt = len(string) - len(temp_string)
    temp_string = string.replace('E','')
    E_cnt = len(string) - len(temp_string)
    temp_string = string.replace('R','')
    R_cnt = len(string) - len(temp_string)
    lists = [Q_cnt,W_cnt,E_cnt,R_cnt]
    # sorted(lists,reverse=True)
    # minimum = lists[-1]
    avg = sum(lists)/len(lists)
    # first_two = lists[:2]
    # cnt = 0
    # for i in first_two:
    #     while i > avg:
    #         cnt += 1
    #         i -=1
    # return cnt
    minimum = min(lists)
    new_lists = []
    for i in lists:
        new_lists.append(i-minimum)
    cnt = 0
    for i in new_lists:
        if i>avg:
            cnt += i-avg

    return cnt








s = "QQWE"

print(Replace_the_Substring_for_Balanced_String(s))
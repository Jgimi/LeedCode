def Replace_the_Substring_for_Balanced_String(s):
    lists = []
    all_letters = ['Q', 'W', 'E', 'R']
    cnt=0
    for i in all_letters:
        for j in s:
            if i==j:
                cnt+=1
        lists.append(cnt)
        cnt=0

    avg = sum(lists)/len(lists)
    cnt_for_new_list = 0
    for i in lists:
        if i>avg:
            cnt_for_new_list += i-avg

    return int(cnt_for_new_list)
    # return lists








s = "WWEQERQWQWWRWWERQWEQ"

print(Replace_the_Substring_for_Balanced_String(s))
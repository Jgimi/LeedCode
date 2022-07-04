def Replace_the_Substring_for_Balanced_String(string):
    new_list = []
    string = string.replace(' ','')
    for i in range(0,len(string),4):
        new_list.append(string[i:i+4])
    cnt = 0
    for i in new_list:
        cnt += len(i) - len(set(i))
    return cnt







s = "WWQQRRRRQRQQ"

print(Replace_the_Substring_for_Balanced_String(s))
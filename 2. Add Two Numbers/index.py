def Add_Two_Numbers(l1,l2):
    def convert(l):
        new_l = []
        if isinstance(l,list):
            pass
        else:
            l = list(str(l))
        for i in l[::-1]:
            new_l.append(i)
        return new_l

    def summ(a,b):
        a2 = [str(integer) for integer in a]
        a2_string = "".join(a2)
        a_int = int(a2_string)
        b2 = [str(integer) for integer in b]
        b2_string = "".join(b2)
        b_int = int(b2_string)
        return a_int+b_int

    return convert(summ(convert(l1),convert(l2)))



l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

print(Add_Two_Numbers(l1,l2))
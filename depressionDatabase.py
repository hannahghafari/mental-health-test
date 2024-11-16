answers = list()
count1 = 0
count2 = 0
count3 = 0
count4 = 0


def result(v):
    answers.append(v)
    # print(answers)


def total():

    global count1, count2, count3, count4
    # print(answers)
    for i in answers:
        # print(i)
        if i == 1:
            count1 += 1
        elif i == 2:
            count2 += 1
        elif i == 3:
            count3 += 1
        else:
            count4 += 1
    # print(count1, count2, count3, count4)
    if count1+count2 > count3+count4:
        Tresult = """you're healthy no need to worry.
        You are on the track of success no matter how harsh it may seem always remember that the hard work will payoff"""

    elif count1+count2 == count3+count4:
        Tresult = """take time to chill more.
        Your mental health needs as much care as the physical one make sure you make time for that"""

    else:
        Tresult = """you're at risk of serious damage. 
        depression is one of the most popular mental disorder ,unfortunaltly,
          but don't worry cause it's a phase and with the help of a terapist you will defeat it."""
    return Tresult


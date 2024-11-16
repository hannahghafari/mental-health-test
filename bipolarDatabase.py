

answers = list()
count1 = 0
count2 = 0


def result(v):
    answers.append(v)
    # print(answers)


def total():

    global count1, count2
    # print(answers)
    for i in answers:
        print(i)
        if i == 1:
            count1 += 1
        else:
            count2 += 1
    # print(count1, count2, count3, count4)
    if count1 < count2:
        Tresult = """you're healthy no need to worry.
        You are on the track of success no matter how harsh it may seem always remember that the hard work will payoff"""

    elif count1 == count2:
        Tresult = """take time to chill more.
        Your mental health needs as much care as the physical one make sure you make time for that"""

    else:
        Tresult = """you're at risk of serious damage. 
        bipolar disorder can be inheritentional i recommand you see a doctor."""
    # return Tresult


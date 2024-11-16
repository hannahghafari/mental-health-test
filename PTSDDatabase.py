

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
        Maybe the trauma has passed now and you don't think about it anymore"""

    elif count1 == count2:
        Tresult = "If the trauma has been uncomfortable for you and it has effected your life try talking with friends, family or a doctor"

    else:
        Tresult = """you're at risk of serious damage. the trauma has been so effective that you don't seem to be ok with that.
          I highly recommend you visit a doctor and solve it"""
    return Tresult

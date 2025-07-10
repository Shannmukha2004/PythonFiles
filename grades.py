def cal_avg(li):
    return sum(li)/len(li)
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    elif avg < 50:
        return "F"
def marks_validate(li):
    for x in li:
        if x>=0 and x<=100:
            continue
        else:
            return False
    return True
def student_main():
    Marks= [80, 90, 70, 85, 78]
    print(marks_validate(Marks))
    print(f"{cal_avg(Marks):.2f}")
    print(grade(cal_avg(Marks)))

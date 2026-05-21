def lowest_score(students):
    lowest_score = float('inf')
    nameLowest = ""
    for student in students:
        total = student["Math"] + student["PROG"] + student["DS1"]
        if total < lowest_score:
            lowest_score = total
            nameLowest = student["name"]
    return lowest_score, nameLowest
def calc_highest_score(students):
    highest_score = 0
    nameHighest = ""
    for student in students:
        total = student["Math"] + student["PROG"] + student["DS1"]
        if total > highest_score:
            highest_score = total
            nameHighest = student["name"]
    return highest_score, nameHighest
def main():
    students = [
        {"name":"belal","Math":95,"PROG":90,"DS1":97},
        {"name":"Hamed","Math":90,"PROG":75,"DS1":94},
        {"name":"ahmed","Math":80,"PROG":60,"DS1":80},
        {"name":"youssef","Math":83,"PROG":91,"DS1":75},
        {"name":"rana","Math":99,"PROG":90,"DS1":92},
        {"name":"sara","Math":85,"PROG":51,"DS1":66}
    ]
    for student in students:        
        total = student["Math"] + student["PROG"] + student["DS1"]
        average = total / 3
        print(f"{student['name']} has an average score of {average:.2f} and a total score of {total}.")
    highest = calc_highest_score(students)
    print(f"The highest score among the students is: {highest[0]} ({highest[1]})")
    lowest = lowest_score(students)
    print(f"The lowest  score among the students is: {lowest[0]} ({lowest[1]})")
main()
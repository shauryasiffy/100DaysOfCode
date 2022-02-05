marks_dict={
    "Harry":81,
    "Ron":78,
    "Hiral":98,
    "Sanmpaj":34,
    "Dhatu":46}

grades_dict={}


# using general for loop in dictionary

for nameX in marks_dict:
    marks=marks_dict[nameX]
    if marks>90:
        grades_dict[nameX]="Outstanding"
    elif marks>80:
        grades_dict[nameX]="Exceeds Expectation"
    elif marks>70:
        grades_dict[nameX]="Acceptable"
    if marks<70:
        grades_dict[nameX]="Fail"
print(grades_dict)


# using items() function

for names, marks in marks_dict.items():
    if marks>90:
        grades_dict[nameX]="Outstanding"
    elif marks>80:
        grades_dict[nameX]="Exceeds Expectation"
    elif marks>70:
        grades_dict[nameX]="Acceptable"
    if marks<70:
        grades_dict[nameX]="Fail"
print(grades_dict)

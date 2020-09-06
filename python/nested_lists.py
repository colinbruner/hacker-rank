if __name__ == "__main__":
    report = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())

        report[name] = score

    # Sort, uniq, and gather all grades from lowest -> highest
    all_grades = list(set(report.values()))
    all_grades.sort()
    second_lowest = all_grades[1]

    students = []
    for student, grade in report.items():
        if grade == second_lowest:
            students.append(student)

    students.sort()
    for student in students:
        print(student)

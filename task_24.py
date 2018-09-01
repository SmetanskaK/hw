def group_by_surname(list_of_enrolled):
    amount_of_students_a_i = 0
    amount_of_students_j_p = 0
    amount_of_students_q_t = 0
    amount_of_students_u_z = 0
    for student in list_of_enrolled:
        name_and_surname = student.split(" ")
        first_letter = str(name_and_surname[1])[0]
        number_of_letter = ord(first_letter)
        if ord("A") <= number_of_letter <= ord("I"):
            amount_of_students_a_i += 1
        elif ord("J") <= number_of_letter <= ord("P"):
            amount_of_students_j_p += 1
        elif ord("Q") <= number_of_letter <= ord("T"):
            amount_of_students_q_t += 1
        else:
            amount_of_students_u_z += 1
    return amount_of_students_a_i, amount_of_students_j_p, \
           amount_of_students_q_t, amount_of_students_u_z


print(group_by_surname(["Mark Zuckerberg", "Elon Musk", "Gregory House"]))







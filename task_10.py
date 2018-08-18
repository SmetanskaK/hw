string = "Marcus Aurelius*121-04-26*180-03-17"
string_list = string.split("*")
birth_date = string_list[1]
death_date = string_list[2]
date_list = birth_date.split("-")
date_list_1 = death_date.split("-")
years_birth = int(date_list[0])
years_death = int(date_list_1[0])
period_of_life = years_death - years_birth
print("Marcus Aurelius,", period_of_life)

string ="Leo Tolstoy*1828-08-28*1910-11-20"
string_list = string.split("*")
birth_date = string_list[1]
death_date = string_list[2]
date_list = birth_date.split("-")
date_list_1 = death_date.split("-")
years_birth = int(date_list[0])
years_death = int(date_list_1[0])
period_of_life = years_death - years_birth
print("Leo Tolstoy,", period_of_life)
#Assignment for post class
# Learning outcome: [variables, print, different data types]
# ask and store the following in variables:


# Store skills in a list
# Print each skill in a formated way.
# Definition of formated
# a little context text
# appropriate string formating like lower case or upper case, or other
# assignment to variable


# Name, last_name, age, age_of_mother, 3 skills
general_info_list ={
    'name' : input("Hello, what is your name: "),
    'last_name' : input("What is your surname? "),
    'age' : int(input("How old are you? ")),
    'age_of_mother' : int(input("How old is your mom? ")),
    #TODO define better skills name
    'skills' : ['Skill1', 'Skills2', 'Skill3']
}
# Print out the information in a formated manor
#print(general_info_list)

# Calculate age difference between response and mother
calc_age = general_info_list['age_of_mother'] - general_info_list['age']

print(f"Hello {general_info_list['name']} {general_info_list['last_name']}\n"
      f"You are {general_info_list['age']}\n"
      f"And you mother age is {general_info_list['age_of_mother']}\n"
      f"And you have {calc_age} years of difference")


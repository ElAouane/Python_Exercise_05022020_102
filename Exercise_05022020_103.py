####################################################
#TASK: # define an empty dictionary# name_dict = {}#
#It should have: Hero, Beginning, middle, end and  #
#2 other things                                    #
####################################################
user_story = {
    'name' : '',
    'Surname' : '',
    'hero' : '',
    'beginning' : '',
    'middle': '',
    'end' : '',
}

########################################################
#TASK: Prompt user for input for a story               #
#User_story = User input                               #
#Beginning,middle, end variable container for use input#
########################################################
# Prompt user for input for a story.
user_story['hero'] = {'Name': input("What is your name"), 'Surname': input(f"May I ask your Surname?")}

beginning = input(f"Hello,{user_story['hero']['Name']} {user_story['hero']['Surname']}  what is your story? ")
user_story['name'] = user_story['hero']['Name']
user_story['Surname'] = user_story['hero']['Surname']
user_story['beginning'] = beginning

middle = input("What is you middle story? ")
user_story['middle'] = middle

end = input("the end: ")
user_story['end'] = end



########################################################
#TASK: Print the user input respons                    #
########################################################
print(f"This is the {user_story['beginning']} and {user_story['middle']} and the {user_story['end']} and the hero is {user_story['hero']['Name']} {user_story['hero']['Surname']}")

########################################################
#TASK: Check dictionary key and values                 #
########################################################
print(user_story)
dob_dict = {'Nisha': '01/22/1984', 'Mack': '04/29/1987', 'Rimmi': '01/21/1987', 'Pooja': '06/27/1990'}


def get_dob(dob_dict):
    print ("Welcome to the birhthday dictionary! We know the birhthdays of: ")
    for key in dob_dict.keys():
        print(key)
    print("Who's birthday do you want to look up?")
    birthday_person = raw_input()
    print("%s's birthday is: %s " % (birthday_person, dob_dict.get(birthday_person, '0/0/1900')))

get_dob(dob_dict)           
# function = a block of code, which is executed when its called

print("\n== Function Menu ==")

def name():
    name = input("What is your preferred name: ")
    if name[0].islower():
        name = name.capitalize()
    return name

def age():
    age = input("How old are you: ")
    return age

def language():
    lang = input("What is your first language: ")
    if lang[0].islower():
        lang = lang.capitalize()
    return lang

def hobby():
    hob = input("What is your favorite hobby: ")
    if hob[0].islower():
        hob = hob.capitalize()
    return hob

def dream():
    drm = input("What is your dream job: ")
    if drm[0].islower():
        drm = drm.capitalize()
    return drm

def all_function(the_name, the_age, the_lang, the_hob, the_drm):
    print("\n == About Me == \n\nMy name is " + the_name + " and I am " + the_age + " years old.\n"
        "The first language I speak is " + the_lang + ".\nMy favorite hobby is " + the_hob + ".\nMy dream job is to be a " + the_drm + '!'
          + "\n\n ============= ")


print("1. Name function")
print("2. Age function")
print("3. Language function")
print("4. Hobby function")
print("5. Dream function")
print("6. About Me")
print("E. Exit")
choice = input("choice: ")

the_name = ""
the_age = ""
the_lang = ""
the_hob = ""
the_drm = ""

while choice != 'e' and choice != 'E':
    if choice == '1':
        print("\nName function")
        the_name = name()
        print("\nHey " + the_name + '!')
    elif choice == '2':
        print("\nAge function")
        the_age = age()
        print("\nYou are " + the_age + " years old")
    elif choice == '3':
        print("\nLanguage function")
        the_lang = language()
        print("\nYour first language is " + the_lang + '!')
    elif choice == '4':
        print("\nHobby function")
        the_hob = hobby()
        print("\nYour favorite hobby is " + the_hob + '!')
    elif choice == '5':
        print("\nDream function")
        the_drm = dream()
        print("\nYour dream job is " + the_drm + '!')
    elif choice == '6':
        print("\nAll function")

        if len(the_name) == 0 or len(the_age) == 0 or len(the_lang) == 0 or len(the_hob) == 0 or len(the_drm) == 0:
            print("Incomplete data")
        else:
          all_function(the_name, the_age, the_lang, the_hob, the_drm)
    else:
        print("\n[Invalid choice]")

    print("\n1. Name function")
    print("2. Age function")
    print("3. Language function")
    print("4. Hobby function")
    print("5. Dream function")
    print("6. About Me")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'E' or choice == 'e':
    print("\n== Exit Program ==")

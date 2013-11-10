import shelve, calling_db

def main():
    
    stack = calling_db.main()
    
    options = ("name", "hometown", "location")
    
    print "Please enter the type of search you would like to perform:\n"
    for choice in options:
        print choice
    
    print "\n"
    
    user_input = raw_input()
    
    while True:
        
        if user_input.lower() == options[0]:
            people = search_name(stack)
            break
            
        elif user_input.lower() == options[1]:
            people = search_hometown(stack)
            break
            
        elif user_input.lower()== options[2]:
            people = search_location(stack)
            break
            
        else:
            print "That is not one of the options"
            for choice in options:
                print choice
            print "\n"
            user_input = raw_input("try again: ")
            
    if len(people) != 0:
        print "Do you want to update a profile?"
        update_option = raw_input("y/n")
        
        while update_option == "Y" or update_option == "y":
            update(people)
            print "Do you want to update a profile?"
            update_option = raw_input("y/n:\t")
    
    run_again()
            

            
def run_again():
    """
    run program again option
    """
    print "\nIf you do not want to run this program again, push enter."
    user_input = raw_input()
    
    if user_input != "":
        main()
            
    
def update(stack):
    """
    update db info
    """
    for index, friend in enumerate(stack):
        print index, friend, "\n"
        
    print "\n"
    person_index = raw_input("Enter the index of the person that you would like to update: ")
    print "\n"
    
    try:
        person_index = int(person_index)
    except:
        pass
    
    print "\n"
    
    try:
        stack[person_index].update()
        
    except:
        print "That index does not exist..."
    
def search_name(stack):
    """
    Searches for the person in db by name
    """
    
    found_people = []
    
    print "\nWho are you looking for?"
    looking_for = raw_input("Please enter their name here: ")
    
    results = []
    
    for people in stack:
        if people.name.lower().find(looking_for) != -1:
            results.append(people)
            
    if len(results) == 0:
        print "That person is not in my database. Sorry."
        
    else:
        print "People Found:\n\n"
        for index, friend in enumerate(results, 0):
            print index,":\n", friend, "\n\n"
            found_people.append(friend)
        
    return found_people

def search_location(stack):
    """
    Searches for the person in db by location
    """
    found_people = []
    
    print "\nWhat location do you want to search for?"
    looking_for = raw_input("Please enter the location here: ")
    
    results = []
    
    for people in stack:
        if people.location.lower().find(looking_for) != -1:
            results.append(people)
            
    if len(results) == 0:
        print "That location is not in my database. Sorry."
        
    else:
        print "People Found:\n\n"
        for index, friend in enumerate(results, 0):
            print index,":\n", friend, "\n\n"
            found_people.append(friend)
        
    return found_people

def search_hometown(stack):
    """
    Searches for the person in db by hometown
    """
    found_people = []
    
    print "\nWhat hometown are you looking for?"
    looking_for = raw_input("Please enter the location here: ")
    
    results = []
    
    for people in stack:
        if people.hometown.lower().find(looking_for) != -1:
            results.append(people)
            
    if len(results) == 0:
        print "That hometown is not in my database. Sorry."
        
    else:
        print "People Found:\n\n"
        for index, friend in enumerate(results, 0):
            print index,":\n", friend, "\n\n"
            found_people.append(friend)
        
    return found_people

def print_all(stack):
    """
    print db to screen
    """
    
    for index, friend in enumerate(stack, 0):
        print index, friend, "\n"
        
    return stack
    
if __name__ == "__main__":
    main()
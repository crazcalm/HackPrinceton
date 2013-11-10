import facebook, shelve
from friend_class import Friend

token = "CAACEdEose0cBAPhCZBYZBIpTikAWfw1tlRaLoEwAigD2XicyHT84Tj9NxNYmC7qN1DgYnJOW2G2AtsdY95qs8veQD3FpbZC1WHdJ8KbHfb0rIY5fyqQASeY87SJ3ZAijOfBBRLzZCSIyXKo4SLmKsIZA4EB9WuleJYAJxaD73LeNMwUz53bwWD5ZAvZCkwy5AVoZD"
token = "CAACEdEose0cBAMQtqgr5mqiM48WAo5WNc2J1lFcG5EDuKKOoWmkXtOFqhTZCXR7PPCAeNRwn4EZAx42Gk4vZAphXVvJ5KVjZBfoSXJKA9CPwKNSYjbBZAgVH5jSFEfdJvEqne0l4YU2IQ0UpLGT8CIZCfazc6x0UIjfns90ifSLsGthZBjPq5Tc2ZAr26DwWmZBwZD"
token = "CAACEdEose0cBAHZAft3D7NPwB0ZCtGzg1zve0dlhjn60VyaZBIrUNEdAnDcZBpFSirNq0bSYi2JlDn3Ho8YvhCe99jO5rZBi9vwXNxgYtXKkQnufrpzBOvdXN7nW62wo1YT9cNe5JHRFqe42mqrf9IOzPGOdbkn7wK3963B36G1lDTjl89wwwK6xJHwX6bQIZD"

print "Here we go again!"

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")


original_info = friends["data"]

keys = ("name", "id", "birthday", "hometown", "location")

def main():
    
    info = friends_info(original_info)
    
    for data in info:
        individual_info(data, keys)

def friend_class_object(friend_dict):
    """
    Will make a friend clas object from the friend_dict info
    """
    name = friend_dict["name"]
    id = friend_dict["id"]
    
    try:
        birthday = friend_dict["birthday"]
    except:
        birthday = "unkown"
    
    try:
        hometown = friend_dict["hometown"]["name"]
    except:
        hometown = "unknown"
    
    try:
        location = friend_dict["location"]["name"]
    except:
        location = "unknown"

    name = Friend(name, id, birthday, hometown, location)
    
    create_db(name)
    
def create_db(friend_object):
    """
    This is my database on my friends
    """
    
    db = shelve.open("friend_db")
    
    
    print "db: %s --> %s\n\n" %(friend_object.name, friend_object)
    db[str(friend_object.name)] = friend_object
    
    db.close()


def individual_info(data, keys):
    """
    Will parse the data and take only the info that I want.
    """
    dict_info = {}
    
    for key in data:
        
        for word in keys:
            if key == word:
                dict_info[key] = data[key]
    
    #print dict_info
    friend_object  = friend_class_object(dict_info)
    
    
    
def friends_info(data):
    """
    Gets my friends information
    """
    # All friends data will be placed in 
    stack = []
    count = 0
    for people in data:
        try:
            stack.append(graph.get_object(people["id"]))
        except:
            count +=1
            print "Didn't work for %s people... \n id: %s" %(count, people["id"])
    
    return stack

if __name__ == "__main__":
    main()
        
        
        
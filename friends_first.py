import facebook

loved_ones =[]

token = "CAACEdEose0cBAPhCZBYZBIpTikAWfw1tlRaLoEwAigD2XicyHT84Tj9NxNYmC7qN1DgYnJOW2G2AtsdY95qs8veQD3FpbZC1WHdJ8KbHfb0rIY5fyqQASeY87SJ3ZAijOfBBRLzZCSIyXKo4SLmKsIZA4EB9WuleJYAJxaD73LeNMwUz53bwWD5ZAvZCkwy5AVoZD"
token = "CAACEdEose0cBAMQtqgr5mqiM48WAo5WNc2J1lFcG5EDuKKOoWmkXtOFqhTZCXR7PPCAeNRwn4EZAx42Gk4vZAphXVvJ5KVjZBfoSXJKA9CPwKNSYjbBZAgVH5jSFEfdJvEqne0l4YU2IQ0UpLGT8CIZCfazc6x0UIjfns90ifSLsGthZBjPq5Tc2ZAr26DwWmZBwZD"
print "Here we go again!"

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")
print type(friends)
print friends

data = friends["data"]

keys = ("name", "id", "birthday", "hometown", "location")
stack = []
for people in data[:10]:
    loved_ones.append(graph.get_object(people["id"]))
    


for testing in loved_ones:
    
    
    
    for key in testing:
        print key, testing[key]
        
        for word in keys:
            if word == key:
                print key, testing[key]
                friend_dict[key] = testing[key]
        
    stack.append(friend_dict)
    
print "\n\n"

for x in stack:
    print stack, "\n"

    



"""
for key in friends:
    print key, "\n"
    
    for keys in key:
        print friends[key], "\n"

print "me: \n", profile
mig = graph.get_object("8850935")
print "\nmig:\n", mig
"""
"""
A class to hold my friends facebook information
"""
import shelve


class Friend:
    
    def __init__(self, name, id, birthday = "unknown", hometown = "unknown", location = "unknown"):
        
        self.name = name
        self.id = id
        self.hometown = hometown
        self.location = location
        self.birthday = birthday
        
    def __repr__(self):
        
        return "name: %s\nid: %s\nbirthday: %sn\nhometown: %s\nlocation: %s" % (self.name, self.id,self.birthday, self.hometown, self.location)
    
    def update(self):
        print self, "\n\n"
        change = raw_input("What would you like to update?: ")
        
        options = ("name", "id", "birthday", "hometown", "location")
        
        if change.lower() == options[0]:
            self.name = raw_input("Enter new value: ")
            print "\n"
            print self
        
        elif change.lower() == options[1]:
            self.id = raw_input("Enter new value: ")
            print "\n"
            print self
            
        elif change.lower() == options[2]:
            self.birthday = raw_input("Enter new value: ")
            print "\n"
            print self
            
        elif change.lower() == options[3]:
            self.hometown = raw_input("Enter new value: ")
            print "\n"
            print self
            
        elif change.lower() == options[4]:
            self.location = raw_input("Enter new value: ")
            print "\n"
            print self
            
        else:
            print "\n"
            print "That input is not an option"
        
        print "\n"
        self.save()
            
    def save(self):
        """
        Re-saves class object in DB
        """
        db = shelve.open("friend_db")
        db[self.name] = self
        db.close()
        
        
        
                 
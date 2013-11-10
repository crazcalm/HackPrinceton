import shelve

def main():
    """
    open the database
    """
    db = shelve.open("friend_db")
    
    stack = []
    
    for key in db:
        stack.append(db[key])
        #print db[key], "\n"
        
    db.close()
    
    return stack
    
if __name__ == "__main__":
    main()
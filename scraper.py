import urllib, calling_db, email
from bs4 import BeautifulSoup

url = "http://www.theguardian.com/world/natural-disasters?page="

def main():
    """
    Controls the flow
    """
    stack = []
    
    # Checking the first ten pages of that website
    for page in range(11):
        soup = create_soup(page = page)
        sentences = scrape(soup)
        
        
        stack += db(sentences, page)
        
    possible_danger(stack)

def possible_danger(stack):
    """
    Format one big massive email
    """
    body = ""
    
    for item in stack:
        body+= "%s\n%s\n%s\n%s%s\n\n" %(item[0], item[1], item[2], url, item[3])
        
    print body
    body = body.replace("\n","<br/>" )
    email.main(body)
    

def comparison1(friend, string):
    """
    checks to see if friend's hometown
    is in news article summary text
    """
    if string.lower().find(friend.hometown.lower()) != -1:
        #print "friend is in trouble!\n"
        #print "hometown",friend.hometown, "\n","string: ", string, "\n"
        return True
                
    else:
        #print "hometown: %s, string: %s\n" %(friend.hometown, string)
        return False
                
def comparison2(friend, string):
    """
    checks to see if friend's location
    is in news article summary text
    """
    if string.lower().find(friend.location.lower()) != -1:
        #print "friend is in trouble!\n",
        #print "location", friend.location, "string: ", string
        return True
                
    else:
        #print "location: %s, sting: %s\n" %(friend.location, string)
        False


def db(sentences, page = 0):
    
    friends = calling_db.main()
    
    stack = []
    
    for friend in friends:
        for string in sentences:
            
            if friend.hometown.lower() != "unknown":
                hometown_unsafe = comparison1(friend, string)
                
                if hometown_unsafe:
                    stack.append([friend.name, friend.hometown, string, page])
            
            elif friend.location.lower()!= "unknown":
                location_unsafe = comparison2(friend, string)
                
                if location_unsafe:
                    stack.append([friend.name, friend.location, string, page])
                    
    return stack
            

                
    
def scrape(soup):
    """
    Scrapes for the html text
    """
    #print soup, "\n\n"
    
    html = soup.find_all("div", {"class": "trailtext"})
    
    stack = []
    
    for stuff in html:
        #print stuff
        p_tag = stuff.find_all("p")
        for text in p_tag:
            for strings in text.strings:
                #print strings
                stack.append(strings)
    return stack
        #for info in stuff.strings:
        #   print info, "\n"
    

    
def create_soup(url = "http://www.theguardian.com/world/natural-disasters?page=", page = 1):
    """
    Goes to a web page and makes it into BeautifulSoup soup
    """
    url += "%s" %(page)
    
    html = urllib.urlopen(url)
    content = html.read()
    soup = BeautifulSoup(content)
    
    #print soup.prettify()
    return soup

if __name__ == "__main__":
    main()
#Syntax
def name_of_function(): # signature
    words = 'function body' # body
    print(words) # body
    return words
print(name_of_function())    

######
ice_cream_flavours = ["Vanilla", "Strawberry", "Mocha"]
def cream_flavours():
    for flavours in ice_cream_flavours:
        print("We eat "+flavours+ " flavour")
        
cream_flavours()

def meet(traveller):
    welcome_message = "Hi " + traveller.title() + ", I'm so glad we'll be going on the trip together!"
    return welcome_message
print(meet('sally'))
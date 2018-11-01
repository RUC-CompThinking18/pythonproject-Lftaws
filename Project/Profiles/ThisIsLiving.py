#The start of the program
from Profiles import Profiles
PProfile = open(Profiles)
#A definition made for the player either creating a profile, or selecting one from the Profiles folder
def ProfileSelect():
    #This class holds the name of the profile, the data that is stored in their playthrough, and location on the map
    class PProfile (str.player, Data, Location)
    if Profiles == 0:
        #Asks for the players name, then saves it to the profiles folder ONLY if there are no profiles detected in the folder.
        str.player = raw_input("What is your name?")
        Output(player) to Profiles
    #Else statement made to have the player pick a profile with raw_input
    else:
        print "Select your profile."
        print PProfiles
        player = raw_input(Profiles)
        #Checks to see if the type between the input and available profiles is valid or not.
        while str.player != Profiles:
            print "That is not a valid profile"
    print "Welcome "+ Player

#This next section of code will dictate what will happen to the game. Either making a new one, continuing, or deleting the save
print """What would you like to do? Start  NEW GAME, CONTINUE, DELETE SAVE? Please type your answer"""
raw_input(GameState)
#The while loop checks to see if the user input matches the available commands.
    while GameState != "New Game" or "Continue" or "Delete Save":
        print "That is not a valid command"

#This if statement happens when the player selects Delete Save, it will, as stated, delete your save
    if GameState == "Delete Save":
        print "Are you sure you want to DELETE your save"

#Raw input is needed in order to delete the player, it imports profiles in case it does not have the information, then can delete the players
#profile, and then update the profiles folder
        if raw_input(GameState) == "Yes":
            import Profiles(player)
            remove(player)
            print "Player has been lost"
            output (profiles)
            return
        #Loops back to player input for GameState
        else:
            print """That is not a valid command please select either NEW GAME, CONTINUE, or DELETE SAVE"""
            raw_input(GameState)




#class Stats[Health,Hunger,Thirst,Rest,Wellness]

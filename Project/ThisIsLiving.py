#The start of the program
from Profiles import profile
Profile == open(Profiles)
#A definition made for the player either creating a profile, or selecting one from the Profiles folder
def ProfileSelect():
    #This class holds the name of the profile/PLAYER, the DATA that is stored in their playthrough, and LOCATION on the map
    #The if statement is to check to see if there are any other save files within the folder. If not, it makes the user create one
    class Profile (player, Data, Location):

        #Self commented notes: tests to see code working. Please Ignore
        #str.player = ""
        #Profiles = 0
        #End of self note block

        if Profiles == 0:
            #Asks for the players name, then saves it to the profiles folder ONLY if there are no profiles detected in the folder.
            #(Self Note) change str.player to player.name for all instances
            player.name = input("What is your name?")
            player.name = Profile
        #Else statement made to have the player pick a profile with raw_input
        else:
            print "Select your profile."
            print Profiles
            player.name == raw_input()
            #Checks to see if the type between the input and available profiles is valid or not.
            while player.name != Profiles:
                print "That is not a valid profile"
        print "Welcome "+ Player

#This next section of code will dictate what will happen to the game. Either making a new one, continuing, or deleting the save
GameState = raw_input("""What would you like to do? Start
NEW GAME, CONTINUE Game, DELETE SAVE?
Please type your answer""")
#The while loop checks to see if the user input matches the available commands.
    while GameState != "New Game" or != "Continue Game" or != "Delete Save":
        GameState = raw_input("""That is not a valid command!
        Please select either
        New Game, Continue, or Delete Save""")
#This if statement happens when the player selects Delete Save, it will, as stated, delete your save
    if GameState = "Delete Save":
        print "Are you sure you want to DELETE your save?""

#Raw input is needed in order to delete the player, it imports profiles in
#case it does not have the information, then can delete the players
#profile, and then update the profiles folder

        if GameState= "Yes" :
            import Profiles(player)
            remove(player)
            print "Player has been lost"
            output (profiles)
            return
        else:
            GameState = raw_input("Please select either New Game, Continue Game, or Delete Save")
        #Loops back to player input for GameState
        while GameState != "Yes" or != "No" :
            GameState = raw_input("""That is not a valid command
            please select either
            NEW GAME, CONTINUE, or DELETE SAVE""")
    #If statements to determine how the data, player stats, and location will be treated.
    #This if statement resets all data stored in the file.
    if GameState == "New Game":
        Stats=0
        Data=0
        Location=0
        return Game(Player)
    #This if statement simply calls the data without editing it.
    if GameState == "Continue Game":
        def Game(Stats,Data,Location)


ProfileSelect()

#Ignore this comment block, these are notes for myself.
#gender = rawinput("Are you a boy or a girl?: ")
#classes are defined as class variable()
#then those classes will have to be defined. self.a self.b self.c
#Ignore this. This block will be added later.
#class Stats[Health,Hunger,Thirst,Rest,Wellness]

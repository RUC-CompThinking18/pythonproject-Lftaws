def game():
    #stats imported for the player to be displayed
    #stats[Health,Wellness,Hunger,Thirst,Rest,Money]
    stats = []
    def before():
        #A check to see if the player is JUST starting their playthrough
        answer = raw_input (""" Welcome THIS IS LIVING? You will be playing as a homeless person, down on their luck in an unforgiving environment. You will have to manage your health, feed yourself, find water and shelter, and try to find money to get out of this situation. Things will be rough, difficult, and unfair. Life always is. On the streets of the city, anything goes, and anything can go wrong. You could even die. Please type I KNOW to begin. \n\n""")
        while answer != ("I KNOW"):
            answer = raw_input ("""I dont believe you understand the situation you currently find youself in. The city is full of hazards, and you must survive, and earn enough money to find a way out of this hell. You risk life and limb living like this, and theres only one way out. Type I KNOW when you are about to begin.\n\n""")

        #Stats are set like this to start the game off with.

    before()
#actual start of the game
    #def gameplay():
        #while Health != 0:
        #Players inventory, items can be added or subtracted here.
        #Inventories will be sorted into what the player can do with them. Such as eat, drink, or use.
    Inventory = {
    "Hot Dog" : 1,
    "Water Bottle" : 1,
    #Pain Killers have no function as of yet
    "Pain Killers" : 1,
    #Sleeping bag has no function as of yet
    "Sleeping Bag" : 1
    }
    #Day and Time
    Time = 0
    # A function that holds how time is reset and what day it will be.
    def TimeDay():
        Day = ["Sunday","Monday","Tuesday","Wednsday","Thursday","Friday","Saturday"]
        Time = 6
        Day = [0]
        if Time > 24:
            Day = Day + 1
            Time = 1
    TimeDay()

    #Stats are being set values and declared as ints.
    Health = 75
    int(Health)
    Wellness = 75
    int(Wellness)
    Hunger = 50
    int(Hunger)
    Thirst = 50
    int(Thirst)
    Rest = 100
    int(Rest)
    Money = 2.5
    float(Money)


    #A while loop that causes the player to select what they want to do
    #While action is blank, this will loop. If health is above 0, this will constantly loop
    action = ""
    while action == "":

        #Setting in case they exceed 100%
        if Health > 100:
            Health = 100
        if Wellness > 100:
            Wellness = 100
        if Hunger > 100:
            Hunger = 100
        if Thirst > 100:
            Thirst = 100
        if Rest > 100:
            Rest = 100
        #or 0%
        if Health < 0:
            Health = 0
        if Wellness < 0:
            Wellness = 0
        if Hunger < 0:
            Hunger = 0
        if Thirst < 0:
            Thirst = 0
        if Rest < 0:
            Rest = 0

        #Block for harming the player for stat neglect.
        #Wellness Block
        if Wellness < 10:
            Health = Health - 10
            print ("\nYou feel like you are dying...\n")
        elif Wellness < 20:
            Health = Health - 8
            print ("\nYou are starting to feel absolutely terrible.\nPlease take care of yourself or you will die.\n")
        elif Wellness < 30:
            Health = Health - 4
            print ("\nYou are feeling very unwell.\nYou must take care of your needs.\n")
        elif Wellness < 40:
            Health = Health - 2
            print ("\nYou are starting to feel unwell\n")
        elif Wellness < 50:
            Health = Health - 1
            print ("\nYou're not feeling so good.\n")

        #Hunger Block
        if Hunger < 10:
            Wellness = Wellness - 5
            Health = Health - 3
            print ("\nYou are at risk of fading away.\n YOU MUST EAT.\n")
        elif Hunger < 20:
            Wellness = Wellness - 4
            Health = Health - 2
            print ("\nYour body aches and you begin to feel weak.\nYou have to find food.\n")
        elif Hunger < 30:
            Wellness = Wellness - 3
            Health = Health - 1
            print ("\nYour stomach growls in dire need of food.\n")
        elif Hunger < 40:
            Wellness = Wellness - 2
            print ("\nYou are feeling hungry.\n")
        elif Hunger < 50:
            Wellness = Wellness - 1
            print ("\nYou are feeling a bit peckish\n")

        #Thirst Block
        if Thirst < 10:
            Wellness = Wellness - 5
            Health = Health - 3
            print ("\nYour throat and body begin to shut down.\nYou NEED a drink\n")
        elif Thirst < 20:
            Wellness = Wellness - 4
            Health -2
            print ("\nYou are dying of dehydration\n")
        elif Thirst < 30:
            Wellness = Wellness - 3
            Health = Health - 1
            print ("You really should get something to drink\n")
        elif Thirst < 40:
            Wellness = Wellness - 2
            print ("\nYou are thirsty.\n")
        elif Thirst < 50:
            Wellness = Wellness - 1
            print ("\nYou feel a bit parched.\n")

        #Rest Block
        if Rest == 0:
            Wellness = Wellness - 5
            print ("\nYou are on the brink of collapse.\n")
        elif Rest < 10:
            Wellness = Wellness - 4
            print ("\nYou struggle to stay awake.\n")
        elif Rest < 20:
            Wellness = Wellness - 3
            print ("\nYou feel exhausted.\n")
        elif Rest < 30:
            Wellness = Wellness - 2
            print ("\nYou should probably get some sleep.\n")
        elif Rest < 40:
            Wellness = Wellness - 1
            print ("\nYou feel a bit tired.\n")
        if Health == 0:
            return "You have died"

        #A display to show players stats and time
        print ("")
        print (int(Health), str(" Health"))
        print (int(Wellness), str(" Wellness"))
        print (int(Hunger), str(" Hunger"))
        print (int(Thirst), str(" Thirst"))
        print (int(Rest), str(" Rest"))
        print (str("$"), int(Money))
        print ("It is " , int(Time) , "o'clock")
        print ("")

        #Asking player for input.

        action = raw_input("""What would you like to do? Beg , Shop , Sleep , Eat , Drink , Medicate\n\n""")

        #If action is to beg, will give money out and reduce stats.
        if action == "Beg" :
            Money = Money + .50
            Time = Time + 1
            Hunger = Hunger - 2
            Thirst = Thirst - 3
            Rest = Rest - 6
            #action = "" resets the loop and asks for prompt again
            action = ""

        #If player chooses to sleep, asks for how long. If its above 8, they get a full sleep.
        #Also reduces player stats based on how many hours they slept. They spend less energy, so lost stats are reduced.
        if action == "Sleep":
            HowMuchSleep = raw_input("""How many hours would you like to sleep for?\n\n""")
            HowMuchSleep = int(HowMuchSleep)
            if HowMuchSleep < 8:
                Rest = Rest + (HowMuchSleep * 10)
                Time = Time + HowMuchSleep
                Hunger = Hunger - (2 * HowMuchSleep)
                Thirst = Thirst - (3 * HowMuchSleep)
                action = ""
            #Checking to see if the player sleeps for 8 or more hours
            if HowMuchSleep >= 8:
                Rest = 100
                Time = Time + HowMuchSleep
                Hunger = Hunger - (2 * HowMuchSleep)
                Thirst = Thirst - (3 * HowMuchSleep)
                HowMuchSleep = 0
                action = ""
            else:
                print "That is not a valid input\n\n"
                action = ""


        #If player chose to eat, they will be prompted to eat what in their inventory
        #This will be based on a list of items that can be edible.
        if action  == "Eat":
            print Inventory
            print()
            print()
            EatWhat = raw_input("What would you like to eat?\n\n")

            #Test block to add hunger when eating a hot dog, and if incorrect prompt is given, brings player back.
            if EatWhat == "Hot Dog":
                Hunger = Hunger + 20
                print ("Delicious\n\n")
                action = ""
            else:
                Print ("You decided to eat nothing.\n\n")
                action = ""

        #Similar to eat block, but this is for drinking
        if action == "Drink":
            print Inventory
            print()
            print()
            DrinkWhat = raw_input("What would you like to drink?\n\n")
            if DrinkWhat == "Water Bottle":
                Thirst = Thirst + 20
                print ("That quenched your thirst.\n\n")
                action = ""
            #If wrong input is put in, the player will drink nothing
            else:
                print ("You decided to not drink anything\n\n")
                action = ""

        if action == "Medicate":
            print Inventory
            print()
            print()
            MedWhat = raw_input("What will you use?\n\n")
            if MedWhat == "Pain Killers":
                Health = Health + 15
                print ("The pain is going away.\n\n")
                action = ""

#gameplay()
game()

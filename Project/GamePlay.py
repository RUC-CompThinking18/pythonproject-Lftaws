import Profile

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
    #A while loop that causes the player to select what they want to do
    #While action is blank, this will loop. If health is above 0, this will constantly loop
    action = ""
    while action == "":
        #A display to show players stats and time
        print ("")
        print (int(Health), str(" Health"))
        print (int(Wellness), str(" Wellness"))
        print (int(Hunger), str(" Hunger"))
        print (int(Thirst), str(" Thirst"))
        print (int(Rest), str(" Rest"))
        print (str("$"), int(Money))
        print ("It is " ,int(Time), "o'clock")
        print ("")
        #Asking player for input.
        #As of Nov 15, there are no options for shopping or medicating, and answers need to be typed as shown
        action = raw_input("""What would you like to do? Beg , Shop , Sleep , Eat , Drink , Medicate\n\n""")
        #If action is to beg, will give money out and reduce stats.
        if action == "Beg" :
            Money = Money + .50
            Time = Time + 1
            Hunger = Hunger - 5
            Thirst = Thirst - 5
            Rest = Rest - 8
            #action = "" resets the loop and asks for prompt again
            action = ""
        #If player chooses to sleep, asks for how long. If its above 8, they get a full sleep.
        #Also reduces player stats based on how many hours they slept. They spend less energy, so lost stats are reduced.
        if action == "Sleep":
            #Sleeping is bugged due to an error with adding the two integers (Time) and (HowMuchSlept)
            HowMuchSleep = raw_input("""How many hours would you like to sleep for?\n\n""")
            Rest = HowMuchSleep * 10
            Time = Time + HowMuchSleep
            Hunger = Hunger - (3 * HowMuchSleep)
            Thirst = Thirst - (5 * HowMuchSleep)
            action = ""
            if HowMuchSleep >= 8:
                Rest = 100
                Time = int(Time) + int(HowMuchSleep)
                Hunger = Hunger - (3 * HowMuchSleep)
                Thirst = Thirst - (5 * HowMuchSleep)
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
        #Block for harming the player for stat neglect.
        # def harm():
         #    if Wellness < 50:
          #     Health = Health - 1
           # elif Wellness < 40:
            #    Health = Health - 2
            #elif Wellness < 30:
             #   Health = Health - 4
  #          elif Wellness < 20:
   #             Health = Health - 8
    #        elif Wellness < 10:
     #           Health = Health - 10
#
 #               if Hunger < 50:
  #                  Wellness = Wellness - 1
   #             elif Hunger < 40:
    #                Wellness = Wellness - 2
     #           elif Hunger < 30:
      #              Wellness = Wellness - 3
       #             Health = Health - 1
        #        elif Hunger < 20:
         #           Wellness = Wellness - 4
          #          Health = Health - 2
           #     elif Hunger < 10:
            #        Wellness = Wellness - 5
             #       Health = Health - 3
              #  harm()
#gameplay()
game()

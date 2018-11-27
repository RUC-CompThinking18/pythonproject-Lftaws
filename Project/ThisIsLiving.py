def game():
    raw_input ("You dont know how it suddenly snuck up on you.\nOne moment your work before being called to your managers office and suddenly been told you were being let go.\nThen when you get home, you found out your apartment was broken into and robbed in your absence.\nThey broke down your door, stole your possessions, and wrecked the place.\n...\nThey even took your rent money to... great.\nYour luck never changed from that moment, the downward spiral from what'd you call grace came as suddenly as being hit by a locomotive.\nBefore you knew it, you were out on the streets of the urban jungle, with only the clothes on your back.\n You only have a few dollars to your name, you'll have to find food and water to survive. How did your life ever come to this?\n\n\n\n ")

    #Lists for edible, drinkable, or medicatable items.
    Edible = ["Snack: 10 Hunger: $1", "Small Meal: 25 Hunger: $3", "Medium Meal: 40 Hunger: $5", "Large Meal: 80 Hunger: $9"]
    Drinkable = ["Small Water: 10 Thirst: $1", "Water Bottle: Thirst: 30 Thirst: $2", "Large Water Bottle: 40 Thirst: $3", "Tea: 20 Thirst & 10 Wellness: $3", "Coffee: 20 Thirst & 10 Rest: $4"]
    Medicateable = ["Bandage: 10 Health: $3", "Asprin: 15 Health: $4", "Caffeine Pills: 10 Health 30 Rest: $6" , "IV Fluid: 20 Health & 40 Thirst: $10", "First-Aid Kit: 50 Health & Wellness 20: $10"]
    #Day and Time
    Time = 0
    # A function that holds how time is reset and what day it will be.
    def TimeDay():
        Day = ["Sunday","Monday","Tuesday","Wednsday","Thursday","Friday","Saturday"]
        Time = 6
        Day = [0]
        if Time == 25:
            Day = Day + 1
            Time = Time - 24
            if Day == 7:
                Day = Day - 7
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
        if Health <= 0:
            action = "You have died."

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

        action = raw_input("""What would you like to do? Beg, Sleep , Eat , Drink , Medicate\n\n""")

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
            print Edible

            EatWhat = raw_input("What would you like to eat?\n\n")

            #A If block for selecting food items for the player to eat.
            #Snack Block
            if EatWhat == "Snack":
                if Money >= 1:
                    Hunger = Hunger + 10
                    print ("It sated your hunger for a little bit\n\n")
                    Money=Money - 1
                    action = ""
                else:
                    print("You didnt have enough money for a snack.")
                    EatWhat = raw_input("What would you like to eat?\n\n")
                    action = ""
            #Small Meal Block
            if EatWhat == "Small Meal":
                if Money >= 3:
                    Hunger = Hunger + 25
                    print ("You Feel a bit fuller.\n\n")
                    Money=Money - 3
                    action = ""
                else:
                    print("You didnt have enough money for a Small Meal.")
                    EatWhat = raw_input("What would you like to eat?\n\n")
                    action = ""
            #Medium Meal Block
            if EatWhat == "Medium Meal":
                if Money >= 5:
                    Hunger = Hunger + 40
                    print ("You have a nice meal, and dont feel as hungry.\n\n")
                    Money=Money - 5
                    action = ""
                else:
                    print("You didnt have enough money for a Medium Meal.")
                    EatWhat = raw_input("What would you like to eat?\n\n")
                    action = ""
            #Large Meal Block
            if EatWhat == "Large Meal":
                if Money >= 9:
                    Hunger = Hunger + 80
                    print ("You have a nice meal, and dont feel as hungry.\n\n")
                    Money=Money - 9
                    action = ""
                else:
                    print("You didnt have enough money for a Medium Meal.")
                    EatWhat = raw_input("What would you like to eat?\n\n")
                    action = ""


        #Similar to eat block, but this is for drinking
        if action == "Drink":
            print Drinkable
            DrinkWhat = raw_input("What would you like to drink?\n\n")

            if DrinkWhat == "Small Water":
                if Money >= 1:
                    Thirst = Thirst + 10
                    print ("You get a small drink\n\n")
                    Money=Money - 1
                    action = ""
                else:
                    print("You didnt have enough money for a Small Water.")
                    DrinkWhat = raw_input("What would you like to Drink?\n\n")
                    action = ""

            if DrinkWhat == "Water Bottle":
                if Money >= 2:
                    Thirst = Thirst + 30
                    print ("Your thirst is sated\n\n")
                    Money=Money - 2
                    action = ""
                else:
                    print("You didnt have enough money for a Water Bottle.")
                    DrinkWhat = raw_input("What would you like to Drink?\n\n")
                    action = ""

            if DrinkWhat == "Large Water Bottle":
                if Money >= 3:
                    Thirst = Thirst + 40
                    print ("You have a large drink\n\n")
                    Money=Money - 3
                    action = ""
                else:
                    print("You didnt have enough money for a Large Water Bottle.")
                    DrinkWhat = raw_input("What would you like to Drink?\n\n")
                    action = ""
            if DrinkWhat == "Tea":
                if Money >= 3:
                    Thirst = Thirst + 20
                    Wellness = Wellness +10
                    print ("You feel a bit better after drinking the Tea\n\n")
                    Money=Money - 3
                    action = ""
                else:
                    print("You didnt have enough money for Tea.")
                    DrinkWhat = raw_input("What would you like to Drink?\n\n")
                    action = ""
            if DrinkWhat == "Coffee":
                if Money >= 4:
                    Thirst = Thirst + 20
                    Rest = Rest + 10
                    print ("You feel a bit more energetic\n\n")
                    Money=Money - 4
                    action = ""
                else:
                    print("You didnt have enough money for Coffee.")
                    DrinkWhat = raw_input("What would you like to Drink?\n\n")
                    action = ""

        if action == "Medicate":
            print Medicateable

            MedWhat = raw_input("What will you use?\n\n")

            if MedWhat == "Bandage":
                if Money >= 3:
                    Health = Health + 10
                    print ("You patched up some old wounds.\n\n")
                    Money=Money - 3
                    DrinkWhat = ""
                    action = ""
                else:
                    print("You didnt have enough money for some Bandages.")
                    MedWhat = raw_input("What would you like to use?\n\n")
                    action = ""

            if MedWhat == "Asprin":
                if Money >= 4:
                    Health = Health + 15
                    print ("You take some asprin to make the pain go away.\n\n")
                    Money=Money - 4
                    action = ""
                else:
                    print("You didnt have enough money for Asprin.")
                    Medwhat = raw_input("What would you like to use?\n\n")
                    action = ""

            if MedWhat == "Caffeine Pills":
                if Money >= 6:
                    Health = Health + 10
                    Rest = Rest + 30
                    print ("You feel more energetic after ingesting the pills.\n\n")
                    Money=Money - 6
                    action = ""
                else:
                    print("You didnt have enough money for the Caffeine Pills.")
                    MedWhat = raw_input("What would you like to use?\n\n")
                    action = ""
#"First-Aid Kit: 50 Health & Wellness 20: $10"
            if MedWhat == "IV Fluid":
                if Money >= 10:
                    Health = Health + 20
                    Thirst = Thirst +40
                    print ("You get some fluid in your system.\n\n")
                    Money=Money - 10
                    action = ""
                else:
                    print("You didnt have enough money for the IV Fluid.")
                    MedWhat = raw_input("What would you like to use?\n\n")
                    action = ""

            if MedWhat == "First-Aid Kit":
                if Money >= 10:
                    Health = Health + 50
                    Wellness = Wellness + 20
                    print ("You use the First-Aid Kit, you feel good as new.\n\n")
                    Money=Money - 10
                    action = ""
                else:
                    print("You didnt have enough money for the First-Aid Kit.")
                    MedWhat = raw_input("What would you like to use?\n\n")
                    action = ""
        if action == "You have died.":
            print ("You look around you. During your final moments of life.\n\n Feeling the uncomfortable pavement you sit upon, which will now be your grave.\n\nCrowds of people, walking in front of you.\nGoing about their days.\nNot one pays attention to you even though you cry, plea, for mercy from the uncaring masses.\n Your vision fades as the elements claim you,\n The masses do not care for you any longer.\nThey dont see you as human.\nEven those who look at you advert their gaze, pretending not to see you.\n You slump over to the pavement, nothing can save you now.\nThe last thing you see is a small child, simply staring at you.\n The child recognizes your agony, but their parent quickly grabs their shoulder, and ushers the child to walk with them.\nDont talk to that person, the parent says.\nThey are like that for a reason, plus, you dont want to give money to some junkie, right honey?")
#gameplay()
game()

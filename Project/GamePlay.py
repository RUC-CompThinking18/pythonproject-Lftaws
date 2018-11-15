import Profile

def game():
    #stats imported for the player to be displayed
    stats[Health,Wellness,Hunger,Thirst,Rest,Money]
    def before():
        #A check to see if the player is JUST starting their playthrough
         if Health and Wellness and Hunger and Thirst and Rest == 0:
             answer = raw_input ("""Welcome THIS IS LIVING? You will be playing as a homeless person, down on their luck in an unforgiving environment. You will have to manage your health, feed yourself, find water and shelter, and try to find money to get out of this situation. Things will be rough, difficult, and unfair. Life always is. On the streets of the city, anything goes, and anything can go wrong. You could even die. Please type I KNOW to begin. """)
        while answer != "I KNOW":
            answer = raw_input ("""I dont believe you understand the situation you currently find youself in. The city is full of hazards, and you must survive, and earn enough money to find a way out of this hell. You risk life and limb living like this, and theres only one way out. Type I KNOW when you are about to begin.""")

            #Stats are set like this to start the game off with.
            stats{
                "Health" = 75
                "Wellness" = 75
                "Hunger" = 50
                "Thirst" = 50
                "Rest" = 100
                "Money" = "$"2.50
#actual start of the game
    while Health != 0:
        def gameplay:

                #Players inventory, items can be added or subtracted here.
                Inventory {
                "Hot Dog" : 1,
                "Water Bottle" : 1,
                "Pain Killers" : 1,
                "Sleeping Bag" : 1
                }

                #Day and Time
                Day = "Sunday"
                Time = 12

                # A function that holds how time is reset and what day it will be.
                def TimeDay():
                    Day["Sunday","Monday","Tuesday","Wednsday","Thursday","Friday","Saturday"]
                    if Time >24:
                        Day = Day + 1
                        Time = 1

                if Health > 100:
                    Health == 100
                if Wellness > 100:
                    Wellness = 100
                if Hunger > 100:
                    Hunger = 100
                if Thirst > 100:
                    Thirst = 100
                if Rest > 100:
                    Rest = 100


                while action != "":
                 action = raw_input("""What would you like to do? Beg , Shop , Sleep , Eat , Drink , Medicate""")
                        if action == "Beg" :
                            Money = Money + .50
                            Time = Time + 1
                            Hunger = Hunger - 5
                            Thirst = Thirst - 5
                            Rest = Rest - 8
                            action = ""
                        if action == "Sleep":
                            HowMuchSleep = raw_input("""How many hours would you like to sleep for?""")
                            Rest = HowMuchSleep * 10
                            Time = Time + HowMuchSleep
                            Hunger = Hunger - (3 * HowMuchSleep)
                            Thirst = Thirst - (5 * HowMuchSleep)
                            action = ""
                            if HowMuchSleep >= 8:
                                Rest = 100
                                Time = Time + HowMuchSleep
                                Hunger = Hunger - (3 * HowMuchSleep)
                                Thirst = Thirst - (5 * HowMuchSleep)
                                action = ""
                        if action  == "Eat":
                            print Inventory
                            print
                            print
                            EatWhat = raw_input("What would you like to eat?")
                            if EatWhat == "Hot Dog":
                                Hunger = Hunger + 20
                                print "Delicious"
                                action = ""
                            else:
                                Print "You decided to eat nothing"
                                action = ""
                        if action == "Drink":
                            DrinkWhat = raw_input("What would you like to drink?")
                            if DrinkWhat == "Water Bottle":
                                Thirst = Thirst + 20
                                print "That quenched your thirst"
                                action = ""
                            else:
                                print "You decided to not drink anything"
                                action = ""

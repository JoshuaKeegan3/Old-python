"""
Things to copy:
New variables
Stuff commented #Ask Players name
Stuff above #Ask how many players
Studd commented #Tell player their cards
"""

#import random
import random
def main():
    #points system 
    NORMAL_POINTS = ['2', '3', '4', '5', '6', '7', '8', '9', '10' ]
    SPECIAL_POINTS = ["K", "Q", "J"]

    #reset variables
    repeat = True
    current_player = 1
    cards_drawn = 0
    previous_first_card = 0
    turns = 0
    points = 0
    player_points = []
    leader = ""
    leader_points = 0
    player_name = ""
    player_names = []

    #player cards
    player_cards = [""]

    #possible cards
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "K", "Q", "J"]
    suits = [" ", " ", " ", " "]

    #Current decks
    card_deck = []
    suit_deck =[]

    #positive replys
    positive_replys = ["yes", "yep", "yea", "yeah","y","hit me"]

    #Shuffle decks together
    for i in range(0,4):
        random.shuffle(cards)
        for i in range(0,13):
            card_deck.append(cards[i])
    for i in range (0, 13):
        random.shuffle(suits)
        for i in range(0,13):
            card_deck.append(cards[i])
    #ask the user how many players
    players = int(input("How many players do you want?"))
    for i in range(0,players):#ask players name
        player_name = input("What is the name of player {}?".format(i + 1))
        player_names.append(player_name.title())
    while turns <= players - 1:
        #give player cards
        previous_first_card = cards_drawn
        cards_drawn += 2
        player_cards = card_deck[previous_first_card : cards_drawn]
        while repeat == True:
            print("{} your cards are:".format(player_names[current_player - 1]))#tell the player their cards
            print(player_cards)
            for card in player_cards:
                if card in SPECIAL_POINTS:
                    points += 10
                elif card in NORMAL_POINTS:
                    points += NORMAL_POINTS.index(card)
                    points += 2
                else:
                    while True: #note aces will be calulated twice so the user my change their choice
                        ace = input("You have an Ace! Do you want the ace to be a one or an eleven?")
                        if ace == "1" or ace == "one":
                            points += 1
                            break
                        elif ace == "11" or ace == "eleven":
                            points += 11
                            break
                        else:
                            print("That is not an option, please try again.")
            if points < 21:
                another_card = input("Do you want another card?")
                another_card.lower()
                if another_card in positive_replys: 
                    player_cards.append(card_deck [cards_drawn])
                    cards_drawn += 1
                    points = 0 #reset points before calculating them again
                else:
                    print("Your final score was {}".format(points))
                    player_points.append(points)
                    break
            elif points == 21:
                print("BlackJack!")
                player_points.append(points)
                break
            else:
                print("Your bust")
                player_points.append(points)
                break
        if leader_points < points and points <= 21:
            leader_points = points
            leader = player_names[current_player - 1]
        
        current_player += 1        
        turns += 1
        points = 0
        repeat = True
    print("The winner is:" )
    print("Player {} with a total of {} points".format(leader, leader_points))

main()

"""
Theory doc for Black Jack none of this is proven to work
"""

#single player
if players = 1:
    #run normal script for one player
     print("Now it is the dealers turn")
    while points < leader_points:
    #calculate points
        if points < leader_points:
            player_cards.append (card_deck [cards_drawn])
                    cards_drawn += 1
                    points = 0 #reset points before calculating them again
        elif points >= leader_points:
            if points > 21:
                print("The Dealer is bust!")
                print("You win!")
            else:
                print("The Dealer scored {} with a hand of".format(points, player_cards))
                print("The Dealer has beaten you :(")

break
#ace input(#goes earlier)
if (points + ll) > leader score and (points + ll) <= 21:
    points += 11
else:
    points += 1
break


#shitty rounds function(#if two players have the same result it will pick the first of the two to win)
rounds = int(input("How many rounds would you like?"))
for rounds in (0, rounds):
    leader = ""
    #normal script
    round_winners.append(leader)
    print("the leader of the overall standings is:")
    for i in range (0, rounds):
        round_leader = round_winners.count(round_winners[i])#counts the number of times a each player wins
    max_wins = round_leader.max()#stores this in a variable
    position_of_round_leader = round_winners.index(max_wins)#finds the position of the person with the most wins in the list of winners
    round_leader = round_winners[position_of_round_leader]#uses this in information to find who the person with the most wins is.
    print("{},with {} wins".format(round_leader, max_wins))#prints the person with the most wins       
    
    

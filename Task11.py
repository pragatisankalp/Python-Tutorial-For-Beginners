                                                                               # Task 11
"""         For this exercies we have provided you with the list of lottery players and also with five
               random lottery numbers.Find out the players with most correct numbers and print out
               their winning and name.
               
               For genrating number we use
               
               import random
               lottery_number=set(random.sample(range(20),5))

               And the list of players  are:
               players= [
               {'name':'Riya', 'numbers':{1,3,5,7,9} },
               {'name':'Priti', 'numbers':{2,4,6,8,10} },
               {'name':'Rahul', 'numbers':{12,14,16,18,10} },
               {'name':'Aman', 'numbers':{13,15,17,18,19} }
               ]
               
               For this exercies assume their will be only 1 winner. Don't worry about two players
               matching the amount of numbers.
               Example:
               The winning are calculated with this formula:
               winning=1000 ** len(common_number)
               
"""
import random
lottery_number=set(random.sample(range(20),5))

players= [
               {'name':'Riya', 'numbers':{1,3,5,7,9} },
               {'name':'Priti', 'numbers':{2,4,6,8,10} },
               {'name':'Rahul', 'numbers':{12,14,16,18,10} },
               {'name':'Aman', 'numbers':{13,15,17,18,19} }
               ]
winning_player=players[0]
for player in players:
    common_number=len((player['numbers']).intersection(lottery_number))
    if common_number > len(winning_player['numbers'].intersection(lottery_number)):
        winning_player=player
winning=1000**len(winning_player['numbers'].intersection(lottery_number))
print(f"{winning_player['name']} won {winning}" )


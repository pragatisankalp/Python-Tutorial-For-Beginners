                                                                             #Task 5
"""
In this problem we have provided you set of lottery numbers:
lottery_numbers={34,46,9,67,12}
you must define a list of two players, each with a name and another set of numbers.
Players  in your list should be dictonaries following this format:
 {
'name': 'player name'
'numbers':{1,2,5,8,12}
 }
Then for each player print out a string that contains their name and how many numbers
they got right.
"""
lottery_numbers={34,46,9,67,12}
players=[
    {
'name': 'Rahul',
'numbers':{1,2,5,8,12}
 },
 {
'name': 'Riya',
'numbers':{1,34,5,8,12}
 }

    ]
name=players[0]['name']
common_num=len(players[0]['numbers'].intersection(lottery_numbers))
print(f"{name} got{common_num} right numbers")

name=players[1]['name']
common_num=len(players[1]['numbers'].intersection(lottery_numbers))
print(f"{name} got{common_num} right numbers")



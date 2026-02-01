# rating: 1200

input = list(map(int, input().split()))

rides = input[0]
ticket = input[1]
rideCost = input[2]
ticketCost = input[3]

ticketRatio = ticket / ticketCost
money = 0

while ticketCost < rides * rideCost and ticketRatio > 1 / rideCost and rides > 0:
    money += ticketCost
    rides -= ticket

if rides < 0:
    rides = 0

money += rides * rideCost

print(money)
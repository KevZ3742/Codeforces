# rating: 900

players = str(input())

dangerous = "NO"
counter = 1

for i in range(len(players)):
    player = players[i]
    
    if i == 0:
        continue
    elif player == players[i-1]:
        counter+=1
    else:
        counter = 1

    if counter == 7:
        dangerous = "YES"
        break

print(dangerous)
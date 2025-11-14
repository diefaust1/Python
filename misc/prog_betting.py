import sys

#progressive betting
bet = int(sys.argv[1])
total_amount = 0
times_gambled = int(sys.argv[2])
chance_to_fail = 50

total_amount = total_amount + bet

print("Current bet: " + str(bet))

for i in range(times_gambled):
    
    bet = bet * 2
    total_amount = total_amount + bet
    chance_to_fail = chance_to_fail / 2
    
    print("Current bet: " + str(bet))

print("Total amount: " + str(total_amount))
print("Times gambled: " + str(times_gambled+1))
print("Chance to fail: " + str(chance_to_fail) + " %")
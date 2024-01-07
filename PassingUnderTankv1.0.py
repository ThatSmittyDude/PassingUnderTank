#PassingUnderTankv1.0
#Author: Austin Smith  
#Unix timestamp: 1704593373
#Email: ThatSmittyDude@outlook.com
#GitHub.com/ThatSmittyDude
#puyinside.com

#Full tank data
fullLaps = float(input("laps on full tank: "))

#adjustment
adjLaps = float(input("desired fuel run in laps: "))

#adjusted tank data
adj = (adjLaps / fullLaps) * 100

#print results
print("recomended fuel percentage", adj)

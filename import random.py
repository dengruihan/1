import random

def simulate(n):
   playerA_wins = 0
   playerB_wins = 0
   for i in range(n):
       playerA_streak = 0
       playerB_streak = 0
       for j in range(3):
           playerA_result = random.choice(["正", "反"])
           playerB_result = random.choice(["正", "反"])
           if playerA_result == "正":
               playerA_streak += 1
           else:
               playerA_streak = 0
           if playerB_result == "正":
               playerB_streak += 1
           else:
               playerB_streak = 0
       if playerA_streak == 3:
           playerA_wins += 1
       elif playerB_streak == 3:
           playerB_wins += 1
   return playerA_wins, playerB_wins

n = 100000000
playerA_wins, playerB_wins = simulate(n)
print("玩家A获胜次数:", playerA_wins)
print("玩家B获胜次数:", playerB_wins)
if playerA_wins > playerB_wins:
   print("玩家A胜率更高")
else:
   print("玩家B胜率更高")
team_name = "Wildcats"

wins = 12
losses = 4

game_played = wins + losses

win_percentage = wins / game_played

if win_percentage > .70:
    print(team_name, "is likely to make the playoffs.")
else:
    print(team_name, "needs to win more games.")

print("Team:", team_name)

if wins > 10:
    print("Winning season!")

def winning_record(wins, losses):
    return wins > losses

result = winning_record(wins, losses)

print("Winning record?", result)


print("Games Played:", game_played)
print("Win Percentage:", win_percentage)
print("Win Percentage:", round(win_percentage * 100, 1), "%")

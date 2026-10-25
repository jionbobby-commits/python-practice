class Player:
    def __init__(self, name, goals, assists, rating):
        self.name = name
        self.goals = goals
        self.assists = assists
        self.rating = rating

    def __str__(self):
        return f"{self.name}：评分 {self.rating}"

    def __add__(self, other):
        return self.goals + other.goals


players = [
    Player("Bobby", 2, 1, 9.0),
    Player("Alex", 1, 2, 8.5),
    Player("Tom", 0, 1, 7.0)
]

print("=== 球员比赛评分 ===")

for player in players:
    print(player)

total_goals = 0
for player in players:
    total_goals += player.goals

print(f"\n球队总进球数：{total_goals}")

combined_goals = players[0] + players[1]
print(f"前两名球员的总进球数：{combined_goals}")

best_player = max(players, key=lambda p: p.rating)
print(f"本场最佳球员：{best_player.name}")
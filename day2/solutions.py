# %%
from zef.ops import *
from zef import *
# %%
with open('input.txt', 'r') as f:
    data = f.readlines()

# %% 
play_points_map = [
    ({"Rock"}, lambda _: 1),
    ({"Paper"}, lambda _: 2),
    ({"Scissors"}, lambda _: 3)
]

# Q1 Maps
win_rules = [
    # Ask about Z 
    (Z[0] == Z[1], lambda _ : 3), # Draw 
    ( 
        {
            ("Rock", "Paper"), 
            ("Paper","Scissors"), 
            ("Scissors", "Rock")
        }, lambda _ : 6), # Win 
    (Any, lambda _ : 0) # Lose
]

opponent_hand_map = [
    ({"A"}, lambda _: "Rock"),
    ({"B"}, lambda _: "Paper"),
    ({"C"}, lambda _: "Scissors")
]

my_hand_map = [
    ({"X"}, lambda _: "Rock"),
    ({"Y"}, lambda _: "Paper"),
    ({"Z"}, lambda _: "Scissors")
]

### Q2 Maps
my_strategy_map = [
    ({"X"}, lambda _: "Lose"),
    ({"Y"}, lambda _: "Draw"),
    ({"Z"}, lambda _: "Win")
]

win_strategy = [
    ({"Rock"}, lambda _: "Paper"),
    ({"Paper"}, lambda _: "Scissors"),
    ({"Scissors"}, lambda _: "Rock")
]

lose_strategy = [
    ({"Rock"}, lambda _: "Scissors"),
    ({"Paper"}, lambda _: "Rock"),
    ({"Scissors"}, lambda _: "Paper")
]

win_score_map = [
    ({"Win"}, lambda _: 6),
    ({"Lose"}, lambda _: 0),
    ({"Draw"}, lambda _: 3),
]
#%%
my_strategy = [
    (Z[1] == "Draw", lambda x : x[0]),
    (Z[1] == "Win", lambda x : x[0] | match[win_strategy] | collect ),
    (Z[1] == "Lose", lambda x : x[0] | match[lose_strategy] | collect )
]
#%%
verbose_data = (
    data 
    | map[trim['\n']] 
    | map[split[" "]] 
    | map[
            lambda x: (
                # is there ways to not use collect here
                x[0] | match[opponent_hand_map] | collect, 
                x[1] | match[my_hand_map] | collect
            )
        ]
    | collect
)

#%%
win_points = (
    verbose_data 
    | map[match[win_rules]]
    | sum
    | collect
)

play_points = (
    verbose_data
    | map[lambda x: x[1] | match[play_points_map] | collect ]
    | sum
    | collect
)

#%%
print(win_points + play_points)
#%%
verbose_data_q2 = (
    data 
    | map[trim['\n']] 
    | map[split[" "]] 
    | map[
            lambda x: (
                # is there ways to not use collect here
                x[0] | match[opponent_hand_map] | collect, 
                x[1] | match[my_strategy_map] | collect
            )
        ]
    | collect
)
#%%
win_points_q2 = (
    verbose_data_q2 
    | map[lambda x: x[1] | match[win_score_map] | collect ]
    | sum
    | collect
)

play_points_q2 = (
    verbose_data_q2 
    | map[match[my_strategy]]
    | map[match[play_points_map]]
    | sum
    | collect
)

print(win_points_q2 + play_points_q2)
# %%

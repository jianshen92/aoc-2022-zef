# %%
from zef.ops import *
from zef import *
# %%
with open('input.txt', 'r') as f:
    data = f.readlines()

# %%
play_points = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
} 

win_points = {
    ("A", "X") : 3,
    ("B", "Y") : 3,
    ("C", "Z") : 3,
    ("A", "Y") : 6,
    ("B", "Z") : 6,
    ("C", "X") : 6,
    ("A", "Z") : 0,
    ("B", "X") : 0,
    ("C", "Y") : 0,
}
# %%
cleaned = data | map[trim['\n']] | map[split[" "]] | collect
# %%
play = (
    cleaned 
    | map[Tuple]
    | map[lambda x:win_points[x]]
    | sum
    | collect 
)

# %%
win = (
    cleaned
    | map[lambda x: play_points[x[1]]]
    | sum
    | collect
)

print(play + win)
# %%

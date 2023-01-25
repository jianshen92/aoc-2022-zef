# %%
from zef.ops import *
# %%
with open('input.txt', 'r') as f:
    data = f.readlines()
# %%
q1_ans = (
    data 
    | map[trim['\n']] 
    ### Not sure if this part can be done better
    | map[lambda x:int(x) if x != '' else x] 
    | group[lambda x: x!='']
    | filter[lambda x: x[0] != '']
    ###
    | map[sum]
    | max
    | collect 
)
# %%
q2_ans = (
    data 
    | map[trim['\n']] 
    ### Not sure if this part can be done better
    | map[lambda x:int(x) if x != '' else x] 
    | group[lambda x: x!='']
    | filter[lambda x: x[0] != '']
    ###
    | map[sum]
    | sort
    | slice[-3,-1]
    | sum
    | collect 
)
# %%
print(q1_ans)
print(q2_ans)
# %%

import pandas as pd

def act_dir_coop_atleast_3times(actor_director: pd.DataFrame) -> pd.DataFrame:
    # Count occurrences of each (actor_id, director_id) pair
    pair_count = actor_director.groupby(["actor_id", "director_id"]).size().reset_index(name="count")
    
    # Filter where count >= 3
    result = pair_count[pair_count["count"] >= 3][["actor_id", "director_id"]]
    
    return result

# Input data
actor_director = pd.DataFrame({
    "actor_id":    [1, 1, 1, 1, 1, 2, 2],
    "director_id": [1, 1, 1, 2, 2, 1, 1],
    "timestamp":   [0, 1, 2, 3, 4, 5, 6]
})

print(act_dir_coop_atleast_3times(actor_director))
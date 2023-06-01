# hmexpcomp

Harmonie experiments comparison tool



## Usage
```python

path_exps_root = Path("/home/dum/hm_home")
paths_selected_exps = sorted(list(path_exps_root.glob("CY46_EXP*")))


dfs = compare_harmonie_experiments(paths_selected_experiments)

df = dfs["ecf/config_exp.h"]

is_same = df.eq(df.iloc[:, 0], axis=0).all(1)
df_diff = df[~is_same]
df_same = df[is_same]
df_diff
```

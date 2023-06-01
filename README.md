# hmexpcomp

Harmonie experiments comparison tool



## Usage
```python
from pathlib import Path
import hmexpcomp

path_exps_root = Path("/home/dum/hm_home")
paths_selected_exps = sorted(list(path_exps_root.glob("CY46_EXP*")))


dfs = hmexpcomp.compare_harmonie_experiments(paths_selected_exps)

df = dfs["ecf/config_exp.h"]

is_same = df.eq(df.iloc[:, 0], axis=0).all(1)
df_diff = df[~is_same]
df_same = df[is_same]
df_diff

                                        CY46_EXP0_DEFAERO  ...                          CY46_EXP2_DEFAERO
CAERO                                            tegenaod  ...                                   tegenaod
OBDIR                    /ec/res4/scratch/dum/OBS_Aut2019  ...           /ec/res4/scratch/dum/OBS_Aut2019
USEAERO                                          climaero  ...                                   climaero
BDDIR           /ec/res4/scratch/dum/BDY_Aut2019/archive/  ...  /ec/res4/scratch/dum/BDY_Aut2019/archive/
CREATE_CLIMATE                      ${CREATE_CLIMATE-yes}  ...                      ${CREATE_CLIMATE-yes}
CLIMDIR                          $HM_DATA/climate/$DOMAIN  ...                   $HM_DATA/climate/$DOMAIN
BUILD                                        ${BUILD-yes}  ...                               ${BUILD-yes}

[7 rows x 33 columns]
```

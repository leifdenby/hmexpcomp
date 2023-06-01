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
df_diff.transpose()

                                               BUILD   USEAERO  ...                                              OBDIR                                              BDDIR
CY46_EXP0_DEFAERO                       ${BUILD-yes}  climaero  ...                   /ec/res4/scratch/dum/OBS_Aut2019          /ec/res4/scratch/dum/BDY_Aut2019/archive/
CY46_EXP0_DEFAERO_AUTUMN_ICET                     mo  climaero  ...                   /ec/res4/scratch/dum/OBS_Aut2019          /ec/res4/scratch/dum/BDY_Aut2019/archive/
CY46_EXP0_DEFAERO_AprFog                          no  climaero  ...                  /ec/res4/scratch/dum/OBDIR_WINTER                 /ec/res4/scratch/dum/BDDIR_WINTER/
CY46_EXP0_DEFAERO_FebFog                          no  climaero  ...                  /ec/res4/scratch/dum/OBDIR_WINTER                 /ec/res4/scratch/dum/BDDIR_WINTER/
CY46_EXP0_DEFAERO_May2023Fog                      no  climaero  ...                              $HM_DATA/observations                         $HM_DATA/${BDLIB}/archive/
CY46_EXP0_DEFAERO_Spring                          no  climaero  ...                 /ec/res4/scratch/dum/OBDIR_SPRING/                 /ec/res4/scratch/dum/BDDIR_SPRING/
CY46_EXP0_DEFAERO_Summer                          no  climaero  ...                 /ec/res4/scratch/dum/OBS2018summer      /ec/res4/scratch/dum/BDDIR2018summer/archive/
CY46_EXP0_DEFAERO_Winter                          no  climaero  ...                /ec/res4/scratch/dum/OBS20202winter              /ec/res4/scratch/dum/BDDIR2020winter/
CY46_EXP0_DEFAERO_Winter_ICET                     no  climaero  ...                /ec/res4/scratch/dum/OBS20202winter              /ec/res4/scratch/dum/BDDIR2020winter/
CY46_EXP1_CAMSCLIMAER                             no  climaero  ...                   /ec/res4/scratch/dum/OBS_Aut2019          /ec/res4/scratch/dum/BDY_Aut2019/archive/
CY46_EXP1_CAMSCLIMAER_AprFog                      no  climaero  ...                  /ec/res4/scratch/dum/OBDIR_WINTER                 /ec/res4/scratch/dum/BDDIR_WINTER/
CY46_EXP1_CAMSCLIMAER_FebFog                      no  climaero  ...                  /ec/res4/scratch/dum/OBDIR_WINTER                 /ec/res4/scratch/dum/BDDIR_WINTER/
CY46_EXP1_CAMSCLIMAER_May2023Fog                  no  climaero  ...  /ec/res4/scratch/dum/hm_home/CY46_EXP0_DEFAERO...  /ec/res4/scratch/dum/hm_home/CY46_EXP0_DEFAERO...
CY46_EXP1_CAMSCLIMAER_Spring                      no  climaero  ...                  /ec/res4/scratch/dum/OBDIR_SPRING                 /ec/res4/scratch/dum/BDDIR_SPRING/
CY46_EXP1_CAMSCLIMAER_Summer                      no  climaero  ...                 /ec/res4/scratch/dum/OBS2018summer      /ec/res4/scratch/dum/BDDIR2018summer/archive/
CY46_EXP1_CAMSCLIMAER_Winter                      no  climaero  ...                /ec/res4/scratch/dum/OBS20202winter              /ec/res4/scratch/dum/BDDIR2020winter/
CY46_EXP1_DEFAERO                       ${BUILD-yes}  climaero  ...                   /ec/res4/scratch/dum/OBS_Aut2019          /ec/res4/scratch/dum/BDY_Aut2019/archive/
CY46_EXP2_CAMSNRT                                 no   camsnrt  ...                   /ec/res4/scratch/dum/OBS_Aut2019          /ec/res4/scratch/dum/BDY_Aut2019/archive/
CY46_EXP2_CAMSNRT_AprFog                          no   camsnrt  ...                  /ec/res4/scratch/dum/OBDIR_WINTER                 /ec/res4/scratch/dum/BDDIR_WINTER/
CY46_EXP2_CAMSNRT_Autumn_ICET                     no   camsnrt  ...                   /ec/res4/scratch/dum/OBS_Aut2019          /ec/res4/scratch/dum/BDY_Aut2019/archive/
CY46_EXP2_CAMSNRT_DMP_PR                ${BUILD-yes}   camsnrt  ...                   /ec/res4/scratch/dum/OBS_Aut2019          /ec/res4/scratch/dum/BDY_Aut2019/archive/
CY46_EXP2_CAMSNRT_DMP_PR_SSEM                     no   camsnrt  ...                   /ec/res4/scratch/dum/OBS_Aut2019          /ec/res4/scratch/dum/BDY_Aut2019/archive/
CY46_EXP2_CAMSNRT_FebFog                          no   camsnrt  ...                  /ec/res4/scratch/dum/OBDIR_WINTER                 /ec/res4/scratch/dum/BDDIR_WINTER/
CY46_EXP2_CAMSNRT_May2023Fog                      no   camsnrt  ...  /ec/res4/scratch/dum/hm_home/CY46_EXP0_DEFAERO...  /ec/res4/scratch/dum/hm_home/CY46_EXP0_DEFAERO...
CY46_EXP2_CAMSNRT_Spring                          no   camsnrt  ...                  /ec/res4/scratch/dum/OBDIR_SPRING                 /ec/res4/scratch/dum/BDDIR_SPRING/
CY46_EXP2_CAMSNRT_Spring_DMP_PR_SSEM              no   camsnrt  ...                  /ec/res4/scratch/dum/OBDIR_SPRING                 /ec/res4/scratch/dum/BDDIR_SPRING/
CY46_EXP2_CAMSNRT_Summer                          no   camsnrt  ...                 /ec/res4/scratch/dum/OBS2018summer      /ec/res4/scratch/dum/BDDIR2018summer/archive/
CY46_EXP2_CAMSNRT_Summer_DMP_PR_SSEM_2            no   camsnrt  ...                 /ec/res4/scratch/dum/OBS2018summer      /ec/res4/scratch/dum/BDDIR2018summer/archive/
CY46_EXP2_CAMSNRT_Summer_min_CDNC                 no   camsnrt  ...                 /ec/res4/scratch/dum/OBS2018summer      /ec/res4/scratch/dum/BDDIR2018summer/archive/
CY46_EXP2_CAMSNRT_Winter                          no   camsnrt  ...                 /ec/res4/scratch/dum/OBS2020winter              /ec/res4/scratch/dum/BDDIR2020winter/
CY46_EXP2_CAMSNRT_Winter_ICET                     no   camsnrt  ...                 /ec/res4/scratch/dum/OBS2020winter              /ec/res4/scratch/dum/BDDIR2020winter/
CY46_EXP2_CAMSNRT_minCDNC                         no   camsnrt  ...                   /ec/res4/scratch/dum/OBS_Aut2019          /ec/res4/scratch/dum/BDY_Aut2019/archive/
CY46_EXP2_DEFAERO                       ${BUILD-yes}  climaero  ...                   /ec/res4/scratch/dum/OBS_Aut2019          /ec/res4/scratch/dum/BDY_Aut2019/archive/

[33 rows x 7 columns]
```

# Sample-Efficient Multiagent Reinforcement Learning with Reset Replay (ICML 2024)

This repository is the official implementation of [Sample-Efficient Multiagent Reinforcement Learning with Reset Replay](), which is published in ICML 2024.

## Running in SMAC

To run MARR-QMIX in SMAC on the map of 5m_vs_6m, run this command after changing directory into '/marr-smac':

```smac
python src/main.py --config=rrmix --env-config=sc2 with env_args.map_name=5m_vs_6m seed=1 t_max=1010000 > 1.log 2>&1 &
```

Change the map_name to run on different maps.

The configuration could be revised in /src/config/algs/rrmix.yaml

## Running in MPE

To run MARR-FACMAC in MPE on the task of 3a, run this command after changing directory into '/marr-mpe'':

```smac
python src/main.py --config=rrfacmac_pp --env-config=particle with env_args.scenario_name=continuous_pred_prey_3a t_max=2000000 > 1.log 2>&1 &
```

Change the scenario_name to run on different tasks.

The configuration could be revised in /src/config/algs/rrfacmac_pp.yaml



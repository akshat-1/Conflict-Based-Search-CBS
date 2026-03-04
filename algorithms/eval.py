# from pathlib import Path
# from typing import Literal

# import yaml
# from pogema_toolbox.evaluator import evaluation

# from pogema_toolbox.registry import ToolboxRegistry

# from create_env import create_env_base



# PROJECT_NAME = 'Benchmark'
# BASE_PATH = Path('experiments')
# MODE: Literal["mapf", "lmapf"] = 'mapf'

# def main():
#     env_cfg_name = 'Environment'
#     ToolboxRegistry.register_env(env_cfg_name, create_env_base, Environment)
    
#     ToolboxRegistry.register_algorithm('RHCR', RHCRInference, RHCRConfig)
#     ToolboxRegistry.register_algorithm('SCRIMP', SCRIMPInference, SCRIMPInferenceConfig)
#     ToolboxRegistry.register_algorithm('Follower', FollowerInference, FollowerInferenceConfig, follower_preprocessor)
#     ToolboxRegistry.register_algorithm('LaCAM', LacamInference, LacamInferenceConfig)
#     ToolboxRegistry.register_algorithm('MATS-LP', MATS_LPInference, MATS_LPConfig)
#     ToolboxRegistry.register_algorithm('DCC', DCCInference, DCCInferenceConfig)
#     # ToolboxRegistry.register_algorithm("MAMBA", MAMBAInference, MAMBAInferenceConfig, mamba_preprocessor)

#     folder_names = [
#         # '01-random',
#         # '02-mazes',
#         # '03-warehouse',
#         # '04-movingai',
#         '05-puzzles', 
#     ]

#     # if MODE == "mapf":
#     #     folder_names += ['06-pathfinding']

#     for folder in folder_names:
#         maps_path = BASE_PATH / folder / "maps.yaml"
#         with open(maps_path, 'r') as f:
#             maps = yaml.safe_load(f)
#         ToolboxRegistry.register_maps(maps)
        
#         config_path = BASE_PATH / folder / f"{Path(folder).name}-{MODE}.yaml"
#         with open(config_path) as f:
#             evaluation_config = yaml.safe_load(f)
        
#         eval_dir = BASE_PATH / folder
#         evaluation(evaluation_config, eval_dir=eval_dir)
#         save_evaluation_results(eval_dir)


# if __name__ == '__main__':
#     main()


from pathlib import Path
from typing import Literal

import yaml
from pogema_toolbox.evaluator import evaluation
from pogema_toolbox.registry import ToolboxRegistry
from pogema_toolbox.create_env import Environment

from create_env import create_env_base
from algorithms.CBS.cbs import MyCBS   # <-- Import CBS

PROJECT_NAME = 'Benchmark'
BASE_PATH = Path('experiments')
MODE: Literal["mapf", "lmapf"] = 'mapf'


def main():
    env_cfg_name = 'Environment'
    ToolboxRegistry.register_env(env_cfg_name, create_env_base, Environment)

    # ✅ Register ONLY CBS
    ToolboxRegistry.register_algorithm('CBS', MyCBS, CBSConfig)

    folder_names = [
        '05-puzzles',
    ]

    for folder in folder_names:
        maps_path = BASE_PATH / folder / "maps.yaml"
        with open(maps_path, 'r') as f:
            maps = yaml.safe_load(f)
        ToolboxRegistry.register_maps(maps)

        config_path = BASE_PATH / folder / f"{Path(folder).name}-{MODE}.yaml"
        with open(config_path) as f:
            evaluation_config = yaml.safe_load(f)

        # Optional: force config to use only CBS (extra safety)
        evaluation_config["algorithms"] = ["CBS"]

        eval_dir = BASE_PATH / folder
        evaluation(evaluation_config, eval_dir=eval_dir)
        save_evaluation_results(eval_dir)


if __name__ == '__main__':
    main()
# Author: Osho Giri
# Created: 02/08/2020, 10:36 AM
# Email: oshopgiri@icloud.com

from aux_functions import start_environment
from configs.read_cfg import read_cfg
from main import generate_json
import importlib
import nvidia_smi
import time

if __name__ == "__main__":
    # Read the config file
    cfg = read_cfg(config_filename='configs/config.cfg', verbose=True)
    cfg.num_agents = 1
    can_proceed = generate_json(cfg)
    # Check if NVIDIA GPU is available
    try:
        nvidia_smi.nvmlInit()
        cfg.NVIDIA_GPU = True
    except:
        cfg.NVIDIA_GPU = False
    if can_proceed:
        # If mode != infer, don't initialize any algorithm
        if cfg.mode == 'infer':
            iterations = 100
            total_distance = 0.0
            max_distance_travelled = 0.0
            mdt_iteration = -1

            for i in range(iterations):
                try:
                    # Start the environment
                    env_process, env_folder = start_environment(env_name=cfg.env_name)

                    algorithm = importlib.import_module('algorithms.' + cfg.algorithm)
                    name = 'algorithm.' + cfg.algorithm + '(cfg, env_process, env_folder)'
                    distance_travelled = eval(name)

                    total_distance += distance_travelled
                    if(distance_travelled > max_distance_travelled):
                        max_distance_travelled = distance_travelled
                        mdt_iteration = i
                    time.sleep(1)
                except KeyboardInterrupt:
                    raise
                except:
                    i -= 1

            print(total_distance / iterations)
            print(mdt_iteration)
        else:
            print('Please change the mode to \'infer\'')
# Author: Osho Giri
# Created: 02/08/2020, 10:36 AM
# Email: oshopgiri@icloud.com

from aux_functions import start_environment
from configs.read_cfg import read_cfg
from main import generate_json
import importlib
import nvidia_smi

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
        # Start the environment
        env_process, env_folder = start_environment(env_name=cfg.env_name)

        # If mode != infer, don't initialize any algorithm
        if cfg.mode == 'infer':
            total_distances = []

            for i in range(1000):
                algorithm = importlib.import_module('algorithms.' + cfg.algorithm)
                name = 'algorithm.' + cfg.algorithm + '(cfg, env_process, env_folder)'
                total_distances.append(eval(name))

            print(total_distances/1000)
        else:
            print('Please change the mode to \'infer\'')
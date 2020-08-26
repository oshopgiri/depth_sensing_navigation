# Evaluating the Performance of an Autonomous UAV Navigation DRL Model Trained using Depth Maps in Similar Environments

## Initial Setup
The system requires the following software to run:

| Software      | Version |
|---------------|---------|
| Anaconda      | 5.2.0   |
| Python        | 3.6.5   |
| CUDA          | 10.0    |
| cuDNN         | 7.6.5   |

Once all the required software are installed, clone the repository:
```bash
git clone https://github.com/oshopgiri/depth_sensing_navigation.git
cd depth_sensing_navigation
```

Install all the required python packages:
```bash
pip install -r requirements_gpu.txt
```

PEDRA environments can be downloaded from [here](/unreal_envs/readme.md). Once downloaded, extract the environment under `unreal_envs` directory.

## Training

Add the required configurations to the following files:
```text
./configs/config.cfg
./configs/DeepREINFORCE.cfg
```

Train the model:
```bash
python main.py
```

## Inferring
Update the required inference configurations to the following files to load weights from the trained model:
```text
./configs/config.cfg
./configs/DeepREINFORCE.cfg
```

Inferring the model:
```bash
python infer.py
```

## Experiment Results
- The model trained for the experiment can be downloaded from [here](https://drive.google.com/file/d/1fS0ISFcwrmoRlQh7SObP2QA3h9MkKEri/view?usp=sharing)
    - Once downloaded, place the `indoor_cloud` directory under `./models/trained/Indoor/`
    - Refer back to Inferring steps
- Training results can be downloaded from [here](https://drive.google.com/file/d/1WCqCSTesxStKHxBR2TWN3TTeoSNiqpUj/view?usp=sharing)

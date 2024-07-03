# Evo Gym

## Pre-requirements
For better experience, we have built the running environment in docker and provide visualization via X11. Please make sure the docker engine and ssh are installed on your pc. 

> Note: Codes are not included in the docker container. The container only provides python and display environment.

### Docker
For installing **docker engine**, please refer to: https://docs.docker.com/engine/install/ubuntu/ and a chinese documentation https://docker-practice.github.io/zh-cn/install/ubuntu.html

> Note: Docker Engine is different from Docker Desktop. Docker Engine is the core of the docker service. While Docker Desktop is a visualized platform for managing containers and images.

Create docker volume named `ws` for files mapping (see what is docker volume at https://zhuanlan.zhihu.com/p/468642439):

```bash
docker volume create --name ws --opt type=none --opt device={path-to-your-code-folder} --opt o=bind
```

Use gpu in docker:
```bash
sudo sh ../nvidia-container-runtime-script.sh
sudo apt-get install nvidia-container-runtime
sudo systemctl restart doccker.service
```


## Build the Environment
Build dockerfile firstly.
```
cd evo_gym/docker
docker build -t 'evo-gym:latest' . 
```
Get the **image_id**.

Run the image, make sure the volume is mounted.
```
xhost +
docker run -it --name evo-gym --gpus all -v ws:/root/ws {image_id} /bin/bash
docker start evo-gym
```
> Note: Replace the {image_id} with the **image_id** in the last step.

Search "Remote - SSH" in vscode Extensions and install it. Then find the container in Dev Containers list and click `Attach in New Window`, and then you can interactively code in container.

## Task Explanation in Brief
All the environments have been registerated in gymnasium, but you are free to change anything in these files.
> This environment is edited from MuJoCo multiagent environment, but it is also free to use single agent.

You can try basic difficulty env examples like this:
```bash
cd evo_gym
python example.py --cfg config/run-to-goal-devant-v0.yaml
```
Tasks:
```
config/run-to-goal-devant-v0.yaml
config/run-to-goal-devbug-v0.yaml
config/run-to-goal-devspider-v0.yaml
```

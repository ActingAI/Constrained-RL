from gymnasium.envs.registration import register
import os

register(
    id='run-to-goal-evoants-v0',
    entry_point='competevo.evo_envs:MultiEvoAgentEnv',
    disable_env_checker=True,
    kwargs={'agent_names': ['evo_ant', 'evo_ant'],
            'init_pos': [(-2, 0, 0.75), (2, 0, 0.75)],
            'ini_euler': [(0, 0, 0), (0, 0, 180)],
            # 'rgb': [(0.98, 0.54, 0.56), (0.11, 0.56, 1)],
            'rgb': [(0.98, 0.87, 0.67), (0.98, 0.87, 0.67)],
            'max_episode_steps': 500,
            },
)

register(
    id='run-to-goal-devants-v0',
    entry_point='competevo.evo_envs:MultiDevAgentEnv',
    disable_env_checker=True,
    kwargs={'agent_names': ['dev_ant', 'dev_ant'],
            'init_pos': [(-1, 0, 0.75), (1, 0, 0.75)],
            'ini_euler': [(0, 0, 0), (0, 0, 180)],
            # 'rgb': [(0.98, 0.54, 0.56), (0.11, 0.56, 1)],
            'rgb': [(0.98, 0.87, 0.67), (0.98, 0.87, 0.67)],
            'max_episode_steps': 500,
            },
)

register(
    id='run-to-goal-devant-v0',
    entry_point='competevo.evo_envs:MultiDevAgentEnv',
    disable_env_checker=True,
    kwargs={'agent_names': ['dev_ant'],
            'init_pos': [(-1, 0, 0.75)],
            'ini_euler': [(0, 0, 0)],
            # 'rgb': [(0.98, 0.54, 0.56)],
            'rgb': [(0.98, 0.87, 0.67)],
            'max_episode_steps': 500,
            },
)

register(
    id='run-to-goal-evoant-v0',
    entry_point='competevo.evo_envs:MultiEvoAgentEnv',
    disable_env_checker=True,
    kwargs={'agent_names': ['evo_ant'],
            # 'init_pos': [(-2, 0, 0.75)],
            # 'ini_euler': [(0, 0, 0)],
            'init_pos': [(2, 0, 0.75)],
            'ini_euler': [(0, 0, 180)],
            # 'rgb': [(0.98, 0.54, 0.56), (0.11, 0.56, 1)],
            'rgb': [(0.98, 0.87, 0.67), (0.98, 0.87, 0.67)],
            'max_episode_steps': 500,
            },
)

register(
    id='run-to-goal-devbugs-v0',
    entry_point='competevo.evo_envs:MultiDevAgentEnv',
    disable_env_checker=True,
    kwargs={'agent_names': ['dev_bug', 'dev_bug'],
            'init_pos': [(-1, 0, 0.75), (1, 0, 0.75)],
            'ini_euler': [(0, 0, 0), (0, 0, 180)],
            # 'rgb': [(0.98, 0.54, 0.56), (0.11, 0.56, 1)],
            'rgb': [(0.98, 0.87, 0.67), (0.98, 0.87, 0.67)],
            'max_episode_steps': 500,
            },
)

register(
    id='run-to-goal-devbug-v0',
    entry_point='competevo.evo_envs:MultiDevAgentEnv',
    disable_env_checker=True,
    kwargs={'agent_names': ['dev_bug'],
            'init_pos': [(-1, 0, 0.75)],
            'ini_euler': [(0, 0, 0)],
            'rgb': [(0.98, 0.87, 0.67)],
            'max_episode_steps': 500,
            },
)

register(
    id='run-to-goal-devspiders-v0',
    entry_point='competevo.evo_envs:MultiDevAgentEnv',
    disable_env_checker=True,
    kwargs={'agent_names': ['dev_spider', 'dev_spider'],
            'init_pos': [(-1, 0, 0.75), (1, 0, 0.75)],
            'ini_euler': [(0, 0, 0), (0, 0, 180)],
            # 'rgb': [(0.98, 0.54, 0.56), (0.11, 0.56, 1)],
            'rgb': [(0.98, 0.87, 0.67), (0.98, 0.87, 0.67)],
            'max_episode_steps': 500,
            },
)

register(
    id='run-to-goal-devspider-v0',
    entry_point='competevo.evo_envs:MultiDevAgentEnv',
    disable_env_checker=True,
    kwargs={'agent_names': ['dev_spider'],
            'init_pos': [(-1, 0, 0.75)],
            'ini_euler': [(0, 0, 0)],
            'rgb': [(0.98, 0.87, 0.67)],
            'max_episode_steps': 500,
            },
)


register(
    id='run-to-goal-animals-v0',
    entry_point='competevo.evo_envs:MultiAnimalEnv',
    disable_env_checker=True,
    kwargs={'agent_names': ['dev_bug', 'dev_bug'],
            'init_pos': [(-1, 0, 0.75), (1, 0, 0.75)],
            'ini_euler': [(0, 0, 0), (0, 0, 180)],
            # 'rgb': [(0.98, 0.54, 0.56), (0.11, 0.56, 1)],
            'rgb': [(0.98, 0.87, 0.67), (0.98, 0.87, 0.67)],
            'max_episode_steps': 500,
            },
)
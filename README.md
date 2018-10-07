# Navigation - Deep reinforcement learning agent
Training an agent to play game using reinforcement learning

## Environment
Environment: Navigation (Modified Unity Environment).Here we will train an agent to collect yellow bananas while avoiding blue bananas. 

Number of state space: The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Given this information, the agent has to learn how to best select actions. Four discrete actions are available, corresponding to:

Number of action space: 4 (right,left,forward,backward)

### When environment is considered to be solved
The task is episodic, and in order to solve the environment, your agent must get an average score of +13 over 100 consecutive episodes.

## Getting Started
To set up your python environment to run the code in this repository, follow the instructions below.

1. Create (and activate) a new environment with Python 3.6.

	- __Linux__ or __Mac__: 
	```bash
	conda create --name drlnd python=3.6
	source activate drlnd
	```
	- __Windows__: 
	```bash
	conda create --name drlnd python=3.6 
	activate drlnd
	```
	
2. Follow the instructions in [this repository](https://github.com/openai/gym) to perform a minimal install of OpenAI gym.  
	- Next, install the **classic control** environment group by following the instructions [here](https://github.com/openai/gym#classic-control).
	- Then, install the **box2d** environment group by following the instructions [here](https://github.com/openai/gym#box2d).
	
3. Clone the repository (if you haven't already!), and navigate to the `python/` folder.  Then, install several dependencies.
```bash
git clone https://github.com/abhismatrix1/navigation.git
cd navigation/python
pip install .
```

4. Create an [IPython kernel](http://ipython.readthedocs.io/en/stable/install/kernel_install.html) for the `game` environment.  
```bash
python -m ipykernel install --user --name game --display-name "game"
```

5. Before running code in a notebook, change the kernel to match the `game` environment by using the drop-down `Kernel` menu. 

![Kernel][image2]

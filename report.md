### Learning Algorithm

1. Agent is trained using Q-learning algorithm with DQN network. It is the basic DQN without any priority experience replay, Double DQN.
2. The deep Q-network is a value based method which tries to learn the optimal action value for given state.
3. The agent follows epsilon-greedy policy where epsilon decays as the training progresses.

### Hyperparameters:

  - BUFFER_SIZE = int(1e5)  # replay buffer size
  - BATCH_SIZE = 64         # minibatch size
  - GAMMA = 0.99            # discount factor
  - TAU = 1e-1              # for soft update of target parameters
  - LR = 5e-4               # learning rate
  - UPDATE_EVERY = 4        # how often to update the network


### Neural network model used. Architecture:

Four layer MLP

```bash
self.fc1=nn.Linear(state_size,160) -> nn.Linear(160,80) -> nn.Linear(80,20) -> nn.Linear(20,action_size)
```

### Plot of scores
![Agent_reward][reward]

### Future Work (improvements)
Applying these techniques to improve
1. Double DQN - Prevents overestimation
2. Prioritized Experience Replay - More important transitions should be sampled with higher probability.
3. Dueling DQN - Results show that this architecture leads to better policy evaluation in the presence of many similar-valued actions

import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        "*** YOUR CODE HERE ***"
        state_size
        action_size
        #self.dropout = nn.Dropout(.3)
        self.fc1=nn.Linear(state_size,160)
        self.fc2=nn.Linear(160,80)
        self.fc3=nn.Linear(80,80)
        #self.fc4=nn.Linear(80,20)
        self.fc5=nn.Linear(80,action_size)

    def forward(self, state):
        """Build a network that maps state -> action values."""
        
        x=F.relu(self.fc1(state))
        x=F.relu(self.fc2(x))
        #x=self.dropout(x)
        x=F.relu(self.fc3(x))
        #x=self.dropout(x)
        #x=F.relu(self.fc4(x))
        x=self.fc5(x)
        
        return x


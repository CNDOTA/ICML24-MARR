import torch
import torch.nn as nn
import torch.nn.functional as F


class RNNAgent(nn.Module):
    def __init__(self, input_shape, args):
        super(RNNAgent, self).__init__()
        self.args = args

        self.fc1 = nn.Linear(input_shape, args.rnn_hidden_dim)
        self.rnn = nn.GRUCell(args.rnn_hidden_dim, args.rnn_hidden_dim)
        self.fc2 = nn.Linear(args.rnn_hidden_dim, args.n_actions)

        if self.args.layer_norm:
            self.fc1_norm = nn.LayerNorm(args.rnn_hidden_dim)
            self.rnn_norm = nn.LayerNorm(args.rnn_hidden_dim)
            # no need for the q-value layer
        if self.args.dropout:
            self.fc1_drop = nn.Dropout(self.args.drop_p)
            self.rnn_drop = nn.Dropout(self.args.drop_p)

    def init_hidden(self):
        # make hidden states on same device as model
        return self.fc1.weight.new(1, self.args.rnn_hidden_dim).zero_()

    def forward(self, inputs, hidden_state):

        x = F.relu(self.fc1(inputs))
        if self.args.layer_norm:
            x = self.fc1_norm(x)
        if self.args.dropout:
            x = self.fc1_drop(x)
        h_in = hidden_state.reshape(-1, self.args.rnn_hidden_dim)
        h = self.rnn(x, h_in)
        if self.args.layer_norm:
            h = self.rnn_norm(h)
        if self.args.dropout:
            h = self.rnn_drop(h)
        q = self.fc2(h)
        return q, h

import numpy as np
import gymnasium as gym

class Model:

    def __init__(self):

        self.learning_rate = 0.8
        self.gamma = 0.95
        self.epsilon = 1.0 
        self.epsilon_decay = 0.999
        self.epsilon_min = 0.1
        self.episodes = 100000
        self.env, self.n_states, self.n_actions = self.create_env()
        self.q_table = np.zeros((self.n_states, self.n_actions))

    def create_env(self):

        self.env = gym.make(
            'FrozenLake-v1',
            desc = None,
            map_name = "4x4",
            is_slippery = False,
        )

        return self.env, self.env.observation_space.n, self.env.action_space.n

    def action(self, state):

        random_n = np.random.random()

        if random_n < self.epsilon:
            return self.env.action_space.sample()
        
        return np.argmax(self.q_table[state])
    
    def update_q_table(self, state, action, reward, next_state, done):

        target = reward + self.gamma * np.max(self.q_table[next_state])

        if done:
            target = reward + self.gamma * 0

        self.q_table[state][action] = self.q_table[state][action] + self.learning_rate * (target - self.q_table[state][action])

    def train(self):

        count = 0

        for ep in range(self.episodes + 1):
            state, info = self.env.reset()
            done = False

            while not done:
                action = self.action(state)
                next_state, reward, terminated, truncated, info = self.env.step(action)

                if reward == 1.0:
                    count += 1

                self.update_q_table(state, action, reward, next_state, terminated)
                state = next_state
                done = terminated or truncated

            self.epsilon = self.epsilon * self.epsilon_decay

            if self.epsilon < self.epsilon_min:
                self.epsilon = self.epsilon_min

            if ep % 500 == 0:
                print(f"Episode: {ep}, winrate: {(count/(ep + 1)) * 100}%")

model = Model()
model.train()



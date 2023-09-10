
class Model():
    def __init__(self, inplace=False):
        self.w1 = 0.3
        self.w2 = 0.3
        self.w3 = 0.4

    def forward(self, features):
        z = self.w1 * features[0] + self.w2 * features[2] + self.w3 * features[1]
        score = (z / 100) 
        return score
    
import numpy as np

class BTMCJ:

    def __init__(self, n_items):
        self.n_items = n_items

    def check(self):
        print("BTMCJ")

    def update_p(self, m, i, p):
        part_1 = []
        part_2 = []

        for j in range(m.shape[1]):
            if m[i, j] != -1:
                part_1.append(m[i, j] * (p[j] / (p[i] + p[j])))
                part_2.append(m[j, i] * (1 / (p[i] + p[j])))
        
        part_3 = np.sum(part_1) / np.sum(part_2)

        return part_3

    def run(self, X
            #, result_output="single"
            ):
        number_of_rounds = len(X)
        m = np.asarray([[0 if i!=j else -1 
              for j in range(self.n_items)] 
                for i in range(self.n_items)])

        for _ in range(number_of_rounds):    # adapt do these follow the same pattern as CJ data in repository?  
            a = X[_][0]
            b = X[_][1]
            winner = X[_][2]

            if winner == a:
                m[a][b] += 1
            elif winner == b:
                m[b][a] += 1

        print(f"m:\n{m}")

        try:
            p = np.asarray([1.0] * self.n_items)
            print(f"Initial p: {p}")
            for _ in range(10_000):
                p_previous = p.copy()
                for i in range(len(p)):
                    p[i] = self.update_p(m, i, p)

                normalising_p = pow(np.prod(p), 1/len(p))
                p = np.asarray(p) / normalising_p

                if np.all(np.abs(p - p_previous) < 1e-6):
                    print(f"Converged! on round: {_}")
                    break

                self.p_scaled = [k * 100 for k in p]
                self.final_rank = np.argsort(-np.array(self.p_scaled))
            
        except Exception as e:
            print(f"Error: {str(e)}")
        
        self.p = p

    # def btm(m):


    def get_ranking(self):
        print("BTMCJ ranking:")
        for i in range(len(self.final_rank)):
            print(f"{i+1}: Item {self.final_rank[i]} - score: {self.p_scaled[self.final_rank[i]]}")
        # print("BTMCJ ranking: {}")
        # return self.final_rank

import numpy as np

class BradleyTerryModel:
    def __init__(self):
        self.weights = None
    
    def fit(self, X, y, max_iter=100, tol=1e-4):
        n_samples, n_features = X.shape
        self.weights = np.ones(n_features)
        
        for _ in range(max_iter):
            prev_weights = np.copy(self.weights)
            
            for i in range(n_features):
                wins = 0
                losses = 0
                
                for j in range(n_samples):
                    if X[j, i] == 1:
                        wins += 1
                    elif X[j, i] == -1:
                        losses += 1
                
                self.weights[i] = np.log(wins / losses)
            
            if np.linalg.norm(self.weights - prev_weights) < tol:
                break
    
    def predict(self, X):
        probabilities = np.exp(X @ self.weights)
        return probabilities / np.sum(probabilities)
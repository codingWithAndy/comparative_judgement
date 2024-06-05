import numpy as np

class GradesPridiction:
    def __init__(
        self, 
        grade_allowcation: list, 
        g_letters:list, 
        n_per_grade:list, 
        threshold:float
    ):
        self.grade_allowcation = grade_allowcation
        self.g_letters = g_letters
        self.n_per_grade = n_per_grade
        self.threshold = threshold

    def create_text_output(
        self, 
        probs: dict
    ):
        position = []
        prev = 0
        
        for n_items in self.n_per_grade:
            position.append(prev + n_items)
            prev += n_items
        for key, value in probs.items():
            found = False
            results = np.asarray(value)
            chances = []
            idx = 0
            for i, pos in enumerate(position):
                if i == 0:
                    chances.append(np.sum(results[:position[0]]))
                else:
                    chances.append(np.sum(results[position[i-1]:position[i]]))
            for i, gl in enumerate(self.g_letters):
                print(f"The probability of item {key} get a {gl} is: {np.around(chances[i]*100, 2)}%")
            g_number = np.argmax(chances)
            grade = self.g_letters[g_number]
            print(f"Most likely grade for item {key} grade: {grade}")
            while found == False:
                total = np.sum(results[:position[idx]])
                if total > self.threshold:
                    chances = total
                    grade = self.g_letters[idx]
                    print(f"The grade above the threshold {self.threshold} for item {key} is: {grade} \nwith a confidence of: {np.around(chances*100, 2)}%\n")
                    found = True
                idx += 1
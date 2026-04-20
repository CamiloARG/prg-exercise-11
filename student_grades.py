from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, student_index):
        score = self.scores[student_index]

        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"

    def find(self,wanted_number):
        found_indices = []

        for i in range(len(self.scores)):
            if self.scores[i] == wanted_number:
                found_indices.append(i)

        return found_indices

    def get_sorted(self):
        scores = list(self.scores)
        old_scores = self.scores[:]

        while True:
            for i in range(1, len(scores)):
                if scores[i] < scores[i - 1]:
                    scores[i], scores[i - 1] = scores[i - 1], scores[i]

                sort_num = list(sorted(old_scores))
                if sort_num == scores:
                    return scores

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    #print(results.get_grade(2))
    #print(results.get_grade(6))
    #print(results.get_grade(7))
    #print(results.find(100))
    #print(results.find(50))
    #print(results.find(77))
    #print(results.get_sorted())
    #print(results.scores)
    number_stu = results.count()
    print(f"Students: {number_stu}")
    scores = results.scores
    for ind,score in enumerate(scores):
        grade = results.get_grade(ind)
        print(f"Student {ind}: {score} points - {grade}")

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())

if __name__ == "__main__":
    main()
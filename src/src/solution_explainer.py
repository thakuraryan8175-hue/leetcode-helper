"""
AI-LeetCode-Mentor
Solution Explainer Module

This module explains algorithm approaches
and helps students understand solutions.
"""


class SolutionExplainer:

    def __init__(self, algorithm):
        self.algorithm = algorithm

    def explain(self):
        explanation = {
            "algorithm": self.algorithm,
            "steps": [
                "Understand the problem requirements",
                "Identify suitable data structures",
                "Apply the algorithm",
                "Verify the solution with examples"
            ],
            "learning_goal": "Understand the logic behind the solution"
        }

        return explanation


if __name__ == "__main__":

    algorithm = "Hash Map Approach"

    explainer = SolutionExplainer(algorithm)

    result = explainer.explain()

    print(result)

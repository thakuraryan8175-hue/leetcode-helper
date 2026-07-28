"""
AI-LeetCode-Mentor
Main Application

Connects all AI mentor modules together.
"""

from problem_analyzer import ProblemAnalyzer
from solution_explainer import SolutionExplainer
from complexity_analyzer import ComplexityAnalyzer


def run_ai_mentor(problem):

    print("\n🧩 AI-LeetCode-Mentor")
    print("=" * 40)

    # Step 1: Analyze Problem
    analyzer = ProblemAnalyzer(problem)
    analysis = analyzer.analyze()

    print("\n🧠 Problem Analysis:")
    print(analysis)


    # Step 2: Explain Solution
    explainer = SolutionExplainer(problem)
    explanation = explainer.explain()

    print("\n💡 Solution Explanation:")
    print(explanation)


    # Step 3: Analyze Complexity
    complexity = ComplexityAnalyzer(
        "Hash Map Approach"
    )

    result = complexity.analyze()

    print("\n📊 Complexity Analysis:")
    print(result)



if __name__ == "__main__":

    problem = """
    Given an array of integers,
    return two numbers whose sum equals target.
    """

    run_ai_mentor(problem)

# main.py
"""
A simple agentic AI example for beginners.
This script defines a basic agent that can set a goal and take a simple action.
"""

class SimpleAgent:
    def __init__(self, name):
        self.name = name
        self.goal = None

    def set_goal(self, goal):
        self.goal = goal
        print(f"{self.name} sets a goal: {self.goal}")

    def act(self):
        if self.goal:
            print(f"{self.name} is working towards: {self.goal}")
        else:
            print(f"{self.name} has no goal yet.")

if __name__ == "__main__":
    agent = SimpleAgent("Agent Smith")
    agent.set_goal("Learn about agentic AI")
    agent.act()

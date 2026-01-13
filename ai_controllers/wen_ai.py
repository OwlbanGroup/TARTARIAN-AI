"""
Wireless Electricity Network AI Controller
AI for load balancing in the Tartarian Wireless Electricity Network.
"""

import numpy as np
from sklearn.linear_model import LogisticRegression  # For decision making


class WENAIController:
    """
    AI controller for network load balancing.
    """

    def __init__(self):
        self.model = LogisticRegression()
        self.data = []

    def balance_load(self, demands):
        """
        Balances loads across nodes.

        Args:
            demands (list): Power demands.

        Returns:
            list: Prioritized allocations.
        """
        priorities = [1 if d > 100 else 0 for d in demands]  # High demand priority
        self.data.append((demands, priorities))
        if len(self.data) > 5:
            X = np.array([d[0] for d in self.data])
            y = np.array([d[1] for d in self.data])
            self.model.fit(X, y)
            predictions = self.model.predict([demands])
            return predictions.tolist()
        return priorities

# Example usage
controller = WENAIController()
priorities = controller.balance_load([120, 80, 150])
print(f"Load Priorities: {priorities}")

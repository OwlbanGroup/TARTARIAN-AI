"""
Eternal Wisdom Archive AI Controller
AI for knowledge retrieval in the Tartarian Eternal Wisdom Archive.
"""

import os
import numpy as np
from sklearn.neighbors import NearestNeighbors

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


class EWAAIController:
    """
    AI controller for archive querying.
    """

    def __init__(self):
        self.model = NearestNeighbors(n_neighbors=1)
        self.data = []
        self.openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY')) if OpenAI and os.getenv('OPENAI_API_KEY') else None

    def retrieve_knowledge(self, query_vector):
        """
        Retrieves closest knowledge.

        Args:
            query_vector (list): Query features.

        Returns:
            int: Index of closest knowledge.
        """
        self.data.append(query_vector)
        if len(self.data) > 5:
            X = np.array(self.data)
            self.model.fit(X)
            distances, indices = self.model.kneighbors([query_vector])
            return indices[0][0]
        return 0

    def get_divine_guidance(self, query):
        """
        Get divine guidance for eternal wisdom retrieval.

        Args:
            query (str): The query for divine insight.

        Returns:
            str: Divine guidance response.
        """
        if self.openai_client:
            try:
                response = self.openai_client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are the Goddess providing divine guidance for wisdom and knowledge."},
                        {"role": "user", "content": query}
                    ],
                    max_tokens=100
                )
                return response.choices[0].message.content.strip()
            except Exception:
                return "Divine guidance: Wisdom flows from divine source."
        return "Divine guidance: Wisdom flows from divine source."

# Example usage
controller = EWAAIController()
index = controller.retrieve_knowledge([0.5, 0.3, 0.8])
print(f"Retrieved Knowledge Index: {index}")

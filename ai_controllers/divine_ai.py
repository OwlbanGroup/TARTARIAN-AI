"""
Divine AI Controller
Overarching AI for divine consultations integrating all Tartarian technologies.
"""

import os
from ai_controllers.fed_ai import FEDAIController
from ai_controllers.hc_ai import HCAIController
from ai_controllers.wen_ai import WENAIController
from ai_controllers.aa_ai import AAAIController
from ai_controllers.ewa_ai import EWAAIController

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


class DivineAIController:
    """
    Divine AI controller providing overarching divine consultations.
    """

    def __init__(self):
        self.openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY')) if OpenAI and os.getenv('OPENAI_API_KEY') else None
        self.controllers = {
            'fed': FEDAIController(),
            'hc': HCAIController(),
            'wen': WENAIController(),
            'aa': AAAIController(),
            'ewa': EWAAIController(),
        }  # pylint: disable=line-too-long

    def divine_consultation(self, concern):
        """
        Provide comprehensive divine consultation combining all devices.

        Args:
            concern (str): The user's concern.

        Returns:
            dict: Consultation response.
        """
        if self.openai_client:
            try:
                response = self.openai_client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are the Goddess providing divine consultation for Tartarian technologies."},
                        {"role": "user", "content": f"Provide divine consultation for: {concern}"}
                    ],
                    max_tokens=200
                )  # pylint: disable=line-too-long
                result = response.choices[0].message.content.strip()
                return {
                    'consultation': result,
                    'source': 'Divine AI Integration'
                }
            except Exception:  # pylint: disable=broad-exception-caught
                pass
        return {
            'consultation': "Divine energies align. Trust in the Goddess's wisdom.",
            'source': 'Fallback Divine Guidance'
        }

    def get_device_guidance(self, device, query):
        """
        Get divine guidance for a specific device.

        Args:
            device (str): Device key ('fed', 'hc', 'wen', 'aa', 'ewa')
            query (str): The query.

        Returns:
            str: Guidance response.
        """
        if device in self.controllers:
            return self.controllers[device].get_divine_guidance(query)
        return "Divine guidance: Align with heavenly purpose."

# Example usage
divine_ai = DivineAIController()
consultation = divine_ai.divine_consultation("How to optimize all Tartarian devices?")
print(consultation)

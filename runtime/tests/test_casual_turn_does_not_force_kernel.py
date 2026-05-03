import unittest

from runtime.contracts.enums import ROUTE_CLASSES
from runtime.core.monitor import classify_turn_route


class CasualTurnRoutingTest(unittest.TestCase):
    def test_casual_turn_stays_light_host_route(self):
        route = classify_turn_route(
            user_text="Thanks con ❤️",
            has_tool_request=False,
            continuity_pressure=False,
            verification_pressure=False,
        )

        self.assertEqual(route["route"], ROUTE_CLASSES[0])
        self.assertFalse(route["kernel_required"])
        self.assertEqual(route["reason"], "casual_turn")


if __name__ == "__main__":
    unittest.main()

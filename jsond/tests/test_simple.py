import datetime
import json
import unittest

import jsond


class TestSimple(unittest.TestCase):

    def test_same_as_json(self):
        """If no date objects exist, then we should be the same as json.
        """
        to_encode = {
            "a": 1,
            "b": 2,
            "c": 3
        }

        self.assertEqual(
            json.dumps(to_encode),
            jsond.dumps(to_encode)
        )

    def test_process_date(self):
        """Test that we can process a date.
        """
        relevant_date = datetime.datetime(2011, 3, 15, 0, 0, 0)

        # We should be able to encode this structure.
        #
        to_encode = {
            "some_value": 345,
            "my_list": [1, 2, 3, 4],
            "relevant_date": relevant_date
        }
        encoded = jsond.dumps(to_encode)

        # And get the same date back when we decode.
        #
        decoded = jsond.loads(encoded)
        self.assertEqual(decoded["relevant_date"], relevant_date)

    def test_safe_for_json(self):
        """When we jsond.dumps something, it should be safe to decode in json.
        """
        relevant_date = datetime.datetime(2011, 3, 15, 0, 0, 0)
        to_encode = {
            "relevant_date": relevant_date
        }
        encoded = jsond.dumps(to_encode)

        # jsond should encode this such that it is safe to decode in json.
        # The only difference is that json will treat the date as a string.
        #
        json_decoded = json.loads(encoded)
        self.assertIsInstance(json_decoded["relevant_date"], basestring)
        self.assertEqual(
            json_decoded["relevant_date"],
            "datetime:2011-03-15T00:00:00"
        )

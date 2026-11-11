import unittest

from duration import breakdown, format_duration, parse_duration


class DurationTests(unittest.TestCase):
    def test_parse_duration(self):
        self.assertEqual(parse_duration("1h30m"), 5400)
        self.assertEqual(parse_duration("45s"), 45)
        self.assertEqual(parse_duration("2m 5s"), 125)
        self.assertEqual(parse_duration("1h2m3s"), 3723)

    def test_parse_rejects_invalid(self):
        for text in ("", "1h30", "90s", "abc", "1x"):
            with self.assertRaises(ValueError):
                parse_duration(text)

    def test_breakdown(self):
        self.assertEqual(breakdown(3723), {"hours": 1, "minutes": 2, "seconds": 3})
        with self.assertRaises(ValueError):
            breakdown(-1)

    def test_format_duration(self):
        self.assertEqual(format_duration(0), "0s")
        self.assertEqual(format_duration(5400), "1h 30m")
        self.assertEqual(format_duration(125), "2m 5s")


class ClockTests(unittest.TestCase):
    def test_format_clock(self):
        from duration import format_clock

        self.assertEqual(format_clock(0), "00:00:00")
        self.assertEqual(format_clock(3723), "01:02:03")

    def test_format_clock_rejects_negative(self):
        from duration import format_clock

        with self.assertRaises(ValueError):
            format_clock(-1)


if __name__ == "__main__":
    unittest.main()

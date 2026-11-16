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


class RemainingUntilTests(unittest.TestCase):
    def test_future_target_returns_exact_seconds(self):
        from datetime import datetime

        from duration import remaining_until

        now = datetime(2026, 11, 16, 17, 0, 0)
        self.assertEqual(
            remaining_until("2026-11-16T18:00:00", now),
            3600,
        )

    def test_past_target_returns_zero(self):
        from datetime import datetime

        from duration import remaining_until

        now = datetime(2026, 11, 16, 18, 0, 0)
        self.assertEqual(remaining_until("2026-11-16T17:00:00", now), 0)

    def test_date_only_target_is_midnight(self):
        from datetime import datetime

        from duration import remaining_until

        now = datetime(2026, 11, 15, 22, 0, 0)
        self.assertEqual(remaining_until("2026-11-16", now), 7200)

    def test_malformed_target_raises(self):
        from duration import remaining_until

        with self.assertRaises(ValueError):
            remaining_until("not-a-date")


if __name__ == "__main__":
    unittest.main()

# countdown-cli

Parse and format durations like 1h30m.

## Usage

```bash
python3 -c "from duration import *; print(parse_duration('1h30m')); print(format_duration(5400))"
python3 -c "from duration import remaining_until; print(remaining_until('2026-11-16T18:00:00'))"
python3 -c "from duration import sum_durations; print(sum_durations(['1h30m', '45s']))"
python3 -c "from duration import format_long; print(format_long(93784))"
python3 -c "from duration import parse_clock; print(parse_clock('01:02:03'))"
```

## Features

- Parse 1h30m, 2m 5s, and 45s durations
- Validation for malformed and oversized components
- Sum duration lists with sum_durations(values)
- Clock output with format_clock(seconds)
- Parse HH:MM:SS clock values with parse_clock(text)
- Long readable output with format_long(seconds)
- Countdown to ISO datetimes with remaining_until(target, now)

## Tests

```bash
python3 -m unittest -q
```

## License

MIT

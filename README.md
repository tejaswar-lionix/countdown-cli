# countdown-cli

Parse and format durations like 1h30m.

## Usage

```bash
python3 -c "from duration import *; print(parse_duration('1h30m')); print(format_duration(5400))"
```

## Features

- Parse 1h30m, 2m 5s, and 45s durations
- Validation for malformed and oversized components
- Clock output with format_clock(seconds)

## Tests

```bash
python3 -m unittest -q
```

## License

MIT

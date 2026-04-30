# Contributing

Contributions are welcome when they improve clarity, safety, portability, or documentation.

## Guidelines

- Keep changes focused and easy to review.
- Do not add functionality intended for unauthorized access or stealth.
- Prefer safe tests that do not execute the PoC path.
- Update the README or changelog when behavior changes.
- Keep examples aligned with the actual file name: `copy-fail.py`.

## Safe Test Command

```bash
python3 -m unittest discover -s tests
```

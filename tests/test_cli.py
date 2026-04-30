import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "copy-fail.py"


class CliTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_help_exits_successfully(self):
        result = self.run_cli("--help")

        self.assertEqual(result.returncode, 0)
        self.assertIn("CVE-2026-31431 Copy Fail PoC", result.stdout)
        self.assertIn("python3 copy-fail.py", result.stdout)

    def test_version_exits_successfully(self):
        result = self.run_cli("--version")

        self.assertEqual(result.returncode, 0)
        self.assertIn("0.1.0", result.stdout)


if __name__ == "__main__":
    unittest.main()

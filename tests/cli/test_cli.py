"""
CLI tests for Talyn (simulate, trace, compile, error handling).
"""
import unittest
import subprocess
import json
import os

class TestCLI(unittest.TestCase):
    def test_simulate_json(self):
        import sys
        env = os.environ.copy()
        # Set PYTHONPATH to project root for subprocess
        env["PYTHONPATH"] = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
        result = subprocess.run(['python', '-m', 'talyn.cli', 'simulate', '--json'], capture_output=True, text=True, env=env)
        self.assertEqual(result.returncode, 0)
        data = json.loads(result.stdout)
        self.assertIn('samples', data)

    def test_trace_graphviz(self):
        env = os.environ.copy()
        env["PYTHONPATH"] = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
        result = subprocess.run(['python', '-m', 'talyn.cli', 'trace', '--dot'], capture_output=True, text=True, env=env)
        self.assertEqual(result.returncode, 0)
        self.assertIn('digraph', result.stdout)

    def test_invalid_input(self):
        env = os.environ.copy()
        env["PYTHONPATH"] = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
        result = subprocess.run(['python', '-m', 'talyn.cli', 'simulate', '--config', 'nonexistent.yaml'], capture_output=True, text=True, env=env)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('error', result.stderr.lower())

if __name__ == "__main__":
    unittest.main()

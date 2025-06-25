## Talyn Testing and Validation Strategy

### Test Categories
- **Unit tests**: Core functions, distributions, and utilities
- **Trace tests**: Validate trace structure, determinism, and correctness
- **CLI tests**: Check command-line interface and output
- **Regression tests**: Compare outputs to gold traces
- **Graph tests**: Validate inference graph construction and optimization

### How to Run Tests
- Unit/regression: `pytest tests/`
- Notebook validation: `pytest --nbval docs/notebooks/tests/`
- CLI: `talyn simulate --test` or via shell scripts
- CI: GitHub Actions or other CI tools (see .github/workflows/)

### Sample Test Outputs
- Pass/fail summary
- Error logs for failed tests
- Output diffs for regression mismatches

### CI Integration Guide
- Configure CI to run all tests on push/PR
- Use `pytest` and `nbval` for notebooks
- Upload coverage and test reports

### Guidelines for Contributing New Test Cases
- Add new tests in `tests/` or `docs/notebooks/tests/`
- Use descriptive names and docstrings
- Include expected outputs or gold traces for regression
- Document new test cases in this file

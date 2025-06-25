# CONTRIBUTING.md

## How to Contribute to Talyn

### Setting Up a Development Environment
- Fork the repository on GitHub
- Clone your fork: `git clone https://github.com/your-username/talyn.git`
- Create a virtual environment: `python -m venv venv && source venv/bin/activate`
- Install dependencies: `pip install -e .[dev]`

### Code Style and Naming Conventions
- Follow PEP8 for Python code
- Use descriptive variable and function names
- Document all public functions and classes with docstrings
- Use type hints where possible

### Where to Write Tests
- Unit tests: `tests/`
- Notebook/validation: `docs/notebooks/tests/`
- Add regression/gold traces as needed

### How to Submit a Pull Request
- Create a new branch for your feature or fix
- Write clear commit messages
- Push to your fork and open a pull request on GitHub
- Reference related issues in your PR description

### Review Process and Communication Rules
- All PRs are reviewed by core maintainers
- Address all review comments before merging
- Be respectful and constructive in all communications
- For major changes, open an issue for discussion before coding

# INSTALL.md

## Requirements
- Python 3.8+
- pip (Python package manager)
- Recommended: virtualenv or conda for isolated environments
- Optional: Docker (for containerized setup)
- System packages: graphviz (for trace visualization), gcc (for some dependencies)

## Installation

### PyPI (Recommended)
```bash
pip install talyn
```

### Local Development
```bash
git clone https://github.com/your-org/talyn.git
cd talyn
pip install -e .
```

### Using setup.py
```bash
python setup.py install
```

### Docker Setup (Optional)
```bash
docker build -t talyn .
docker run -it talyn
```

## CLI Installation and Shell Completion
After installation, the `talyn` CLI should be available in your PATH.

To enable shell completion (bash/zsh):
```bash
talyn --install-completion
```

## Known Installation Issues & Fixes
- **Missing graphviz:**
  - Install with `sudo apt-get install graphviz` (Linux) or `brew install graphviz` (macOS)
- **Permission errors:**
  - Use a virtual environment or run with `--user`
- **Windows path issues:**
  - Ensure Python and Scripts directories are in your PATH
- **C/C++ compiler errors:**
  - Install gcc/g++ (Linux) or build tools for Windows

If you encounter other issues, please open an issue on GitHub or see the FAQ.md.

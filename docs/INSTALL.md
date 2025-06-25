# INSTALL.md

## System Requirements

- **Python:** 3.8 or higher (CPython recommended for performance and compatibility)
- **pip:** Python package manager (ensure latest version)
- **Recommended:**
  - `virtualenv` or `conda` for isolated environments (prevents dependency conflicts)
  - `Docker` for containerized, reproducible deployments (especially for quant/HFT production)
- **System Packages:**
  - `graphviz` (for trace/graph visualization)
  - `gcc` or equivalent C/C++ compiler (for optional extensions)

---

## Installation Steps

### 1. Install via PyPI (Recommended)

```bash
pip install talyn
```
- Installs the latest stable release.
- No external dependencies—pure stdlib Python for maximum portability.

### 2. Local Development Install

```bash
git clone https://github.com/your-org/talyn.git
cd talyn
pip install -e .
```
- Installs in "editable" mode; changes to source code are reflected immediately.
- Recommended for research, prototyping, and contributing to Talyn.

### 3. Using setup.py (Legacy)

```bash
python setup.py install
```
- For legacy workflows or custom packaging needs.

### 4. Docker Setup (Optional, for Quant/HFT Deployments)

```bash
docker build -t talyn .
docker run -it talyn
```
- Provides a fully isolated, reproducible environment—ideal for production, compliance, and CI/CD.
- Customize the Dockerfile for specific hardware, OS, or security requirements.

---

## Environment Management

- **virtualenv:**
  - Create a new environment: `python -m venv venv`
  - Activate: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
- **conda:**
  - Create: `conda create -n talyn python=3.8`
  - Activate: `conda activate talyn`
- **Why use environments?**
  - Prevents package conflicts and ensures reproducibility—essential for quant/HFT workflows.

---

## CLI Installation and Shell Completion

After installation, the `talyn` CLI should be available in your PATH.

To enable shell completion (bash/zsh):

```bash
talyn --install-completion
```

---

## Troubleshooting & Known Issues

- **Missing graphviz:**
  - Linux: `sudo apt-get install graphviz`
  - macOS: `brew install graphviz`
  - Windows: Download from [graphviz.org](https://graphviz.org/download/)
- **Permission errors:**
  - Use a virtual environment or install with `pip install --user talyn`
- **PATH issues (Windows):**
  - Ensure Python and Scripts directories are in your PATH environment variable.
- **C/C++ compiler errors:**
  - Linux: `sudo apt-get install build-essential`
  - Windows: Install [Build Tools for Visual Studio](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- **Reproducibility:**
  - Always set explicit random seeds for deterministic results—critical for audit and compliance in quant/HFT.
- **Support:**
  - Open an issue on GitHub or consult the FAQ for further help.

---

## Best Practices for Quant/HFT Users

- Use Docker or virtual environments for all production deployments.
- Log all environment details (Python version, OS, Talyn commit) for reproducibility.
- For compliance, maintain a requirements.txt or environment.yml with exact versions.

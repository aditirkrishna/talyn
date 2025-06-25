<p align="center">
  <img src="https://raw.githubusercontent.com/aditirkrishna/talyn/main/docs/assets/talyn_logo.png" alt="Talyn Logo" width="180"/>
</p>

<h1 align="center">Talyn</h1>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License"/>
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue.svg" alt="Python 3.7+"/>
  <img src="https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg" alt="Status: Production Ready"/>
  <img src="https://img.shields.io/badge/Platform-Cross--platform-lightgrey.svg" alt="Platform: Cross-platform"/>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/aditirkrishna/talyn/main/docs/assets/probability_icon.png" alt="Probability Icon" width="50"/>
  <img src="https://raw.githubusercontent.com/aditirkrishna/talyn/main/docs/assets/simulation_icon.png" alt="Simulation Icon" width="50"/>
  <img src="https://raw.githubusercontent.com/aditirkrishna/talyn/main/docs/assets/inference_icon.png" alt="Inference Icon" width="50"/>
</p>

---

> **Talyn** is a first-principles simulation kernel for probabilistic modeling and inference, designed for clarity, extensibility, and mathematical rigor.

---

## What is Talyn?

Talyn is a simulation-native probabilistic programming system. It empowers you to define, simulate, and analyze complex probabilistic models using a trace-first, execution-based approach—no abstraction layers or symbolic graphs. Talyn is designed for researchers, educators, and engineers who want full transparency and control over every probabilistic computation.

---

## Key Features

- **Simulation-based inference** (no static graphs, pure execution)
- **Transparent execution traces** for every run
- **Supports**: Monte Carlo, importance sampling, belief propagation, particle filtering, and more
- **Composable, dynamic model definitions** (YAML or Python DSL)
- **CLI and Python API** for flexible workflows
- **Extensible**: add new distributions or inference methods easily
- **Academic-grade testing and validation suite**

---

## Installation & Quick Start

```bash
pip install talyn
# or for local development
pip install -e .
```

Minimal CLI example:
```bash
talyn simulate coin.yaml
```

---

## Project Structure

- `talyn/` — Core library (sampler, trace, inference, etc.)
- `docs/` — Documentation and Jupyter notebooks
- `tests/` — Unit and regression tests
- `examples/` — Example models and scripts

---

## Tutorials & Notebooks

See [NOTEBOOKS.md](NOTEBOOKS.md) for a categorized list of Jupyter notebooks, including tutorials, validation, and benchmarks.

---

## License & Citation

This project is licensed under the [MIT License](LICENSE.md).

For academic use, please cite using the BibTeX entry in [CITATION.md](CITATION.md).

---

<footer align="center">
  <sub><i>built with <span style="color:red">❤️</span> by aditi ramakrishnan</i></sub>
</footer>

# Talyn

A first-principles simulation kernel for probabilistic modeling and inference.

## What is Talyn?
Talyn is a simulation-native probabilistic programming system. It enables users to define, simulate, and analyze complex probabilistic models using a trace-first, execution-based approach—without abstraction layers or symbolic graph construction.

## Key Features
- Simulation-based inference (no static graphs)
- Transparent execution traces for every run
- Supports MC, importance sampling, BP, particle filtering, and more
- Composable, dynamic model definitions (YAML or Python DSL)
- CLI and Python API for flexible workflows
- Extensible: add new distributions or inference methods easily
- Academic-grade testing and validation suite

## Installation & Quick Start
```bash
pip install talyn
# or for local development
python setup.py install
```

Minimal CLI example:
```bash
talyn simulate coin.yaml
```

## Project Structure
- `talyn/` — Core library (sampler, trace, inference, etc.)
- `docs/` — Documentation and Jupyter notebooks
- `tests/` — Unit and regression tests
- `examples/` — Example models and scripts

## Tutorials & Notebooks
See [NOTEBOOKS.md](NOTEBOOKS.md) for a categorized list of Jupyter notebooks, including tutorials, validation, and benchmarks.

## License & Citation
See [LICENSE.md](LICENSE.md) for open-source terms. For academic use, please cite using the BibTeX in [CITATION.md](CITATION.md).

## Screenshot
![Trace Visualization Example](docs/assets/trace_example.png)

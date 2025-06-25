# BENCHMARKS.md

## Talyn Performance Benchmarks: Methodology & Results

This document details the benchmarking methodology, metrics, and results for Talyn’s core probabilistic inference and simulation engines. All experiments are designed for maximal reproducibility and relevance to real-world quantitative research and HFT use cases.

---

### 1. Benchmarking Methodology

- **Models Benchmarked:**
  - **Hidden Markov Model (HMM):** Canonical for state-space and time-series inference; widely used in quant/risk.
  - **Particle Filter:** Sequential Monte Carlo for online estimation—critical in signal processing and trading.
  - **Large Factor Graphs:** Stress-tests Talyn’s graph compilation and inference on high-dimensional, sparse structures.
- **Hardware:**
  - Specify exact CPU model, RAM, and OS for each run (e.g., Intel i7-12700K, 32GB RAM, Ubuntu 22.04).
  - All runs are single-threaded unless otherwise noted.
- **Software:**
  - Python version, Talyn version/commit, and any relevant system libraries.
  - No numpy/scipy: all results are pure stdlib Python for maximal portability and auditability.
- **Reproducibility:**
  - All scripts set explicit random seeds and log all parameters.
  - See `docs/notebooks/tests/09_graph_runtime_benchmarking.ipynb` for full experiment code.

---

### 2. Metrics & Interpretation

- **Runtime (seconds):** Wall-clock time for inference/simulation; measured via `time.perf_counter()`.
- **Memory Usage (MB):** Peak memory during inference, measured with `tracemalloc` or OS utilities.
- **Effective Sample Size (ESS):** For particle filters, measures the quality/diversity of the sample population.
- **Scalability:** How runtime and memory scale with model size (nodes/edges) and sample count.
- **Variance:** Each experiment is repeated ≥5 times; report mean ± stddev.
- **Comparison:** Benchmarked against Pyro and PyMC where possible (see table below).

---

### 3. Runtime Comparison Table

| Model         | Talyn (s) | Pyro (s) | PyMC (s) |
|---------------|-----------|----------|----------|
| HMM (T=100)   |           |          |          |
| Particle Filt |           |          |          |
| Graph (N=100) |           |          |          |

*Note: All results are for single-threaded, pure Python execution. Pyro/PyMC may use numpy/torch backends.*

---

### 4. Particle Filter Performance (Varying N)

- **ESS vs N:** Demonstrates sample degeneracy and resampling efficiency as particle count increases.
- **Runtime vs N:** Shows computational scaling; critical for real-time estimation in trading systems.
- **Interpretation:** In HFT, low-latency online inference is essential—Talyn’s SMC is optimized for this regime.

---

### 5. Graph Inference Scaling Results

- **Inference Time vs Graph Size:** Stress-test Talyn’s DAG/factor graph compilation and message passing.
- **Memory Usage vs Graph Size:** Relevant for large-scale risk models and portfolio inference.
- **Technical Note:** All graphs are sparse; dense graphs may exhibit different scaling.

---

### 6. Memory Usage and Graph Size Stats

| Nodes | Edges | Memory (MB) |
|-------|-------|-------------|
|       |       |             |

---

### 7. Technical Notes & Best Practices

- Always specify hardware/software in results for reproducibility.
- Use fixed seeds and log all parameters.
- For HFT/quant, batch and streaming (online) performance are both relevant—Talyn supports both modes.
- For variance and reliability, repeat each run multiple times and report mean ± stddev.
- For full scripts and raw data, see `docs/notebooks/tests/09_graph_runtime_benchmarking.ipynb`.

---

### 8. References
- [Talyn Architecture](ARCHITECTURE.md)
- [Performance Notebook](../notebooks/tests/09_graph_runtime_benchmarking.ipynb)
- [Pyro](https://pyro.ai/), [PyMC](https://www.pymc.io/)

# BENCHMARKS.md

## Talyn Performance Experiments

### Benchmark Setup
- Models: HMM, particle filter, large factor graphs
- Hardware: CPU model, RAM, OS (specify in each run)
- Software: Python version, Talyn version, dependencies

### Runtime Comparison Tables
| Model         | Talyn (s) | Pyro (s) | PyMC (s) |
|---------------|-----------|----------|----------|
| HMM (T=100)   |           |          |          |
| Particle Filt |           |          |          |
| Graph (N=100) |           |          |          |

### Particle Filter Performance (Varying N)
- Plot: Effective sample size vs N
- Plot: Runtime vs N

### Graph Inference Scaling Results
- Plot: Inference time vs graph size
- Plot: Memory usage vs graph size

### Memory Usage and Graph Size Stats
- Table: Nodes, edges, memory (MB) for each benchmark

### Notes
- All benchmarks should be reproducible (include seeds)
- For full scripts, see docs/notebooks/tests/09_graph_runtime_benchmarking.ipynb

# ARCHITECTURE.md

## Talyn System Design Overview

### Core Components
- **Sampler**: Implements all random variable sampling
- **Trace Engine**: Records execution traces, manages variable scopes
- **Graph Compiler**: Converts traces to inference graphs (DAG/factor graph)
- **Inference Engine**: Runs MC, BP, particle filtering, etc.

### Class/Module Structure Overview
- `talyn/simulation/`: Sampling and simulation logic
- `talyn/trace/`: Trace object and manipulation
- `talyn/inference/`: Inference algorithms
- `talyn/cli.py`: Command-line interface
- `talyn/distributions/`: Primitive and composite distributions

### Data Flow: Input → Execution → Output
1. **Input**: Model file (YAML, Python DSL)
2. **Execution**: Model is simulated, trace is recorded
3. **Output**: Trace, statistics, inference results, graphs

### Simulation Pipeline Diagram
```
Model → [Sampler] → [Trace Engine] → [Graph Compiler] → [Inference Engine] → Output
```

### Extensibility Notes
- Add new distributions by subclassing base sampler
- Add new inference methods by extending inference engine
- Modular design: each component can be swapped or extended

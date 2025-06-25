# INFERENCE.md

## Inference Theory and Implementation in Talyn

### Supported Inference Types
- Monte Carlo (MC) sampling
- Importance sampling
- Belief propagation (BP)
- Particle filtering (sequential Monte Carlo)

### Graph Transformations for Inference
- Model is compiled to an inference graph (DAG or factor graph)
- Variable elimination and message passing for BP
- Trace pruning for efficient inference

### Trace Conditioning Logic
- Observed variables are clamped in the trace
- Conditioning updates the trace and propagates constraints
- Supports both hard and soft evidence

### Inference Graph Compilation
- Model → execution trace → inference graph
- Graph optimizations: pruning, variable reordering, factorization

### Factorization Semantics
- Factors represent conditional dependencies
- Supports unary, pairwise, and higher-order factors
- Factor product and marginalization rules

### Limitations and Assumptions
- Assumes discrete or continuous variables with tractable densities
- Some inference methods may not converge on loopy or highly multimodal graphs
- Dynamic models may require special handling for trace replay

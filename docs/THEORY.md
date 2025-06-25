# THEORY.md

## Mathematical Foundations of Talyn

### Simulation-Based Inference
- Models are defined as generative processes
- Inference is performed by simulating traces and conditioning on observations

### Composition and Randomness
- Random variables are composed via function application and dependency
- Supports both static and dynamic (runtime) composition

### Probabilistic Programming Semantics
- Execution traces represent full model runs
- Each trace is a sample from the joint distribution
- Supports recursion, control flow, and higher-order functions

### Trace Semantics and Graph Representations
- Traces are DAGs of random and deterministic variables
- Graphs are compiled from traces for efficient inference

### Comparison to Other Frameworks
- **Pyro/PyMC**: Graph-based, symbolic, static by default
- **JAX**: Functional, but not simulation-native
- **Talyn**: Trace-first, simulation-native, no abstraction layers

### Justification for Architectural Choices
- Trace-first design enables transparency and debugging
- Simulation-native approach allows dynamic models and full control
- No hidden abstraction layers: what you write is what is executed

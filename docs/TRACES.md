## Talyn Execution Trace Format and Structure

### JSON Trace Format Schema
- Each trace is a JSON object with fields:
  - `nodes`: mapping from variable names to values and metadata
  - `edges`: list of dependencies (parent → child)
  - `rng_state`: (optional) random number generator state

#### Example Trace Object
```json
{
  "nodes": {
    "mu": {"value": 0.5, "type": "latent", "dependencies": [], "scope": "global"},
    "x": {"value": 1.2, "type": "observed", "dependencies": ["mu"], "scope": "global"}
  },
  "edges": [["mu", "x"]],
  "rng_state": 123456
}
```

### Field Explanations
- `value`: Realized value of the variable
- `type`: `latent`, `observed`, or `deterministic`
- `dependencies`: List of parent variables
- `scope`: Variable scope (global, local, etc.)

### Visualizing and Interpreting the DAG
- Each node is a random or deterministic variable
- Edges represent dependencies (data flow)
- Use Graphviz or Talyn's built-in tools to render the trace

### Using Traces in Inference/Optimization
- Traces can be replayed for likelihood evaluation
- Used for gradient estimation, posterior inference, and debugging
- Can be exported for use in other tools or for reproducibility

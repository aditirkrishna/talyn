## Talyn CLI Usage Manual

### Available Commands
- `talyn simulate <model.yaml>`: Run a simulation from a model file
- `talyn trace <model.yaml>`: Output the execution trace for a model
- `talyn compile <model.yaml>`: Compile a model to an inference graph
- `talyn analyze <trace.json>`: Analyze or visualize a trace
- `talyn help`: Show all available commands and options

### Command Examples
```bash
talyn simulate coin.yaml
# Simulate a model and print results

talyn trace coin.yaml --output trace.json
# Save execution trace to file

talyn compile hmm.yaml --output graph.dot
# Compile HMM model to inference graph (DOT format)
```

### Input Formats
- **YAML**: Human-readable model definitions (recommended)
- **JSON**: For programmatic or large models
- **Python DSL**: For advanced users (see MODEL_SPEC.md)

### Output Interpretation
- **Simulation**: Prints or saves samples, statistics, and traces
- **Trace**: JSON object with all random choices and dependencies
- **Compile**: DOT/JSON graph for further analysis or visualization

### Common Workflows
1. Write a model in YAML (see examples/ or MODEL_SPEC.md)
2. Simulate: `talyn simulate mymodel.yaml`
3. Analyze: `talyn trace mymodel.yaml --output trace.json`
4. Visualize: `talyn compile mymodel.yaml --output graph.dot`
5. Use output in downstream analysis or notebooks

# FAQ.md

## Frequently Asked Questions about Talyn

### Why simulation over symbolic definition?
Simulation allows for dynamic, execution-based models that can include control flow, recursion, and data-dependent structure. This enables more flexible and transparent modeling than static, symbolic graphs.

### What’s the difference between traces and graphs?
- **Trace**: A record of one execution of the model, including all random choices and dependencies (a sample path).
- **Graph**: A static or compiled representation of all possible dependencies, used for inference and optimization.

### How is Talyn different from other PPLs?
Talyn is simulation-native and trace-first: models are executed as code, not compiled to a static graph. This enables dynamic models, full transparency, and easier debugging.

### What to do if inference diverges?
- Check model specification for identifiability and well-posedness
- Try different inference algorithms (MC, BP, particle filter)
- Increase sample size or adjust proposal distributions
- Consult the TESTING.md and INFERENCE.md for troubleshooting tips

### CLI or Python — what’s the use case for each?
- **CLI**: For reproducible, scriptable workflows and batch runs
- **Python API**: For interactive development, advanced composition, and integration with other tools

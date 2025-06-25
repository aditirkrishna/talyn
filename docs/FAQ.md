## Frequently Asked Questions — Talyn

### Why does Talyn use simulation (execution-based) rather than symbolic/static graph definitions?

Simulation enables dynamic, code-driven models with arbitrary control flow, recursion, and data-dependent structure. This is essential for representing real-world trading strategies, adaptive risk models, and HFT systems—where the model topology may depend on streaming data or conditional logic. Symbolic/static graphs are limited to fixed topologies and cannot easily express such complexity.

**Technical Note:** Simulation-first design allows for full transparency, step-by-step debugging, and post-hoc audit trails—critical for quant, HFT, and regulated environments.

---

### What’s the difference between a trace and a graph in Talyn?
- **Trace:** A trace is a complete record of a single execution (sample path) of the probabilistic program. It logs every random choice, dependency, and intermediate value. Traces are essential for debugging, reproducibility, and compliance.
- **Graph:** The graph is a static representation (DAG or factor graph) compiled from one or more traces. It encodes all variable dependencies for use in inference algorithms (e.g., belief propagation, variable elimination).

**In Practice:** Traces are used for simulation, audit, and replay; graphs are used for scalable inference and optimization.

---

### How is Talyn different from other probabilistic programming languages (PPLs)?

- **Simulation-Native:** Models are executed as Python code, not compiled to a static graph. This allows for dynamic, data-driven models and easier debugging.
- **No External Dependencies:** Pure stdlib Python—portable, auditable, and easy to deploy in quant/HFT environments.
- **Trace-First Philosophy:** Every run is auditable and reproducible; no "black box" inference.
- **CLI/API Parity:** Everything available in the CLI is also exposed via Python API for research and production integration.

---

### What should I do if inference diverges or results are unstable?

- **Model Specification:** Ensure your model is identifiable and well-posed. Ambiguity or redundancy in model structure can cause divergence.
- **Algorithm Selection:** Try alternative inference algorithms (Monte Carlo, belief propagation, particle filtering). Some methods are better suited for specific model classes.
- **Parameter Tuning:** Increase sample size, adjust proposal distributions, or regularize priors.
- **Diagnostics:** Use trace plots, effective sample size (ESS), and log-likelihood curves to diagnose convergence.
- **Reference Docs:** See `TESTING.md` and `INFERENCE.md` for detailed troubleshooting guides and best practices.

---

### When should I use the CLI vs the Python API?

- **CLI:** Ideal for reproducible, scriptable batch runs, integration with shell pipelines, and production deployment. All runs are logged and can be replayed for audit/compliance.
- **Python API:** Best for interactive development, rapid prototyping, and advanced model composition. Enables integration with research notebooks, custom analytics, and live trading systems.

**Best Practice:** Develop and validate interactively (API), then deploy and audit via CLI for production and compliance.

---

### Additional Troubleshooting & Tips

- **Reproducibility:** Always set explicit random seeds for deterministic results.
- **Performance:** Use batch mode for large-scale inference; streaming mode for online/HFT workloads.
- **Support:** For further questions, open an issue on GitHub or consult the full documentation.

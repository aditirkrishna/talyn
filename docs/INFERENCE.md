## Inference Theory and Implementation in Talyn

This document provides a rigorous overview of inference algorithms, graph transformations, and conditioning logic as implemented in Talyn. All methods are designed for mathematical transparency, auditability, and extensibility, with special attention to quant/HFT applications.

---

### 1. Inference Types Supported

- **Monte Carlo (MC) Sampling:**
  - Draws independent samples from the model to estimate expectations and probabilities.
  - Used for risk estimation, option pricing, and scenario analysis in quant finance.
- **Importance Sampling:**
  - Samples from a proposal distribution and reweights to estimate expectations under the target.
  - Useful for rare event estimation and stress-testing.
- **Belief Propagation (BP):**
  - Message-passing on factor graphs; computes marginal distributions efficiently for tree-structured or sparse models.
  - Enables scalable inference in large portfolio or network models.
- **Particle Filtering (Sequential Monte Carlo):**
  - Online inference for state-space models (e.g., HMMs, regime-switching models).
  - Critical for real-time estimation and adaptive trading strategies.

---

### 2. Mathematical Background: Graph Transformations

- **Model → Trace → Graph:**
  - Probabilistic program is executed to produce a trace (sample path).
  - Trace is compiled into a directed acyclic graph (DAG) or factor graph, encoding all variable dependencies.
- **Variable Elimination:**
  - Systematic marginalization of variables for exact inference (when tractable).
- **Message Passing:**
  - BP and related algorithms propagate local messages (beliefs) to compute marginals or MAP estimates.
- **Trace Pruning:**
  - Unused or irrelevant branches are pruned for efficiency; essential for large-scale or real-time inference.

---

### 3. Conditioning and Evidence

- **Clamping Observed Variables:**
  - Observed data is clamped in the trace, and all downstream dependencies are updated.
- **Hard vs Soft Evidence:**
  - Hard: Variable is fixed to an observed value.
  - Soft: Likelihood weighting or virtual evidence is used for partial/incomplete observations.
- **Constraint Propagation:**
  - Conditioning propagates through the graph, updating all dependent variables and factors.

---

### 4. Factorization Semantics

- **Factors:** Represent conditional dependencies between variables (unary, pairwise, higher-order).
- **Product Rule:** Joint probability is factorized as a product of factors (e.g., $P(x, y, z) = f_1(x, y) f_2(y, z)$).
- **Marginalization:** Sums/integrates out variables to compute marginals or conditional probabilities.
- **Graphical Structure:** Factor graphs provide a flexible and efficient representation for both discrete and continuous models.

---

### 5. Limitations and Assumptions

- **Tractability:** Exact inference is only feasible for models with limited treewidth or structure; otherwise, approximate methods are used.
- **Convergence:** Some algorithms (e.g., loopy BP, MCMC) may not converge or may mix slowly on highly multimodal or loopy graphs.
- **Dynamic Models:** Special care is needed for models with changing topology or data-dependent structure (common in HFT/quant).
- **Numerical Stability:** All computations are implemented to minimize underflow/overflow, but extreme probabilities should be handled with care.

---

### 6. Practical Tips for Quant/HFT Applications

- **Batch vs Online:** Use MC/BP for batch risk or scenario analysis; use particle filtering for real-time estimation.
- **Diagnostics:** Always monitor effective sample size (ESS), log-likelihood, and trace plots for convergence and stability.
- **Auditability:** All inference runs are fully traceable and reproducible—critical for regulatory compliance.
- **Extensibility:** New inference algorithms can be integrated by subclassing and registering with the inference engine.

---

### 7. References
- Koller & Friedman, *Probabilistic Graphical Models*
- Murphy, *Machine Learning: A Probabilistic Perspective*
- [Talyn Architecture](ARCHITECTURE.md)
- [Testing & Validation](TESTING.md)

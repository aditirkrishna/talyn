# MODEL_SPEC.md

## Talyn Modeling Language Specification

### Syntax Reference
- Models are defined in YAML (or Python DSL)
- Each variable is assigned a distribution or deterministic function
- Dependencies are explicit via variable references

#### Example
```yaml
model:
  mu: Normal(0, 1)
  x: Normal(mu, 1)
simulate: x
```

### Supported Distributions & Assignments
- Bernoulli, Uniform, Normal, Beta, Exponential, etc.
- Nested assignments: variables can depend on other variables
- Deterministic assignments: `z: mu + 1`

### Dynamic vs Static Models
- **Dynamic**: Model structure can change at runtime (e.g., control flow, recursion)
- **Static**: Fixed structure, all dependencies known at parse time

### Randomness Scoping & Reuse
- Each random variable is uniquely identified in the trace
- Reusing variable names in different scopes is supported (see hierarchical models)

### Compositional Operators
- `+`, `-`, `*`, `/`, `sin`, `exp`, etc. (Pythonic syntax)
- Map, apply, bind for higher-order composition

### Reserved Keywords & Internal Variables
- `model`, `simulate`, `observe`, `trace`, `compile`
- Internal: `_rng_state`, `_trace_id`, etc.

"""
Talyn decision: Value iteration algorithm for MDPs.
"""
from typing import Dict, Any, Tuple
from .mdp import MDP, State, Action

def value_iteration(mdp: MDP, theta: float = 1e-6) -> Dict[State, float]:
    """
    Perform value iteration to compute optimal state-value function.
    Args:
        mdp: Finite MDP instance
        theta: Convergence threshold
    Returns:
        Dictionary mapping state -> optimal value V*
    """
    V: Dict[State, float] = {s: 0.0 for s in mdp.states}
    while True:
        delta = 0.0
        for s in mdp.states:
            v_old = V[s]
            action_values = []
            for a in mdp.actions[s]:
                q_sa = 0.0
                for s_prime, p in mdp.P[(s, a)]:
                    r = mdp.R.get((s, a, s_prime), 0.0)
                    q_sa += p * (r + mdp.gamma * V[s_prime])
                action_values.append(q_sa)
            V[s] = max(action_values) if action_values else 0.0
            delta = max(delta, abs(v_old - V[s]))
        if delta < theta:
            break
    return V

def extract_policy(mdp: MDP, V: Dict[State, float]) -> Dict[State, Action]:
    """Derive greedy policy π* from optimal value function V*."""
    policy: Dict[State, Action] = {}
    for s in mdp.states:
        best_a = None
        best_q = -float('inf')
        for a in mdp.actions[s]:
            q_sa = 0.0
            for s_prime, p in mdp.P[(s, a)]:
                r = mdp.R.get((s, a, s_prime), 0.0)
                q_sa += p * (r + mdp.gamma * V[s_prime])
            if q_sa > best_q:
                best_q = q_sa
                best_a = a
        policy[s] = best_a
    return policy

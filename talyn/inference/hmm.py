"""
Talyn inference: Hidden Markov Model algorithms (forward, viterbi).
"""
from typing import List, Tuple
import math

def forward_algorithm(
    observations: List[int],
    transition: List[List[float]],
    emission: List[List[float]],
    initial: List[float]
) -> float:
    """
    Compute likelihood P(observations) using forward algorithm.
    Assumes discrete emissions indexed as integers.
    """
    n_states = len(initial)
    alpha = [initial[i] * emission[i][observations[0]] for i in range(n_states)]
    for obs in observations[1:]:
        next_alpha = [0.0]*n_states
        for j in range(n_states):
            s = 0.0
            for i in range(n_states):
                s += alpha[i]*transition[i][j]
            next_alpha[j] = s*emission[j][obs]
        alpha = next_alpha
    return sum(alpha)

def viterbi(
    observations: List[int],
    transition: List[List[float]],
    emission: List[List[float]],
    initial: List[float]
) -> Tuple[List[int], float]:
    """
    Most probable hidden state sequence (Viterbi).
    Returns (state_sequence, log_prob)
    """
    n_states = len(initial)
    delta = [math.log(initial[i])+math.log(emission[i][observations[0]]) for i in range(n_states)]
    psi = [[0]*n_states]
    for obs in observations[1:]:
        next_delta = []
        back = []
        for j in range(n_states):
            probs = [delta[i]+math.log(transition[i][j]) for i in range(n_states)]
            best_i = max(range(n_states), key=lambda i: probs[i])
            next_delta.append(probs[best_i]+math.log(emission[j][obs]))
            back.append(best_i)
        delta = next_delta
        psi.append(back)
    # backtrace
    T = len(observations)
    last_state = max(range(n_states), key=lambda i: delta[i])
    states = [last_state]
    for t in range(T-2,-1,-1):
        last_state = psi[t+1][last_state]
        states.append(last_state)
    states.reverse()
    return states, max(delta)

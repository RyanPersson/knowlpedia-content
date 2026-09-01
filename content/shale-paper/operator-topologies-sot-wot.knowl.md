+++
id = "shale-paper/operator-topologies-sot-wot"
title = "Strong vs Weak Operator Topology"
kind = "knowl"
summary = "The strong and weak operator topologies on the bounded operators of a Hilbert space."
aliases = ["operator-topologies-sot-wot", "Strong vs Weak Operator Topology"]
domains = ["shale-paper"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "shale-paper/operator-topologies-sot-wot.md"
+++

Let \(H\) be a Hilbert space and \(B(H)\) its bounded linear operators. A net \((T_i)\) in \(B(H)\) converges to \(T\in B(H)\):

- in the **strong operator topology (SOT)** if \(\lVert T_i x-Tx\rVert\to0\) for every \(x\in H\);
- in the **weak operator topology (WOT)** if \(\langle T_i x,y\rangle\to\langle Tx,y\rangle\) for every \(x,y\in H\).

## Remarks

SOT convergence implies WOT convergence. Neither implication reverses to operator-norm convergence in general.

## Examples

- If \(\lVert T_i-T\rVert\to0\) in operator norm, then \(T_i\to T\) in both SOT and WOT.

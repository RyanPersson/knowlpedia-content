+++
id = "shale-paper/operator-topologies-sot-wot"
title = "Strong vs Weak Operator Topology"
kind = "knowl"
summary = "The strong and weak operator topologies on the bounded operators of a Hilbert space."
aliases = ["operator-topologies-sot-wot", "Strong vs Weak Operator Topology"]
domains = ["shale-paper"]
legacy_source_path = "shale-paper/operator-topologies-sot-wot.md"
prerequisites = ["linear-algebra/hilbert-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(H\) be a [[linear-algebra/hilbert-space|Hilbert space]] and \(B(H)\) its bounded [[linear-algebra/linear-operator|linear operators]]. A net \((T_i)\) in \(B(H)\) converges to \(T\in B(H)\):

- in the **[[operator-algebras/strong-operator-topology|strong operator topology]] (SOT)** if \(\lVert T_i x-Tx\rVert\to0\) for every \(x\in H\);
- in the **[[operator-algebras/weak-operator-topology|weak operator topology]] (WOT)** if \(\langle T_i x,y\rangle\to\langle Tx,y\rangle\) for every \(x,y\in H\).

## Remarks

SOT convergence implies WOT convergence. Neither implication reverses to [[linear-algebra/operator-norm|operator-norm]] convergence in general.

## Examples

- If \(\lVert T_i-T\rVert\to0\) in [[linear-algebra/operator-norm|operator norm]], then \(T_i\to T\) in both SOT and WOT.

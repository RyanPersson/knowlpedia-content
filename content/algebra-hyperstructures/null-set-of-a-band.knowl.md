+++
id = "algebra-hyperstructures/null-set-of-a-band"
title = "Nullset of a band"
kind = "definition"
summary = "The ideal of formal sums declared null in a band."
aliases = ["null set of a band", "band nullset", "band null set"]
domains = ["algebra-hyperstructures"]
section_mode = "progressive"
prerequisites = ["algebra-hyperstructures/band"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

For a [[algebra-hyperstructures/band|band]] \(B\), its **nullset** is the
distinguished ideal
\[
N_B\subseteq B^+=\mathbb N[B]/\langle0\rangle.
\]
Thus the empty sum lies in \(N_B\), and
\[
\alpha,\beta\in N_B,\quad \gamma\in B^+
\quad\Longrightarrow\quad
\alpha+\beta\in N_B,\qquad \gamma\alpha\in N_B.
\]
Membership \(\sum a_i\in N_B\) means that the formal sum \(\sum a_i\) is
declared **null**.

The band axiom additionally requires each \(a\in B\) to have a unique
\(-a\in B\) with \(a+(-a)\in N_B\). Ideal closure alone does not imply the
[[algebra-hyperstructures/fusion-rule-for-bands|fusion rule]].

## Terminology

The band literature uses the single word **nullset** for \(N_B\). This is not
the same as a null ideal used to form a quotient of a band: the nullset is
part of the band itself.

## References
Matthew Baker, Tong Jin, and Oliver Lorscheid,
[*New building blocks for \(\mathbb F_1\)-geometry: bands and band schemes*, Definition 1.1](https://arxiv.org/abs/2402.09612).

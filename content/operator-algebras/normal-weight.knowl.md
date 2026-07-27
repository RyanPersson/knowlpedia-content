+++
id = "operator-algebras/normal-weight"
title = "Normal weight"
kind = "definition"
summary = "A weight on a von Neumann algebra that preserves suprema of increasing positive nets."
aliases = ["order-continuous weight", "ultraweakly lower-semicontinuous weight"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]]
and let
\(\varphi:M_+\to[0,+\infty]\) be a
[[operator-algebras/weight-on-von-neumann-algebra|weight]]. The weight
\(\varphi\) is **normal** if, for every increasing net
\((x_i)\) in \(M_+\) having supremum \(x\in M_+\),
\[
\varphi(x)=\sup_i\varphi(x_i).
\]
This is order [[measure-theory/continuity-from-below-measure|continuity from below]] and includes nets, not only sequences.
When \(\varphi\) is finite everywhere, its linear extension is normal exactly
when it is a [[operator-algebras/normal-functional|normal functional]].
Normality imposes no faithfulness or semifiniteness, and it does not mean norm
continuity: every finite
[[operator-algebras/positive-linear-functional|positive functional]] is
norm-continuous, whereas only some are ultraweakly continuous.

## Lower semicontinuity

A weight on \(M\) is normal exactly when it is lower semicontinuous on \(M_+\)
for the [[operator-algebras/ultraweak-topology|ultraweak topology]]: if
\(x_i\to x\) ultraweakly, then
\[
\varphi(x)\leq\liminf_i\varphi(x_i).
\]
Equivalently, every sublevel set
\(\{x\in M_+:\varphi(x)\leq c\}\) is ultraweakly closed. This equivalence is
specific to the von Neumann algebra setting and its order-complete positive
cone [Takesaki, vol. I, Chapter VII, §1](https://doi.org/10.1007/978-1-4612-6188-9).

## Tests and consequences

Normality implies complete additivity on arbitrary orthogonal families of
positive elements, with sums interpreted as suprema of finite [[real-analysis/partial-sums|partial sums]].
Testing only increasing sequences is insufficient on a general von Neumann
algebra; sequential tests become adequate only under additional countability
or \(\sigma\)-finiteness hypotheses. The net formulation in the core avoids
silently imposing such hypotheses.

## Examples and distinctions

The canonical trace on \(B(H)\) is normal even when \(H\) is nonseparable: an
increasing net of positive operators has traces increasing to the trace of its
supremum. Every vector functional is normal. Singular states on
\(B(H)\), when they exist, are bounded positive functionals but are not
normal; regarded as finite weights, they fail the increasing-net condition.
Thus finiteness and norm continuity do not substitute for normality.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter III, §2 and Chapter VII, §1 on normal functionals and normal weights.
2. Masamichi Takesaki, *Theory of Operator Algebras II*, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-662-10451-4). Relevant: the opening chapters on normal weights and modular theory.

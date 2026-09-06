+++
id = "operator-algebras/normal-semifinite-faithful-weight"
title = "Normal semifinite faithful weight"
kind = "definition"
summary = "A weight on a von Neumann algebra that is simultaneously normal, semifinite, and faithful."
aliases = ["n.s.f. weight", "f.n.s. weight", "faithful normal semifinite weight"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/weight-on-von-neumann-algebra", "operator-algebras/normal-weight", "operator-algebras/semifinite-weight", "operator-algebras/faithful-weight"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]]. A
[[operator-algebras/weight-on-von-neumann-algebra|weight]]
\(\varphi:M_+\to[0,\infty]\) is a **normal semifinite faithful weight**, or
**n.s.f. weight**, if all three conditions hold: it is
[[operator-algebras/normal-weight|normal]], so it preserves suprema of
increasing nets in \(M_+\); [[operator-algebras/semifinite-weight|semifinite]],
so its finite part is order-dense in \(M_+\); and
[[operator-algebras/faithful-weight|faithful]], so
\(\varphi(x)=0\) for \(x\in M_+\) implies \(x=0\). A weight may take the value
\(\infty\), so an n.s.f. weight need not be a bounded functional or a state.

## The three conditions

Normality requires
\(\varphi(\sup_i x_i)=\sup_i\varphi(x_i)\) for every increasing net in
\(M_+\). Semifiniteness means
\[
\varphi(x)=\sup\{\varphi(y):0\leq y\leq x,\ \varphi(y)<\infty\}
\qquad(x\in M_+).
\]
Faithfulness excludes nonzero positive elements of weight zero. Each
condition is independent and must be checked separately; the conjunction is
the standard one used in modular theory.

## Examples

The ordinary [[operator-algebras/operator-trace|trace]] on \(B(H)\), allowed
to take the value \(\infty\), is normal, semifinite, and faithful. On a
[[operator-algebras/commutative-von-neumann-algebra|commutative von Neumann algebra]] \(L^\infty(X,\mu)\), integration against a
faithful semifinite measure gives an n.s.f. weight. A faithful
[[operator-algebras/normal-state|normal state]] is an n.s.f. weight whose value
at the identity is one, hence is finite everywhere; the general weight notion
allows substantially more algebras.

## Role and terminology

N.s.f. weights supply the Hilbert-space construction and modular objects used
in Tomita–Takesaki theory when no
[[operator-algebras/faithful-normal-state|faithful normal state]] is available.
Some authors order the adjectives as “faithful normal semifinite” and
abbreviate this as f.n.s.; this denotes the same three properties, not a
different kind of weight. The order of the adjectives carries no mathematical
content.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras II*, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-662-10451-4). Relevant: Chapter VII, §1 on normal, semifinite, faithful weights, and Chapter VIII on modular automorphism groups.

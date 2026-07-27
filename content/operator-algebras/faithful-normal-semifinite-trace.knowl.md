+++
id = "operator-algebras/faithful-normal-semifinite-trace"
title = "Faithful normal semifinite trace"
kind = "definition"
summary = "A tracial weight on a von Neumann algebra that is faithful, normal, and semifinite."
aliases = ["f.n.s. trace", "semifinite faithful normal trace"]
domains = ["operator-algebras", "noncommutative-geometry"]
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]].
A **faithful normal semifinite trace**, or **f.n.s. trace**, is a
[[operator-algebras/tracial-weight|tracial weight]]
\(\tau:M_+\to[0,+\infty]\) that is simultaneously normal, semifinite, and
faithful: it preserves suprema of increasing positive nets; every positive
element is the supremum of positive subelements having finite trace; and
\(\tau(x)=0\) for \(x\in M_+\) implies \(x=0\). Equivalently, it is a
[[operator-algebras/normal-semifinite-faithful-weight|normal semifinite
[[operator-algebras/faithful-weight|faithful weight]]]] satisfying \(\tau(x^*x)=\tau(xx^*)\) for every \(x\in M\).

## Finite-trace approximation

Semifiniteness supplies enough finite-trace elements for analysis even when
\(\tau(1)=+\infty\). In particular, finite-trace projections can approximate
the identity in the
[[operator-algebras/strong-operator-topology|strong operator topology]], and
they generate the relative
compact ideal used in semifinite Fredholm theory. Normality ensures that the
trace of an increasing approximation converges to the trace of its supremum;
faithfulness ensures that trace zero detects the zero positive element
[Takesaki, Chapter V](https://doi.org/10.1007/978-1-4612-6188-9).

## Examples and structural role

The canonical [[operator-algebras/operator-trace|operator trace]] on \(B(H)\)
is an f.n.s. trace, although it is finite only when \(H\) is
finite-dimensional. On \(L^\infty(X,\mu)\),
integration against a faithful semifinite measure gives an f.n.s. trace. A
type \(\mathrm{II}_\infty\) factor has an f.n.s. trace unique up to positive
scalar multiplication.

A von Neumann algebra is
[[operator-algebras/semifinite-von-neumann-algebra|semifinite]] exactly when it
admits an f.n.s. trace. Type III algebras admit [[operator-algebras/normal-semifinite-faithful-weight|n.s.f. weights]] but no f.n.s.
trace; traciality is the decisive extra property
[Takesaki, Chapter V](https://doi.org/10.1007/978-1-4612-6188-9).

## Conventions and scope

The order of the adjectives varies: “normal faithful semifinite” and
“faithful normal semifinite” describe the same conjunction. Semifiniteness
does not mean \(\tau(1)<\infty\), and an f.n.s. trace should not be confused
with the finite-dimensional matrix trace. Some sources build semifiniteness
from density of the finite left ideal rather than order approximation; for a
[[operator-algebras/normal-weight|normal weight]] on a von Neumann algebra
these formulations agree.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V on traces and semifinite von Neumann algebras.
2. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, AMS, 1997. [AMS record](https://bookstore.ams.org/GSM-16). Relevant: §7.2 on normal semifinite traces.

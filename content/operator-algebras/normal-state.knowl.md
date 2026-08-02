+++
id = "operator-algebras/normal-state"
title = "Normal state"
kind = "definition"
summary = "A state on a von Neumann algebra that belongs to its predual."
aliases = ["sigma-weakly continuous state"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]]. A
[[operator-algebras/state-cstar-algebra|state]] \(\varphi:M\to\mathbb C\) is
**normal** if it is a [[operator-algebras/normal-functional|normal
functional]], equivalently if \(\varphi\) is a positive norm-one element of the
[[operator-algebras/predual|predual]] \(M_*\). For a
[[operator-algebras/positive-linear-functional|positive functional]] this
means that whenever an increasing bounded net \((x_i)\) in \(M_+\) has
supremum \(x\),
\[
\varphi(x)=\sup_i\varphi(x_i).
\]
Normality is therefore an order-continuity, or equivalently ultraweak
continuity, requirement. It does not assert that \(\varphi\) is faithful or
pure.

## Equivalent characterizations

For a positive linear functional on \(M\), membership in \(M_*\), ultraweak
continuity, and preservation of suprema of bounded increasing nets in \(M_+\)
are equivalent. Normality can also be characterized by complete additivity on
orthogonal families of projections. These equivalences are part of the
standard predual theory of von Neumann algebras.

## Concrete form on \(B(H)\)

Every normal state on \(B(H)\) is represented by a positive trace-class
operator \(\rho\) with \(\operatorname{Tr}(\rho)=1\):
\[
\varphi(x)=\operatorname{Tr}(\rho x).
\]
Conversely, every such [[quantum-foundations/density-operator|density
operator]] defines a normal state.
[[operator-algebras/vector-state|Vector states]]
\(x\mapsto\langle x\xi,\xi\rangle\), with \(\|\xi\|=1\), correspond to
rank-one [[quantum-foundations/density-operator|density operators]] and are normal.

## Distinctions

**Warning.** Normality depends on the von Neumann algebra structure, not merely
on the underlying \(C^*\)-algebra. A state on a von Neumann algebra may be
singular and hence nonnormal. Faithfulness instead requires
\(\varphi(x)>0\) for every nonzero \(x\in M_+\); purity means extremality in the
state space. These three properties are logically distinct.

## References

1. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, AMS, 1997. [DOI record](https://doi.org/10.1090/gsm/016). Relevant: §7.1 on normal functionals and states.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter III, §2 on the predual and normal functionals.

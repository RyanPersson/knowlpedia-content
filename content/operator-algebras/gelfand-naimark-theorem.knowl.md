+++
id = "operator-algebras/gelfand-naimark-theorem"
title = "Gelfand–Naimark theorem"
kind = "theorem"
summary = "Every abstract C*-algebra has a faithful concrete representation by bounded Hilbert-space operators."
aliases = ["abstract C*-algebras are operator algebras", "faithful representation theorem"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/faithful-cstar-representation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Gelfand–Naimark theorem.** For every abstract complex
[[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(A\), there are a Hilbert
space \(H\) and a
[[operator-algebras/faithful-cstar-representation|faithful representation]]
\[
\pi:A\longrightarrow\mathcal B(H).
\]
The map \(\pi\) is automatically isometric, so its image is a norm-closed
\(*\)-subalgebra of \(\mathcal B(H)\). It may be chosen nondegenerate; when
\(A\) is unital, it may be chosen unital. Thus the abstract axioms for a
\(C^*\)-algebra describe exactly the algebras that can be realized concretely
as norm-closed operator algebras closed under adjoints.

## GNS proof architecture

For each [[operator-algebras/state-cstar-algebra|state]] of \(A\), the
[[operator-algebras/gns-construction|GNS construction]] produces a cyclic
representation. Taking their
[[operator-algebras/universal-representation|universal direct sum]] gives a
representation \(\pi_u\). Since [[operator-algebras/states-separate-positive-elements|states separate positive elements]],
\(\pi_u(a)\neq0\) whenever \(a\neq0\), hence \(\pi_u\) is faithful. The
\(C^*\)-identity then makes every injective \(*\)-homomorphism isometric.

## Consequences and scope

The theorem justifies moving freely between abstract and concrete
\(C^*\)-algebras. It does not say that a representation is unique: one algebra
usually has many inequivalent faithful representations on different Hilbert
spaces. The commutative [[operator-algebras/gelfand-duality|Gelfand representation theorem]], which realizes a
commutative \(C^*\)-algebra as functions on its spectrum, is a stronger
specialized statement and should not be conflated with this operator
representation theorem.

## Historical formulation

One standard proof combines
[[operator-algebras/positive-linear-functional|positive functionals]] with
the GNS construction.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: Theorem 3.4.1 and its GNS proof.
2. I. Gelfand and M. Neumark, “On the imbedding of normed rings into the ring of operators in Hilbert space,” *Matematicheskii Sbornik* 12(54), no. 2 (1943), 197–217. [Stable journal record](https://www.mathnet.ru/eng/sm6155). Relevant: the original faithful-representation theorem.

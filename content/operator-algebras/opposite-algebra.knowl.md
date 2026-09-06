+++
id = "operator-algebras/opposite-algebra"
title = "Opposite algebra"
kind = "definition"
summary = "The C*-algebra obtained by reversing multiplication while retaining the norm and involution."
aliases = ["opposite C*-algebra", "A-opposite"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/cstar-algebra", "linear-algebra/vector-space", "algebra-rings/opposite-ring", "algebra-modules/algebra-homomorphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A\) be a complex
[[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. Its **opposite algebra**
\(A^{\mathrm{op}}\) has the same complex [[linear-algebra/vector-space|vector space]], norm, and involution as
\(A\), but multiplication
\[
a^{\mathrm{op}}b^{\mathrm{op}}=(ba)^{\mathrm{op}}.
\]
Thus \((a^{\mathrm{op}})^*=(a^*)^{\mathrm{op}}\) and
\(\|a^{\mathrm{op}}\|=\|a\|\). These operations satisfy the
\(C^*\)-identity, so \(A^{\mathrm{op}}\) is again a \(C^*\)-algebra. This is
the normed involutive refinement of the
[[algebra-rings/opposite-ring|opposite ring]] construction. The canonical map
\(a\mapsto a^{\mathrm{op}}\) reverses products; it is not generally an
[[algebra-modules/algebra-homomorphism|algebra homomorphism]] \(A\to A^{\mathrm{op}}\).

## Modules and representations

A right action of \(A\) is equivalently a left action of
\(A^{\mathrm{op}}\): writing \(\xi a\) as
\(\rho(a^{\mathrm{op}})\xi\) converts
\((\xi a)b=\xi(ab)\) into the homomorphism law for \(\rho\). This is why
bimodules are represented by commuting left actions of \(A\) and
\(A^{\mathrm{op}}\). If \(A\) is commutative, the canonical product-reversing
map is an isomorphism because reversing multiplication changes nothing.

## Real spectral-triple convention

For a [[noncommutative-geometry/real-spectral-triple|real spectral triple]] with representation \(\pi\) and antiunitary real
structure \(J\), the standard right representation is
\[
\pi^{\mathrm{op}}(b^{\mathrm{op}})=J\pi(b^*)J^{-1}.
\]
The involution inside this formula makes \(\pi^{\mathrm{op}}\) complex-linear
under the usual antiunitary convention. The order-zero condition requires
\([\pi(a),\pi^{\mathrm{op}}(b^{\mathrm{op}})]=0\). The first-order condition
additionally requires
\(\bigl[\, [D,\pi(a)],\pi^{\mathrm{op}}(b^{\mathrm{op}})\,\bigr]=0\), where the inner
commutator uses its
[[functional-analysis/bounded-commutator|bounded extension]]. These are the
standard bimodule conventions for a real spectral triple.

## Examples and cautions

For matrix algebras, transposition gives a complex-linear
\(*\)-isomorphism \(M_n(\mathbb C)^{\mathrm{op}}\cong M_n(\mathbb C)\).
More generally, a \(C^*\)-algebra may be isomorphic to its opposite without a
preferred isomorphism, and such an isomorphism is extra structure. The
notations \(a^{\mathrm{op}}\), \(a^\circ\), and \(a^0\) vary across the
literature; the last two often denote the represented right action rather
than the abstract element itself.

## References

1. Alain Connes, “Noncommutative Geometry and Reality,” *Journal of Mathematical Physics* 36 (1995), 6194–6231. [DOI record](https://doi.org/10.1063/1.531241). Relevant: §2 on the opposite-algebra representation and order conditions.
2. Alain Connes and Matilde Marcolli, *Noncommutative Geometry, Quantum Fields and Motives*, American Mathematical Society, 2008. [DOI record](https://doi.org/10.1090/coll/055). Relevant: Chapter 1 on real spectral triples and bimodule conventions.

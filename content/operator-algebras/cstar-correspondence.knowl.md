+++
id = "operator-algebras/cstar-correspondence"
title = "C*-correspondence"
kind = "definition"
summary = "A right Hilbert C*-module equipped with a nondegenerate left action by adjointable operators."
aliases = ["C*-correspondence from A to B", "Hilbert C*-bimodule", "C*-module correspondence"]
domains = ["operator-algebras", "algebra-modules"]
prerequisites = ["operator-algebras/hilbert-cstar-module", "operator-algebras/nondegenerate-star-homomorphism", "algebra-modules/bimodule", "operator-algebras/adjointable-operator-hilbert-module"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(A\) and \(B\) be \(C^*\)-algebras. A **\(C^*\)-correspondence from
\(A\) to \(B\)** is a right
[[operator-algebras/hilbert-cstar-module|Hilbert \(B\)-module]] \(E\) together
with a
[[operator-algebras/nondegenerate-star-homomorphism|nondegenerate \(*\)-homomorphism]]
\[
\varphi:A\longrightarrow\mathcal L_B(E)
\]
into its adjointable operators. Writing \(a\cdot\xi=\varphi(a)\xi\) makes
\(E\) an [[algebra-modules/bimodule|\((A,B)\)-bimodule]], with compatibility
\(\langle a\cdot\xi,\eta\rangle_B=\langle\xi,a^*\cdot\eta\rangle_B\).
Nondegeneracy means that the closed span of \(\varphi(A)E\) is \(E\). Some
authors allow degenerate left actions, so that convention must be stated when
comparing sources.
The left action is by bounded [[operator-algebras/adjointable-operator-hilbert-module|adjointable module maps]], not arbitrary linear
endomorphisms.

## Morphisms and composition

The direction “from \(A\) to \(B\)” records the left \(A\)-action and right
\(B\)-valued inner product. A correspondence from \(A\) to \(B\) and one from
\(B\) to \(C\) compose by the [[operator-algebras/internal-tensor-product-correspondences|interior tensor product]] over \(B\). The identity
correspondence on \(A\) is \(A\) itself, with multiplication actions and
inner product \(\langle a,b\rangle_A=a^*b\).

## Compact left actions

The left action need not be injective and need not take values in
\(\mathcal K_B(E)\). Requiring
\(\varphi(A)\subseteq\mathcal K_B(E)\) is an additional compactness
hypothesis. The kernel of \(\varphi\) and the ideal on which the left action
is compact play central roles in Cuntz–Pimsner covariance.

## Distinction from imprimitivity bimodules

A correspondence is not automatically a Morita equivalence. An imprimitivity
bimodule has a compatible full left \(A\)-valued inner product and identifies
\(A\) with \(\mathcal K_B(E)\) through its left action; fullness on the right
is also required. Ordinary correspondences may fail every one of these extra
conditions.

## References

1. E. Christopher Lance, *Hilbert C*-Modules: A Toolkit for Operator Algebraists*, Cambridge University Press, 1995. [Publisher record](https://doi.org/10.1017/CBO9780511526206). Relevant: Chapter 4 on tensor products and correspondences.
2. Takeshi Katsura, “On C*-algebras associated with C*-correspondences,” *Journal of Functional Analysis* 217 (2004), 366–401. [DOI record](https://doi.org/10.1016/j.jfa.2004.03.010). Relevant: §1 on correspondences and their left actions.

+++
id = "harmonic-analysis/bernstein-decomposition"
title = "Bernstein decomposition"
kind = "theorem"
summary = "The category of smooth representations of a reductive p-adic group decomposes into blocks indexed by inertial supercuspidal support."
aliases = ["Bernstein block decomposition", "Bernstein components", "Bernstein blocks"]
domains = ["harmonic-analysis", "langlands", "algebra-representation-theory"]
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "algebra-fields-galois/nonarchimedean-local-field", "algebraic-geometry-foundations/levi-subgroup", "harmonic-analysis/supercuspidal-representation", "algebra-representation-theory/character", "harmonic-analysis/smooth-representation-totally-disconnected-group", "algebra-category-theory/full-subcategory"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]]
over a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]] \(F\).
A **cuspidal pair** is a pair \((M,\sigma)\) consisting of a
[[algebraic-geometry-foundations/levi-subgroup|Levi subgroup]] and an
irreducible [[harmonic-analysis/supercuspidal-representation|supercuspidal
representation]] of \(M(F)\).  Two such pairs are **inertially equivalent** if
they become \(G(F)\)-conjugate after twisting \(\sigma\) by an unramified
[[algebra-representation-theory/character|character]] of \(M(F)\).

The **Bernstein decomposition** is the product decomposition

\[
\operatorname{Rep}(G(F))
\simeq\prod_{\mathfrak s}\operatorname{Rep}^{\mathfrak s}(G(F))
\]

of the category of
[[harmonic-analysis/smooth-representation-totally-disconnected-group|smooth
complex representations]] into
[[algebra-category-theory/full-subcategory|full subcategories]]
indexed by inertial classes \(\mathfrak s=[M,\sigma]_G\).  An irreducible
representation belongs to the block \(\mathfrak s\) exactly when its
supercuspidal support has inertial class \(\mathfrak s\).

## Blocks and geometry

Each block is an indecomposable summand cut out by a central idempotent in an
appropriate categorical sense.  Unramified characters of \(M(F)\) form a
complex torus, and a finite stabilizer acts on it.  The resulting quotient is
the **Bernstein variety** attached to \(\mathfrak s\).

Regular functions on these components form the
[[harmonic-analysis/bernstein-center|Bernstein center]]. Types and
[[harmonic-analysis/hecke-algebra-locally-compact-group-pair|Hecke
algebras]] often give explicit algebraic models of individual blocks.

## References

1. Joseph Bernstein, “Le ‘centre’ de Bernstein,” in *Représentations des
   groupes réductifs sur un corps local*, Travaux en Cours, Hermann, 1984,
   1–32.
2. Colin J. Bushnell and Philip C. Kutzko, *The Admissible Dual of
   \(\mathrm{GL}(N)\) via Compact Open Subgroups*, Annals of Mathematics
   Studies 129, Princeton University Press, 1993.

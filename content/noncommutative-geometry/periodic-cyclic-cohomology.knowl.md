+++
id = "noncommutative-geometry/periodic-cyclic-cohomology"
title = "Periodic cyclic cohomology"
kind = "definition"
summary = "The Z/2-graded stabilization of cyclic cohomology under Connes's degree-two periodicity operator."
aliases = ["HP cohomology", "periodic (b,B)-cohomology"]
domains = ["noncommutative-geometry", "algebra-homological"]
prerequisites = ["noncommutative-geometry/cyclic-cohomology"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(A\) be a unital algebra over a characteristic-zero field. Connes's periodicity operator gives maps
\[
S:HC^n(A)\longrightarrow HC^{n+2}(A)
\]
on [[noncommutative-geometry/cyclic-cohomology|cyclic cohomology]]. The **periodic cyclic cohomology** of \(A\) is the \(\mathbb Z/2\)-graded theory
\[
HP^i(A)=\varinjlim_k HC^{2k+i}(A),\qquad i\in\{0,1\},
\]
with transition maps \(S\). It therefore identifies a cyclic-cohomology class with each of its degree-two periodic images and retains parity rather than an absolute nonnegative degree.

## The periodic cochain complex

Equivalently, \(HP^\bullet(A)\) is computed by the full direct-sum totalization of Connes's periodic \((b,B)\)-bicomplex. In mixed-complex notation one may use Laurent polynomials in a formal variable \(u\) of cohomological degree \(2\), with differential \(b+uB\). The direct-sum condition means that each cochain has only finitely many nonzero degree components. This finiteness is essential: replacing that totalization by an unrestricted direct product is a different completion and need not compute periodic cyclic cohomology.

For Banach or locally convex algebras, continuous periodic cyclic cohomology uses continuous multilinear cochains. Algebraic and continuous versions need not agree.

## Pairings and geometric meaning

The [[noncommutative-geometry/chern-character-fredholm-module|Chern character of a summable Fredholm module]] naturally determines a class in \(HP^0(A)\) or \(HP^1(A)\) according to parity. Its pairing with \(K\)-theory recovers the Fredholm index. For suitable smooth commutative algebras, periodic cyclic cohomology is described by parity-grouped de Rham currents; this is one reason that degree-two stabilization is geometrically natural.

Periodic cyclic cohomology is invariant under matrix stabilization and, in characteristic zero under standard hypotheses, has excision properties that make it a robust receptacle for Chern characters.

## Comparison with other cyclic theories

Ordinary cyclic cohomology remembers every degree \(HC^n(A)\); periodic cyclic cohomology takes the direct limit under \(S\). [[noncommutative-geometry/entire-cyclic-cohomology|Entire cyclic cohomology]] instead permits infinite even or odd cochain sequences subject to analytic factorial-growth conditions. Negative, periodic, entire, analytic, and local cyclic theories arise from different totalizations or completions, so their symbols and cocycles are not interchangeable.

For nonunital algebras one commonly uses reduced cochains of a unitization or a relative complex. The chosen convention should be stated when excision or pairings are involved.

## References

1. J.-L. Loday, *Cyclic Homology*, 2nd ed., Springer, 1998. [Publisher record](https://doi.org/10.1007/978-3-662-11389-9). Relevant: chapters 2 and 5 on the \((b,B)\)-bicomplex, the periodicity operator, and periodic cyclic theory.
2. A. Connes, “Non-Commutative Differential Geometry,” *Publications Mathématiques de l'IHÉS* 62 (1985), 41–144. [DOI record](https://doi.org/10.1007/BF02698807). Relevant: §§II.1–II.3 on cyclic cohomology, periodicity, and Chern characters.
3. A. Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-maintained text](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). Relevant: Chapter III on cyclic cohomology and Chapter IV on Fredholm-module characters.

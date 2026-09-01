+++
id = "differential-geometry/frolicher-spectral-sequence"
title = "Frölicher spectral sequence"
kind = "definition"
summary = "The spectral sequence of the type filtration on the complex de Rham complex of a complex manifold."
aliases = ["Dolbeault-to-de Rham spectral sequence"]
domains = ["differential-geometry", "algebra-homological"]
prerequisites = ["differential-geometry/complex-manifold", "differential-geometry/de-rham-complex", "differential-geometry/dolbeault-cohomology"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(X\) be a [[differential-geometry/complex-manifold|complex manifold]]. Filter its complex-valued [[differential-geometry/de-rham-complex|de Rham complex]] by holomorphic degree in the decomposition \(\Omega^k(X;\mathbb C)=\bigoplus_{p+q=k}\Omega^{p,q}(X)\). The resulting **Frölicher spectral sequence** has
\[
E_1^{p,q}\cong H_{\bar\partial}^{p,q}(X),\qquad
d_r:E_r^{p,q}\longrightarrow E_r^{p+r,q-r+1},
\]
and converges to \(H_{\mathrm{dR}}^{p+q}(X;\mathbb C)\) with its induced filtration. Its first page is therefore [[differential-geometry/dolbeault-cohomology|Dolbeault cohomology]], while its limiting page gives the associated graded pieces of complex de Rham cohomology. Convergence alone does not supply a canonical direct-sum decomposition of de Rham cohomology.

## Construction and early pages

The identities \(d=\partial+\bar\partial\), \(\partial^2=\bar\partial^2=0\), and \(\partial\bar\partial+\bar\partial\partial=0\) make the spaces of \((p,q)\)-forms a double complex. Taking \(\bar\partial\)-cohomology first gives \(E_1\), and \(d_1\) is induced by \(\partial\). Higher differentials record successive obstructions to correcting a representative by forms of increasing holomorphic degree. Frölicher's original construction relates these pages to topological invariants.

## Degeneration and the Kähler case

The sequence **degenerates at \(E_r\)** when all differentials from page \(r\) onward vanish, so \(E_r=E_\infty\). If \(X\) is a compact [[differential-geometry/kahler-manifold|Kähler manifold]], Hodge theory gives degeneration already at \(E_1\) and identifies de Rham cohomology with the direct sum of its \((p,q)\)-pieces. General compact complex manifolds need not have \(E_1\)-degeneration.

## Conventions and scope

Some sources call this the Hodge-to-de Rham or Hodge–de Rham spectral sequence. Indexing may begin at \(E_0\) or \(E_1\), and decreasing versus increasing filtrations can reverse displayed bidegrees. The core uses the decreasing filtration by holomorphic degree and the cohomological differential convention shown there.

## References

1. Alfred Frölicher, “Relations between the cohomology groups of Dolbeault and topological invariants,” *Proceedings of the National Academy of Sciences* 41 (1955), 641–644. [DOI record](https://doi.org/10.1073/pnas.41.9.641). Relevant: construction and the resulting inequalities.
2. Claire Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge Studies in Advanced Mathematics 76, Cambridge University Press, 2002. [DOI record](https://doi.org/10.1017/CBO9780511615344). Relevant: §8.1, the Frölicher spectral sequence and Kähler degeneration.

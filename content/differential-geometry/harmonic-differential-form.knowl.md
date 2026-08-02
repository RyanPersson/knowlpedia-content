+++
id = "differential-geometry/harmonic-differential-form"
title = "Harmonic differential form"
kind = "definition"
summary = "A differential form annihilated by the Hodge Laplacian of a Riemannian metric."
aliases = ["harmonic form"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \((M,g)\) be an oriented
[[differential-geometry/riemannian-manifold|Riemannian manifold]], and let
\(\alpha\in\Omega^k(M)\) be a smooth differential form. The form
\(\alpha\) is **harmonic** when
\[
\Delta\alpha=0,
\]
where
\[
\Delta=d\delta+\delta d
\]
is the [[differential-geometry/hodge-laplacian|Hodge Laplacian]] and
\(\delta\) is the [[differential-geometry/codifferential|codifferential]]
determined by \(g\) and the orientation. Harmonicity therefore depends on
the Riemannian metric. On a compact manifold without boundary, it is
equivalent to the pair of first-order conditions
\(d\alpha=0\) and \(\delta\alpha=0\); that equivalence need not hold for
arbitrary smooth forms on a noncompact manifold.

## Energy characterization

When \(M\) is compact and has no boundary, formal adjointness and Stokes'
theorem give
\[
\langle\Delta\alpha,\alpha\rangle_{L^2}
=\lVert d\alpha\rVert_{L^2}^2
+\lVert\delta\alpha\rVert_{L^2}^2.
\]
Thus \(\Delta\alpha=0\) forces both summands to vanish. Conversely, a closed
and coclosed form is harmonic directly from the definition of \(\Delta\).
The compactness and boundary hypotheses justify the integrated identity
without extra boundary terms or decay assumptions.

The space of harmonic \(k\)-forms is denoted
\(\mathcal H^k(M,g)=\ker(\Delta:\Omega^k(M)\to\Omega^k(M))\). On a compact
manifold it is finite-dimensional, and the
[[differential-geometry/hodge-theorem|Hodge theorem]] identifies it with
degree-\(k\) de Rham cohomology.

## Examples and near-misses

On a flat torus, differential forms with constant coefficients are
harmonic. In degree zero, harmonic forms are precisely harmonic functions;
on a connected compact manifold every such function is constant.

The function \(f(x)=x\) on \(\mathbb R\) is a decisive noncompact warning:
with the Euclidean metric, \(\Delta f=0\), but \(df=dx\neq0\). Hence a
harmonic smooth form on a noncompact manifold need not be closed and
coclosed under the unrestricted smooth definition. \(L^2\)-harmonic forms
require a specified self-adjoint realization and are a separate analytic
setting.

## References

1. Mark Andrea A. de Cataldo, *The Hodge Theory of Projective Manifolds*, Imperial College Press, 2007. [Author-hosted book PDF](https://www.math.stonybrook.edu/~mde/papers/MyHodgeTheoryBook.pdf). Relevant: §2.3, especially Definition 2.3.1 and Lemma 2.3.2.
2. Raymond O. Wells, Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008. [Springer DOI record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: Chapter IV, §2 on harmonic forms and Hodge theory.

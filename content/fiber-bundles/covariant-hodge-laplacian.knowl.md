+++
id = "fiber-bundles/covariant-hodge-laplacian"
title = "Covariant Hodge Laplacian"
kind = "definition"
summary = "The covariant Hodge Laplacian is the second-order operator obtained by anticommuting a covariant exterior derivative with its formal adjoint."
aliases = ["gauge-covariant Laplacian", "Delta_A"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
+++

Let \(E\to M\) be a [[fiber-bundles/vector-bundle|vector bundle]] with [[fiber-bundles/bundle-metric|bundle metric]] and compatible [[fiber-bundles/connection-on-a-vector-bundle|connection]] \(A\) over an oriented [[differential-geometry/riemannian-manifold|Riemannian manifold]]. The **covariant Hodge Laplacian** on \(E\)-valued \(k\)-forms is
\[
\Delta_A=d_A d_A^*+d_A^*d_A:
\Omega^k(M;E)\longrightarrow\Omega^k(M;E),
\]
where \(d_A\) is the [[fiber-bundles/exterior-covariant-derivative|exterior covariant derivative]] and \(d_A^*\) is its [[fiber-bundles/formal-adjoint-of-covariant-exterior-derivative|formal adjoint]]. It is a formally self-adjoint elliptic operator with scalar principal symbol \(|\xi|^2\operatorname{id}\). Unlike the ordinary de Rham differential, \(d_A^2\) need not vanish: curvature acts on the coefficient bundle.
The operator preserves form degree and depends on both the Riemannian metric and the connection.

## Energy identity and kernel

On a compact manifold without boundary,
\[
\langle\Delta_A\alpha,\alpha\rangle_{L^2}
=\|d_A\alpha\|_{L^2}^2+\|d_A^*\alpha\|_{L^2}^2.
\]
Consequently, a smooth form lies in \(\ker\Delta_A\) exactly when it is both \(d_A\)-closed and \(d_A^*\)-closed. This conclusion uses compactness or boundary conditions that eliminate boundary terms.

If \(A\) is flat, then \(d_A^2=0\), so \((\Omega^\bullet(M;E),d_A)\) is a complex and the kernel represents cohomology through the corresponding [[differential-geometry/hodge-theorem|Hodge theorem]]. For a curved connection, \(\ker\Delta_A\) remains analytically meaningful, but it is not generally a cohomological model.

## Weitzenböck form

The covariant Hodge Laplacian has a Weitzenböck decomposition
\[
\Delta_A=\nabla_A^*\nabla_A+\mathcal R_g+\mathcal R_{F_A},
\]
where the last two terms are zeroth-order actions of the Riemannian curvature and the curvature of \(A\). Thus the distinction between \(\Delta_A\) and the rough connection Laplacian is precisely a curvature correction. This is why “connection Laplacian” is not used here as an unqualified alias.

In [[fiber-bundles/gauge-theory|gauge theory]], the operator and its gauge-fixed variants control infinitesimal deformations and regularity of connections [Freed–Uhlenbeck, chapter 2].

## References

1. Daniel S. Freed and Karen K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: chapter 2, covariant differential operators, ellipticity, and gauge-theoretic estimates.
2. Raymond O. Wells Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008. [DOI record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: chapter IV, Hodge Laplacians and elliptic operator theory.

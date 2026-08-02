+++
id = "differential-geometry/differential-operator-vector-bundles"
title = "Differential operator between vector bundles"
kind = "definition"
summary = "A linear map on smooth bundle sections whose value at a point depends on only finitely many derivatives of the section there."
aliases = ["linear differential operator", "order of a differential operator", "bundle differential operator"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(E\) and \(F\) be smooth [[fiber-bundles/vector-bundle|vector bundles]] over the same [[fiber-bundles/smooth-manifold|smooth manifold]] \(M\). A **linear differential operator of order at most \(m\)** is a [[linear-algebra/linear-map|linear map]]
\[
D:\Gamma^\infty(E)\longrightarrow\Gamma^\infty(F)
\]
such that, in every coordinate neighborhood and bundle trivialization, it has the form
\[
Ds=\sum_{|\alpha|\leq m}a_\alpha\,\partial^\alpha s,
\]
where each \(a_\alpha\) is a smooth bundle-homomorphism-valued coefficient. The least such \(m\) is the **order** of \(D\). Thus \(D(s)(x)\) depends only on the \(m\)-jet of \(s\) at \(x\), not on values of \(s\) away from \(x\).

## Intrinsic characterization

For \(f\in C^\infty(M)\), let \(M_f\) denote multiplication by \(f\) and set \(\operatorname{ad}_{M_f}(D)=[D,M_f]\). The operator \(D\) has order at most \(m\) exactly when every \((m+1)\)-fold iterated commutator vanishes:
\[
\operatorname{ad}_{M_{f_m}}\cdots\operatorname{ad}_{M_{f_0}}(D)=0.
\]
This formulation is independent of coordinates and trivializations. Order-zero operators are precisely smooth bundle homomorphisms acting pointwise.

## Structure and examples

Orders add under composition: if \(D_1\) and \(D_2\) have orders at most \(m_1\) and \(m_2\), then \(D_2D_1\) has order at most \(m_1+m_2\). A [[fiber-bundles/covariant-derivative-of-a-section|covariant derivative]] is first order, while a connection Laplacian is second order. The leading-order coefficients assemble into the [[differential-geometry/principal-symbol|principal symbol]], which controls [[differential-geometry/elliptic-differential-operator|ellipticity]].

## Conventions and scope

**Warning.** “Differential operator” may also mean a nonlinear local operator or an operator on distributions. This knowl concerns linear operators on smooth sections. Declaring order at most \(m\) allows the actual order to be smaller; the zero operator therefore has every nonnegative upper order bound.

## References

1. R. O. Wells Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008. [Publisher record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: chapter IV, differential operators and symbols.
2. H. B. Lawson Jr. and M.-L. Michelsohn, *Spin Geometry*, Princeton University Press, 1989. [Publisher record](https://doi.org/10.1515/9781400883912). Relevant: chapter III, differential operators on vector bundles.

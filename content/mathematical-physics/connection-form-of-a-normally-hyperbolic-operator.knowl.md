+++
id = "mathematical-physics/connection-form-of-a-normally-hyperbolic-operator"
title = "Connection form of a normally hyperbolic operator"
kind = "theorem"
summary = "Every normally hyperbolic operator is uniquely a connection wave operator plus a bundle endomorphism."
aliases = ["connection decomposition of a normally hyperbolic operator"]
domains = ["mathematical-physics", "partial-differential-equations", "differential-geometry"]
prerequisites = ["differential-geometry/lorentzian-manifold","mathematical-physics/normally-hyperbolic-operator","fiber-bundles/levicivita-connection-connection","differential-geometry/connection-laplacian"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(E\to(M,g)\) be a smooth vector bundle over a [[differential-geometry/lorentzian-manifold|Lorentzian manifold]]. Every [[mathematical-physics/normally-hyperbolic-operator|normally hyperbolic operator]]
\[
P:\Gamma^\infty(E)\longrightarrow\Gamma^\infty(E)
\]
has a unique expression
\[
P=-\operatorname{tr}_g\bigl((\nabla^E)^2\bigr)+B,
\]
where \(\nabla^E\) is a connection on \(E\), \(B\in\Gamma^\infty(\operatorname{End}E)\), and
\[
(\nabla^E)^2_{X,Y}s
=\nabla^E_X\nabla^E_Ys-\nabla^E_{\nabla^{\mathrm{LC}}_X Y}s
\]
is the covariant Hessian formed with the [[fiber-bundles/levicivita-connection-connection|Levi–Civita connection]] of \(g\).

Thus \(P\) is the [[differential-geometry/connection-laplacian|connection wave operator]] determined by a unique connection, plus a uniquely determined zeroth-order potential \(B\). The displayed negative trace matches the principal-symbol convention
\[
\sigma_2(P)(x,\xi)=-g_x^{-1}(\xi,\xi)\operatorname{id}_{E_x}.
\]

## References

1. Christian Bär, Nicolas Ginoux, and Frank Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007. [Publisher record](https://doi.org/10.4171/037). Relevant: Lemma 1.5.5.

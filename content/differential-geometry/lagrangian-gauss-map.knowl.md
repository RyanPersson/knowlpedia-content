+++
id = "differential-geometry/lagrangian-gauss-map"
title = "Lagrangian Gauss map"
kind = "definition"
summary = "The tangent-plane map of a Lagrangian immersion, valued intrinsically in the Lagrangian-Grassmannian bundle."
aliases = ["Gauss map of a Lagrangian immersion"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(f:L^n\to(M^{2n},\omega)\) be a [[differential-geometry/lagrangian-submanifold|Lagrangian immersion]] into a [[differential-geometry/symplectic-manifold|symplectic manifold]]. Write \(\operatorname{Lag}(TM)\to M\) for the bundle whose fiber at \(p\) is the [[differential-geometry/lagrangian-grassmannian|Lagrangian Grassmannian]] of \(T_pM\). The **Lagrangian Gauss map** is
\[
\gamma_f:L\longrightarrow\operatorname{Lag}(TM),\qquad
\gamma_f(x)=df_x(T_xL)\subset T_{f(x)}M,
\]
and it covers \(f\). Equivalently, it is a section of the [[fiber-bundles/pullback-bundle|pullback bundle]] \(f^*\operatorname{Lag}(TM)\). If \(M=V\) is a [[differential-geometry/symplectic-vector-space|symplectic vector space]], translation canonically identifies all tangent spaces with \(V\), so \(\gamma_f\) is an ordinary map \(L\to\Lambda(V)\). For a general \(M\), such a fixed-target map requires a symplectic trivialization of \(f^*TM\).

## Why the target is Lagrangian

Because \(f^*\omega=0\), the subspace \(df_x(T_xL)\) is isotropic. Its dimension is \(n\), half the dimension of \(T_{f(x)}M\), so it is Lagrangian. Thus the Lagrangian condition is exactly what makes the ordinary tangent-plane Gauss map factor through the Lagrangian-Grassmannian subbundle rather than the full Grassmann bundle.

## Trivialized form

Given a symplectic trivialization
\[
\tau:f^*TM\overset{\sim}{\longrightarrow}L\times(V,\omega_0),
\]
the Gauss map becomes \(\gamma_{f,\tau}(x)=\tau_x(df_x(T_xL))\in\Lambda(V)\). Replacing \(\tau\) by a varying symplectic transformation acts pointwise on \(\Lambda(V)\). Therefore constructions that pull back a class from one fixed Lagrangian Grassmannian must record the trivialization or an equivalent Maslov datum when the ambient [[fiber-bundles/tangent-bundle|tangent bundle]] is not canonically trivialized.

## Examples

For the [[fiber-bundles/zero-section|zero section]] \(Q\hookrightarrow T^*Q\), the Gauss map selects the horizontal Lagrangian tangent planes along the zero section. If \(L\subset\mathbb R^{2n}\) is an affine Lagrangian plane, \(\gamma_L\) is constant. By contrast, a half-dimensional [[differential-geometry/immersed-submanifold|immersed submanifold]] on which \(\omega\) does not vanish has tangent planes outside \(\operatorname{Lag}(TM)\), so its tangent-plane map is not a Lagrangian Gauss map.

## Relation to Maslov data

In a symplectic vector space, pulling the [[differential-geometry/maslov-class-lagrangian-grassmannian|universal Maslov class]] on \(\Lambda(V)\) back along \(\gamma_f\) gives the Maslov class of the immersion. For a general symplectic manifold, the intrinsic section into \(f^*\operatorname{Lag}(TM)\) is still canonical, while an integral phase or grading can require additional ambient Maslov-covering data [Seidel, §2](https://arxiv.org/abs/math/9903049).

## References

1. V. I. Arnol'd, “On a characteristic class entering into conditions of quantization,” *Functional Analysis and Its Applications* 1 (1967), 1–14. [DOI record](https://doi.org/10.1007/BF01079201). Relevant: the Gauss map of a Lagrangian submanifold and the Maslov class.
2. Paul Seidel, “Graded Lagrangian submanifolds,” *Bulletin de la Société Mathématique de France* 128 (2000), 103–149. [arXiv record](https://arxiv.org/abs/math/9903049). Relevant: §2, Maslov coverings and gradings.

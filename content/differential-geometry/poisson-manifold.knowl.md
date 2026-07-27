+++
id = "differential-geometry/poisson-manifold"
title = "Poisson manifold"
kind = "definition"
summary = "A smooth manifold whose smooth functions carry a Lie bracket that is a derivation in each argument."
aliases = ["Poisson space"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]]. A **Poisson
structure** on \(M\) is a bilinear operation on its
[[differential-geometry/algebra-of-smooth-functions|algebra of smooth
functions]],
\[
\{-,-\}:C^\infty(M)\times C^\infty(M)\longrightarrow C^\infty(M)
\]
that is skew-symmetric, satisfies the Jacobi identity, and obeys the Leibniz rule \(\{f,gh\}=\{f,g\}h+g\{f,h\}\). A **Poisson manifold** is a pair \((M,\{-,-\})\). Equivalently, the bracket is determined by a smooth bivector field \(\pi\in\Gamma(\wedge^2 TM)\) through \(\{f,g\}=\pi(df,dg)\), and the Jacobi identity is equivalent to the vanishing of the Schouten bracket \([\pi,\pi]\).

## Hamiltonian vector fields and leaves

For \(f\in C^\infty(M)\), the derivation \(g\mapsto\{f,g\}\) is represented by a [[fiber-bundles/vector-field|vector field]] \(X_f\), called the [[differential-geometry/hamiltonian-vector-field|Hamiltonian vector field]] of \(f\). At each point, the map \(\pi^\sharp:T^*M\to TM\) defined by
\[
\beta(\pi^\sharp\alpha)=\pi(\alpha,\beta)
\]
has image tangent to a canonical, generally singular foliation. Each leaf carries a symplectic form, and its dimension is the even [[linear-algebra/rank|rank]] of \(\pi\). The construction and its integrability are developed in [Vaisman, Chapters 1–2](https://doi.org/10.1007/978-3-0348-8495-2).

## Relationship to symplectic and Lie theory

Every [[differential-geometry/symplectic-manifold|symplectic manifold]] determines a Poisson structure by inverting its nondegenerate \(2\)-form, subject to the stated sign convention. Poisson manifolds allow the rank to vary and therefore include genuinely degenerate examples. The dual \(\mathfrak g^*\) of a finite-dimensional [[lie-groups/lie-algebra|Lie algebra]] has the linear Lie–Poisson bracket, characterized on linear functions by the [[fiber-bundles/lie-bracket|Lie bracket]] of \(\mathfrak g\). Thus Poisson geometry simultaneously extends symplectic geometry and records infinitesimal Lie-theoretic data.

## Conventions and scope

**Warning.** Sign conventions differ. Here \(X_f(g)=\{f,g\}\) and \(\beta(\pi^\sharp\alpha)=\pi(\alpha,\beta)\). Authors who define Hamiltonian vector fields or the inverse of a symplectic form with the opposite sign obtain the opposite displayed Poisson bracket. “Poisson space” may also denote a singular or algebraic object; this knowl defines only the smooth-manifold notion. The equivalent bracket and bivector formulations, including the Schouten-bracket criterion, follow [Laurent-Gengoux, Pichereau, and Vanhaecke, Chapter 1](https://doi.org/10.1007/978-3-642-31090-4).

## References

1. Izu Vaisman, *Lectures on the Geometry of Poisson Manifolds*, Progress in Mathematics 118, Birkhäuser, 1994. [Publisher record](https://doi.org/10.1007/978-3-0348-8495-2). Relevant: Chapters 1–3.
2. Camille Laurent-Gengoux, Anne Pichereau, and Pol Vanhaecke, *Poisson Structures*, Grundlehren der mathematischen Wissenschaften 347, Springer, 2013. [Publisher record](https://doi.org/10.1007/978-3-642-31090-4). Relevant: Chapter 1.

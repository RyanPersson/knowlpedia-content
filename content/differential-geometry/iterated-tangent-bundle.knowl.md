+++
id = "differential-geometry/iterated-tangent-bundle"
title = "Iterated tangent bundle"
kind = "definition"
summary = "A tangent bundle obtained by repeatedly applying the tangent functor to a smooth manifold."
aliases = ["second tangent bundle", "TTM"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]]. Its **iterated tangent bundles** are defined recursively by
\[
T^0M=M,\qquad T^{r+1}M=T(T^rM)\quad(r\geq0),
\]
using the [[differential-geometry/tangent-functor|tangent functor]]. In particular, \(T^2M=T(TM)\), usually written \(TTM\), is the second [[fiber-bundles/tangent-bundle|tangent bundle]]. If \(M\) has dimension \(n\), then \(T^rM\) has dimension \(2^rn\). For a [[fiber-bundles/smooth-map|smooth map]] \(f:M\to N\), repeated differentiation gives \(T^rf:T^rM\to T^rN\); hence each fixed iterate \(T^r\) is again a covariant [[algebra-category-theory/functor|functor]] on smooth manifolds.

## The double vector-bundle structure of \(TTM\)

The second tangent bundle has two natural projections to \(TM\):
\[
\tau_{TM}:TTM\to TM,\qquad T\tau_M:TTM\to TM,
\]
where \(\tau_M:TM\to M\) is the tangent-bundle projection. Each projection makes \(TTM\) a [[fiber-bundles/vector-bundle|vector bundle]] over \(TM\), and the two structures satisfy compatibility axioms. Thus \(TTM\) is the basic example of a double vector bundle, not merely an ordinary vector bundle with duplicated notation.

## Canonical involution

A smooth two-parameter map \(\gamma(s,t)\) into \(M\) determines an element of \(TTM\) by differentiating first in one parameter and then in the other. Interchanging the parameters defines the canonical involution
\[
\kappa_M:TTM\longrightarrow TTM,\qquad \kappa_M^2=\operatorname{id}_{TTM}.
\]
It exchanges the two vector-bundle projections. In induced coordinates \((x,v;\dot x,\dot v)\), it has the form
\[
\kappa_M(x,v;\dot x,\dot v)=(x,\dot x;v,\dot v).
\]
This construction is natural in \(M\).

## Examples and conventions

For a [[linear-algebra/vector-space|vector space]] \(V\), translation gives \(TV\cong V\times V\) and \(T^rV\cong V^{2^r}\), although the canonical projections still distinguish the factors. For a general manifold no global product decomposition exists.

**Warning.** \(T^rM\) denotes repeated application of \(T\), not the bundle of [[differential-geometry/jet-of-a-smooth-map|\(r\)-jets of curves]]. The latter records derivatives through order \(r\) modulo a jet equivalence and has dimension \((r+1)n\), whereas the iterated tangent bundle has dimension \(2^rn\). Authors sometimes use “higher tangent bundle” for either construction, so the notation must be checked.

## References

1. Ivan Kolář, Peter W. Michor, and Jan Slovák, *Natural Operations in Differential Geometry*, Springer, 1993. [Springer DOI record](https://doi.org/10.1007/978-3-662-02950-3). Relevant: Chapter VI, iterated tangent functors and natural transformations.
2. Kirill C. H. Mackenzie, *General Theory of Lie Groupoids and Lie Algebroids*, Cambridge University Press, 2005. [Cambridge DOI record](https://doi.org/10.1017/CBO9781107325883). Relevant: Chapter 9, double vector bundles and the canonical involution of \(TTM\).

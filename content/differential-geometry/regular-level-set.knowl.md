+++
id = "differential-geometry/regular-level-set"
title = "Regular level set"
kind = "definition"
summary = "The preimage of a regular value of a smooth map between manifolds."
aliases = ["regular fiber", "regular preimage"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-map", "fiber-bundles/smooth-manifold", "fiber-bundles/regular-value", "differential-geometry/embedded-submanifold"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(f:M\to N\) be a [[fiber-bundles/smooth-map|smooth map]] between finite-dimensional [[fiber-bundles/smooth-manifold|smooth manifolds]], and let \(y\in N\) be a [[fiber-bundles/regular-value|regular value]] of \(f\). The subset
\[
S=f^{-1}(y)
\]
is called a **regular level set**, **regular fiber**, or **regular preimage** of \(f\). By the regular-value theorem, \(S\) is an [[differential-geometry/embedded-submanifold|embedded submanifold]] of \(M\); when nonempty, it has codimension \(\dim N\), and for every \(x\in S\),
\[
T_xS=\ker(df_x).
\]
The empty preimage is regular under the standard vacuous convention. When \(N=\mathbb R\), this is the usual level set of a smooth function at a regular value.

## Local normal form

For each \(x\in S\), the submersion theorem supplies coordinates near \(x\) and \(y\) in which
\[
f(u_1,\ldots,u_m)=(u_{m-n+1},\ldots,u_m).
\]
In these coordinates the level set is the coordinate slice on which the last \(n=\dim N\) coordinates are constant. This both gives the induced smooth structure and explains the tangent-space formula.

## Examples and a near miss

For \(f:\mathbb R^n\to\mathbb R\), \(f(x)=\|x\|^2\), each \(r>0\) is a regular value and \(f^{-1}(r)\) is a sphere of dimension \(n-1\). The value \(0\) is critical because \(df_0=0\), although its level set \(\{0\}\) happens to be a submanifold. Thus “is a submanifold” does not imply “is a regular level set for the displayed defining map.”

For a submersion \(f:M\to N\), every fiber is a regular level set.

## Conventions and scope

Some authors use “level set” only for real-valued functions and “fiber” for general targets. This knowl allows an arbitrary finite-dimensional target manifold. If \(M\) or \(N\) has boundary or corners, a clean embedded-submanifold conclusion can require additional boundary compatibility or transversality hypotheses; the core states the boundaryless theorem.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Graduate Texts in Mathematics 218, Springer, 2012. [Springer DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 5, especially Theorem 5.12, the regular level set theorem.
2. Victor Guillemin and Alan Pollack, *Differential Topology*, AMS Chelsea Publishing, 2010 reprint. [AMS DOI record](https://doi.org/10.1090/chel/370). Relevant: Chapter 1, submersions and the preimage theorem.

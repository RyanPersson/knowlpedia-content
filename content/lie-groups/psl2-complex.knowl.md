+++
id = "lie-groups/psl2-complex"
title = "PSL(2,C)"
kind = "example"
summary = "The center quotient of SL(2,C), viewed either as a complex Lie group or as a six-dimensional real Lie group."
aliases = ["projective special linear group PSL(2,C)", "PSL2C"]
domains = ["lie-groups", "complex-analysis"]
section_mode = "progressive"
+++

The complex projective special linear group is
\[
PSL(2,\mathbb C):=SL(2,\mathbb C)/\{\pm I\}.
\]
It is a connected [[lie-groups/complex-lie-group|complex Lie group]] of complex dimension \(3\). Its underlying real Lie group has real dimension \(6\), and its Lie algebra is \(\mathfrak{sl}_2(\mathbb C)_{\mathbb R}\).

## Equivalent matrix description

Because every nonzero complex number has a square root, every class in \(PGL_2(\mathbb C)\) has a determinant-one representative, unique up to sign. Hence
\[
PSL(2,\mathbb C)\cong PGL_2(\mathbb C).
\]
This equality is special to fields for which the required determinant roots exist and must not be transferred to arbitrary fields.

## Three geometric roles

The group acts faithfully by [[complex-analysis/mobius-transformation|Möbius transformations]] on the [[complex-analysis/riemann-sphere|Riemann sphere]]. Its underlying real Lie group is isomorphic to [[lie-groups/proper-orthochronous-lorentz-group|\(SO^+(1,3)\)]], and it is the orientation-preserving isometry group of [[differential-geometry/hyperbolic-three-space|hyperbolic \(3\)-space]]. These are compatible through the common action on the conformal boundary \(S^2\), but they are actions on three different geometric objects.

## Langlands context: three separate roles

The same rank-one objects occur in geometric Langlands, but in logically distinct roles:

1. **Möbius automorphisms.** The complex Lie group
   \(PSL(2,\mathbb C)\cong PGL_2(\mathbb C)\) is
   \(\operatorname{Aut}_{\mathrm{hol}}(\mathbb P^1(\mathbb C))\). This is an
   automorphism-group statement about the analytic Riemann sphere.
2. **Reductive and dual group.** The algebraic group \(PGL_2\) is the adjoint
   connected reductive group of type \(A_1\) and the Langlands dual group of
   \(SL_2\). Its complex points agree with \(PSL(2,\mathbb C)\), but its
   Langlands-dual role comes from root data, not from the Möbius action.
3. **Base curve.** The algebraic curve \(\mathbb P^1_{\mathbb C}\) can itself
   be the base curve of a geometric-Langlands problem; it is not the structure
   group or dual group. The unmarked and ramified cases behave differently, as
   explained at [[langlands/projective-line-in-geometric-langlands|the
   projective line in geometric Langlands]].

Consequently there is no additional conjectural correspondence obtained merely
by identifying the Riemann sphere with \(\mathbb P^1(\mathbb C)\) and its
holomorphic automorphism group with \(PSL(2,\mathbb C)\).

## References

1. Alan F. Beardon, *The Geometry of Discrete Groups*, Springer, 1983, Chapters 3 and 7. [Publisher record](https://doi.org/10.1007/978-1-4612-1146-4).
2. John G. Ratcliffe, *Foundations of Hyperbolic Manifolds*, 3rd ed., Springer, 2019, Chapters 3–4. [Publisher record](https://doi.org/10.1007/978-3-030-31597-9).

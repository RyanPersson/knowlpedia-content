+++
id = "differential-geometry/del-j-operator"
title = "The del-J operator"
kind = "definition"
summary = "The first-order differential operator obtained by conjugating d-bar with a second complex structure on a hypercomplex manifold."
aliases = ["partial-J operator", "∂_J operator", "quaternionic d-bar operator on a hypercomplex manifold"]
domains = ["differential-geometry", "quaternionic-analysis", "complex-analysis"]
section_mode = "progressive"
+++

Let \((M,I,J,K)\) be a
[[differential-geometry/hypercomplex-manifold|hypercomplex manifold]], and use
the type decomposition determined by \(I\). The **del-J operator** is
\[
\partial_J=J^{-1}\circ\bar\partial\circ J.
\]
It maps \(I\)-type \((p,q)\) forms to type \((p+1,q)\) forms and satisfies
\[
\partial\partial_J=-\partial_J\partial.
\]

## Action of \(J\) on forms

The endomorphism \(J\) acts on forms by pullback on every argument. Because
\(IJ=-JI\), it exchanges the \((p,q)\) and \((q,p)\) types determined by
\(I\). Conjugating \(\bar\partial\) by this action therefore produces another
operator of \((1,0)\)-degree.

## Quaternionic potentials

For a real smooth function \(u\), the form
\(\partial\partial_Ju\) is a real \((2,0)\)-form in the quaternionic sense.
Its positivity defines
[[differential-geometry/quaternionic-plurisubharmonic-function-hypercomplex|
quaternionic plurisubharmonicity on a hypercomplex manifold]], and strict
positivity produces local [[differential-geometry/hkt-metric|HKT metrics]].

## Convention warning

Some sources let \(I,J,K\) act on tangent vectors on the right and write the
same construction with the corresponding right-action signs. The invariant
content is the conjugated Dolbeault operator and the anticommutation identity;
formulas should not mix left- and right-action conventions.

## References

1. Semyon Alesker and Misha Verbitsky, “Plurisubharmonic functions on hypercomplex manifolds and HKT-geometry,” *Journal of Geometric Analysis* 16 (2006), 375–399. [arXiv record](https://arxiv.org/abs/math/0510140). Relevant: §2.

+++
id = "langlands/projective-line-in-geometric-langlands"
title = "The projective line in geometric Langlands"
kind = "context"
summary = "Why unmarked P1 has sparse spectral data and marked P1 supports rich ramified geometric-Langlands examples."
aliases = ["geometric Langlands on P1", "geometric Langlands on the Riemann sphere"]
domains = ["langlands", "algebraic-geometry-foundations"]
section_mode = "progressive"
+++

The projective line \(X=\mathbb P^1_{\mathbb C}\) is a valid base curve for
[[langlands/geometric-langlands-correspondence|geometric Langlands]], but the
unramified classical spectral problem is sparse. Since the analytic sphere is
simply connected, every ordinary unramified complex local system has trivial
monodromy. Its automorphisms and derived deformations mean that the spectral
stack is not literally a featureless point, but there are no nontrivial
classical monodromy representations.

## Marked projective line

Choose \(D=\{x_1,\ldots,x_n\}\) and put
\(U=\mathbb P^1\setminus D\). Then
\[
\pi_1(U)=
\langle m_1,\ldots,m_n\mid m_1m_2\cdots m_n=1\rangle,
\]
so local systems can have nontrivial monodromy around the marked points.
Prescribed conjugacy classes, regular or irregular singularities, and
automorphic level structures lead to
[[langlands/ramified-geometric-langlands|ramified geometric Langlands]].

For three marked points, \(U\) is the pair of pants. Nadler and Yun proved a
geometric Langlands equivalence for \(SL_2\) and \(PGL_2\) in a tamely
ramified pair-of-pants setting.

## Three distinct appearances of PGL2

These facts should not be conflated:

1. \(\mathbb P^1\simeq PGL_2/B\) is a rank-one flag variety.
2. \(PGL_2(\mathbb C)\) is the holomorphic automorphism group of the Riemann
   sphere.
3. \(PGL_2\) is the Langlands dual group of \(SL_2\).

Only the third determines the spectral group for an \(SL_2\) geometric
Langlands problem. There is no separate conjectural bridge caused merely by
the Möbius action.

## References

1. David Nadler and Zhiwei Yun, “Geometric Langlands correspondence for
   \(SL(2)\), \(PGL(2)\) over the pair of pants,” *Compositio Mathematica*
   155 (2019), 1835–1942.
   [arXiv](https://arxiv.org/abs/1610.08398).

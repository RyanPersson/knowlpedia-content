+++
id = "lie-groups/essentially-skew-adjoint-derived-operators"
title = "Essential skew-adjointness of derived representation operators"
kind = "theorem"
summary = "A derived operator on smooth vectors closes to the skew-adjoint generator of the corresponding one-parameter unitary group."
aliases = ["essentially self-adjoint infinitesimal generators", "closure of dπ(X)"]
domains = ["lie-groups", "functional-analysis"]
section_mode = "progressive"
+++

Let \(\pi\) be a [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] of a Lie group
\(G\) on \(\mathcal H\), and let \(X\) lie in its [[lie-groups/lie-algebra|Lie algebra]]. On the dense
invariant domain \(\mathcal H^\infty\), the
[[lie-groups/derived-representation-on-smooth-vectors|derived operator]]
\[
d\pi(X)v=\left.\frac{d}{dt}\right|_{t=0}\pi(\exp(tX))v
\]
is essentially skew-adjoint. If \(A_X\) is the self-adjoint
[[lie-groups/infinitesimal-generator-unitary-representation|Stone
generator]] determined by \(\pi(\exp(tX))=e^{itA_X}\), then
\[
\overline{d\pi(X)|_{\mathcal H^\infty}}=iA_X.
\]
Equivalently, \(-i\,d\pi(X)\) is essentially self-adjoint on
\(\mathcal H^\infty\), and its closure is \(A_X\).

## Why essential skew-adjointness holds

[[lie-groups/stone-theorem-one-parameter-unitary-groups|Stone's theorem]]
first identifies the maximal skew-adjoint generator \(iA_X\) of the
one-parameter subgroup. Smooth vectors lie in its domain and the derivative
there agrees with \(d\pi(X)\). Smoothing arbitrary vectors by convolution
against compactly supported smooth functions on \(G\) produces a dense
invariant subspace of smooth vectors that is a core for \(A_X\). Agreement on
this core forces the stated closure
[Warner, §4.4](https://doi.org/10.1007/978-3-642-50275-0).

## Consequences

The operator \(d\pi(X)\) has a unique skew-adjoint extension, so its closure
recovers the original subgroup by
\[
\pi(\exp(tX))=\exp\!\left(t\,\overline{d\pi(X)}\right).
\]
There is therefore no ambiguity in passing between the global unitary action
along \(\exp(\mathbb RX)\) and its infinitesimal action. Spectral theory
applies to the self-adjoint operator \(A_X=-i\,\overline{d\pi(X)}\).

## Domains and sign conventions

**Warning.** The conclusion concerns \(d\pi(X)\) restricted to the common
smooth-vector domain. An arbitrary smaller dense invariant domain need not be
a core, and a merely skew-symmetric operator need not be essentially
skew-adjoint. Authors who write one-parameter groups as \(e^{-itH}\) call
\(H=i\,\overline{d\pi(X)}\) the self-adjoint generator; this differs by a sign
from the convention \(e^{itA_X}\) used here.

## References

1. Garth Warner, *Harmonic Analysis on Semi-Simple Lie Groups I*, Grundlehren der mathematischen Wissenschaften 188, Springer, 1972. [DOI record](https://doi.org/10.1007/978-3-642-50275-0). Relevant: §4.4 on differentiable vectors and infinitesimal operators.
2. Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press, 1972. [DOI record](https://doi.org/10.1016/B978-0-12-585001-8.X5001-6). Relevant: §VIII.4 on Stone's theorem and generators.

+++
id = "lie-groups/complex-lie-algebra-sl5"
title = "Complex Lie algebra sl5(C)"
kind = "knowl"
summary = "The 24-dimensional simple complex Lie algebra of rank 4 and Dynkin type A4."
aliases = ["complex-lie-algebra-sl5", "sl5(C)", "sl(5,C)", "complex Lie algebra sl5"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

The **complex Lie algebra** \(\mathfrak{sl}_5(\mathbb C)\) consists of trace-zero \(5\times5\) complex matrices with commutator bracket. It is [[lie-groups/simple-lie-algebra|simple]], of complex dimension \(24\), rank \(4\), and [[lie-groups/dynkin-diagram|Dynkin type]] \(A_4\).

Its four [[lie-groups/fundamental-representation|fundamental representations]] are the exterior powers
\[
\mathbb C^5,\quad \Lambda^2\mathbb C^5,\quad
\Lambda^3\mathbb C^5,\quad\Lambda^4\mathbb C^5,
\]
of dimensions \(5,10,10,5\). After choosing a volume form, the last two are dual to the first two. The adjoint representation has dimension \(24\).

## Root data

For the diagonal [[lie-groups/cartan-subalgebra|Cartan subalgebra]], the roots are \(\varepsilon_i-\varepsilon_j\) for \(i\ne j\). The [[lie-groups/simple-root|simple roots]] \(\varepsilon_i-\varepsilon_{i+1}\), \(1\leq i\leq4\), give the four-node chain \(A_4\). The [[lie-groups/weyl-group|Weyl group]] is the symmetric group \(S_5\), acting by permuting the diagonal coordinates.

## Groups and real forms

The [[lie-groups/simply-connected-lie-group|simply connected]] complex group is \(SL(5,\mathbb C)\), whose center is \(\mu_5\); its adjoint quotient is \(PSL(5,\mathbb C)\). The [[lie-groups/compact-real-form|compact real form]] integrates to \(SU(5)\). The finite-dimensional complex representations of the compact and complex forms share the same highest-weight classification, but the groups and their real [[lie-groups/lie-algebra|Lie algebras]] are different objects.

## Paper context

The block-diagonal subgroup
\[
S(U(2)\times U(3))\subset SU(5)
\]
is isomorphic to \((U(1)\times SU(2)\times SU(3))/\mathbb Z_6\). Restricting the \(32\)-dimensional [[algebra-modules/exterior-algebra|exterior algebra]] \(\Lambda\mathbb C^5\) to this subgroup gives one Standard Model generation together with antiparticles and a [[mathematical-physics/right-handed-neutrino-gauge-singlet|right-handed neutrino]].

In the three-generation construction, a unique compatible copy of \(\mathfrak{sl}_5\) fits into a chain through the [[lie-groups/complex-lie-algebra-sl6|complex Lie algebra \(\mathfrak{sl}_6\)]] and the [[lie-groups/exceptional-lie-algebra-e7|exceptional Lie algebra \(\mathfrak e_7\)]]:
\[
\mathfrak g_{\mathrm{SM}}\subset\mathfrak{sl}_5
\subset\mathfrak{sl}_6
\subset\mathfrak e_7.
\]
This is also the \(A_4\) term of the regular-subalgebra chain summarized by the [[lie-groups/en-series-of-lie-algebras|\(E_n\) series]].

## References

1. William Fulton and Joe Harris, *Representation Theory: A First Course*, Springer, 1991, Sections 13 and 15. [Publisher record](https://doi.org/10.1007/978-1-4612-0979-9).
2. John C. Baez and John Huerta, *The Algebra of Grand Unified Theories*, *Bulletin of the American Mathematical Society* 47 (2010), 483--552. [DOI](https://doi.org/10.1090/S0273-0979-10-01294-2).
3. John C. Baez, *Three Generations in E7*, 2026. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
4. John C. Baez and Paul Schwahn, *The Standard Model Gauge Group from the Exceptional Jordan Algebra*, 2026. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).

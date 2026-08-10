+++
id = "lie-groups/en-series-of-lie-algebras"
title = "En series of Lie algebras"
kind = "knowl"
summary = "The extended E_n convention linking the exceptional types E6, E7, E8 to D5, A4, and A2+A1 by successive Dynkin-node deletion."
aliases = ["en-series-of-lie-algebras", "E_n series", "En series", "extended E-series"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

The **\(E_n\) series of complex Lie algebras**, in the convention relevant here, is the sequence
\[
\begin{array}{c|c|c|c}
n & E_n & \text{Dynkin type} & (\operatorname{rank},\dim)\\ \hline
3 & \mathfrak{sl}_3\oplus\mathfrak{sl}_2 & A_2\!+\!A_1 &(3,11)\\
4 & \mathfrak{sl}_5 & A_4 &(4,24)\\
5 & \mathfrak{so}_{10} & D_5 &(5,45)\\
6 & \mathfrak e_6 & E_6 &(6,78)\\
7 & \mathfrak e_7 & E_7 &(7,133)\\
8 & \mathfrak e_8 & E_8 &(8,248).
\end{array}
\]
For \(n=6,7,8\) this is the usual exceptional \(E\)-family. The notation for \(n=3,4,5\) is an extension convention, not a claim that those algebras are exceptional.

## Regular inclusions

A compatible choice of roots gives a chain of [[lie-groups/semisimple-lie-algebra|semisimple]] regular subalgebras
\[
\mathfrak{sl}_3\oplus\mathfrak{sl}_2
\subset\mathfrak{sl}_5
\subset\mathfrak{so}_{10}
\subset\mathfrak e_6
\subset\mathfrak e_7
\subset\mathfrak e_8.
\]
Combinatorially, successive terms are obtained by adding a node to a compatible [[lie-groups/dynkin-diagram|Dynkin diagram]], or in the reverse direction by deleting an appropriate node. The inclusions are additional structure: an abstract isomorphism class named in the table does not by itself select a particular embedded copy in the next algebra.

Useful adjacent branching patterns include
\[
\begin{aligned}
\mathfrak e_6&\downarrow\mathfrak{so}_{10}\oplus\mathbb C,
&\mathbf{78}&=\mathbf{45}_0\oplus\mathbf1_0
\oplus\mathbf{16}_{3}\oplus\mathbf{16}^*_{-3},\\
\mathfrak e_8&\downarrow\mathfrak e_7\oplus\mathfrak{sl}_2,
&\mathbf{248}&=(\mathbf{133},\mathbf1)\oplus(\mathbf1,\mathbf3)
\oplus(\mathbf{56},\mathbf2).
\end{aligned}
\]
Charge signs and the labeling of dual [[differential-geometry/spinor-module|spin modules]] depend on conventions.

## Lower indices and convention warning

Extensions below \(E_3\) are not uniform across the literature. A common convention sets \(E_2\) to \(A_1\) plus a one-dimensional abelian algebra and \(E_1=A_1\), but other contexts use different global groups, real forms, or extra \(U(1)\) factors. For this reason, a bare symbol \(E_n\) with \(n<6\) should be accompanied by an explicit algebra or group.

The table concerns **complex Lie algebras**. Compact group versions require choices of global form and sometimes finite [[lie-groups/central-quotient-of-a-lie-group|central quotients]]; one cannot recover those choices from a Dynkin diagram alone.

## Paper context

The three-generation construction uses the truncated chain
\[
\mathfrak{sl}_3\oplus\mathfrak{sl}_2
\subset\mathfrak{sl}_5\subset\mathfrak{so}_{10}
\subset\mathfrak e_6\subset\mathfrak e_7
\]
as a systematic root-removal framework. Its Standard Model algebra has an additional one-dimensional central summand, so \(\mathfrak g_{\mathrm{SM}}=\mathbb C\oplus\mathfrak{sl}_2\oplus\mathfrak{sl}_3\) is reductive rather than equal to the semisimple \(E_3\) term.

## References

1. Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 4--6*, Springer, 2002, Plates I and IV--VII. [Publisher record](https://doi.org/10.1007/978-3-540-89394-3).
2. John C. Baez and John Huerta, *Division Algebras and Supersymmetry II*, *Advances in Theoretical and Mathematical Physics* 15 (2011), 1373--1410, Section 3. [DOI](https://doi.org/10.4310/ATMP.2011.v15.n5.a3).
3. John C. Baez, *Three Generations in E7*, 2026. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).

+++
id = "differential-geometry/compactly-supported-differential-form"
title = "Compactly supported differential form"
kind = "definition"
summary = "A differential form whose nonzero locus has compact closure."
aliases = ["differential form with compact support", "compact-support differential form"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]] and let \(\omega\) be a [[fiber-bundles/differential-k-form|differential \(k\)-form]] on \(M\). Its support is
\[
\operatorname{supp}\omega=\overline{\{p\in M:\omega_p\ne0\}}.
\]
The form \(\omega\) is **compactly supported** if \(\operatorname{supp}\omega\) is a [[topology/compact-set|compact set]]. Thus it vanishes outside some compact subset of \(M\). The [[linear-algebra/vector-space|vector space]] of compactly supported \(k\)-forms is denoted \(\Omega_c^k(M)\). If \(M\) is compact, then every smooth differential form on \(M\) is compactly supported.

## Operations preserving compact support

The [[fiber-bundles/exterior-derivative|exterior derivative]] maps \(\Omega_c^k(M)\) to \(\Omega_c^{k+1}(M)\) because \(\operatorname{supp}(d\omega)\subseteq\operatorname{supp}\omega\). If \(\eta\) is any smooth form, then \(\eta\wedge\omega\) is compactly supported. Pullback along a [[fiber-bundles/smooth-map|smooth map]] need not preserve compact support, but pullback along a [[differential-geometry/proper-smooth-map|proper smooth map]] does.

## Integration and cohomology

On an oriented \(n\)-manifold, every \(\omega\in\Omega_c^n(M)\) has a well-defined finite integral, even when \(M\) is noncompact. The complex \((\Omega_c^\bullet(M),d)\) defines [[differential-geometry/compactly-supported-de-rham-cohomology|compactly supported de Rham cohomology]]. Compact support is also the hypothesis that removes contributions “at infinity” in the compact-support version of [[differential-geometry/stokes-theorem|Stokes' theorem]].

## Examples and boundary cases

If \(\varphi\) is a [[differential-geometry/bump-function|bump function]] and \(\eta\) is any differential form, then \(\varphi\eta\) is compactly supported. The standard volume form on \(\mathbb R^n\) is not compactly supported. On the manifold \(M=(0,1)\), the form \(dx\) is not compactly supported: its support is all of \(M\), which is not compact even though it is bounded as a subset of \(\mathbb R\).

## References

1. Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982. [DOI record](https://doi.org/10.1007/978-1-4757-3951-0). Relevant: de Rham theory, integration, and compact supports.
2. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: differential forms, integration on manifolds, and de Rham cohomology.

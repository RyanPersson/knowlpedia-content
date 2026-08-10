+++
id = "lie-groups/standard-sl5-in-e7"
title = "Standard sl5 in e7"
kind = "theorem"
summary = "There is a unique sl5 subalgebra between a good Standard Model algebra and the standard sl6, and it is regular in e7."
aliases = ["standard sl5", "Standard Model sl5 in e7", "sl5 SM"]
domains = ["lie-groups", "mathematical-physics"]
section_mode = "progressive"
+++

For a good embedded [[mathematical-physics/standard-model-lie-algebra|Standard Model Lie algebra]] and its [[lie-groups/standard-sl6-in-e7|standard \(\mathfrak{sl}_6\)]], there is a unique [[lie-groups/lie-subalgebra|Lie subalgebra]] \(\mathfrak s\cong\mathfrak{sl}_5(\mathbb C)\) such that
\[
\mathfrak g_{\mathrm{SM}}
\subset\mathfrak s
\subset\mathfrak{sl}_6^{\mathrm{SM}}.
\]
This \(\mathfrak s\) is [[lie-groups/regular-lie-subalgebra|regular]] in \(\mathfrak e_7\) and is called the **standard \(\mathfrak{sl}_5\)**, denoted \(\mathfrak{sl}_5^{\mathrm{SM}}\).

All displayed containments are Lie-subalgebra inclusions. In particular,
\[
\mathfrak g_{\mathrm{SM}}
\subset\mathfrak{sl}_5^{\mathrm{SM}}
\subset\mathfrak{sl}_6^{\mathrm{SM}}
\subset\mathfrak e_7
\]
is a chain, not a direct-sum decomposition.

## Root-system construction

Let \(\mathfrak h_{\mathrm{SM}}\) be the [[lie-groups/cartan-subalgebra|Cartan subalgebra]] of the regular \(\mathfrak g_{\mathrm{SM}}\), and let \(U\) be its real form in the \(E_7\) root space. The roots in \(\Phi(E_7)\cap U\) form an \(A_4\) subsystem of \(20\) roots, hence define a regular copy of [[lie-groups/complex-lie-algebra-sl5|\(\mathfrak{sl}_5\)]]. Since \(U\perp P\), this subsystem lies in the \(A_5\) roots of \(\mathfrak{sl}_6^{\mathrm{SM}}\).

## Why uniqueness does not require regularity

View the defining module of \(\mathfrak{sl}_6^{\mathrm{SM}}\) as \(\mathbb C^6\). Any embedded \(\mathfrak{sl}_5\subset\mathfrak{sl}_6\) acts as
\[
\mathbb C^6=W\oplus L,
\qquad \dim W=5,
\qquad \dim L=1,
\]
with \(W\) the defining module and \(L\) trivial. Under \(\mathfrak g_{\mathrm{SM}}\), the [[lie-groups/fixed-vector-subspace|fixed-vector subspace]] of the defining \(\mathbb C^6\) is exactly one line, so \(L\) is forced. The remaining irreducible \(3\)- and \(2\)-dimensional Standard Model summands admit no [[fiber-bundles/equivariant-map|equivariant map]] to \(L\), so their invariant complement \(W\), and hence the embedded \(\mathfrak{sl}(W)\), are forced as well.

## Physical representation-theory role

This is the Lie-algebra form of the [[mathematical-physics/georgi-glashow-su5-embedding|Georgi–Glashow \(SU(5)\) embedding]]. Restricting the generation modules through
\(\mathfrak{sl}_6^{\mathrm{SM}}\supset\mathfrak{sl}_5^{\mathrm{SM}}\supset\mathfrak g_{\mathrm{SM}}\) produces the [[mathematical-physics/standard-model-exterior-algebra-representation|exterior-algebra model of one Standard Model generation]].

## References

1. John C. Baez, “Three Generations in E7,” 2026, Proposition 8. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
2. Howard Georgi and Sheldon L. Glashow, “Unity of All Elementary-Particle Forces,” *Physical Review Letters* 32 (1974), 438–441. [DOI record](https://doi.org/10.1103/PhysRevLett.32.438).
3. John C. Baez and John Huerta, “The Algebra of Grand Unified Theories,” *Bulletin of the American Mathematical Society* 47 (2010), 483–552. [arXiv:0904.1556](https://arxiv.org/abs/0904.1556).

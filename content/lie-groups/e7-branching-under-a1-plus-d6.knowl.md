+++
id = "lie-groups/e7-branching-under-a1-plus-d6"
title = "E7 branching under A1 + D6"
kind = "theorem"
summary = "Under each generation sl2 plus so12 subalgebra, the adjoint module of e7 branches as (3,1) plus (1,66) plus (2,32)."
aliases = ["E7 to A1 D6 branching", "e7 under sl2 plus so12", "133 branching to 3 66 64"]
domains = ["lie-groups", "representation-theory", "mathematical-physics"]
section_mode = "progressive"
+++

For any one of the three mutually centralizing pairs
\[
\mathfrak m_k
=\mathfrak{sl}_2(\beta_k)\oplus\mathfrak{so}_{12}(\beta_k)
\subset\mathfrak e_7,
\]
the adjoint representation of \(\mathfrak e_7\), restricted to \(\mathfrak m_k\), has the [[lie-groups/branching-rule-for-lie-representations|branching rule]]
\[
\mathbf{133}
\;\downarrow_{A_1+D_6}
= (\mathbf 3,\mathbf 1)
\oplus(\mathbf 1,\mathbf{66})
\oplus(\mathbf 2,\mathbf{32}).
\]
Here \(\mathbf3\) and \(\mathbf2\) are respectively the adjoint and [[lie-groups/defining-representation-of-a-classical-lie-algebra|defining]] \(\mathfrak{sl}_2\)-modules, \(\mathbf{66}\) is the adjoint \(\mathfrak{so}_{12}\)-module, and \(\mathbf{32}\) is one [[lie-groups/half-spin-representation|half-spin representation]] of \(\mathfrak{so}_{12}\).

## What the direct sum means

Equivalently, as an \(\mathfrak m_k\)-module and hence as a vector space,
\[
\mathfrak e_7
=\mathfrak{sl}_2(\beta_k)
\oplus\mathfrak{so}_{12}(\beta_k)
\oplus(\mathbf2\otimes\mathbf{32}).
\]
The first two summands together form the Lie subalgebra \(\mathfrak m_k\). The \(64\)-dimensional last summand is an invariant module, not a Lie subalgebra and not asserted to be closed under the \(\mathfrak e_7\) bracket.

## Weight-space explanation

The roots not belonging to the \(A_1+D_6\) subsystem pair with \(\beta_k\) by \(\pm1\). Thus their root spaces form copies of the defining \(\mathfrak{sl}_2\)-module. Either \(\pm1\) eigenspace has dimension \(32\), with distinct equal-length \(D_6\) weights, identifying it as a half-spin module.

## Convention for 32

The two chiral half-spin representations of \(\mathfrak{so}_{12}\) are exchanged by a [[lie-groups/dynkin-diagram-automorphisms-and-dual-representations|Dynkin-diagram automorphism]] of \(D_6\). Calling the occurring module \(\mathbf{32}\) rather than \(\mathbf{32}'\) is therefore a convention; the branching rule is invariant after exchanging the two labels.

## References

1. John C. Baez, “Three Generations in E7,” 2026, Proposition 5. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
2. R. Slansky, “Group Theory for Unified Model Building,” *Physics Reports* 79 (1981), 1–128. [DOI record](https://doi.org/10.1016/0370-1573(81)90092-2).
3. E. B. Dynkin, “Semisimple Subalgebras of Semisimple Lie Algebras,” *American Mathematical Society Translations*, Series 2, 6 (1957), 111–244.

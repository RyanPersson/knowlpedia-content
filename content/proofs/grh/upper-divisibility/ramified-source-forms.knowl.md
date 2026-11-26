+++
id = "proofs/grh/upper-divisibility/ramified-source-forms"
title = "Ramified source forms"
kind = "definition"
summary = "The source forms whose mean under the powers of the scaling generator at each prime dividing pi_N is zero."
aliases = ["ramified source form", "central representation on source forms", "ramifying operator"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.ramifiedSourceForms", "New.Data.centralRep", "New.algFormCentralRep", "New.Data.ramifyingOp"]
lean_files = ["src/New/UpperBound/Size/ShortColumns.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] and let \(\mathcal S\) be the complex vector space of [[?lean:New.Data.SourceForm|source forms]]: the algebraic forms on the finite adelic unitary group of \(X_0\), of the weight of \(X_0\), fixed under right translation by the [[?lean:New.Data.levelX|level of stage \(0\)]]. A norm-one finite adele \(z\in U(1)(\mathbb{A}_f)\) acts on \(\mathcal S\) by right translation by its scalar matrix, \((z\varphi)(g)=\varphi(g\,z)\) (scalar matrices commute with the level, so \(\mathcal S\) is preserved); this is the **central representation**. For each of the primes \(w\mid\pi_N\) let \(z_w\) be the [[proofs/grh/upper-divisibility/scaling-generator|scaling generator]]. The space of **ramified source forms** is
\[
\mathcal S^{\mathrm{ram}}\;=\;\Bigl\{\varphi\in\mathcal S:\ \sum_{i=0}^{N-2}z_w^{\,i}\varphi=0\ \text{for every prime }w\mid\pi_N\Bigr\}.
\]
For a set \(s\) of primes dividing \(\pi_N\), the **ramifying operator** is \(R_s=\prod_{w\in s}(1-z_w)\) acting on \(\mathcal S\).

## Remarks

Since \(z_w^{N-1}\) lies in the level, \(z_w\) acts on \(\mathcal S\) with order dividing \(N-1\), and the condition says that \(\varphi\) has no component on which the character of \((\mathcal O_E/w)^\times\) through which \(z_w\) acts is trivial: \(\varphi\) is "ramified at \(w\)". See [[proofs/grh/upper-divisibility/ramified-source-forms-are-the-image-of-the-ramifying-operator|the description as an image]].

## References

1. Lean: `New.Data.ramifiedSourceForms`, `New.Data.centralRep`, `New.Data.ramifyingOp` in `src/New/UpperBound/Size/ShortColumns.lean`.

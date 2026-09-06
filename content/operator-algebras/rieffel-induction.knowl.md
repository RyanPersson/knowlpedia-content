+++
id = "operator-algebras/rieffel-induction"
title = "Rieffel induction"
kind = "definition"
summary = "The representation of one C-star algebra obtained by tensoring a correspondence with a representation of its coefficient algebra."
aliases = ["induction by a Hilbert C*-module", "induced representation via correspondence"]
domains = ["operator-algebras", "algebra-representation-theory"]
prerequisites = ["operator-algebras/cstar-correspondence", "operator-algebras/nondegenerate-cstar-representation", "operator-algebras/internal-tensor-product-correspondences", "linear-algebra/inner-product"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(E\) be a
[[operator-algebras/cstar-correspondence|\(C^*\)-correspondence]] from \(A\)
to \(B\), with left action
\(\varphi:A\to\mathcal L_B(E)\), and let
\(\pi:B\to\mathcal B(H_\pi)\) be a
[[operator-algebras/nondegenerate-cstar-representation|nondegenerate
representation]].
**Rieffel induction through \(E\)** is the representation of \(A\) on the
[[operator-algebras/internal-tensor-product-correspondences|internal tensor
product]] \(E\otimes_\pi H_\pi\) defined by
\[
\operatorname{Ind}_E(\pi)(a)(\xi\otimes h)
=(\varphi(a)\xi)\otimes h.
\]
Here \(E\otimes_\pi H_\pi\) is obtained by balancing
\(\xi b\otimes h=\xi\otimes\pi(b)h\), quotienting the null space of its
induced [[linear-algebra/inner-product|inner product]], and completing. Adjointability of \(\varphi(a)\)
makes the formula well defined and bounded.

## Action on intertwiners

If \(T:H_\pi\to H_\rho\) intertwines two representations of \(B\), then
\[
1_E\otimes T:E\otimes_\pi H_\pi\longrightarrow E\otimes_\rho H_\rho
\]
intertwines their [[algebra-representation-theory/induced-representation|induced representations]]. Induction therefore acts
functorially on [[operator-algebras/nondegenerate-star-homomorphism|nondegenerate representation]] categories and preserves
unitary equivalence. Tensor-product associativity identifies induction
through a composite correspondence with successive induction.

## Imprimitivity theorem

When \(E\) is an
[[operator-algebras/imprimitivity-bimodule|\(A\)-\(B\) imprimitivity
bimodule]], Rieffel induction is an equivalence between the categories of
nondegenerate representations of \(B\) and \(A\). Induction through the
conjugate bimodule \(\widetilde E\) is a quasi-inverse. Consequently, strong
Morita equivalence preserves the representation-theoretic structure encoded
by ideals and [[algebra-representation-theory/irreducible-representation|irreducible representations]].

## Examples and scope

For the identity \(B\)-\(B\) correspondence \(E=B\), the map
\(b\otimes h\mapsto\pi(b)h\) identifies
\(\operatorname{Ind}_B(\pi)\) with \(\pi\). For a full Hilbert \(B\)-module
\(E\), induction implements the equivalence between \(B\) and
\(\mathcal K_B(E)\).

**Warning.** A general correspondence still defines induction, but need not
give an equivalence: a nonfaithful left action can annihilate part of \(A\),
and lack of fullness can lose representations of \(B\).

## References

1. Marc A. Rieffel, “Induced representations of C*-algebras,” *Advances in Mathematics* 13 (1974), 176–257. [DOI record](https://doi.org/10.1016/0001-8708%2874%2990068-1). Relevant: §§2–6 on Hilbert modules, induction, and the imprimitivity theorem.
2. Iain Raeburn and Dana P. Williams, *Morita Equivalence and Continuous-Trace C*-Algebras*, American Mathematical Society, 1998. [AMS DOI record](https://doi.org/10.1090/surv/060). Relevant: Chapter 3 on induced representations and Morita equivalence.

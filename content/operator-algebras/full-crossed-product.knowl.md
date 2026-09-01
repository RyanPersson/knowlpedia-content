+++
id = "operator-algebras/full-crossed-product"
title = "Full crossed product"
kind = "definition"
summary = "The universal C*-completion of the convolution algebra of a C*-dynamical system."
aliases = ["universal crossed product", "maximal crossed product"]
domains = ["operator-algebras", "dynamical-systems"]
prerequisites = ["operator-algebras/cstar-dynamical-system", "operator-algebras/crossed-product-convolution-star-algebra", "operator-algebras/covariant-representation-cstar-dynamical-system", "operator-algebras/integrated-form-covariant-representation"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

For a [[operator-algebras/cstar-dynamical-system|\(C^*\)-dynamical system]] \((A,G,\alpha)\), define on the [[operator-algebras/crossed-product-convolution-star-algebra|convolution \(*\)-algebra \(C_c(G,A)\)]]
\[
\|f\|_{\mathrm u}
=\sup_{(\pi,U)}\|(\pi\rtimes U)(f)\|,
\]
where the supremum ranges over all [[operator-algebras/covariant-representation-cstar-dynamical-system|covariant representations]] and \(\pi\rtimes U\) denotes their [[operator-algebras/integrated-form-covariant-representation|integrated forms]]. The **full crossed product**, written \(A\rtimes_\alpha G\), is the completion of \(C_c(G,A)\) in this universal \(C^*\)-norm. It retains all covariant representations, rather than selecting only the regular ones.

## Universal property

There are canonical nondegenerate maps \(i_A:A\to M(A\rtimes_\alpha G)\) and \(i_G:G\to\mathcal U(M(A\rtimes_\alpha G))\) forming a covariant pair, and the linear span of
\[
i_A(a)\int_G f(s)i_G(s)\,ds
\]
is dense as \(a\) and \(f\) vary. Every covariant pair \((\pi,U)\) factors uniquely through a [[operator-algebras/nondegenerate-star-homomorphism|nondegenerate representation]] of \(A\rtimes_\alpha G\). In this sense the full crossed product is a [[operator-algebras/universal-cstar-algebra|universal \(C^*\)-algebra]] for covariant representations.

## Relation to the reduced completion

Every [[operator-algebras/regular-covariant-representation|regular covariant representation]] contributes to the universal norm, so the identity on \(C_c(G,A)\) extends to a canonical surjective \(*\)-homomorphism onto the [[operator-algebras/reduced-crossed-product|reduced crossed product]]:
\[
A\rtimes_\alpha G\longrightarrow A\rtimes_{\alpha,r}G.
\]
This map need not be injective. If \(G\) is [[harmonic-analysis/amenable-locally-compact-group|amenable]], it is an isomorphism for every action; equality for one particular action does not by itself imply that \(G\) is amenable.

## Standard cases

For \(A=\mathbb C\) with the trivial action, the full crossed product is the [[operator-algebras/full-group-cstar-algebra|full group \(C^*\)-algebra]] \(C^*(G)\). For a trivial action on general \(A\), it is canonically the [[operator-algebras/maximal-cstar-tensor-product|maximal \(C^*\)-tensor product]] \(A\otimes_{\max}C^*(G)\). If \(G\) is discrete, the dense algebraic core consists of finite sums \(\sum_s a_su_s\) with relations \(u_sau_s^*=\alpha_s(a)\).

## Conventions and scope

The adjective “full” is synonymous with “universal” or “maximal” in this context. It must not be confused with the reduced crossed product, even when the two happen to be isomorphic. For nondiscrete \(G\), the canonical group unitaries and often the coefficient algebra live naturally in the [[operator-algebras/multiplier-algebra|multiplier algebra]] rather than inside the crossed product itself.

## References

1. Dana P. Williams, Crossed Products of \(C^*\)-Algebras, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: §2.3, Lemma 2.27 on the universal norm, and §2.6 on the universal property.
2. Gert K. Pedersen, \(C^*\)-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §7.6 on covariant representations and crossed products.

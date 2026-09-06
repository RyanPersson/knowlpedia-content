+++
id = "langlands/global-langlands-parameter"
title = "Global Langlands parameter"
kind = "knowl"
summary = "A conjectural global admissible homomorphism into an L-group whose localizations are local Langlands parameters."
aliases = ["global L-parameter", "global Langlands parameterization"]
domains = ["langlands", "number-theory", "representation-theory"]
section_mode = "progressive"
prerequisites = ["langlands-letter/knowls/global-local-fields-completions", "algebraic-geometry-foundations/reductive-algebraic-group", "langlands/l-group", "algebra-groups/conjugacy-class", "algebra-fields-galois/place-of-global-field", "langlands/local-l-parameter"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(F\) be a
[[langlands-letter/knowls/global-local-fields-completions|global field]] and
\(G\) a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
\(F\)-group]]. In
the conjectural Langlands formalism, a **global Langlands parameter** is an
admissible homomorphism

\[
\varphi:\mathcal L_F\longrightarrow {}^L G
\]

from a global Langlands group \(\mathcal L_F\) to the
[[langlands/l-group|\(L\)-group]], considered up to
[[algebra-groups/conjugacy-class|conjugacy]] by \(\widehat G\). For every
[[algebra-fields-galois/place-of-global-field|place]] \(v\),
localization should produce a
[[langlands/local-l-parameter|local \(L\)-parameter]]
\(\varphi_v\).

## Number-field status

For a number field, the required group \(\mathcal L_F\) has not been
constructed in the generality demanded by the program. The display is
therefore a conjectural organizing language, not an available definition of
a concrete [[topology/topological-group|topological group]].

Different realizations retain different parts of the expected parameter:
complex representations of hypothetical Langlands groups, motivic Galois
groups, and [[langlands/compatible-system-of-galois-representations|compatible systems]] of \(\ell\)-adic Galois representations are
related but are not interchangeable without hypotheses.

## Function-field status

For a global function field, the
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois group]]
is concrete.
Vincent Lafforgue's [[langlands/excursion-operator|excursion operators]] attach semisimple
\(\widehat G\)-valued global Galois parameters to
[[langlands/cuspidal-automorphic-representation|cuspidal automorphic data]].
This is a major theorem, but it does not turn the entire general packet and
multiplicity formalism into a literal bijection.

## Expected information

A global parameter should determine compatible
[[langlands/l-packet|local packets]]
\(\Pi_{\varphi_v}\), global \(L\)-functions, and a global packet inside the
[[langlands/restricted-tensor-product-automorphic-representation|restricted
product]] of the local packets. A multiplicity formula is then
needed to decide which tensor products occur automorphically and with what
multiplicity.

## Tempered and Arthur parameters

A bounded global Langlands parameter is expected to describe tempered
automorphic phenomena. The discrete spectrum also contains non-tempered
representations, for which an [[langlands/arthur-parameter|Arthur parameter]]
adds an \(\operatorname{SL}_2(\mathbb C)\)-factor. The two parameter notions
must not be conflated.

## References

1. James Arthur, “A note on the automorphic Langlands group,” *Canadian
   Mathematical Bulletin* 45 (2002), 466–482.
   [DOI](https://doi.org/10.4153/CMB-2002-051-0).
2. Vincent Lafforgue, “Chtoucas pour les groupes réductifs et paramétrisation
   de Langlands globale,” *Journal of the American Mathematical Society* 31
   (2018), 719–891. [arXiv](https://arxiv.org/abs/1209.5352).

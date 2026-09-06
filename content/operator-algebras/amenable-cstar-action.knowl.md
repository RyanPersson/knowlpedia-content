+++
id = "operator-algebras/amenable-cstar-action"
title = "Amenable action on a C*-algebra"
kind = "definition"
summary = "A C*-dynamical action admitting an equivariant conditional mean after passage to the bidual."
aliases = ["amenable C*-dynamical system", "amenable group action"]
domains = ["operator-algebras", "dynamical-systems"]
prerequisites = ["operator-algebras/cstar-dynamical-system", "lie-groups/left-translation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((A,G,\alpha)\) be a [[operator-algebras/cstar-dynamical-system| \(C^*\)-dynamical system]]. In the Anantharaman-Delaroche convention,
\(\alpha\) is an **amenable action** if its normal extension to \(A^{**}\)
admits a \(G\)-equivariant conditional mean
\[
E:L^\infty(G)\,\bar\otimes\,A^{**}\longrightarrow A^{**}
\]
with \(E(1\otimes x)=x\). Here \(G\) acts diagonally: by [[lie-groups/left-translation|left translation]] on
\(L^\infty(G)\) and by \(\alpha^{**}\) on \(A^{**}\). The map \(E\) is
required to be unital, completely positive, and contractive. This is
amenability of the action, not merely amenability of the acting group; the
coefficient algebra participates essentially in the averaging process.

## Crossed-product consequence

Amenability makes the [[algebra-representation-theory/regular-representation|regular representation]] faithful: the canonical
surjection
\[
A\rtimes_\alpha G\longrightarrow A\rtimes_{\alpha,r}G
\]
from the [[operator-algebras/full-crossed-product|full crossed product]] to
the [[operator-algebras/reduced-crossed-product|reduced crossed product]] is
an isomorphism. The converse requires care: equality of these two
completions for a particular action is generally called weak containment
and need not, without extra hypotheses, imply amenability.

If \(G\) itself is amenable, every action of \(G\) is amenable. Conversely,
the trivial action on \(\mathbb C\) is amenable exactly when \(G\) is
amenable.

## Commutative and discrete pictures

For a countable discrete \(G\) acting on a locally compact [[topology/hausdorff-space|Hausdorff space]]
\(X\), the definition for \(A=C_0(X)\) agrees with topological amenability of
the action, equivalently amenability of the transformation groupoid
\(G\ltimes X\). In the discrete case it can also be expressed by
approximately equivariant, positive-type functions with coefficients in the
center of \(A^{**}\). These formulations explain why an action of a
nonamenable group may still be amenable.

## Conventions and scope

Several nonequivalent notions are called amenability for actions outside the
standard hypotheses: measurewise amenability, topological amenability,
strong amenability, and variants for exact or nonunital systems. A theorem
should specify its convention. The conditional-mean formulation above is
the one used for \(C^*\)-dynamical systems here.

## References

1. Claire Anantharaman-Delaroche and Jean Renault, *Amenable Groupoids*, Monographies de L’Enseignement Mathématique 36, Geneva, 2000. [Publisher record](https://www.unige.ch/math/EnsMath/en/monographies/monographie-no-36). Relevant: Chapter 3 on amenable actions and their operator-algebraic consequences.
2. Nathanial P. Brown and Narutaka Ozawa, *\(C^*\)-Algebras and Finite-Dimensional Approximations*, Graduate Studies in Mathematics 88, American Mathematical Society, 2008. [AMS DOI record](https://doi.org/10.1090/gsm/088). Relevant: Chapter 4 on amenable actions and crossed products.

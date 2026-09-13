+++
id = "measure-theory/measure-completion"
title = "Completion of a measure space"
kind = "definition"
summary = "The extension that makes all subsets of existing null sets measurable."
aliases = ["completion of a measure"]
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/complete-measure", "measure-theory/sigma-algebra", "shared-foundations/set-difference"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **completion** of \((X,\Sigma,\mu)\) uses the sigma-algebra
\[
\overline\Sigma=\{E\subseteq X:A\subseteq E\subseteq B
\text{ for some }A,B\in\Sigma\text{ with }\mu(B\setminus A)=0\}.
\]
Set \(\overline\mu(E)=\mu(A)\) for any such pair. This is well-defined because any two lower approximations differ only by null sets, and \(\overline\mu\) extends \(\mu\). It makes the space [[measure-theory/complete-measure|complete]].

## Lebesgue measure

Completing Borel Lebesgue measure adds all subsets of Borel null sets. Likewise, completing the product of one-dimensional Lebesgue measures gives full Lebesgue measure in the product Euclidean space. Completion changes the measurable sets but not the values on sets measurable before the extension.

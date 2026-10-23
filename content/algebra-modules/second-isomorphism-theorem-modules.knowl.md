+++
id = "algebra-modules/second-isomorphism-theorem-modules"
title = "Second isomorphism theorem for modules"
kind = "knowl"
summary = "For submodules A,B ≤ M, one has (A+B)/B ≅ A/(A∩B)."
aliases = ["second-isomorphism-theorem-modules", "Second isomorphism theorem for modules"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/second-isomorphism-theorem-modules.md"
prerequisites = ["algebra-modules/submodule", "shared-foundations/intersection", "algebra-modules/quotient-module", "algebra-modules/first-isomorphism-theorem-modules"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Second isomorphism theorem (modules)**: Let \(M\) be an \(R\)-module and let \(A,B\) be [[algebra-modules/submodule|submodules]] of \(M\). Then there is a natural isomorphism of \(R\)-modules
\[
(A+B)/B \;\cong\; A/(A\cap B),
\]
where \(A\cap B\) is the [[shared-foundations/intersection|intersection]] and each quotient is a [[algebra-modules/quotient-module|quotient module]].

In the square below, the composite \(A\hookrightarrow A+B\twoheadrightarrow (A+B)/B\) is surjective with kernel \(A\cap B\), and this induces the bottom isomorphism:

```tikz-cd
A \arrow[r, hook] \arrow[d, two heads] & A+B \arrow[d, two heads] \\
A/(A\cap B) \arrow[r, "\cong"] & (A+B)/B
```

This isomorphism is obtained by restricting the quotient map \(M\to M/B\) to \(A\), and it is a standard application of the [[algebra-modules/first-isomorphism-theorem-modules|first isomorphism theorem]].

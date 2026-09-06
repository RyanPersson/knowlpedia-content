+++
id = "functional-analysis/banach-algebra-spectral-radius-formula"
title = "Spectral radius formula for a Banach algebra"
kind = "theorem"
summary = "The spectral radius of a Banach-algebra element is the asymptotic growth rate of the norms of its powers."
aliases = ["Gelfand spectral radius formula", "Beurling formula", "spectral radius formula"]
domains = ["functional-analysis", "operator-algebras"]
prerequisites = ["functional-analysis/banach-algebra", "functional-analysis/banach-algebra-spectral-radius"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a complex [[functional-analysis/banach-algebra|Banach algebra]] and \(a\in A\). The **spectral radius formula** states that the [[functional-analysis/banach-algebra-spectral-radius|spectral radius]] of \(a\) satisfies
\[
r_A(a)=\lim_{n\to\infty}\lVert a^n\rVert^{1/n}
=\inf_{n\geq1}\lVert a^n\rVert^{1/n}.
\]
If \(A\) is nonunital, \(r_A(a)\) means the spectral radius computed in its unitization. The limit exists because \(\lVert a^{m+n}\rVert\leq\lVert a^m\rVert\lVert a^n\rVert\), so the logarithms form a subadditive sequence. The formula identifies spectral size with asymptotic power growth.

## Proof idea

The inequality \(r_A(a)\leq\lVert a^n\rVert^{1/n}\) follows by applying the
[[operator-algebras/spectral-mapping-theorem|spectral mapping theorem]]:
\(\sigma_A(a^n)=\{\lambda^n:\lambda\in\sigma_A(a)\}\). Conversely, the
resolvent expansion
\[
(\lambda1_A-a)^{-1}
=\sum_{n=0}^{\infty}\lambda^{-n-1}a^n
\]
converges whenever \(|\lambda|\) exceeds the limiting power-growth rate.
Hence no spectral point can lie outside the corresponding disk.

## Consequences and examples

An element is quasinilpotent exactly when
\(\lVert a^n\rVert^{1/n}\to0\). For a normal element \(a\) of a
\(C^*\)-algebra, \(\lVert a^n\rVert=\lVert a\rVert^n\), so
\(r_A(a)=\lVert a\rVert\). In contrast, a nonzero nilpotent matrix has
spectral radius zero although its norm is positive, showing why
\(r_A(a)=\lVert a\rVert\) fails for general elements.

## Conventions and scope

The limit concerns the \(n\)-th roots of norms, not the sequence
\(\lVert a^n\rVert\) itself. The equality with the infimum is an application
of the subadditive lemma after taking logarithms, with zero powers handled
separately. Over a real Banach algebra, the usual spectral radius is defined
after complexification; the core theorem is stated directly for complex
algebras.

## References

1. Gerard J. Murphy, *\(C^*\)-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: Theorem 1.2.3 on the spectral radius formula.
2. F. Bonsall and J. Duncan, *Complete Normed Algebras*, Springer, 1973. [DOI record](https://doi.org/10.1007/978-3-642-65669-9). Relevant: “Concepts and Elementary Results” on spectra and the spectral radius in complete normed algebras.

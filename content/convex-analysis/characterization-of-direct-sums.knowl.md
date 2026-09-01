+++
id = "convex-analysis/characterization-of-direct-sums"
title = "Characterization of direct sums"
kind = "knowl"
summary = "A sum is direct iff every element has a unique decomposition into components"
aliases = ["characterization-of-direct-sums", "Characterization of direct sums"]
domains = ["convex-analysis"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "convex-analysis/characterization-of-direct-sums.md"
+++

**Theorem.**
Let \(M\) and \(N\) be linear subspaces of a vector space \(Y\). Then
\[
Y=M\oplus N
\]

if and only if every \(y\in Y\) admits a **unique** representation
\[
y=a+b \quad\text{with } a\in M,\ b\in N.
\]

## Remarks

**Context.** This result explains why [[convex-analysis/direct-sum-of-subspaces|direct sums]] behave like "coordinate decompositions" with respect to the two subspaces.

**Proof sketch.**
- (\(\Rightarrow\)) If \(y=a+b=a'+b'\), then \(a-a'=b'-b\in M\cap N=\{0\}\), so \(a=a'\) and \(b=b'\).
- (\(\Leftarrow\)) Existence gives \(Y=M+N\), since \(M,N\subseteq Y\). Uniqueness gives \(M\cap N=\{0\}\): if \(x\in M\cap N\), then \(x=x+0=0+x\), so \(x=0\).

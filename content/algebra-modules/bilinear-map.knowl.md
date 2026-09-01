+++
id = "algebra-modules/bilinear-map"
title = "Bilinear map"
kind = "definition"
summary = "A map of modules that is linear in each variable; over a noncommutative ring, tensor products instead represent biadditive balanced maps."
aliases = ["bilinear-map", "Bilinear map"]
domains = ["algebra-modules"]
prerequisites = ["algebra-rings/commutative-ring", "shared-foundations/cartesian-product"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-modules/bilinear-map.md"
+++

A **bilinear map** between \(R\)-modules (for a [[algebra-rings/commutative-ring|commutative ring]] \(R\)) is a function \(\beta\colon M\times N\to P\) from a [[shared-foundations/cartesian-product|cartesian product]] of \(R\)-modules such that, for each fixed argument, the resulting map is \(R\)-linear in the other:
\[
\beta(m+m',n)=\beta(m,n)+\beta(m',n),\quad \beta(m,n+n')=\beta(m,n)+\beta(m,n'),
\]
\[
\beta(rm,n)=r\,\beta(m,n),\quad \beta(m,rn)=r\,\beta(m,n).
\]

## Balanced maps for tensor products

Let \(R\) be an arbitrary ring, let \(M\) be a right \(R\)-module, let \(N\)
be a left \(R\)-module, and let \(A\) be an abelian group. A map
\(\beta:M\times N\to A\) is **\(R\)-balanced** if it is additive in each
variable and
\[
\beta(mr,n)=\beta(m,rn)
\]
for every \(m\in M\), \(n\in N\), and \(r\in R\). No \(R\)-module structure
on \(A\) is required.

These biadditive balanced maps are the maps represented by the
[[algebra-modules/tensor-product-universal-property|universal property of the tensor product]]:
they correspond uniquely to homomorphisms of abelian groups
\[
M\otimes_RN\longrightarrow A.
\]
Thus ordinary \(R\)-bilinearity over a commutative ring and balancedness for
a right-left module pair are related but distinct notions.

## Examples

- For any [[algebra-rings/ring|ring]] \(R\), multiplication
  \(\mu:R\times R\to R\) is biadditive and \(R\)-balanced when its codomain is
  viewed as an abelian group. If \(R\) is commutative, multiplication is also
  \(R\)-bilinear in the sense of the first definition.
- For a commutative ring \(R\) and an \(R\)-module \(M\), the evaluation pairing \(M^\vee\times M\to R\) is bilinear, where \(M^\vee\) is the [[algebra-modules/dual-module|dual module]].

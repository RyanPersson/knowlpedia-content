+++
id = "algebra-modules/tensor-product-universal-property"
title = "Universal property of the tensor product"
kind = "knowl"
summary = "Balanced bilinear maps out of M×N correspond to linear maps out of M⊗N."
aliases = ["tensor-product-universal-property", "Universal property of the tensor product"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/tensor-product-universal-property.md"
prerequisites = ["algebra-modules/bilinear-map", "algebra-modules/module-homomorphism"]
dependency_heuristic = "semantic-spotcheck-review-v1"
dependency_review_count = 2
+++

Let \(R\) be a ring, \(M\) a right \(R\)-module, and \(N\) a left \(R\)-module. A pair \((T,\tau)\) has the **universal property of the tensor product** if \(T\) is an abelian group, \(\tau\colon M\times N\to T\) is biadditive and balanced,
\[
\tau(mr,n)=\tau(m,rn),
\]
and every biadditive balanced map \(f\colon M\times N\to A\) to an abelian group \(A\) factors uniquely through a homomorphism \(\overline f:T\to A\).

When such \((T,\tau)\) exists, it is unique up to unique isomorphism; one writes \(T=M\otimes_R N\) and \(\tau(m,n)=m\otimes n\), producing the [[algebra-modules/tensor-product|tensor product]]. The universal property is the mechanism that turns bilinear constructions into linear ones (i.e. [[algebra-modules/module-homomorphism|module homomorphisms]], when the target has compatible structure).

## Examples

- The canonical pairing \(M\times R\to M\), \((m,r)\mapsto mr\), induces a natural isomorphism \(M\otimes_R R\cong M\).
- Any balanced bilinear pairing \(M\times N\to P\) factors uniquely as \(M\times N\to M\otimes_R N\to P\).

+++
id = "algebra-modules/tensor-product-universal-property-prop"
title = "Tensor product universal property"
kind = "knowl"
summary = "The tensor product represents balanced bilinear maps out of a pair of modules."
aliases = ["tensor-product-universal-property-prop", "Tensor product universal property"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/tensor-product-universal-property-prop.md"
prerequisites = ["algebra-modules/tensor-product", "algebra-modules/bilinear-map", "algebra-modules/tensor-product-universal-property"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(M\) be a right \(R\)-module and \(N\) a left \(R\)-module. There is an abelian group \(M\otimes_R N\) and a biadditive map
\[
\tau:M\times N\longrightarrow M\otimes_R N
\]
satisfying \(\tau(mr,n)=\tau(m,rn)\). For every abelian group \(A\) and every biadditive map \(b:M\times N\to A\) satisfying \(b(mr,n)=b(m,rn)\), there is a unique group homomorphism \(\phi:M\otimes_R N\to A\) such that \(b=\phi\circ\tau\).

This is the standard representing property of the [[algebra-modules/tensor-product|tensor product]], packaging [[algebra-modules/bilinear-map|bilinear maps]] into a universal object; compare [[algebra-modules/tensor-product-universal-property|the tensor product universal property]].

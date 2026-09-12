+++
id = "algebra-rings/quaternion-real-place-ramification"
title = "Ramification of a quaternion algebra at a real place"
kind = "definition"
summary = "The real scalar extension is Hamilton’s division algebra rather than a matrix algebra."
aliases = ["real ramification of a quaternion algebra"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/quaternion-algebra", "algebra-fields-galois/field-embedding", "algebra-modules/tensor-product-algebras", "linear-algebra/quaternion-division-algebra"]
+++

Let \(B\) be a quaternion algebra over a number field \(K\), and \(\sigma:K\hookrightarrow\mathbb R\) a real embedding. Then \(B\) is **ramified at the real place \(\sigma\)** if
\[
B\otimes_{K,\sigma}\mathbb R\cong\mathbb H,
\]
the [[linear-algebra/quaternion-division-algebra|Hamilton division algebra]]. Otherwise this scalar extension is \(M_2(\mathbb R)\), and the algebra is split at that place. The tensor product uses \(\sigma\) for the \(K\)-algebra structure on \(\mathbb R\).

## Sign test

For \(B=(a,b)_K\), ramification at \(\sigma\) is equivalent to \(\sigma(a)<0\) and \(\sigma(b)<0\). Rescaling the generators reduces that case to \((-1,-1)_{\mathbb R}\). If either parameter is positive, its square root yields a split presentation.

## Arithmetic significance

An imaginary quadratic field has no real embeddings, so “ramified at all real places” is vacuous there. This is why its split quaternion algebra is allowed in the [[lie-groups/arithmetic-kleinian-group|arithmetic Kleinian construction]].

## References

1. F. W. Gehring, C. Maclachlan, G. J. Martin, and A. W. Reid, *Arithmeticity, discreteness and volume*, Transactions of the AMS 349 (1997). [Author-hosted paper](https://math.rice.edu/~ar99/ADV.pdf), §4, Lemma 4.1.

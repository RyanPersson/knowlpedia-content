+++
id = "lie-groups/bianchi-group-arithmeticity"
title = "Arithmeticity of Bianchi groups"
kind = "theorem"
summary = "A Bianchi group is the projective norm-one group of the full matrix order over an imaginary quadratic number ring."
aliases = []
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/bianchi-group", "lie-groups/arithmetic-kleinian-group", "algebra-rings/quaternion-order", "algebra-groups/quaternion-order-norm-one-group"]
+++

Every [[algebra-groups/bianchi-group|Bianchi group]] is an [[lie-groups/arithmetic-kleinian-group|arithmetic Kleinian group]]. Specifically, for an imaginary quadratic field \(K\), take
\[
B=M_2(K),\qquad\mathcal O=M_2(\mathcal O_K).
\]
Then \(\mathcal O^1=\operatorname{SL}_2(\mathcal O_K)\), whose projective image is the Bianchi group.

## Verification of the defining conditions

The field \(K\) has exactly one pair of complex embeddings and no real embeddings. Therefore the condition of ramification at every real place imposes no restriction. The algebra is split, the matrix order is full and finitely generated, and the reduced norm is the determinant. The complex embedding is obtained by applying \(K\hookrightarrow\mathbb C\) to each matrix entry.

Discreteness is supplied by the [[lie-groups/bianchi-group-nonuniform-lattice|Bianchi lattice theorem]], independently of this identification of the arithmetic data.

## References

1. F. W. Gehring, C. Maclachlan, G. J. Martin, and A. W. Reid, *Arithmeticity, discreteness and volume*, Transactions of the AMS 349 (1997). [Author-hosted paper](https://math.rice.edu/~ar99/ADV.pdf), §4, arithmetic-group construction.

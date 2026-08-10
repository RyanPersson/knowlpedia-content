+++
id = "nonassociative-algebra/automorphism-transitivity-on-jordan-frames"
title = "Automorphism transitivity on Jordan frames"
kind = "theorem"
summary = "The identity component of the automorphism group of a simple Euclidean Jordan algebra acts transitively on its ordered Jordan frames."
aliases = ["transitivity on Jordan frames", "Jordan frame homogeneous space", "automorphism action on Jordan frames"]
domains = ["nonassociative-algebra", "lie-groups"]
section_mode = "progressive"
+++

Let \(J\) be a simple
[[nonassociative-algebra/euclidean-jordan-algebra|Euclidean Jordan algebra]],
and let \(K=\operatorname{Aut}(J)^{\circ}\) be the
[[lie-groups/identity-component-of-a-lie-group|identity component]] of its
automorphism group. Then \(K\) acts transitively on ordered
[[nonassociative-algebra/jordan-frame|Jordan frames]]: for any two frames

\[
(c_1,\ldots,c_r),\qquad(d_1,\ldots,d_r),
\]

there is \(k\in K\) satisfying \(k(c_i)=d_i\) for every \(i\).

## Homogeneous frame space

Fix an ordered frame \(\mathbf c=(c_1,\ldots,c_r)\). Its space of ordered
frames is therefore the homogeneous space

\[
K/K_{\mathbf c},
\qquad
K_{\mathbf c}=\{k\in K:k(c_i)=c_i\text{ for every }i\}.
\]

Here \(K_{\mathbf c}\) is the **pointwise** stabilizer of all labelled frame
entries. This transitivity is what lets the Jordan spectral theorem move a
diagonalization from one chosen frame to any other convenient frame.

## Ordered, unordered, and connected stabilizers

If the same frame is regarded as the unordered set
\(C=\{c_1,\ldots,c_r\}\), its setwise stabilizer is

\[
K_C=\{k\in K:k(C)=C\}.
\]

There is a homomorphism \(K_C\to S_r\) recording the permutation of the frame
entries, and its kernel is \(K_{\mathbf c}\). Thus a setwise stabilizer may be
strictly larger than the pointwise stabilizer even though the acting group
\(K\) is connected. Moreover, the identity component \((K_C)^{\circ}\) lies
in \(K_{\mathbf c}\), but the pointwise stabilizer itself need not be replaced
by its identity component without a separate connectedness argument.

For the Albert algebra \(H_3(\mathbb O)\), \(K=F_4\), the pointwise stabilizer
of a labelled frame is \(\mathrm{Spin}(8)\), while the setwise stabilizer also
contains permutations of the three idempotents. This is the distinction used
in the [[nonassociative-algebra/spin8-stabilizer-of-an-albert-algebra-frame|Albert
frame-stabilizer theorem]].

## Scope of the theorem

Simplicity is part of the statement. A general Euclidean Jordan algebra is a
direct sum of simple ideals, and its automorphisms must respect the resulting
factor structure up to permutations of isomorphic factors. Frame-orbit
statements in that setting therefore require keeping track of which primitive
idempotents belong to which simple ideal.

## References

1. Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones*, Oxford
   University Press, 1994, Chapter IV, Theorem 2.5. [Publisher record](https://doi.org/10.1093/oso/9780198534778.001.0001).
2. John F. Adams, *Lectures on Exceptional Lie Groups*, University of Chicago
   Press, 1996, Chapters 1–3. [Publisher record](https://press.uchicago.edu/ucp/books/book/chicago/L/bo3627754.html).

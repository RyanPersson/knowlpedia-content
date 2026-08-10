+++
id = "lie-groups/spin8-triality"
title = "Spin(8) triality"
kind = "theorem"
summary = "The order-six outer symmetry of Spin(8) that permutes its vector and two half-spin representations."
aliases = ["triality", "D4 triality", "Spin(8) triality automorphism"]
domains = ["lie-groups", "representation-theory"]
section_mode = "progressive"
+++

The compact simply connected Lie group \(\operatorname{Spin}(8)\) has outer automorphism group
\[
\operatorname{Out}(\operatorname{Spin}(8))\cong S_3.
\]
Under twisting by these automorphisms, \(S_3\) permutes the three inequivalent eight-dimensional irreducible real representations:
\[
8_v,\qquad 8_s=\Delta^+,\qquad 8_c=\Delta^-.
\]
Here \(8_v\) is the vector representation factoring through \(SO(8)\), while \(8_s\) and \(8_c\) are the two [[lie-groups/half-spin-representation|half-spin representations]]. This symmetry is called **triality**.

## Dynkin-diagram origin

The [[lie-groups/dynkin-diagram|Dynkin diagram]] of type \(D_4\) has one central node joined to three outer nodes. Every permutation of the outer nodes preserves the diagram, giving its automorphism group \(S_3\). The three outer nodes label the highest weights of \(8_v,8_s,8_c\), so the diagram symmetry permutes these representations.

Triality is exceptional to \(D_4\). For \(D_m\) with \(m\geq5\), the two spin nodes can still be exchanged, but the vector node is distinguished and the diagram automorphism group has only two elements.

## Invariant trilinear form

Clifford multiplication gives a nonzero \(\operatorname{Spin}(8)\)-equivariant map
\[
8_v\otimes8_s\longrightarrow8_c.
\]
After choosing invariant inner products, this is equivalent to an invariant trilinear form
\[
t:8_v\otimes8_s\otimes8_c\longrightarrow\mathbb R.
\]
The triality symmetry can be realized so that it permutes the three factors together with the corresponding group automorphisms. This is a representation-theoretic shadow of the close relation between \(\operatorname{Spin}(8)\) and the octonions.

## What triality does not say

The three representations are not isomorphic as representations for a fixed, unchanged action of \(\operatorname{Spin}(8)\). Rather, an outer automorphism of the group changes which representation is being used: for a suitable \(\varphi\), one has \(8_v\circ\varphi\cong8_s\), and similarly for the other permutations.

Likewise, the labels \(8_s\) and \(8_c\), or \(+\) and \(-\), depend on a choice of the two spin nodes and on chirality conventions. Triality preserves the unordered triple.

## References

1. John F. Adams, *Lectures on Exceptional Lie Groups*, University of Chicago Press, 1996, Chapter 3. [Publisher record](https://press.uchicago.edu/ucp/books/book/chicago/L/bo3622388.html).
2. John C. Baez, “The Octonions,” *Bulletin of the American Mathematical Society* **39** (2002), 145–205, §§2.4 and 4.1. [DOI record](https://doi.org/10.1090/S0273-0979-01-00934-X).
3. William Fulton and Joe Harris, *Representation Theory: A First Course*, Springer, 1991, §20. [Publisher record](https://doi.org/10.1007/978-1-4612-0979-9).

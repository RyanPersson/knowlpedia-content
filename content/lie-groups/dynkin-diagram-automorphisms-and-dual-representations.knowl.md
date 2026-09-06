+++
id = "lie-groups/dynkin-diagram-automorphisms-and-dual-representations"
title = "Dynkin-diagram automorphisms and dual representations"
kind = "theorem"
summary = "Diagram symmetries act on highest weights, while the opposition involution gives the highest weight of the dual representation."
aliases = ["opposition involution", "dual highest-weight involution", "Dynkin automorphism and contragredient"]
domains = ["lie-groups", "representation-theory"]
section_mode = "progressive"
prerequisites = ["lie-groups/semisimple-lie-algebra", "lie-groups/simple-root", "lie-groups/cartan-matrix", "lie-groups/highest-weight-representation", "lie-groups/weyl-group", "lie-groups/root-system", "algebra-representation-theory/irreducible-representation", "lie-groups/highest-weight", "lie-groups/dual-representation-lie", "linear-algebra/matrix"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\mathfrak g\) be a complex [[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]] with chosen [[lie-groups/simple-root|simple roots]] \(\Delta=\{\alpha_i\}\). A **Dynkin-diagram automorphism** is a permutation of \(\Delta\) preserving the [[lie-groups/cartan-matrix|Cartan matrix]]. It permutes the fundamental weights and, after choosing a compatible automorphism of \(\mathfrak g\), sends irreducible [[lie-groups/highest-weight-representation|highest-weight representations]] to irreducible highest-weight representations with the correspondingly permuted labels.

Let \(w_0\) be the longest element of the [[lie-groups/weyl-group|Weyl group]]. The **opposition involution** of the based [[lie-groups/root-system|root system]] is characterized by
\[
\alpha_i\longmapsto -w_0(\alpha_i).
\]
If \(V_\lambda\) is the [[algebra-representation-theory/irreducible-representation|irreducible representation]] of [[lie-groups/highest-weight|highest weight]] \(\lambda\), then its [[lie-groups/dual-representation-lie|dual representation]] has highest weight
\[
\lambda^*=-w_0\lambda.
\]
Thus the opposition involution is precisely the Dynkin-diagram symmetry governing contragredient highest weights.

## The simple types

For an irreducible root system, the opposition involution is nontrivial exactly in the following cases:

- in type \(A_n\) for \(n\geq2\), it reverses the chain, sending \(\omega_i\) to \(\omega_{n+1-i}\);
- in type \(D_{2k+1}\), it exchanges the two spin nodes;
- in type \(E_6\), it is the unique nontrivial diagram symmetry.

It is the identity in types \(A_1\), \(B_n\), \(C_n\), \(D_{2k}\), \(E_7\), \(E_8\), \(F_4\), and \(G_2\). In those types every finite-dimensional irreducible complex representation is self-dual, although its invariant [[linear-algebra/bilinear-form|bilinear form]] may be symmetric or alternating.

## Other diagram symmetries

Not every diagram automorphism is the duality involution. The clearest example is \(D_4\): its full diagram automorphism group is \(S_3\), producing [[lie-groups/spin8-triality|triality]], while its opposition involution is the identity. More generally, a diagram symmetry defines a twisting operation on representations whether or not it arises from dualization.

## Group-level caution

The highest-weight formula is initially a statement for the complex semisimple Lie algebra, or equivalently for its [[lie-groups/simply-connected-lie-group|simply connected]] complex group. For a non-simply-connected group, only some dominant integral weights exponentiate to representations. Diagram automorphisms that preserve the relevant character lattice descend to that global group; others may exist only on a covering group or on the [[lie-groups/lie-algebra|Lie algebra]].

The formula \(-w_0\lambda\) is independent of a numbering of diagram nodes. Translating it into named fundamental weights requires a declared Dynkin-labeling convention.

## References

1. James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer, 1972, §§13 and 21. [Publisher record](https://doi.org/10.1007/978-1-4684-9444-2).
2. William Fulton and Joe Harris, *Representation Theory: A First Course*, Springer, 1991, §§13–20. [Publisher record](https://doi.org/10.1007/978-1-4612-0979-9).
3. Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 4–6*, Springer, 2002, Chapters VI, §§1–4. [Publisher record](https://doi.org/10.1007/978-3-540-89394-3).

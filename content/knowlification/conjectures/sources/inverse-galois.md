Let \(K\) be a field and \(G\) a finite group. A finite Galois realization of \(G\) over \(K\) consists of a field extension \(L/K\) that is finite, normal, and separable, together with a group isomorphism
\[
G\cong \operatorname{Aut}_K(L),
\]
where \(\operatorname{Aut}_K(L)\) is the group of field automorphisms of \(L\) fixing \(K\) pointwise. For a finite Galois extension this automorphism group is the Galois group \(\operatorname{Gal}(L/K)\).

## Conjecture

Every finite group has a Galois realization over the rational field \(\mathbb Q\). In symbols, for every finite group \(G\), there is a finite Galois extension \(L/\mathbb Q\) such that
\[
\operatorname{Gal}(L/\mathbb Q)\cong G.
\]

The problem is existential: neither the extension nor a defining polynomial is supplied. A constructive solution for a particular group usually produces a polynomial \(f\in\mathbb Q[x]\), proves that its splitting field is Galois over \(\mathbb Q\), and computes the resulting group.

## Known boundary

The problem is solved for many families, including finite abelian groups and symmetric groups. Over a rational function field \(K(t)\) of characteristic zero, every finite group occurs as a Galois group; specializing from such a regular realization to \(\mathbb Q\) is powerful but does not settle all groups.

## Formal source

This page follows `FormalConjectures/Wikipedia/InverseGalois.lean`. Its predicate packages the extension field, its \(K\)-algebra structure, the Galois property, and a multiplicative equivalence with the group of \(K\)-automorphisms.

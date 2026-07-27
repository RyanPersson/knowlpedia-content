+++
id = "operator-algebras/sakai-characterization-theorem"
title = "Sakai characterization theorem"
kind = "theorem"
summary = "A C*-algebra is a W*-algebra exactly when it is isometrically a Banach dual space."
aliases = ["Sakai theorem", "dual C*-algebra characterization", "W*-algebra characterization theorem"]
domains = ["operator-algebras", "functional-analysis"]
section_mode = "progressive"
+++

The **Sakai characterization theorem** states that a
[[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(M\) is a
\(W^*\)-algebra if and only if there is a Banach space \(E\) such that \(M\)
is isometrically isomorphic, as a Banach space, to \(E^*\). In that case
\(E\) is canonically isometrically isomorphic to the
[[operator-algebras/predual|predual]] \(M_*\), and \(M\) admits a faithful
[[operator-algebras/normal-representation|normal representation]] whose image is a
[[operator-algebras/von-neumann-algebra|concrete von Neumann algebra]]. Thus
being a Banach dual forces the operator-algebraic weak-star structure; it is
not an additional hypothesis.

## Content of the theorem

The difficult direction begins with only the \(C^*\)-algebra operations, norm,
and an isometric identification \(M=E^*\). Sakai's theorem shows that the
resulting weak-star topology is compatible with multiplication and
involution, identifies the normal functionals, and yields a concrete
weak-operator-closed realization
[Sakai, Theorem 1.16.7](https://doi.org/10.1007/978-3-642-61993-9).
Conversely, the canonical predual of any concrete von Neumann algebra makes
it a Banach dual.

## Uniqueness and terminology

The predual obtained in the theorem is unique up to the canonical isometric
isomorphism that preserves evaluation on \(M\). Accordingly, abstract
\(W^*\)-algebras and concrete von Neumann algebras are equivalent viewpoints,
although a concrete realization still includes a choice of Hilbert space and
representation. The phrase “dual \(C^*\)-algebra” is potentially ambiguous
in older literature and should not replace the precise Banach-dual
formulation.

## References

1. Shôichirô Sakai, \(C^*\)-Algebras and \(W^*\)-Algebras, Springer, 1971; Classics in Mathematics reprint, 1998. [DOI record](https://doi.org/10.1007/978-3-642-61993-9). Relevant: Theorem 1.16.7 and the abstract characterization of \(W^*\)-algebras.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter III on preduals, normal representations, and concrete von Neumann algebras.

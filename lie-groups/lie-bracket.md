---
title: "Lie Bracket"
description: "A bilinear operation on a vector space satisfying antisymmetry and the Jacobi identity."
---

A **Lie bracket** on a {{< knowl id="vector-space" section="linear-algebra" text="vector space" >}} \(\mathfrak{g}\) is a bilinear map
$$
[\ ,\ ]:\mathfrak{g}\times\mathfrak{g}\to\mathfrak{g}
$$
such that, for all \(X,Y,Z\in\mathfrak{g}\),
$$
[X,Y]=-[Y,X]
\quad\text{and}\quad
[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0.
$$
A vector space equipped with a Lie bracket is a {{< knowl id="lie-algebra" text="Lie algebra" >}}.

## Intuition and standard source of examples
If an associative product \(AB\) is available (e.g. matrices), the commutator
$$
[A,B]=AB-BA
$$
is a Lie bracket. This is why Lie brackets are often thought of as measuring “noncommutativity.”

Another fundamental example is the commutator of {{< knowl id="vector-field" section="fiber-bundles" text="vector fields" >}} on a manifold.

## Adjoint operator
Given a Lie algebra \(\mathfrak{g}\), each \(X\in\mathfrak{g}\) defines a linear map
$$
\operatorname{ad}_X:\mathfrak{g}\to\mathfrak{g},\qquad \operatorname{ad}_X(Y)=[X,Y],
$$
which is the {{< knowl id="adjoint-representation-of-a-lie-algebra" text="adjoint representation" >}} at the Lie algebra level.

## Brackets from Lie groups
For a {{< knowl id="lie-group" text="Lie group" >}} \(G\), the canonical Lie bracket on \(T_eG\) is defined using {{< knowl id="left-invariant-vector-field" text="left-invariant vector fields" >}}; see {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra of a Lie group" >}}.

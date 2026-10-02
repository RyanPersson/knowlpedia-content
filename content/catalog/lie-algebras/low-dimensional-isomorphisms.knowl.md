+++
id = "catalog/lie-algebras/low-dimensional-isomorphisms"
title = "Low-dimensional Lie algebra isomorphisms"
kind = "index"
summary = "Low-dimensional Lie algebra isomorphisms."
aliases = ["Low-dimensional Lie algebra isomorphisms"]
domains = ["catalog", "lie-groups"]
section_mode = "continuous"
prerequisites = ["lie-groups/lie-algebra-isomorphism", "lie-groups/underlying-real-lie-algebra"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

**Low-dimensional Lie algebra isomorphisms** identify several different matrix constructions after the scalar field is fixed. The identities below are Lie-algebra statements; a corresponding group map can have a nontrivial discrete kernel.

## Explicit identifications

The following catalogue arrows retain the defining field:

- [[catalog/lie-algebras/so-4-r|\(\mathfrak{so}(4)\)]] and [[catalog/lie-algebras/su-2-direct-sum-su-2|su(2) direct sum with itself]]: Identify so(4) with bivectors in oriented Euclidean four-space. The self-dual and anti-self-dual bivectors are commuting three-dimensional ideals, each isomorphic to so(3), hence to su(2).
- [[catalog/lie-algebras/so-4-c|\(\mathfrak{so}(4,\mathbb C)\)]] and [[catalog/lie-algebras/sl-2-c-direct-sum-sl-2-c|sl(2,C) direct sum with itself]]: Complexify the compact so(4) decomposition and the real form su(2).
- [[catalog/lie-algebras/so-2-2-r|\(\mathfrak{so}(2,2)\)]] and [[catalog/lie-algebras/sl-2-r-direct-sum-sl-2-r|sl(2,R) direct sum with itself]]: The action (X,Y)·A=XA−AY on real 2-by-2 matrices preserves determinant, a form of signature (2,2). Its infinitesimal kernel is zero: XA=AY for every A forces X=Y scalar, and trace zero then forces both to vanish. Both algebras have dimension six.
- [[catalog/lie-algebras/su-2|\(\mathfrak{su}(2)\)]] and [[catalog/lie-algebras/sp-1|sp(1) — compact symplectic Lie algebra]]: Identify imaginary quaternions with trace-zero skew-Hermitian 2-by-2 matrices; quaternion multiplication is represented by matrix multiplication.
- [[catalog/lie-algebras/su-2|\(\mathfrak{su}(2)\)]] and [[catalog/lie-algebras/so-3-r|so(3,R) — real orthogonal Lie algebra]]: The adjoint action on the three-dimensional imaginary-quaternion space preserves its [[linear-algebra/euclidean-norm|Euclidean norm]], is faithful infinitesimally, and both algebras have dimension three.
- [[catalog/lie-algebras/sp-2|\(\mathfrak{sp}(2)\)]] and [[catalog/lie-algebras/so-5-r|so(5,R) — real orthogonal Lie algebra]]: Act by X·A=XA−AX on traceless Hermitian quaternionic 2-by-2 matrices. This five-dimensional real space has positive form tr(A²); an element in the kernel commutes with every Hermitian matrix. Commuting with diagonal projections makes it diagonal; commuting with all quaternionic off-diagonal entries makes it a real scalar. Skew-adjointness then forces it to vanish. Source and target both have dimension ten.
- [[catalog/lie-algebras/su-4|\(\mathfrak{su}(4)\)]] and [[catalog/lie-algebras/so-6-r|so(6,R) — real orthogonal Lie algebra]]: The exterior-square representation preserves the symmetric wedge pairing on Λ²C⁴. Its compatible antilinear Hodge involution has a six-dimensional real fixed space; the differentiated action is faithful and both algebras have dimension fifteen.
- [[catalog/lie-algebras/sl-2-r|\(\mathfrak{sl}(2,\mathbb R)\)]] and [[catalog/lie-algebras/sp-2-r|sp(2,R) — real symplectic Lie algebra]]: For a 2-by-2 matrix X, XᵀJ+JX=(tr X)J.
- [[lie-groups/example-sl2c|\(\mathfrak{sl}(2,\mathbb C)\)]] and [[catalog/lie-algebras/sp-2-c|sp(2,C) — complex symplectic Lie algebra]]: The same matrix identity holds over C.
- [[lie-groups/example-sl2c|\(\mathfrak{sl}(2,\mathbb C)\)]] and [[catalog/lie-algebras/so-3-c|so(3,C) — complex orthogonal Lie algebra]]: The adjoint action preserves the nondegenerate [[lie-groups/killing-form|Killing form]]; its kernel is the zero center, and both algebras have dimension three.
- [[catalog/lie-algebras/sl-2-r|\(\mathfrak{sl}(2,\mathbb R)\)]] and [[catalog/lie-algebras/so-2-1-r|so(2,1) — indefinite orthogonal real Lie algebra]]: The form tr(X²) on trace-zero real 2-by-2 matrices has signature (2,1). Its adjoint action is injective and dimension three.
- [[catalog/lie-algebras/sl-2-c-underlying-real|\(\mathfrak{sl}(2,\mathbb C)_{\mathbb R}\)]] and [[catalog/lie-algebras/so-3-1-r|so(3,1) — indefinite orthogonal real Lie algebra]]: The action X·H=XH+HX* on Hermitian 2-by-2 complex matrices infinitesimally preserves determinant, a [[linear-algebra/quadratic-form|quadratic form]] of signature (1,3). If this action vanishes then X is skew-Hermitian and commutes with every [[linear-algebra/hermitian-matrix|Hermitian matrix]], hence is scalar; trace zero forces X=0. Both algebras have real dimension six, and changing the sign of the form does not change its [[lie-groups/orthogonal-lie-algebra|orthogonal Lie algebra]].
- [[catalog/lie-algebras/sp-4-c|\(\mathfrak{sp}(4,\mathbb C)\)]] and [[catalog/lie-algebras/so-5-c|so(5,C) — complex orthogonal Lie algebra]]: Complexify the compact sp(2)–so(5) isomorphism.
- [[catalog/lie-algebras/sl-4-c|\(\mathfrak{sl}(4,\mathbb C)\)]] and [[catalog/lie-algebras/so-6-c|so(6,C) — complex orthogonal Lie algebra]]: Complexify the compact su(4)–so(6) isomorphism.
- [[catalog/lie-algebras/so-1-1-r|\(\mathfrak{so}(1,1)\)]] and [[catalog/lie-algebras/abelian-1-r|Abelian real Lie algebra of dimension 1]]: Both algebras have one basis vector and zero bracket.
- [[catalog/lie-algebras/so-2-r|\(\mathfrak{so}(2)\)]] and [[catalog/lie-algebras/abelian-1-r|Abelian real Lie algebra of dimension 1]]: Both algebras have one basis vector and zero bracket, despite different global groups.
- [[catalog/lie-algebras/u-1|\(\mathfrak u(1)\)]] and [[catalog/lie-algebras/abelian-1-r|Abelian real Lie algebra of dimension 1]]: The real-linear map it↦t identifies the zero brackets.
- [[catalog/lie-algebras/sl-1-h|\(\mathfrak{sl}(1,\mathbb H)\)]] and [[catalog/lie-algebras/sp-1|sp(1) — compact symplectic Lie algebra]]: A quaternion has zero real part exactly when its conjugate is its negative.

## Distinguishing scalar restriction

\(\mathfrak{sl}(2,\mathbb C)\) has complex dimension three, while its [[lie-groups/underlying-real-lie-algebra|underlying real Lie algebra]] has real dimension six. It cannot be real-linearly isomorphic to the three-dimensional \(\mathfrak{sl}(2,\mathbb R)\). Triality in \(\mathfrak{so}(8)\) concerns automorphisms permuting representations; it does not identify the vector and spinor modules without twisting.

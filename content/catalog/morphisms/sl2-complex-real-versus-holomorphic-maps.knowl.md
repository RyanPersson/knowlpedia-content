+++
id = "catalog/morphisms/sl2-complex-real-versus-holomorphic-maps"
title = "Conjugation on SL(2,C) distinguishes real and complex group maps"
kind = "example"
summary = "Entrywise conjugation is a real Lie-group automorphism but not a holomorphic one."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["catalog/categories/real-lie-groups", "catalog/categories/complex-lie-groups"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

For \(G=SL(2,\mathbb C)\), entrywise complex conjugation
\[
c:G\longrightarrow G,\qquad c(A)=\overline A,
\]
is an automorphism in the [[catalog/categories/real-lie-groups|real Lie-group category]] but is not a morphism in the [[catalog/categories/complex-lie-groups|complex Lie-group category]]. It is smooth, multiplicative, and involutive, but antiholomorphic rather than holomorphic.

## Direct verification

Conjugation respects determinant and matrix multiplication, so it maps \(G\) to itself and obeys \(c(AB)=c(A)c(B)\). It is its own inverse. Its differential at the identity is \(X\mapsto\overline X\) on \(\mathfrak{sl}_2(\mathbb C)\), which is real-linear but sends \(iX\) to \(-i\overline X\). For nonzero \(X\), this fails complex linearity, so the original map is not holomorphic.

## Other recorded maps

For each \(B\in GL_2(\mathbb C)\), the map \(A\mapsto BAB^{-1}\) is a holomorphic automorphism of \(G\). Composing it with \(c\) supplies antiholomorphic real automorphisms. The constant map \(A\mapsto I_2\) is a group endomorphism in both categories and is not an automorphism.

These formulas provide families of maps. This knowl does not claim a classification of every abstract group endomorphism or every real or holomorphic group endomorphism; the associated catalogue records are marked partial.

## Where linear endomorphisms live

\(SL(2,\mathbb C)\) is not closed under addition or scalar multiplication. Real-linear versus complex-linear endomorphisms therefore require a specified [[linear-algebra/vector-space|vector space]], such as its [[lie-groups/example-sl2c|Lie algebra \(\mathfrak{sl}_2(\mathbb C)\)]] or the ambient matrix algebra. A [[linear-algebra/linear-map|linear map]] of the ambient space need not restrict to a [[algebra-groups/group-homomorphism|group homomorphism]].

See the [[catalog/morphisms/linear-endomorphisms-of-sl2-complex|explicit linear-endomorphism comparison]] for its Lie algebra.

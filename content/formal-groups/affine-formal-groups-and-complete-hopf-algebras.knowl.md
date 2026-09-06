+++
id = "formal-groups/affine-formal-groups-and-complete-hopf-algebras"
title = "Affine formal groups and complete Hopf algebras"
kind = "theorem"
summary = "Formal spectrum gives a contravariant equivalence between affine adic formal groups and admissible complete commutative Hopf algebras."
aliases = ["complete Hopf algebra anti-equivalence", "formal groups and complete Hopf algebras"]
domains = ["formal-groups", "algebra-coalgebras", "algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/formal-spectrum", "algebra-topological/completed-tensor-product", "algebra-topological/adic-ring"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Fix a commutative base ring \(k\) and an adic category in which affine formal
schemes are formal spectra of complete separated \(k\)-algebras with specified
ideals of definition. [[algebraic-geometry-foundations/formal-spectrum|Formal spectrum]] restricts to a contravariant
equivalence
\[
\left\{\text{affine adic formal groups over \(k\)}\right\}
\simeq
\left\{\text{admissible complete commutative Hopf \(k\)-algebras}\right\}^{\mathrm{op}}.
\]
On the algebraic side, the comultiplication takes values in the
[[algebra-topological/completed-tensor-product|completed tensor product]], and
all structure maps are continuous.

## Correspondence on objects and morphisms

For an affine formal group \(G=\operatorname{Spf}(A)\), pullback of
multiplication, identity, and inverse gives the
[[formal-groups/coordinate-hopf-algebra|complete coordinate Hopf algebra]]
\(\mathcal O(G)=A\). Conversely, the Hopf structure maps on an admissible
complete algebra \(A\) dualize to the group-object diagrams on
\(\operatorname{Spf}(A)\).

A formal-group homomorphism \(f:G\to H\) corresponds to the continuous
Hopf-algebra homomorphism
\[
f^*:\mathcal O(H)\longrightarrow\mathcal O(G).
\]
The reversal of arrows is the ordinary pullback-of-functions variance.

## Scope

The topology and the admissible class of [[algebra-topological/adic-ring|adic rings]] are part of the theorem.
Forgetting them loses the completed tensor product and can make formal
spectrum unavailable. The statement is affine; a non-affine formal group is
encoded by a sheaf of complete coordinate algebras rather than by one global
[[algebra-coalgebras/hopf-algebra|Hopf algebra]].

## References

1. Michiel Hazewinkel, *Formal Groups and Applications*, Pure and Applied Mathematics 78, Academic Press, 1978; AMS reprint, 2012. [Publisher record](https://doi.org/10.1090/chel/078). Relevant: Chapters I–II.
2. The Stacks Project Authors, “Formal schemes à la EGA.” [Section 87.2, Tag 0AHY](https://stacks.math.columbia.edu/tag/0AHY).

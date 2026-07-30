+++
id = "formal-groups/coordinate-hopf-algebra"
title = "Coordinate Hopf algebra of an affine formal group"
kind = "definition"
summary = "The complete commutative Hopf algebra contravariantly encoding an affine formal group."
aliases = ["formal Hopf algebra", "complete coordinate Hopf algebra", "Hopf algebra of a formal group"]
domains = ["formal-groups", "algebra-coalgebras", "algebraic-geometry-foundations"]
section_mode = "progressive"
+++

Let \(k\) be a commutative ring and let
\(G=\operatorname{Spf}(A)\) be an affine [[formal-groups/formal-group|formal
group]] over \(k\), where \(A\) is a complete separated commutative
topological \(k\)-algebra. Pullback along the multiplication, identity, and
inverse of \(G\) gives continuous maps
\[
\Delta:A\longrightarrow A\widehat\otimes_k A,\qquad
\varepsilon:A\longrightarrow k,\qquad
S:A\longrightarrow A.
\]
Together with the multiplication and unit of \(A\), these maps make \(A\) a
**complete commutative Hopf algebra**: the ordinary tensor product in the
[[algebra-coalgebras/hopf-algebra|Hopf-algebra]] axioms is replaced by the
[[algebra-topological/completed-tensor-product|completed tensor product]].
The resulting topological Hopf algebra \(A=\mathcal O(G)\) is the **coordinate
Hopf algebra** of \(G\).

## The structure identities

The group axioms pull back, in the opposite direction, to
\[
(\Delta\widehat\otimes\operatorname{id})\Delta
=
(\operatorname{id}\widehat\otimes\Delta)\Delta,
\]
\[
(\varepsilon\widehat\otimes\operatorname{id})\Delta
=\operatorname{id}_A
=
(\operatorname{id}\widehat\otimes\varepsilon)\Delta,
\]
and
\[
m_A(S\widehat\otimes\operatorname{id})\Delta
=u_A\varepsilon
=m_A(\operatorname{id}\widehat\otimes S)\Delta.
\]
Thus \(\Delta\), \(\varepsilon\), and \(S\) encode multiplication, identity,
and inversion on \(G\), respectively. Although \(A\) is commutative as an
algebra, \(\Delta\) need not be cocommutative; cocommutativity of \(\Delta\)
is equivalent to commutativity of the formal group.

## Contravariant equivalence

In a fixed category of affine adic formal schemes, formal spectrum gives an
anti-equivalence between admissible complete adic \(k\)-algebras and affine
formal schemes. It therefore restricts to an anti-equivalence
\[
\left\{\text{affine formal groups over }k\right\}
\simeq
\left\{\text{admissible complete commutative Hopf \(k\)-algebras}\right\}^{\mathrm{op}}.
\]
A formal-group homomorphism \(f:G\to H\) corresponds to the continuous
Hopf-algebra homomorphism
\(f^\*:\mathcal O(H)\to\mathcal O(G)\). The topology and the class of
admissible adic rings are part of this statement; forgetting them can destroy
both the completed tensor product and the formal spectrum.

## Formal group laws in coordinates

Suppose \(k\) is a field and the pointed formal scheme underlying \(G\) is a
\(d\)-dimensional [[formal-groups/formal-affine-space|formal disc]]. A choice
of coordinates identifies
\[
A\cong k[[x_1,\ldots,x_d]]
\quad\text{and}\quad
A\widehat\otimes_k A
\cong k[[x_1,\ldots,x_d,y_1,\ldots,y_d]].
\]
Under this identification, the comultiplication is determined by
\[
\Delta(x_i)=F_i(x_1,\ldots,x_d,y_1,\ldots,y_d),
\]
where \(F=(F_1,\ldots,F_d)\) is the corresponding
[[formal-groups/formal-group-law|formal group law]]. The counit sends every
\(x_i\) to \(0\), and the antipode records the inverse power series. Changing
coordinates changes the displayed power series but not the underlying
coordinate Hopf algebra up to continuous Hopf-algebra isomorphism.

## Scope

This equivalence is an affine statement. Non-affine formal groups require
sheaves of complete coordinate algebras rather than one global Hopf algebra.
Over more general bases, completed tensor products and formal spectra also
require explicit adic hypotheses. In the finite-dimensional formally smooth
setting over a characteristic-zero field, the continuous dual near the
augmentation recovers the
[[formal-groups/distribution-algebra|distribution algebra]] and hence the
tangent Lie algebra.

## References

1. Michiel Hazewinkel, *Formal Groups and Applications*, Pure and Applied Mathematics 78, Academic Press, 1978; AMS reprint, 2012. [Publisher record](https://doi.org/10.1090/chel/078). Relevant: Chapters I and II on formal groups, formal group laws, and Hopf-algebra coordinates.
2. Michel Demazure and Pierre Gabriel, *Groupes algébriques, tome I: Géométrie algébrique, généralités, groupes commutatifs*, Masson, 1970. Relevant: the formal-group and formal-Lie-group constructions.
3. The Stacks Project Authors, *Formal Algebraic Spaces*, [Section 87.2: Formal schemes à la EGA](https://stacks.math.columbia.edu/tag/0AHY) and [Section 87.5: Completed tensor product](https://stacks.math.columbia.edu/tag/0AMU).

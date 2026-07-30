+++
id = "differential-geometry/clifford-algebra-as-super-enveloping-quotient"
title = "Clifford algebra as a super-enveloping quotient"
kind = "theorem"
summary = "A Clifford algebra is obtained by fixing the central character in the enveloping algebra of a quadratic Lie superalgebra."
aliases = ["Clifford algebra from a Lie superalgebra"]
domains = ["differential-geometry", "supergeometry"]
section_mode = "progressive"
+++

Let \(k\) have characteristic different from \(2\), let
\((V,q)\) be a quadratic vector space, and put
\(b_q(v,w)=q(v+w)-q(v)-q(w)\). Define a
[[supergeometry/lie-superalgebra|Lie superalgebra]]
\[
\mathfrak h_q=kz\oplus V
\]
by declaring \(z\) even and central, every element of \(V\) odd, and
\[
[v,w]=-b_q(v,w)z.
\]
For the Clifford convention \(v^2=-q(v)1\), there is an isomorphism of
superalgebras
\[
\operatorname{Cl}(V,q)
\cong
U(\mathfrak h_q)/(z-1),
\]
where \(U(\mathfrak h_q)\) is the
[[supergeometry/universal-enveloping-algebra-of-lie-superalgebra|universal
enveloping algebra]].

## Verification of the relation

Because \(v,w\) are odd, the defining enveloping-algebra relation reads
\[
vw+wv=[v,w]=-b_q(v,w)z.
\]
After imposing \(z=1\), this becomes the polarized Clifford relation. Setting
\(w=v\) gives
\[
2v^2=-b_q(v,v)=-2q(v),
\]
and hence \(v^2=-q(v)\). The universal properties of the two quotient algebras
then give the stated isomorphism.

## Interpretation

The odd bracket in \(\mathfrak h_q\) stores the quadratic form as a central
even value. The quotient \(z=1\) chooses a nonzero central character. Choosing
\(z=0\) instead gives
\[
U(\mathfrak h_q)/(z)\cong\Lambda V,
\]
so the exterior and Clifford algebras appear as two central fibers of the same
super-enveloping construction.

## Conventions

If the alternative Clifford convention \(v^2=+q(v)\) is used, define
\([v,w]=+b_q(v,w)z\) instead. The sign in the Lie-superalgebra bracket and the
sign in the Clifford relation must be changed together.

## References

1. P. Deligne and J. W. Morgan, “Notes on supersymmetry (following Joseph
   Bernstein),” in *Quantum Fields and Strings: A Course for Mathematicians*,
   Volume 1, American Mathematical Society, 1999. Relevant: Sections 1–2.
2. I. M. Musson, *Lie Superalgebras and Enveloping Algebras*, American
   Mathematical Society, 2012. [DOI
   record](https://doi.org/10.1090/gsm/131). Relevant: Chapters 1 and 6.

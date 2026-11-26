+++
id = "proofs/grh/upper-seesaw/cover-multiplicity"
title = "Cover multiplicity of a finite set of cosets"
kind = "definition"
summary = "The number of classes of S modulo S meet A whose translates of a finite set T of cosets cover a given coset."
aliases = ["coverMultiplicity", "cut"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.coverMultiplicity", "New.Seesaw.coverMultiplicity_smul", "New.Seesaw.coverMultiplicity_eq_index_stabilizer"]
lean_files = ["src/New/UpperBound/Seesaw/IntegralAsCosetSum.lean"]
proof_status = "full"
+++

Let \(H\) be a [[algebra-groups/group|group]] with subgroups \(S,A,J\), and let \(T\) be a finite
subset of the set \(H/J\) of left cosets, on which \(H\) acts by left translation. The **cover
multiplicity** of \(t\in H/J\) is
\[
m_T(t)=\#\bigl\{\,r\,(S\cap A)\in S/(S\cap A)\;:\; r\in S,\ r^{-1}t\in T\,\bigr\},
\]
the number of classes in \(S/(S\cap A)\) having a representative \(r\) with \(t\in rT\); it is set
to \(0\) if this number is infinite. A finite set \(T\) used in this way is called a **cut**.

## Properties

1. \(m_T(pt)=m_T(t)\) for \(p\in S\).
2. Let \(C\subseteq H/J\) meet every \(S\)-orbit in at most one point, and suppose
   \(T=\{t: p^{-1}t\in C\text{ for some }p\in S\cap A\}\). Then for \(t\in C\), with
   \(Z=\operatorname{Stab}_S(t)\) the [[algebra-groups/stabilizer|stabiliser]],
   \(m_T(t)=[Z:Z\cap A]\) ([[algebra-groups/index-of-subgroup|index]]; \(0\) if infinite).

## Proof

(1) Left translation by \(p^{-1}\) is a bijection of \(S/(S\cap A)\) carrying
\(\{r:r^{-1}pt\in T\}\) onto \(\{r':r'^{-1}t\in T\}\) (\(r'=p^{-1}r\)).

(2) We show that the set of classes counted at \(t\) is the \(Z\)-orbit of the trivial class in
\(S/(S\cap A)\). If \(r^{-1}t\in T\), there is \(p\in S\cap A\) with \(p^{-1}r^{-1}t\in C\); this
point lies in the \(S\)-orbit of \(t\in C\), so it equals \(t\), i.e. \(z=rp\in Z\) and
\(r(S\cap A)=z(S\cap A)\). Conversely for \(z\in Z\), \(z^{-1}t=t\in C\subseteq T\). The orbit of
the trivial class under \(Z\) is in bijection with \(Z/(Z\cap A)\), since the stabiliser of the
trivial class in \(Z\) is \(Z\cap A\). \(\blacksquare\)

## References

1. Lean: `New.Seesaw.coverMultiplicity`, `New.Seesaw.coverMultiplicity_smul`, `New.Seesaw.coverMultiplicity_eq_index_stabilizer` in `src/New/UpperBound/Seesaw/IntegralAsCosetSum.lean`.

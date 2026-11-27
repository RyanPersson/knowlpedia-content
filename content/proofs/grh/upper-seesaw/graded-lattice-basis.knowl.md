+++
id = "proofs/grh/upper-seesaw/graded-lattice-basis"
title = "The glued lattice basis of a graded space"
kind = "construction"
summary = "An explicit basis of a lattice in a hermitian space X plus a string, gluing the last vector of X to the middle string vector when the string is odd."
aliases = ["graded lattice basis", "glued Gram matrix", "the frame spans the glued lattice"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.gradedLatticeBasis", "New.Grading.SpansLattice", "New.Seesaw.gluedGram"]
lean_files = ["src/New/UpperBound/Seesaw/AdmissibleCombinations.lean"]
+++

Let \(R\) be a commutative ring with an involution \(x\mapsto\bar x\). Let \(X'\) be a finite set,
\(s\ge0\), and consider the free \(R\)-module with basis
\[
(x_i)_{i\in X'},\qquad y,\qquad z_0,\dots,z_{s-1};
\]
the \(x_i\) and \(y\) span "\(X=X'\sqcup\{y\}\)" and \(z_0,\dots,z_{s-1}\) is the *string*. For
units \(a,\pi\in R^{\times}\) and \(u\in R\) with \(\bar u u=1\), the **glued lattice basis**
\(\mathcal{B}(a,\pi,u)\) consists of the following vectors.

* If \(s\) is odd, with middle index \(c=(s-1)/2\):
  \[
  x_i\ (i\in X'),\qquad y'=\bar\pi^{-1}y+u(\pi\bar\pi)^{-1}z_{c},\qquad u\,z_b\ (0\le b<s).
  \]
* If \(s\) is even:
  \[
  x_i\ (i\in X'),\qquad y,\qquad u\,a^{-1}z_b\ (2b<s),\qquad u\,\bar a\,z_b\ (2b\ge s).
  \]

It is written as a square matrix whose columns are these vectors, indexed by a set \(\iota\) through
a bijection \(e\colon (X'\sqcup\{y\})\sqcup\{0,\dots,s-1\}\to\iota\).

**The glued Gram matrix.** For \(p,q\in R\), \(G(p,q)\) is the matrix of the form on the same basis
with: \(\langle x_i,x_j\rangle=\delta_{ij}\); \(\langle z_b,z_{b'}\rangle=1\) if \(b+b'=s-1\),
\(b\ne b'\); \(\langle z_c,z_c\rangle=-p\) for the middle vector (odd \(s\)); all other pairings of
string vectors \(0\); \(\langle y,y\rangle=q\) and \(\langle y,z_c\rangle=\langle z_c,y\rangle=-1\)
if \(s\) is odd; \(\langle y,y\rangle=1\) and \(y\perp z_b\) if \(s\) is even; \(y\perp x_i\),
\(x_i\perp z_b\); and all pairings not listed are \(0\), in particular \(\langle y,z_b\rangle=\langle z_b,y\rangle=0\) for \(b\ne c\) when \(s\) is odd.

**The frame spans the glued lattice.** Let \(E\) be a [[?c:CM field|CM field]], \(V\) a
[[?lean:New.Space|hermitian space with a point]] over \(E\), and \(Y\) a
[[?lean:New.Grading|grading]] of \(V\) as \(X\) plus a string of \(s\) vectors with parameter
\(N\). For [[?c:Idele group|finite ideles]] \(a,\pi\) and a finite adele \(u\) of norm one (\(\bar uu=1\)), the grading
\(Y\) **spans the lattice** of \((a,\pi,u)\) if the finite part \(x_f\) of the point of \(V\)
satisfies
\[
x_f=\mathcal{B}(a,\pi,u)\cdot k\qquad\text{for some } k\in \mathrm{GL}_\iota(\widehat{\mathcal{O}}_E),
\]
that is, the columns of \(x_f\) and of \(\mathcal{B}(a,\pi,u)\) span the same
\(\widehat{\mathcal{O}}_E\)-lattice in \(\mathbb{A}_{E,f}^{\iota}\).

## Remarks

The [[?lean:New.gradedGram|graded Gram matrix]] is the form with \(\langle x,x\rangle=1\) on all of
\(X\), the string paired antidiagonally with \(-N\) in the middle, and \(X\perp\) string. For odd
\(s\) the lattice spanned by the standard basis fails to be [[?c:Self-dual lattice|self-dual]] exactly at the places where \(N\) is not a unit (the middle vector has norm \(-N\); all other blocks are unimodular; for \(N\) a unit, e.g. \(N=1\), it is already unimodular) — in the application, at the places above the level prime \(N\). Gluing \(y\) to \(z_c\) repairs this when \(N=\pi\bar\pi\); see
[[proofs/grh/upper-seesaw/graded-lattice-basis-unimodular|unimodularity of the glued lattice]].

## References

1. Lean: `New.gradedLatticeBasis`, `New.Grading.SpansLattice`, `New.Seesaw.gluedGram` in `src/New/UpperBound/Seesaw/AdmissibleCombinations.lean`.

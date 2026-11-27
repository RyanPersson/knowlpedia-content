+++
id = "proofs/grh/upper-seesaw/neighbour-lattice"
title = "The neighbour lattice of a pair of edges"
kind = "construction"
summary = "An explicit unitary carries the standard lattice of Hom(X', X-minus plus X'') to a lattice that is a neighbour of it above N and has rows scaled by norm-one factors away from N."
aliases = ["neighbour matrix", "neighbour axis", "neighbour translation", "scaling at M", "neighbour vector"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.PairIndex", "New.Seesaw.selfOrConj", "New.Seesaw.IsNeighbourVector", "New.Seesaw.IsScalingAtM", "New.Seesaw.neighbourAxis", "New.Seesaw.neighbourScale", "New.Seesaw.neighbourMatrix", "New.Seesaw.neighbourCoeff", "New.Seesaw.neighbourTranslation", "New.Seesaw.neighbourUnitary", "New.Seesaw.scalingUnitary", "New.Seesaw.kroneckerOne", "New.Seesaw.latticeUnitary", "New.Seesaw.neighbourLattice", "New.Seesaw.vanishingAbove", "New.Seesaw.awayLattice", "New.Seesaw.AwayLatticeQuotient", "New.Seesaw.neighbourCosetRep", "New.Seesaw.conjTranspose_mul_one_add_smul_vecMulVec", "New.Seesaw.star_one_add_neighbourScale_mul", "New.Seesaw.star_neighbourAxis_dotProduct_self", "New.Seesaw.isNeighbourVector_col_neighbourMatrix"]
lean_files = ["src/New/UpperBound/Seesaw/NeighbourLattice.lean"]
+++

Let \(E\) be a [[?c:CM field|CM field]] with [[?lean:New.WeilData|Weil data]], and
\(\eta\in\widehat{\mathcal{O}}_E\) the fixed integral adele of norm \(\eta\bar\eta=-1\)
([[?lean:New.Weil.normNegOne|Lean: the unit of norm \(-1\)]]). Consider definite spaces with
orthonormal bases indexed by \(X\sqcup\{e\}\), \(X'\) and \(X''\sqcup\{e''\}\); the **pair index**
set \(I=(X\sqcup\{e\})\sqcup(X''\sqcup\{e''\})\) indexes a basis of \(X^{-}\oplus X''\). Let
\((P,N,\pi)\) be a [[proofs/grh/upper-seesaw/split-squarefree-factorisation|split squarefree
factorisation]] with \(N\) a natural number, and \(j=1_P\in\mathbb{A}_{E,f}\) the idempotent of
\(P\).

**Neighbour matrix.** Put
\[
\rho=e+\bar\eta\,\bar j\,e''\in\mathbb{A}_{E,f}^{I},\qquad
A=j(\pi-1)+\bar j(\bar\pi^{-1}-1),\qquad \gamma=1+A\,\rho\rho^{*}.
\]
Since \(j\bar j=0\), \(\rho^{*}\rho=1\); and \(1+A\) is \(\pi\) at \(P\), \(\bar\pi^{-1}\) at
\(\bar P\), \(1\) elsewhere, so \(\overline{(1+A)}(1+A)=1\). Hence \(\gamma\) is unitary (for a unit
vector \(\rho\) with projection \(Q=\rho\rho^{*}\),
\((1+AQ)^{*}(1+AQ)=1+(\bar A+A+\bar AA)Q=1\)): it scales \(\rho\) by \(1+A\) and fixes
\(\rho^{\perp}\), and is the identity at all places outside \(P\cup\bar P\).

**Scaling at \(M\).** Let \(\beta\in\widehat{\mathcal{O}}_E\), \(\delta\in\mathbb{A}_{E,f}\) and
\(\kappa\colon I\to\mathbb{A}_{E,f}\). The family \(\kappa\) is a **scaling at \(M\)** for
\((N,\beta,\delta)\) if: \(\delta\bar\delta=1\); \(\delta_w=1\) and \(\beta_w\) is a unit at all
\(w\mid N\); each \(\kappa_b\in\{1,\delta\}\); \(\bar\beta\kappa_b\) is integral for all \(b\); and
\(\beta\kappa_b\) is integral for \(b\) in the first block, \(\bar\beta\kappa_b\) for \(b\) in the
second. (In the application \(\beta\bar\beta=M\) and \(\delta\) generates \((\beta/\bar\beta)\).)

**Neighbour lattice.** The **lattice unitary** is \(u=(\gamma\cdot\operatorname{diag}\kappa)\otimes1_{X'}\),
acting on \(I\times X'\)-matrices by left multiplication on columns. The **neighbour lattice** is
\[
\mathcal{N}=u\cdot\widehat{\mathcal{O}}_E^{\,I\times X'}\subseteq\mathbb{A}_{E,f}^{\,I\times X'} .
\]
Its **away part** \(\mathcal{N}^{\mathrm{aw}}\) is the subgroup of elements vanishing at all places
of \(P\cup\bar P\); the **away quotient** is \(\mathcal{N}^{\mathrm{aw}}\) modulo its integral
elements, a finite group.

**Neighbour translations.** For residues \(y\colon X'\to(\mathbb{Z}/N)^{P}\), let
\(y/N\in\mathbb{A}_{E,f}^{X'}\) be the adele vector with component \(\tilde y_w/N\) at \(w\in P\), where \(\tilde y_w\in\{0,\dots,N-1\}\) is the integer representative of \(y_w\), and \(0\)
elsewhere. The **neighbour translation** \(n(y)\) is the \(I\times X'\)-matrix with row
\(\eta\,\overline{y/N}\) at \(e\), row \(-\overline{y/N}\) at \(e''\), and zero rows elsewhere; it is
supported at \(\bar P\). For a class \(q\) of the away quotient with chosen representative
\(t_q\), the **coset representative** is \(n(y)+t_q\).

**Neighbour vectors.** For \(\delta,c\in\mathbb{A}_{E,f}\), a vector \(x\in\mathbb{A}_{E,f}^{I}\) is
a **neighbour vector** with coefficient \(c\) if \(\delta c=c\); \(x_i\) is integral for
\(i\ne e,e''\); \(\bar\pi x_i\) is integral for all \(i\); and \(c-\pi^{-1}x_e\),
\(\bar\eta c-\pi^{-1}x_{e''}\) are integral. Column \(m\) of \(\gamma\) is a neighbour vector with
the **neighbour coefficient** \(c_m\): \(c_e=A\pi^{-1}\bar j\), \(c_{e''}=A\pi^{-1}\eta j\), and
\(c_m=0\) otherwise (when the places above the prime \(N\) are exactly \(P\cup\bar P\), so that
\(\delta\) is \(1\) on the support of \(A\)). Indeed, with \(\varpi=j+(1-j)\pi^{-1}\), which is integral because \(\pi\) is a unit off \(P\):
\[
c_m-\pi^{-1}\gamma_{e,m}=-\varpi\,\delta_{e,m},\qquad \bar\eta c_m-\pi^{-1}\gamma_{e'',m}=-\varpi\,\delta_{e'',m}.
\]
(Entries: \(\gamma_{i,m}=\delta_{i,m}+A\rho_i\bar\rho_m\) with \(\bar\rho_e=1\),
\(\bar\rho_{e''}=\eta j\). For \(m=e\):
\(c_e-\pi^{-1}(1+A)=-\pi^{-1}-\pi^{-1}A(1-\bar j)=-\pi^{-1}-\pi^{-1}j(\pi-1)=-\varpi\), using
\(A(1-\bar j)=j(\pi-1)\). For \(m=e''\) in the first identity both terms are \(A\pi^{-1}\eta j\).
For \(m=e''\) in the second: \(\bar\eta\eta A\pi^{-1}j-\pi^{-1}(1+A\bar\eta\bar j\eta j)=-A\pi^{-1}j-\pi^{-1}=-\varpi\),
using \(\bar\eta\eta=-1\), \(j\bar j=0\), \(Aj=j(\pi-1)\); for \(m=e\) both terms are
\(\bar\eta A\pi^{-1}\bar j\).) The other conditions: \(\delta c_m=c_m\) since \(\delta=1\) on the
support of \(A\); \(\gamma_{i,m}=\delta_{i,m}\) for \(i\ne e,e''\) since \(\rho_i=0\); and
\(\bar\pi\gamma_{i,m}\) is integral since \(\bar\pi A=j\bar\pi(\pi-1)+\bar j(1-\bar\pi)\) is.

## Remarks

For a pair of edges at a split level whose middle grading spans the prescribed glued lattice and which lifts neighbour vectors, the neighbour lattice is the [[proofs/grh/upper-seesaw/zero-term-lattice|zero term lattice]] of the
splitting of the pair: this is part 1 of
[[proofs/grh/upper-seesaw/admissible-evaluation-of-edge-pairs|the admissible evaluation of edge pairs]], where the hypotheses are stated; see also
[[proofs/grh/upper-seesaw/neighbour-vacuum|the vacuum of the neighbour lattice]].

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Seesaw/NeighbourLattice.lean`.

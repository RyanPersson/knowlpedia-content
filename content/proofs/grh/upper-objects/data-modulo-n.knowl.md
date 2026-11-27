+++
id = "proofs/grh/upper-objects/data-modulo-n"
title = "Direct, mirror and glued data modulo N"
kind = "definition"
summary = "The functions on matrices over the completions at a split level that are used as local theta data at N: last-row, last-column, character, direct, mirror and glued data."
aliases = ["direct datum", "mirror datum", "glued datum", "last row datum", "last column datum", "character datum"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsSplitLevel.liftFn", "New.IsSplitLevel.lastRowDatum", "New.IsSplitLevel.lastColDatum", "New.IsSplitLevel.charDatum", "New.IsSplitLevel.directDatum", "New.IsSplitLevel.mirrorDatum", "New.IsSplitLevel.gluedDatum", "New.IsSplitLevel.gluedDatum_eq_sum", "New.IsSplitLevel.lastRowDatum_apply", "New.IsSplitLevel.directDatum_apply", "New.IsSplitLevel.lastRowDatum_conj_diagNInv", "New.IsSplitLevel.primitiveVectors"]
lean_files = ["src/New/UpperBound/Objects/LiftLawsModuloN.lean"]
+++

Let \(P\) be a [[proofs/grh/upper-objects/split-level|split level]] for the prime \(N\) in the CM field \(E\), with \(E_P,\mathcal O_P\), reduction \(x\mapsto\bar x\), character \(\psi_N\), and the notation \(n^+=n\sqcup\{\ast\}\), \(e_\ast\), \(D_N\) of that page. Let \(n,n',n''\) be finite index sets.

**Definition.** For a function \(f\) on \(n'\times n\) matrices over \((\mathbb Z/N)^P\), its **extension** \(f^\sharp\) is the function on \(n'\times n\) matrices \(T\) over \(E_P\) with \(f^\sharp(T)=f(\bar T)\) if all entries of \(T\) lie in \(\mathcal O_P\) and \(f^\sharp(T)=0\) otherwise. The following complex-valued functions are extensions:

* the **last-row datum** on \(n'^+\times n^+\) matrices: \(\mathbf 1[\text{the last row of }\bar T\text{ is }e_\ast]\);
* the **last-column datum** for \(y\in((\mathbb Z/N)^P)^{n'}\) on \(n'\times n^+\) matrices: \(\mathbf 1[\text{the last column of }\bar T\text{ is }y]\);
* the **character datum** for \(y\in((\mathbb Z/N)^P)^{n}\) on \(n'^+\times n\) matrices: \(\psi_N(\bar T_\ast\cdot y)\), where \(\bar T_\ast\) is the last row and \(\cdot\) the standard bilinear pairing;
* the **direct datum** on \(n'^+\times n^+\) matrices: the last-column datum for \(y=e_\ast\), i.e. \(\mathbf 1[T\text{ integral},\ \bar T e_\ast=e_\ast]\);
* the **mirror datum** on \(n'^+\times n^+\) matrices: the character datum for \(y=e_\ast\), i.e. \(\psi_N(\bar T_{\ast\ast})\) on integral \(T\).

The **glued datum** is the function of a pair \((T,R)\), \(T\) an \(n'\times n^+\) matrix and \(R\) an \(n''^+\times n'\) matrix over \(E_P\), that equals \(\psi_N\big((\bar R\bar T)_{\ast\ast}\big)\) if \(T\) and \(R\) are both integral and \(0\) otherwise.

A vector \(y\in((\mathbb Z/N)^P)^{n}\) is **primitive** if for every \(w\in P\) some entry \(y_a\) has a nonzero (equivalently, unit) component at \(w\).

## Properties

**Glued datum as a sum.** For all \(T,R\),
\[
\operatorname{glued}(T,R)=\sum_{y\in((\mathbb Z/N)^P)^{n'}}\operatorname{lastcol}_y(T)\cdot\operatorname{char}_y(R).
\]
Indeed, if \(T\) is not integral both sides vanish; if \(T\) is integral exactly the term with \(y=\bar Te_\ast\) survives and \((\bar R\bar T)_{\ast\ast}=\bar R_\ast\cdot\bar Te_\ast\).

**In terms of absolute values.** The last-row datum is \(1\) at \(T\) iff \(\lvert T_{ij,w}\rvert_w\le1\) for all \(i,j,w\), \(\lvert T_{\ast j,w}\rvert_w\le e^{-1}\) for \(j\in n\), and \(\lvert T_{\ast\ast,w}-1\rvert_w\le e^{-1}\); the direct datum is the same with the last column \(T_{i\ast}\), \(i\in n'\), in place of the last row. This is the criterion for the reduction on the page [[proofs/grh/upper-objects/split-level|split level]].

**Change of lattice.** For every \(n'^+\times n^+\) matrix \(T\) over \(E_P\),
\[
\operatorname{lastrow}\big(D_N^{-1}\,T\,D_N\big)=\operatorname{direct}(T).
\]
*Proof.* Put \(C=D_N^{-1}TD_N\). Then \(C_{ij}=T_{ij}\) for \(i\in n',j\in n\), \(C_{\ast\ast}=T_{\ast\ast}\), \(C_{\ast j}=N\,T_{\ast j}\) and \(C_{i\ast}=N^{-1}T_{i\ast}\). Since \(\lvert N\rvert_w=e^{-1}\), \(\lvert C_{i\ast}\rvert_w\le1\) iff \(\lvert T_{i\ast}\rvert_w\le e^{-1}\), and \(\lvert C_{\ast j}\rvert_w\le e^{-1}\) iff \(\lvert T_{\ast j}\rvert_w\le1\). Comparing the two descriptions by absolute values (and using \(e^{-1}\le1\) for the redundant conditions) gives the claim. \(\square\)

## Remarks

In terms of *marked lattices* (a lattice \(L\) at \(P\) with a vector \(\varepsilon\in L/NL\) that is nonzero at every place), written in bases whose last vector lifts \(\varepsilon\): the direct datum is \(\mathbf 1[SL\subseteq L',\ S\varepsilon=\varepsilon']\); in bases of the enlarged lattices \(L^+=L+\mathcal O\varepsilon/N\) and \(L'^+\) it becomes the last-row datum (this is the change-of-lattice identity); and the mirror datum, for a matrix written in a basis of the original source lattice \(L\) and of the enlarged target lattice \(L'^+\) (in original bases a matrix \(T\) must first be replaced by \(D_N^{-1}T\)), is \(\mathbf 1[SL\subseteq L'^+]\,\psi_N(u'(S\varepsilon))\), with \(u'\) read modulo \(N\), where \(u'\) is the linear form on \(L'^+\) with kernel \(L'\) and \(u'(\varepsilon'/N)=1\). This interpretation is the comment at the head of the Lean file; only the matrix definitions above are used in proofs.

## References

1. Lean: `New.IsSplitLevel.lastRowDatum`, `lastColDatum`, `charDatum`, `directDatum`, `mirrorDatum`, `gluedDatum`, `gluedDatum_eq_sum`, `lastRowDatum_conj_diagNInv` in `src/New/UpperBound/Objects/LiftLawsModuloN.lean`.

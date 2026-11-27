+++
id = "proofs/grh/upper-seesaw/double-lift-data"
title = "Double lift data and the finite evaluation of a pair of edges"
kind = "construction"
summary = "For two consecutive lifts between graded spaces with strings of lengths s, s-1, s-2, the grade-zero part of V-minus plus V'' is X-minus plus X'' plus hyperbolic planes; this gives a splitting and an evaluation of finite data."
aliases = ["grade zero part", "consecutive strings", "middle double lift", "last double lift", "finite evaluation of an edge pair", "stacked string map"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.GradeZeroPart", "New.Seesaw.GradeZeroPart.splitting", "New.Seesaw.GradeZeroPart.hom", "New.Seesaw.stackedStringMap", "New.Seesaw.stackedStringMapFin", "New.Seesaw.HasConsecutiveStrings", "New.Seesaw.DoubleLiftData", "New.Seesaw.DoubleLiftData.homZeroPart", "New.Seesaw.DoubleLiftData.splitting", "New.Seesaw.DoubleLiftData.finEval", "New.Seesaw.DoubleLiftData.arrowTensor_finEval", "New.Seesaw.middleDoubleLift", "New.Seesaw.lastDoubleLift"]
lean_files = ["src/New/UpperBound/Seesaw/EdgePairEvaluation.lean"]
+++

Let \(V,V',V''\) be [[?lean:New.Space|hermitian spaces with points]] over a [[?c:CM field|CM field]]
\(E\) with [[?lean:New.Grading|gradings]] \(Y,Y',Y''\): definite parts \(X,X',X_0\) of grade \(0\)
plus strings of lengths \(s,s',s''\), with the same parameter \(N\).

**Grade zero part.** Let integer weights \(\mathrm{wt}\) be given on the basis of a space \(V\). A
**grade zero part** of \(V\) is a space \(V''\) with a rational isometry \(V''\to V\) onto the span
of the basis vectors of weight \(0\) (given with a labelling of those vectors by the basis of
\(V''\)), under the assumption that the Gram matrix of \(V\) pairs two basis vectors only if their
weights add to \(0\). It determines a [[?lean:New.Space.Splitting|splitting]] of \(V\) over \(V''\):
the [[?c:Isotropic subspace|isotropic]] frame \(k\) consists of the basis vectors of positive weight, the dual frame is
\(l=J^{-1}k\), and \(i\) is the inclusion. (The numbers of basis vectors of positive and of
negative weight agree, because the projections onto them are conjugate by \(J\).) If all weights
are even and the string of \(Y'\) has even length, then \(\operatorname{Hom}(X',V'')\) is a grade
zero part of \(\operatorname{Hom}(V',V)\) for the weights \(\mathrm{wt}(r)-\operatorname{gr}'(r')\).

**Consecutive strings.** \((Y,Y',Y'')\) *have consecutive strings* if \(s\) is odd, \(s'=s-1\),
\(s''=\max(s'-1,0)\), and \(Y,Y'\) have the same constant.

**Double lift data.** For finite sets \(X''\) and \(q\), **double lift data** for \((Y,Y',Y'')\)
consist of: consecutive strings; the evenness of \(\dim V+\dim V''\); a grade zero part of
\(V^{-}\oplus V''\) (\(V^-\) is \(V\) with the negative form), namely the orthogonal sum of \(q\)
[[?c:Hyperbolic plane|hyperbolic planes]] and the standard definite spaces on \(X\) (negated) and \(X''\); a
determinant-preserving homomorphism \(\epsilon\colon U(X_0)(\mathbb{A})\to U(X'')(\mathbb{A})\)
such that the inclusion of the grade zero part intertwines the action of \((g,k)\in U(X)\times U(X_0)\)
on \(V^-\oplus V''\) with \(1\oplus g\oplus\epsilon(k)\); and an injection of \(q\) into the basis
vectors of \(V'\) of grade \(1\) such that, in the rows of grade zero, the corresponding columns of
the **stacked string map** \((T^{*},T')\colon V'\to V^{-}\oplus V''\) are the constant \(c_{Y'}\)
times the second basis vector of the corresponding plane, and all other columns vanish. Here
\(T\colon V\to V'\) and \(T'\colon V'\to V''\) are the
[[?lean:New.Grading.stringMap|string maps]] and \(T^{*}\) the adjoint of \(T\).

Two instances are constructed:

* the **middle double lift** (\(s\ne1\) odd, strings \(s,s-1,s-2\); \(X''=X_0\), one plane): the
  plane is spanned by \((z-z')/(2N)\) and \(z+z'\), where \(z,z'\) are the middle string vectors of
  \(V\) and \(V''\), of norms \(N\) (in \(V^-\)) and \(-N\);
* the **last double lift** (\(s=1\), so \(Y',Y''\) have no string; \(N=p\bar p\) with \(p\in E\);
  \(X''=X_0\sqcup\{\ast\}\), no plane): the vector \(z/p\), \(z\) the string vector of \(V\), of
  norm \(1\) in \(V^-\), is adjoined to \(X_0\) as last basis vector of \(X''\), and \(\epsilon(k)\)
  fixes it.

**Splitting and evaluation.** Double lift data give a splitting of
\(\operatorname{Hom}(V',V^-\oplus V'')\) over \(\operatorname{Hom}(X',X^-\oplus X'')\): first to the
grade zero part \(\operatorname{Hom}(X',\text{planes}\oplus X^-\oplus X'')\), then removing the maps
into the hyperbolic planes. The **finite evaluation** is the linear map
\[
\operatorname{ev}\colon\mathcal{S}\bigl(\operatorname{Hom}(V',V^-\oplus V'')\bigr)\to
\mathcal{S}_f\bigl(\operatorname{Hom}(X,X')\bigr)\otimes\mathcal{S}_f\bigl(\operatorname{Hom}(X',X'')\bigr)
\]
that applies the translation \(\varrho_f(\tau)\), \(\tau=\alpha^{-1}\bigl(S^{\flat}\bigr)_f\), where \(S=(T^{*},T')\) is the stacked string map, \(S^{\flat}\) its adelic coordinate vector in the frame of \(\operatorname{Hom}(V',V^{-}\oplus V'')\) (the points of the spaces, not the rational bases), \((\cdot)_f\) the finite part and \(\alpha\) the finite idele of the Weil data (so \(\tau\) is not simply the finite part of the matrix of \(S\)); then applies the
[[proofs/grh/upper-seesaw/finite-zero-term|finite zero term]] of this splitting, and splits the
result by a left inverse of the [[?lean:New.Seesaw.arrowTensor|join of finite data]]
\(\mathcal{S}_f\otimes\mathcal{S}_f\to\mathcal{S}(\operatorname{Hom}(X',X^-\oplus X''))\). On joined
finite data \(\Phi\ast\Psi\) (with \(\Phi\) on \(\operatorname{Hom}(V,V')\), \(\Psi\) on
\(\operatorname{Hom}(V',V'')\)) the left inverse is exact: the join of \(\operatorname{ev}(\Phi\ast\Psi)\)
equals the finite zero term of the translated \(\Phi\ast\Psi\), because the finite zero term and the
finite Heisenberg operators preserve finite parts, which are the range of the join.

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Seesaw/EdgePairEvaluation.lean`.

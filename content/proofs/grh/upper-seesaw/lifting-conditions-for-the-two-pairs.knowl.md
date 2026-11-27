+++
id = "proofs/grh/upper-seesaw/lifting-conditions-for-the-two-pairs"
title = "The lifting and denominator conditions for the middle and the last double lift"
kind = "lemma"
summary = "Neighbour vectors lift to the lattice and denominators match, for the middle double lift with trivial scaling and for the last double lift with the scaling delta at the last vector."
aliases = ["last scaling"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.liftsNeighbours_middleDoubleLift", "New.Seesaw.matchesDenominators_middleDoubleLift", "New.Seesaw.lastScaling", "New.Seesaw.liftsNeighbours_lastDoubleLift", "New.Seesaw.matchesDenominators_lastDoubleLift"]
lean_files = ["src/New/UpperBound/Seesaw/AdmissibleEvaluation.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/upper-seesaw/admissible-evaluation-of-edge-pairs|the admissible
evaluation of edge pairs]]: flip scale \(s_E\), unit \(\eta\) of norm \(-1\), conditions "lifts
neighbours" and "matches denominators".

In both cases \((Y,Y',Y'')\) [[proofs/grh/upper-seesaw/double-lift-data|have consecutive strings]]; this includes that \(Y\) and \(Y'\) have the same constant, \(c_Y=c_{Y'}\), which is needed for the double lifts to be defined.

**Lemma.**

1. (**Middle double lift.**) Let \(Y,Y',Y''\) have consecutive strings of lengths \(m\ne1\) odd,
   \(m-1\), \(m-2\), with \(\dim V+\dim V''\) even. Suppose \(Y\) and \(Y''\)
   [[proofs/grh/upper-seesaw/graded-lattice-basis|span the lattices]] of \((a,\pi,u)\) and
   \((a,\pi,u'')\), and \(s_Eu=\bar\eta\,\delta\,u''\). Then the middle double lift lifts neighbours
   for \((\pi,u,\kappa=1,\delta)\), and matches denominators for \(\kappa=1\) and every \(\beta\).
2. (**Last double lift.**) Let \((Y,Y',Y'')\) have consecutive strings of lengths \(1,0,0\) (in particular \(c_Y=c_{Y'}\)), \(V''\) be standard,
   \(\dim V+\dim V''\) even and \(N=p\bar p\) with \(\pi\) the principal idele of \(p\). Suppose
   \(Y\) spans the lattice of \((a,\pi,u)\) and \(s_Eu=\bar\eta\delta\). Let \(\kappa\) be the
   **last scaling**: \(\delta\) at \(e''\) and \(1\) elsewhere. Then the last double lift lifts
   neighbours for \((\pi,u,\kappa,\delta)\); and it matches denominators for \((\kappa,\beta)\)
   provided \(\bar\beta\delta\) and \(\beta\) have the same valuation at every [[algebra-fields-galois/place-of-global-field|finite place]].

## Proof

*Two tests.* (i) A vector \(y\) of \(V^{-}\oplus V''\) lies in the lattice iff its first block
divided by \(s_E\) lies in the lattice of \(V\) and its second block in that of \(V''\): the
inverse point of \(V^-\oplus V''\) is block diagonal with blocks \(s_E^{-1}x_f(V)^{-1}\) and
\(x_f(V'')^{-1}\). (ii) Let \(Y\) span the lattice of \((a,\pi,u)\) with odd string and middle
vector \(z\). A vector with coordinates \(x_i\) on \(X\), \(x_e\) at \(e\), \(u(\pi^{-1}x_e+c')\)
at \(z\) and \(0\) at the other string vectors lies in the lattice provided \(x_i\),
\(\bar\pi x_e\) and \(c'\) are integral: its coordinates in the
[[proofs/grh/upper-seesaw/graded-lattice-basis|glued basis]] are \(x_i\), \(\bar\pi x_e\) (at the
glued vector \(\bar\pi^{-1}e+u(\pi\bar\pi)^{-1}z\), which contributes
\(u(\pi\bar\pi)^{-1}\bar\pi x_e=u\pi^{-1}x_e\) at \(z\)) and \(c'\) (at \(uz\)).

Let \((c,x)\) be a neighbour vector: \(\delta c=c\); \(x_i\) integral for \(i\ne e,e''\);
\(\bar\pi x_e,\bar\pi x_{e''}\) integral; \(c-\pi^{-1}x_e\) and \(\bar\eta c-\pi^{-1}x_{e''}\)
integral.

(1) In the middle double lift the plane has the basis \((z-z'')/(2N)\), \(z+z''\) (\(z,z''\) the
middle string vectors of \(V,V''\)) and the inclusion is the identity on the definite parts. With
\(\kappa=1\) the lift vector has coordinates: \(s_Ex_i\) on \(X\sqcup e\); \(s_Euc\) at \(z\);
\(x_i\) on \(X''\sqcup e''\); \(s_Euc\) at \(z''\); \(0\) at the other string vectors.

*First block*, divided by \(s_E\): \(x\) on \(X\sqcup e\) and \(uc=u(\pi^{-1}x_e+c')\) at \(z\) with
\(c'=c-\pi^{-1}x_e\) integral. Test (ii) applies.

*Second block*: by the hypothesis \(s_Eu=\bar\eta\delta u''\) and \(\delta c=c\), the coordinate at
\(z''\) is \(u''\bar\eta c=u''(\pi^{-1}x_{e''}+c'')\) with \(c''=\bar\eta c-\pi^{-1}x_{e''}\)
integral. Test (ii) applies to \(Y''\) (its string length \(m-2\) is odd).

*Denominators*: the inclusion joins an index of \(X\sqcup e\) only to indices of \(V\) and an index
of \(X''\sqcup e''\) only to indices of \(V''\), so both weights are \(\beta\), resp. both
\(\bar\beta\).

(2) In the last double lift there is no plane; the inclusion is the identity on \(X\sqcup e\) and
on \(X''=X_0\), and sends \(e''\) to \(p^{-1}z\), with \(z\) the string vector of \(V\). With the
last scaling the lift vector has coordinates: \(s_Ex_i\) on \(X\sqcup e\);
\(\pi^{-1}\delta x_{e''}\) at \(z\) (as \(\pi^{-1}=p^{-1}\)); \(x_i\) on \(X''\).

*First block*, divided by \(s_E\): \(x\) on \(X\sqcup e\) and \(s_E^{-1}\delta\,\pi^{-1}x_{e''}\) at
\(z\). From \(s_Eu=\bar\eta\delta\) and \(\eta\bar\eta=-1\): \(s_E^{-1}\delta=-\eta u\). So the
coordinate at \(z\) is \(-u\eta\pi^{-1}x_{e''}=u(\pi^{-1}x_e+c')\) with
\[
c'=-\pi^{-1}x_e-\eta\pi^{-1}x_{e''}=(c-\pi^{-1}x_e)+\eta\,(\bar\eta c-\pi^{-1}x_{e''}),
\]
integral (the terms in \(c\) cancel because \(\eta\bar\eta=-1\)). Test (ii) applies (\(m=1\)).

*Second block*: \(V''\) is standard, its point is \(1\) and its string is empty; the coordinates
are the \(x_i\), \(i\in X''\), which are integral.

*Denominators*: the only index joined across blocks is \(e''\) (second block, weight
\(\bar\beta\), scaled by \(\kappa_{e''}=\delta\)), joined to \(z\) in \(V\) (weight \(\beta\)); the
hypothesis says \(\bar\beta\delta\) and \(\beta\) have equal valuations. All other joined pairs lie
in the same block with \(\kappa=1\). \(\blacksquare\)

## References

1. Lean: `New.Seesaw.liftsNeighbours_middleDoubleLift`, `New.Seesaw.matchesDenominators_middleDoubleLift`, `New.Seesaw.liftsNeighbours_lastDoubleLift`, `New.Seesaw.matchesDenominators_lastDoubleLift` in `src/New/UpperBound/Seesaw/AdmissibleEvaluation.lean`.

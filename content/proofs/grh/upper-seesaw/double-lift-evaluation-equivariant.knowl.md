+++
id = "proofs/grh/upper-seesaw/double-lift-evaluation-equivariant"
title = "The finite evaluation of a pair of edges is equivariant"
kind = "theorem"
summary = "The zero term along the double lift splitting carries the triple Weil action of U(X) x U(X') x U(X_0) on the graded spaces to that on the definite spaces with no extra scalar, and the finite evaluation is equivariant."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.GradeZeroPart.zeroTerm_hom_omega", "New.Seesaw.DoubleLiftData.zeroTerm_splitting_tripleWeil", "New.Seesaw.DoubleLiftData.finEval_arrowProduct_equivariant", "New.Seesaw.inclX_mul_stringMap_mul_inclX_inv"]
lean_files = ["src/New/UpperBound/Seesaw/EdgePairEvaluation.lean"]
proof_status = "outline"
+++

Let \(\mathcal{D}\) be [[proofs/grh/upper-seesaw/double-lift-data|double lift data]] for gradings
\(Y,Y',Y''\) of \(V,V',V''\), with definite parts \(X,X',X_0\), target index set \(X''\) and
homomorphism \(\epsilon\colon U(X_0)\to U(X'')\). For
[[?lean:New.AutChar|automorphic characters]] \(a,b\) of the norm-one adeles, the
[[?lean:New.Seesaw.tripleWeil|triple Weil operator]] \(W_{a,b}(g,g',k)\) on
\(\mathcal{S}(\operatorname{Hom}(V',V^-\oplus V''))\) is the Weil operator of \((g',g\oplus k)\) times
three scalar characters: that of \((g,g')\) made from \(a\), that of \((g',k)\) made from \(b\), and
one made from the splitting character \(\upsilon\) and the ranks of \(V'\) and \(V\).

**Theorem.**

1. For adelic points \(g,g',k\) of \(U(X),U(X'),U(X_0)\), embedded into the big groups by the
   gradings, and all \(f\):
   \[
   Z_{\mathcal{D}}\bigl(W_{a,b}(g,g',k)f\bigr)=W_{a,b}\bigl(g,g',\epsilon(k)\bigr)\,Z_{\mathcal{D}}(f),
   \]
   where \(Z_{\mathcal{D}}\) is the zero term along the splitting of \(\mathcal{D}\) and the right
   operator is the triple Weil operator of the definite spaces \(X,X',X''\).
2. For finite points \(g,g',k\) and \(k'\) with \(\epsilon(1,k)=(1,k')\), and finite data \(\Phi\)
   on \(\operatorname{Hom}(V,V')\), \(\Phi'\) on \(\operatorname{Hom}(V',V'')\):
   \[
   \operatorname{ev}\bigl(\omega_a(g,g')\Phi\ast\omega_b(g',k)\Phi'\bigr)
   =\bigl(\omega_a(g,g')\otimes\omega_b(g',k')\bigr)\operatorname{ev}(\Phi\ast\Phi'),
   \]
   where \(\omega_a,\omega_b\) are the [[?lean:New.Seesaw.liftWeilFin|finite Weil actions twisted by
   the characters]], on the graded spaces on the left and on the definite spaces on the right.

## Proof

(Outline; re-read against the Lean proofs. Asserted: the two library statements named below and the final comparison of the exponents of \(\upsilon\), which Lean settles by linear arithmetic on the ranks.) (1) The zero term is taken in two stages. *Stage one*, to the grade zero part: for a
grade zero part with even weights and \(s'\) even, the zero term carries the Weil operator of
\((h,g)\) (with \(g\) the identity off weight zero, acting as \(g_0\) on the zero part) to that of
\((h,g_0)\) times \(\upsilon\bigl(\det g^{\,s'/2}(\det h)^{-r}\bigr)^{-1}\), \(r\) the number of
basis vectors of positive weight. This comes from the parabolic law of the zero term: on the
[[?c:Isotropic subspace|isotropic]] frame the group element acts by a block matrix whose determinant is the argument of
\(\upsilon\) (Lean: `GradeZeroPart.zeroTerm_hom_omega` via `zeroTerm_omega_of_inclMatrix`; the
entrywise verification was not reproduced). *Stage two*, removing the [[?c:Hyperbolic plane|hyperbolic planes]], on which
the element acts trivially (`homTarget_zeroTerm_pairWeil`), gives the factor \(\upsilon(\det g')^{\lvert q\rvert}\).
The remaining claim is that the total exponents of \(\upsilon\) at \(\det g,\det g',\det k\) agree
on both sides; this follows from the rank formulas and the parities (\(s'\) and
\(\dim V+\dim V''\) even), and \(\det\epsilon(k)=\det k\).

(2) Apply the join to both sides and use the exactness of the left inverse on finite data. The
elements coming from \(U(X),U(X'),U(X_0)\) have trivial real part, so (1) passes to the finite zero
term. The triple Weil operator commutes with the translation by the stacked string map because
\(g'\,T\,g^{-1}=T\) and \(k\,T'\,g'^{-1}=T'\): the string maps kill the definite parts and have
image in the strings, which the embedded groups fix. Finally the translation and the Weil operators
split over the two factors of the join (asserted; `homHeisenbergOp_arrowProduct`,
`arrowProduct_twistedPairWeil`, `pairWeil_homHeisenbergOp`). \(\blacksquare\)

## References

1. Lean: `New.Seesaw.DoubleLiftData.zeroTerm_splitting_tripleWeil`, `New.Seesaw.DoubleLiftData.finEval_arrowProduct_equivariant`, `New.Seesaw.GradeZeroPart.zeroTerm_hom_omega` in `src/New/UpperBound/Seesaw/EdgePairEvaluation.lean`.

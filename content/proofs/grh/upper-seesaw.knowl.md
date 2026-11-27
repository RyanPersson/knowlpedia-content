+++
id = "proofs/grh/upper-seesaw"
title = "Upper bound: the seesaw identity"
kind = "page"
summary = "On ramified source forms, the chain of indefinite theta lifts of a Poincaré series equals a nonzero constant times a definite chain of lifts whose finite data are integral away from the modulus of the twist and bounded in size when the modulus is empty."
aliases = ["seesaw", "the seesaw identity chapter"]
domains = ["proofs"]
section_mode = "continuous"
prerequisites = []
lean_files = ["src/New/UpperBound/Seesaw/AdmissibleCombinations.lean", "src/New/UpperBound/Seesaw/StandardLines.lean", "src/New/UpperBound/Seesaw/Sandwich.lean", "src/New/UpperBound/Seesaw/GluedLevel.lean", "src/New/UpperBound/Seesaw/EdgePairEvaluation.lean", "src/New/UpperBound/Seesaw/IntegralAsCosetSum.lean", "src/New/UpperBound/Seesaw/LevelIdeles.lean", "src/New/UpperBound/Seesaw/Frequency.lean", "src/New/UpperBound/Seesaw/NeighbourLattice.lean", "src/New/UpperBound/Seesaw/NeighbourVacuum.lean", "src/New/UpperBound/Seesaw/AdmissibleEvaluation.lean", "src/New/UpperBound/Seesaw/UnfoldingStages.lean", "src/New/UpperBound/Seesaw/GoodDatum.lean", "src/New/UpperBound/Seesaw/Cut.lean", "src/New/UpperBound/Seesaw/SeesawIdentity.lean"]
+++

This chapter proves the [[proofs/grh/upper-seesaw/seesaw-identity|seesaw identity]]: for the
[[?lean:New.Data|data]] of the proof, a linear form \(t\) and an archimedean point \(g\), there is
a constant \(c\ne0\) such that for every [[?lean:New.Data.Twist|twist]] \(\vartheta\)
\[
\Theta_\vartheta\bigl(\mathcal{P}_{g,t}\varphi\bigr)=c\cdot\operatorname{CL}_\vartheta(\Psi_\vartheta)(\varphi)
\qquad(\varphi\ \text{a ramified source form}),
\]
where the left side is the [[?lean:New.Data.lowerChain|lower chain]] of \(m\)
[[?c:Theta lift|theta lifts]] \(Y_0\to\dots\to Y_m\) applied to the
[[?c:Poincaré series|Poincaré series]] of \(\varphi\), and the right side is the
[[?lean:New.Data.compositeLift|composite lift]]: a finite combination of chains of lifts between
the *definite* spaces \(X_0\to\dots\to X_m\), restricted to \(Y_m\subset X_m\), whose coefficients
\(\Psi_\vartheta\) form a [[?lean:New.Data.IsChainDatum|chain datum]] — integral away from the
modulus of \(\vartheta\), bounded for the empty modulus, supported at the level, invariant
under the levels. The identity is what lets the upper bound of the main argument be read off from
theta series of definite lattices. It does not say that either side is nonzero.

## Notation

\(E=K(\zeta)\) is the CM field of the data, with complex conjugation \(x\mapsto\bar x\);
\(\mathbb{A}_{E,f}\) its finite adeles and \(\widehat{\mathcal{O}}\) the integral ones.
\(M=p_0p_1=\pi_M\bar\pi_M\) and \(N=\pi_N\bar\pi_N\) are the level integers, \(m=2\varrho+2\) the
number of lifts. \(X_j\) are the definite spaces of the upper chain. For \(j<m\), \(Y_j\) is \(X_j\) plus a
*string* of \(m-1-j\) further basis vectors paired antidiagonally; when the string length is odd
its middle vector has norm \(-N\) (an even string has no middle vector)
([[proofs/grh/upper-seesaw/tower-gradings-and-evaluated-data|gradings of the tower]]). At the top,
\(Y_m\) is a standard definite space of rank \(n_m-1\) with an empty string: it is the span of the
basis vectors of \(X_m\) other than the last, so \(Y_m\subset X_m\) has codimension one, and forms
on \(X_m\) are restricted to it. \(\varrho_f(x)\)
is the finite Heisenberg operator of the Weil representation, \(v_0\) the vacuum. A tame character
\(\vartheta\) carries a chosen finite modulus \(Q\): its tame part is trivial outside \(Q\), and for a twist it is nontrivial at every place of \(Q\); the levels, cuts and bounds of the intermediate statements use this chosen \(Q\). \(q=\mathrm{N}Q\) is the product of the norms of its places, and
\(\mathcal{C}=M^{fn_m^2}\).

## 1. Bookkeeping: admissible combinations

All integrality and size statements are carried by one notion: an
[[proofs/grh/upper-seesaw/admissible-combination|admissible combination]] is a finite combination
\(\sum r(x)v_x\) whose coefficients have a fixed denominator
[[proofs/grh/upper-seesaw/integral-away|away from \(n\)]] and, when a proposition \(p\) holds,
bounded absolute sum at every conjugate. They obey
[[proofs/grh/upper-seesaw/admissible-combination-substitution|substitution]] and a
[[proofs/grh/upper-seesaw/admissible-combination-calculus|calculus]] (linear and bilinear maps,
roots of unity, pure tensors, clearing a denominator). The index sets are
[[proofs/grh/upper-seesaw/translation-groups|groups of translations]] with denominators away from
\(q\). Two sources of such combinations are
[[proofs/grh/upper-seesaw/moved-vacuum-admissible|moved vacua]] and
[[proofs/grh/upper-seesaw/schrodinger-operator-admissible|values of Schrödinger operators]]; the
scalars that occur are units by
[[proofs/grh/upper-seesaw/l-adic-units-multiplier-and-characters|an \(l\)-adic unit lemma]].

## 2. The lattices of the graded spaces

The frame of \(Y_k\) spans an explicit
[[proofs/grh/upper-seesaw/graded-lattice-basis|glued lattice]]
([[proofs/grh/upper-seesaw/tower-lattice-data|verified for the tower]]), which is
[[proofs/grh/upper-seesaw/graded-lattice-basis-unimodular|unimodular]] because
\(N=\pi_N\bar\pi_N\) is a
[[proofs/grh/upper-seesaw/split-squarefree-factorisation|split squarefree factorisation]]; the
form has the [[proofs/grh/upper-seesaw/graded-gram-signature|expected signature]]. The lattice is
described [[proofs/grh/upper-seesaw/standard-lattice-membership|coordinate by coordinate]]; its
intersection \(\Lambda^-\) with the span of the string and its projection \(\Lambda^+\) are
[[proofs/grh/upper-seesaw/string-lattices-line-by-line|sums of lines]] that differ only by \(1/N\)
at the middle vector, with [[proofs/grh/upper-seesaw/string-sum-lattice-criteria|explicit
generators]] in the basis of string powers. The shift to the next space satisfies
[[proofs/grh/upper-seesaw/shift-of-string-lattice|\(\operatorname{sh}\Lambda^+=a\Lambda'^-\)]], and
a vector of \(\Lambda^+\setminus\Lambda^-\)
[[proofs/grh/upper-seesaw/generator-of-plus-over-minus|generates the quotient at a place above
\(N\)]]. Elements of \(U(X_k)\) satisfying a congruence modulo \(\pi_N\)
[[proofs/grh/upper-seesaw/glued-level-congruences|stabilise the glued lattice]].

## 3. Unfolding the lower chain

Pairing \(\Theta_\vartheta(\mathcal{P}\varphi)\) with a form on \(Y_m\) and moving the lifts to the
other side one at a time produces [[proofs/grh/upper-seesaw/unfolding-stages|functions
\(\mathcal{W}_k\) on \(U(Y_k)\)]] by repeated unfolding along the Bessel subgroups of the gradings.
Two consecutive steps are computed together: by the
[[proofs/grh/upper-seesaw/double-unfolding-integral|double unfolding integral]], two Bessel
integrals of constant terms at the shifts collapse to a double theta integral over the definite
groups \(U(X)\times U(X')\) of the joined datum, translated along the strings and cut down by a
zero term. The algebra behind this is the
[[proofs/grh/upper-seesaw/double-lift-data|double lift data]]: the grade zero part of
\(V^-\oplus V''\) is \(X^-\oplus X''\) plus hyperbolic planes, the
[[proofs/grh/upper-seesaw/finite-zero-term|finite zero term]] along the resulting splitting gives
the [[proofs/grh/upper-seesaw/double-lift-data|finite evaluation]] of a pair of edges, and this
evaluation is [[proofs/grh/upper-seesaw/double-lift-evaluation-equivariant|equivariant]].
Consequently, after each pair of steps
[[proofs/grh/upper-seesaw/unfolding-stage-as-coefficient-of-chain|\(\mathcal{W}_{2i}\) is a
coefficient of the definite chain]] \(X_0\to\dots\to X_{2i}\) applied to \(\varphi\), with the
*evaluated data* as finite data.

## 4. Support, cuts, and finite sums

For a ramified \(\varphi\), the functions \(\mathcal{W}_j\) have
[[proofs/grh/upper-seesaw/support-of-unfolding-stages|bounded support]]: where
\(\mathcal{W}_j\ne0\), the lattice of the point is sandwiched between
\(\bar{\mathfrak q}^{\,j}\Lambda^-\) and \(\mathfrak q^{-j}\Lambda^-\). The proof combines the
[[proofs/grh/upper-seesaw/shift-maps-lattices|frequency lemma]] (a nonzero constant term at the
shift forces a lattice inclusion), the
[[proofs/grh/upper-seesaw/lattice-bounds-induction-step|sandwich induction]] and its dichotomy,
and the vanishing of \(\mathcal{W}\) where the
[[proofs/grh/upper-seesaw/lattice-splitting-and-scalings|lattice splits]] at a place above \(N\) —
the only place where ramification of \(\varphi\) is used. Bounded support allows each outer
integral to be replaced by a finite weighted sum:
[[proofs/grh/upper-seesaw/integral-as-sum-over-cut|an integral over the Bessel quotient is a
constant times a sum over a cut]] weighted by inverse
[[proofs/grh/upper-seesaw/cover-multiplicity|cover multiplicities]], and
[[proofs/grh/upper-seesaw/cut-with-multiplicities-dividing-powers|cuts whose multiplicities divide
powers of \(q\)]] exist. This gives the
[[proofs/grh/upper-seesaw/stage-cuts|stage cuts]] \(\Omega_j\) and the
[[proofs/grh/upper-seesaw/cut-sum|cut sums]], and the
[[proofs/grh/upper-seesaw/iterated-unfolding|iterated unfolding]] of the whole lower chain.

## 5. Integrality of the evaluated data

The finite zero term of a vacuum is governed by the
[[proofs/grh/upper-seesaw/zero-term-lattice|zero term lattice]], which for a pair of edges is the
[[proofs/grh/upper-seesaw/neighbour-lattice|neighbour lattice]]: a neighbour of the standard
lattice above \(N\), with rows scaled by norm-one factors at \(M\). Its classes modulo integral
points have [[proofs/grh/upper-seesaw/neighbour-lattice-representatives|explicit representatives]],
and summing the translates of the vacuum over them gives
[[proofs/grh/upper-seesaw/neighbour-vacuum|glued translates of the vacua of the two edges]].
Hence [[proofs/grh/upper-seesaw/admissible-evaluation-of-edge-pairs|the finite evaluation is an
admissible evaluation]], once the
[[proofs/grh/upper-seesaw/lifting-conditions-for-the-two-pairs|lifting and denominator conditions]]
are checked for the middle and the last pair. Since the
[[proofs/grh/upper-seesaw/point-data-admissible|translated point data are admissible combinations
of translates of the vacuum]], the
[[proofs/grh/upper-seesaw/evaluated-data-admissible|tensor of all evaluated data is an admissible
combination of glued vacua]], with denominator \(\mathcal{C}^{2m}\) away from \(q\).

## 6. The identity

At the [[proofs/grh/upper-seesaw/top-of-the-chain|top of the chain]], \(Y_m\) is definite and a
period against a form on \(Y_m\) is an inner product with a restricted form. The
[[proofs/grh/upper-seesaw/seesaw-datum|seesaw datum]] \(\varphi_\vartheta\) is the cut sum of the
evaluated tensors; it is invariant and admissible. Then
[[proofs/grh/upper-seesaw/lower-chain-of-poincare-series|the lower chain of the Poincaré series is
\(c_0\) times the restricted upper chain with datum \(\varphi_\vartheta\)]], and clearing the
denominator gives the [[proofs/grh/upper-seesaw/seesaw-identity|seesaw identity]] with the size
bound \(M^{3fmn_m^2}\) for the trivial modulus.

## Status

The chapter has 51 items; of the 42 items with a proof-status label, 35 are full and 7 are outlines. Every Lean file of the folder has been read in full, proofs included. The outlines
are: the [[proofs/grh/upper-seesaw/finite-zero-term|finite zero term]] (mixed model inputs),
[[proofs/grh/upper-seesaw/double-lift-evaluation-equivariant|equivariance of the finite
evaluation]] (two library statements and a comparison of exponents),
[[proofs/grh/upper-seesaw/admissible-evaluation-of-edge-pairs|the admissible evaluation]] (one
block identity), [[proofs/grh/upper-seesaw/double-unfolding-integral|the double unfolding
integral]] and [[proofs/grh/upper-seesaw/unfolding-stage-as-coefficient-of-chain|its consequence]]
(Bessel integrals of the library), [[proofs/grh/upper-seesaw/stage-cuts|the stage cuts]] (a
finiteness statement for lattices), and [[proofs/grh/upper-seesaw/top-of-the-chain|the top of the
chain]] (two archimedean statements). In each, the asserted steps are named by their Lean
declarations. A complete proof may cite a statement of the library part of the Lean source by a
link, and may depend on an outlined item of this chapter; the dependence is always through a link.

Small auxiliary items: [[proofs/grh/upper-seesaw/adjoint-on-weighted-translations|adjoints on
weighted translations]], [[proofs/grh/upper-seesaw/vacuum-translate-away-from-level|moving a
translate away from \(N\)]], [[proofs/grh/upper-seesaw/point-datum-periods|periods of the point
datum]].

## References

1. Lean: the fifteen files of `src/New/UpperBound/Seesaw/`.
2. S. Kudla, *Seesaw dual reductive pairs*, in *Automorphic forms of several variables* (Katata 1983), Progress in Mathematics 46, Birkhäuser, 1984, 244–268.

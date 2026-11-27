+++
id = "proofs/grh/upper-seesaw/neighbour-vacuum"
title = "The vacuum of the neighbour lattice as a combination of glued translates"
kind = "theorem"
summary = "The explicitly indexed sum of the translates of the vacuum by neighbour translations plus representatives of the away quotient (a full system of representatives of the neighbour lattice when the level is split), translated by a vector away from N and read on the two edges, is an admissible combination of glued translates of the vacua of the edges."
aliases = ["glued translate", "admissible evaluation", "IsAdmissibleEval"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.stdPairSpace", "New.Seesaw.gluedTranslate", "New.Seesaw.IsAdmissibleEval", "New.Seesaw.semichar_eq_one_of_smul_eq", "New.Seesaw.finHeisenbergOp_neighbourTranslation_add", "New.Seesaw.finHeisenbergOp_comm_neighbourTranslation", "New.Seesaw.finHeisenbergOp_vacElem_eq_smul_arrowTensor", "New.Seesaw.arrowTensor_doubleLiftGluing", "New.Seesaw.exists_sum_finHeisenbergOp_neighbourTranslation_eq", "New.Seesaw.isAdmissibleCombination_finHeisenbergOp_sum_neighbourCosetRep"]
lean_files = ["src/New/UpperBound/Seesaw/NeighbourVacuum.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/upper-seesaw/neighbour-lattice|the neighbour lattice]], with \(N\)
prime, \((P,N,\pi)\) split squarefree and \(\kappa\) a scaling at \(M\) for \((N,\beta,\delta)\).
Let \(Z=\operatorname{Hom}(X',(X\sqcup e)^{-}\oplus(X''\sqcup e''))\) be the **standard pair space**,
with vacuum \(v_0\), and let
\(\mathcal{S}_f(\operatorname{Hom}(X\sqcup e,X'))\otimes\mathcal{S}_f(\operatorname{Hom}(X',X''\sqcup e''))\xrightarrow{\ \ast\ }\mathcal{S}(Z)\)
be the [[?lean:New.Seesaw.arrowTensor|join of finite data on the two edges]], with its chosen left
inverse \(\ast^{-1}\).

**Definition (glued translate).** For [[?c:Finite adele ring of a number field|finite adelic]] matrices \(t=(t_1,t_2)\) on the two edges,
\[
\mathrm{gl}(t_1,t_2)=\Gamma_N\bigl(\varrho_f(t_1)v_0\otimes\varrho_f(t_2)v_0\bigr),
\]
where \(\Gamma_N\) is the [[?lean:New.Seesaw.doubleLiftGluing|gluing operator]] of the pair: the
sum over residues \(y\colon X'\to(\mathbb{Z}/N)^{P}\) of the translation of the first factor by the
last column \(-y/N\) and of the second factor by the last row \(-\overline{y/N}\).

**Definition (admissible evaluation).** Let \(V,V',V''\) be [[?c:Hermitian space|hermitian spaces]] and \(d\) a family of
finite adeles indexed by the basis of \(V^-\oplus V''\). A map \(L\) from
\(\mathcal{S}(\operatorname{Hom}(V',V^{-}\oplus V''))\) to the tensor product of finite data of the
two standard edges is an **admissible evaluation** (for \(N,P,\beta,d\)) if there is a constant
\(C\) such that for every \(n\) coprime to \(N\), every proposition \(p\), and every \(y\) in the
[[proofs/grh/upper-seesaw/translation-groups|weighted translations]] \(T_n(d)\) (rows weighted by
\(d\)), the vector \(L(\varrho_f(y)v_0)\) is an
[[proofs/grh/upper-seesaw/admissible-combination|admissible combination]] of the vectors
\(C\cdot\mathrm{gl}(t_1,t_2)\), \(t_1,t_2\in T_n(\bar\beta)\), with denominator
\(D_\beta\) away from \(n\) (here \(D_\beta\) is the number of \(I\times X'\)-matrices over \(\widehat{\mathcal{O}}_E/(\beta)\) if finite, and \(0\) otherwise, as in [[proofs/grh/upper-seesaw/neighbour-lattice-representatives|the representatives theorem]]; with \(D_\beta=0\) the denominator condition is empty) and size
\(1\) under \(p\).

**Theorem.** (Only the split squarefree factorisation is used here; that the vectors \(n(y)+t_q\) represent all classes of \(\mathcal{N}\) modulo integral points needs in addition the split level hypothesis, i.e. residue degree one above \(N\).) Let \(x\in T_n\bigl((\beta_i)\bigr)\) (\(\beta_i=\beta\) on the first block of rows,
\(\bar\beta\) on the second) vanish at all places of \(P\cup\bar P\), and let \(K\) be the order of
the away quotient. Then
\[
\ast^{-1}\Bigl(\varrho_f(x)\sum_{(y,q)}\varrho_f\bigl(n(y)+t_q\bigr)v_0\Bigr)
\]
(sum over residue families \(y\) and classes \(q\) of the away quotient) is an admissible
combination of the vectors \(K\cdot\mathrm{gl}(t_1,t_2)\), \(t_1,t_2\in T_n(\bar\beta)\), with
denominator \(D_\beta\) away from
\(n\) and size \(1\) under an arbitrary proposition.

## Proof

The proof uses the following facts about the finite Heisenberg operators and the join (linked Lean
statements of the library):

In the formulas below, for matrices \(x,y\) the expression \(y^{*}x\) inside \(\psi\) or the semicharacter denotes the scalar pairing \(\langle y,x\rangle=\sum_{i,j}\bar y_{ij}x_{ij}=\operatorname{tr}(y^{*}x)\) of the vectors of all entries.

* (**composition**)
  \(\varrho_f(x)\varrho_f(y)=\psi\bigl(\bar c_0\,y^{*}x\bigr)\,\varrho_f(x+y)\) and
  \(\varrho_f(x)\varrho_f(y)=\psi(y^{*}x)\,\varrho_f(y)\varrho_f(x)\), where \(\psi\) is the
  self-dual additive character of the finite adeles (values roots of unity) and \(c_0\) the fixed
  integral adele with \(c_0+\bar c_0=1\)
  ([[?lean:New.Space.finHeisenbergOp_finHeisenbergOp|composition law]],
  [[?lean:New.Space.finHeisenbergOp_comm|commutation law]]);
* (**join**) the join of the two vacua is the vacuum of \(Z\), the join is injective on finite
  data, and for a matrix \(z\) with blocks \(z^{(1)}\) (rows in the first block) and \(z^{(2)}\):
  \[
  \varrho_f(z)(f\ast f')=\operatorname{sc}(z^{(1)})^{2}\cdot\bigl(\varrho_f(\eta\,z^{(1)*})f\bigr)\ast\bigl(\varrho_f(z^{(2)})f'\bigr),
  \]
  where \(\operatorname{sc}(x)=\psi(c_0x^{*}x/2)\) is the semicharacter, a root of unity, and
  \(z^{(1)*}\) the conjugate transpose
  ([[?lean:New.Seesaw.finHeisenbergOp_arrowProduct|translation of a join]]).

*Step 1 (commutation).* \(n(y)\) is supported at \(\bar P\), and \(x\), \(t_q\) vanish at
\(P\cup\bar P\); so \(n(y)^{*}x=0\) and by the composition laws
\(\varrho_f(n(y)+x)=\varrho_f(n(y))\varrho_f(x)\) and
\(\varrho_f(x)\varrho_f(n(y))=\varrho_f(n(y))\varrho_f(x)\). Also, a vector \(v\) supported at
\(\bar P\) has \(v^{*}v=0\) because \(j\bar j=0\); hence \(\operatorname{sc}(v)=1\).

*Step 2 (gluing).* For finite data \(\Phi,\Psi\) on the two edges,
\[
\bigl(\Gamma_N(\Phi\otimes\Psi)\bigr)^{\ast}=\sum_y\varrho_f(n(y))\,(\Phi\ast\Psi).
\]
Indeed, by the join formula with \(z=n(y)\): the first block of \(n(y)\) has the single nonzero
row \(\eta\,\overline{y/N}\) at \(e\), so \(\eta\,z^{(1)*}\) has the single nonzero column
\(\eta\bar\eta\,y/N=-y/N\) at \(e\); the second block has the single nonzero row
\(-\overline{y/N}\) at \(e''\); and the semicharacter of the first block is \(1\) by Step 1. These
are exactly the translations in the definition of \(\Gamma_N\). By linearity the identity holds for
all tensors.

*Step 3 (one translate).* Let \(z\in T_n((\beta_i))\). By the join formula and the fact that the
join of the vacua is the vacuum,
\(\varrho_f(z)v_0=\operatorname{sc}(z^{(1)})^{2}\bigl(\varrho_f(t_1)v_0\otimes\varrho_f(t_2)v_0\bigr)^{\ast}\)
with \(t_1=\eta z^{(1)*}\), \(t_2=z^{(2)}\). Both lie in \(T_n(\bar\beta)\): for \(t_2\) by
definition, and for \(t_1\) because conjugation exchanges the condition "\(\beta x\) integral at
\(w\)" with "\(\bar\beta\bar x\) integral at \(\bar w\)", \(n\) is rational, and \(\eta\) is
integral. With Step 2,
\[
\sum_y\varrho_f(n(y))\varrho_f(z)v_0=\zeta\cdot\mathrm{gl}(t_1,t_2)^{\ast},\qquad\zeta=\operatorname{sc}(z^{(1)})^{2}\ \text{a root of unity}.
\]

*Step 4 (the sum).* By Step 1,
\[
\varrho_f(x)\sum_{(y,q)}\varrho_f(n(y)+t_q)v_0=\sum_q\sum_y\varrho_f(n(y))\,\varrho_f(x)\varrho_f(t_q)v_0
=\sum_q\xi_q\sum_y\varrho_f(n(y))\varrho_f(x+t_q)v_0,
\]
with \(\xi_q=\psi(\bar c_0\,t_q^{*}x)\) a root of unity. Here \(x+t_q\in T_n((\beta_i))\) because
the away lattice lies in the weighted translations
([[proofs/grh/upper-seesaw/neighbour-lattice-representatives|part 2 of the representatives
theorem]]). By Step 3 the term of \(q\) is \(\xi_q\zeta_q\,\mathrm{gl}(t^{q})^{\ast}\) with
\(t^{q}\in T_n(\bar\beta)^{2}\). Applying \(\ast^{-1}\), which inverts the join on its range,
\[
\ast^{-1}(\dots)=\sum_q\frac{1}{K}\cdot\Bigl(\xi_q\zeta_q\cdot K\,\mathrm{gl}(t^{q})\Bigr).
\]
The \(K\) coefficients \(1/K\) have absolute sum \(1\) at every conjugate, and
\(K\) divides \(D_\beta\) by the
same part 2, so \(D_\beta\cdot(1/K)\) is an integer (zero if \(D_\beta=0\)), hence [[proofs/grh/upper-seesaw/integral-away|integral away from \(n\)]]. By rules 1
and 5 of the [[proofs/grh/upper-seesaw/admissible-combination-calculus|calculus]] (finite sums;
change of family up to roots of unity) the claim follows. \(\blacksquare\)

## Remarks

A further lemma of the same file, [[proofs/grh/upper-seesaw/vacuum-translate-away-from-level|moving a translate away from \(N\)]], is used later: if \(n\) is coprime to \(N\), the places above
\(N\) are \(P\cup\bar P\), and \(y\in T_n((\beta_i))\), then \(\varrho_f(y)v_0\) is a root of unity
times \(\varrho_f(y')v_0\) with \(y'=y-1_{P\cup\bar P}\,y\in T_n((\beta_i))\) vanishing above
\(N\). Indeed \(\beta\) is a unit above \(N\) and the places above \(N\) do not divide \(n\), so the
part \(l=1_{P\cup\bar P}y\) is integral; and translates of the vacuum by vectors differing by a
lattice vector agree up to a root of unity.

## References

1. Lean: `New.Seesaw.isAdmissibleCombination_finHeisenbergOp_sum_neighbourCosetRep` and the lemmas listed in the front matter, in `src/New/UpperBound/Seesaw/NeighbourVacuum.lean`.

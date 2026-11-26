+++
id = "proofs/grh/upper-seesaw/admissible-evaluation-of-edge-pairs"
title = "The finite evaluation of a pair of edges is an admissible evaluation"
kind = "theorem"
summary = "Under the lifting and denominator conditions, the finite evaluation sends translates of the vacuum to admissible combinations of glued translates."
aliases = ["lattice lift", "lifts neighbours", "matches denominators"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.flipScale", "New.Seesaw.DoubleLiftData.liftVector", "New.Seesaw.DoubleLiftData.LiftsNeighbours", "New.Seesaw.DoubleLiftData.MatchesDenominators", "New.Seesaw.DoubleLiftData.neighbourLift", "New.Seesaw.DoubleLiftData.latticeLift", "New.Seesaw.DoubleLiftData.conjTranspose_latticeLift_mulVec_stackedStringMapFin", "New.Seesaw.DoubleLiftData.latticeLift_eq_latticeUnitary_add_isotropic", "New.Seesaw.DoubleLiftData.isIntMatrix_latticeLift", "New.Seesaw.DoubleLiftData.zeroTermLattice_splitting_eq", "New.Seesaw.DoubleLiftData.conjTranspose_latticeLift_mulVec_mem", "New.Seesaw.DoubleLiftData.latticeUnitary_mulVec_conjTranspose_latticeLift_mulVec", "New.Seesaw.DoubleLiftData.conjTranspose_iFin_mulVec_mem", "New.Seesaw.DoubleLiftData.exists_finEval_finHeisenbergOp_vacElem", "New.Seesaw.DoubleLiftData.exists_zeroTermFin_splitting_vacElem_eq_sum", "New.Seesaw.isAdmissibleEval_finEval", "New.Seesaw.inv_xFin_mulVec_mem_of_spansLattice"]
lean_files = ["src/New/UpperBound/Seesaw/AdmissibleEvaluation.lean"]
proof_status = "outline"
+++

Let \(\mathcal{D}\) be [[proofs/grh/upper-seesaw/double-lift-data|double lift data]] for gradings
\(Y,Y',Y''\) of \(V,V',V''\) with definite parts \(X\sqcup e\), \(X'\sqcup e'\) and target index set
\(X''\sqcup e''\), planes indexed by \(q\). Let \(N\) be prime with places above it \(P\cup\bar P\)
([[?lean:New.IsSplitLevel|split level]]), \((P,N,\pi)\) a
[[proofs/grh/upper-seesaw/split-squarefree-factorisation|split squarefree factorisation]], and
\(\kappa\) a [[proofs/grh/upper-seesaw/neighbour-lattice|scaling at \(M\)]] for \((N,\beta,\delta)\).
Let \(s_E\) be the **flip scale**, the [[?c:Idele group|finite idele]] \(\bar\eta\,\bar\alpha\alpha^{-1}\) by which
negating the form scales the point of a space.

**Conditions.** For a unitary adele \(u\):

* (**lifts neighbours**) for every
  [[proofs/grh/upper-seesaw/neighbour-lattice|neighbour vector]] \(x\) with coefficient \(c\), the
  vector of grade zero in \(V^-\oplus V''\) with component \(\kappa x\) in \(X^-\oplus X''\) (the
  part in \(X^-\) multiplied by \(s_E\)) and coefficient \(s_Euc\) at the second basis vector of each
  plane lies in the lattice of \(V^{-}\oplus V''\);
* (**matches denominators**) whenever the inclusion of the grade zero part joins an index \(b\) of
  \(X^-\oplus X''\) to an index \(i\) of \(V^-\oplus V''\), \(\beta_i\) and \(\beta_b\kappa_b\) have
  the same valuation at every [[algebra-fields-galois/place-of-global-field|finite place]] (\(\beta_\cdot=\beta\) on first blocks, \(\bar\beta\) on
  second blocks).

**Theorem.** Suppose \(Y'\) [[proofs/grh/upper-seesaw/graded-lattice-basis|spans the lattice]] of
some \((a,\pi,u')\) and both conditions hold. Then:

1. the [[proofs/grh/upper-seesaw/zero-term-lattice|zero term lattice]] of the splitting of
   \(\mathcal{D}\) is the neighbour lattice \(\mathcal{N}\) (with \(X'\sqcup e'\) as column set);
2. the finite zero term of the vacuum of \(\operatorname{Hom}(V',V^-\oplus V'')\) is a nonzero
   multiple of \(\sum_{(y,q)}\varrho_f(n(y)+t_q)v_0\);
3. the [[proofs/grh/upper-seesaw/double-lift-data|finite evaluation]] \(\operatorname{ev}\) of
   \(\mathcal{D}\) is an [[proofs/grh/upper-seesaw/neighbour-vacuum|admissible evaluation]] for
   \((N,P,\beta)\) and the weights \(d_i=\beta_i\).

## Proof

Write \(W=\operatorname{Hom}(V',V^{-}\oplus V'')\) with vacuum \(v_0\), \(Z\) for the standard pair
space with columns \(X'\sqcup e'\), \(\tau\) for the finite coordinates of the stacked string map,
\(i_f,k_f\) for the finite frames of the splitting of \(\mathcal{D}\), and
\(u_{\mathcal{N}}=(\gamma\operatorname{diag}\kappa)\otimes1\) for the lattice unitary.

*The lattice lift.* For \(c\in\mathbb{A}_{E,f}\) and \(x\in\mathbb{A}_{E,f}^{I}\) the **lift
vector** \(\lambda(c,x)\in\mathbb{A}_{E,f}^{\iota\sqcup\iota''}\) is the image, under the inclusion
of the grade zero part, of the vector with coefficient \(0\) at the first and \(s_Euc\) at the
second basis vector of each plane, \(s_E\kappa_ix_i\) at \(i\in X\sqcup e\) and \(\kappa_ix_i\) at
\(i\in X''\sqcup e''\). Let \(A\) be the matrix whose column \(j\) is \(\lambda(c_j,\gamma_j)\) in
lattice coordinates of \(V^{-}\oplus V''\) (\(\gamma_j\) the column of \(\gamma\), \(c_j\) its
neighbour coefficient), \(R\) the rows of the point of \(V'\) at \(X'\sqcup e'\), and
\(B=A\otimes R^{\mathsf T}\), the matrix of \(x\mapsto AxR\).

(a) \(R\) is integral: \(m'\) is even, so the glued basis of \(Y'\) is the identity on
\(X'\sqcup e'\), and the rows of the point \(x'_f=\mathcal{B}'k\) at these indices are rows of
\(k\in\mathrm{GL}(\widehat{\mathcal{O}})\).

(b) \(R^{*}=x'^{-1}_f\cdot(\text{inclusion of }X'\sqcup e')\), because \(x'^{-1}_f=x'^{*}_fJ'\) and
\(J'=1\) on \(X'\sqcup e'\). Hence \(B^{*}\tau=0\): applying \(B^{*}\) first restricts the map
\((T^{*},T')\) to \(X'\sqcup e'\), where it vanishes — \(T'\) kills the definite part of \(V'\),
and \(T^{*}\) does too since the image of \(T\) lies in the string of \(V'\), which is orthogonal
to \(X'\sqcup e'\).

(c) \(B=i_f\,u_{\mathcal{N}}+k_f\,C\), where \(C\) is zero at the frame indices of positive degree
and is \((s_Eu\,c_j)\otimes1\) at the planes. In Lean this is proved by unfolding the definitions
of the two-stage splitting (grade zero part, then removal of the planes) and of \(A\): in the grade
zero part, the lifted column \(j\) is the column of \(\gamma\operatorname{diag}\kappa\) read in the
frame of \(X^{-}\oplus X''\) (whose finite point is \(\operatorname{diag}(s_E,1)\)), plus
\(s_Euc_j\) times the isotropic vector of each plane; both summands are then Kronecker products
with the same second factor \(R^{\mathsf T}\). This unfolding
(`latticeLift_eq_latticeUnitary_add_isotropic`) is the one step of this proof that is asserted
rather than recomputed here.

(d) \(B\) is integral: an entry of \(A\) is a coordinate of the lift of a column of \(\gamma\)
with its neighbour coefficient, which is a neighbour vector
([[proofs/grh/upper-seesaw/neighbour-lattice|the neighbour lattice]]), so it is integral by the
condition "lifts neighbours"; and \(R\) is integral by (a).

(e) For \(y\) vanishing above \(N\): \(u_{\mathcal{N}}B^{*}y=i_f^{*}y\). By (c),
\(B^{*}=u_{\mathcal{N}}^{*}i_f^{*}+C^{*}k_f^{*}\). The neighbour coefficients are supported at
\(P\cup\bar P\), so \(C=1_{P\cup\bar P}C\) and \(C^{*}k_f^{*}y=C^{*}k_f^{*}(1_{P\cup\bar P}y)=0\);
and \(u_{\mathcal{N}}u_{\mathcal{N}}^{*}=1\).

(f) \(B^{*}\) maps \(T_n((\beta_i))\) into \(T_n((\beta_b\kappa_b))\). By the [[proofs/grh/upper-seesaw/adjoint-on-weighted-translations|criterion for
adjoints of integral matrices]] (if \(M\) is integral and \(M_{ij}\) vanishes at \(\bar w\) whenever
the weights \(d_i,d'_j\) have different valuations at \(w\), then \(M^{*}\) maps \(T_n(d)\) into
\(T_n(d')\); this is immediate from \((M^{*}y)_j=\sum_i\overline{M_{ij}}y_i\)), it suffices that
\(A_{ij}\) vanishes at \(\bar w\) whenever \(\beta_i\) and \(\beta_j\kappa_j\) have different
valuations at \(w\). Such a \(w\) is not above \(N\) (there all these are units and \(\kappa=1\)).
Outside \(P\cup\bar P\), column \(j\) of \(\gamma\) is the basis vector \(j\) and \(c_j=0\), so the
lift is \(\kappa_j\) (times \(s_E\) or \(1\)) times column \(j\) of the inclusion. Its coordinate
at \(i\) is a sum over indices \(l\) in the same block as \(i\) (the point of \(V^-\oplus V''\) is
block diagonal) with nonzero entry \((l,j)\) of the inclusion; for those, "matches denominators"
gives that \(\beta_l=\beta_i\) and \(\beta_j\kappa_j\) have equal valuations — excluded. So the sum
is empty.

(1) By (c) and (d), part 1 of [[proofs/grh/upper-seesaw/zero-term-lattice|the zero term lattice
lemma]] applies with \(g=u_{\mathcal{N}}\): \(u_{\mathcal{N}}L^{\circ}\subseteq L'_{\mathcal{D}}\),
and equality holds since both lattices are self-dual.

(2) By (1), part 4 of the same lemma, and
[[proofs/grh/upper-seesaw/neighbour-lattice-representatives|part 5 of the representatives
theorem]] (the \(n(y)+t_q\) lie in \(\mathcal{N}\) and represent it uniquely modulo integral
points): \(Z^{f}(v_0)=c\sum_{(y,q)}\varrho_f(n(y)+t_q)v_0\) with \(c\ne0\).

(3) Take \(C=c\cdot K\). Let \(n\) be coprime to \(N\), \(p\) a proposition and
\(y\in T_n((\beta_i))\). By [[proofs/grh/upper-seesaw/vacuum-translate-away-from-level|moving a translate away from \(N\)]],
\(\varrho_f(y)v_0=\xi\,\varrho_f(y')v_0\) with \(\xi\) a root of unity and \(y'\in T_n((\beta_i))\)
vanishing above \(N\). By definition,
\(\operatorname{ev}(\varrho_f(y')v_0)=\ast^{-1}Z^{f}\bigl(\varrho_f(\tau)\varrho_f(y')v_0\bigr)\), and
\(\varrho_f(\tau)\varrho_f(y')=\xi'\varrho_f(\tau+y')\) with \(\xi'\) a root of unity. By part 5 of
the zero term lattice lemma (with the integral matrix \(B=i_fu_{\mathcal{N}}+k_fC\)),
\[
Z^{f}\bigl(\varrho_f(\tau+y')v_0\bigr)=\zeta\,\varrho_f\bigl(u_{\mathcal{N}}B^{*}(\tau+y')\bigr)Z^{f}(v_0)=\zeta\,\varrho_f(i_f^{*}y')\,Z^{f}(v_0),
\]
with \(\zeta\) zero or a root of unity, using (b) and (e). The vector \(x=i_f^{*}y'\) vanishes
above \(N\), and by (e) and part 1 of the representatives theorem's proof
\(x=u_{\mathcal{N}}B^{*}y'=\kappa\cdot B^{*}y'\); by (f) it lies in \(T_n((\beta_b))\). By (2) and
[[proofs/grh/upper-seesaw/neighbour-vacuum|the theorem on the vacuum of the neighbour lattice]],
\(\ast^{-1}\bigl(\varrho_f(x)Z^{f}(v_0)\bigr)\) is \(c\) times an admissible combination of the
\(K\,\mathrm{gl}(t_1,t_2)\), i.e. an admissible combination of the \(C\,\mathrm{gl}(t_1,t_2)\), with
the stated denominator and size \(1\). Multiplying by \(\xi\xi'\zeta\) preserves this
([[proofs/grh/upper-seesaw/admissible-combination-calculus|rule 4]]). \(\blacksquare\)

## Remarks

Status: the argument is complete except for the block identity (c), and it rests on
[[proofs/grh/upper-seesaw/zero-term-lattice|the zero term lattice lemma]], which is itself an
outline.

## References

1. Lean: `New.Seesaw.isAdmissibleEval_finEval`, `New.Seesaw.DoubleLiftData.zeroTermLattice_splitting_eq`, `New.Seesaw.DoubleLiftData.exists_zeroTermFin_splitting_vacElem_eq_sum` and the lemmas listed in the front matter, in `src/New/UpperBound/Seesaw/AdmissibleEvaluation.lean`.

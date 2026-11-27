+++
id = "proofs/grh/upper-seesaw/stage-cuts"
title = "The cuts for the outer variables"
kind = "lemma"
summary = "For each stage j there is a finite set of classes modulo the level, stable under the integral Bessel points, consisting of points integral away from q, with multiplicities dividing powers of q and nonzero on the support of the unfolding."
aliases = ["stage cut", "cut points", "cut multiplicity"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsStageCut", "New.Data.exists_conj_pow_mem_stdLevel", "New.Data.exists_isStageCut", "New.Data.cutPoints", "New.Data.cutMultiplicity", "New.Data.isStageCut_cutPoints", "New.Data.mk_mem_cutPoints_zero", "New.Data.mem_localLevel_of_mem_cutPoints", "New.Data.exists_cutMultiplicity_dvd", "New.Data.smul_mem_cutPoints_iff", "New.Data.cutMultiplicity_smul", "New.Data.card_le_residueMatrixCount"]
lean_files = ["src/New/UpperBound/Seesaw/Cut.lean"]
proof_status = "outline"
+++

Let \(D\) be the [[?lean:New.Data|data]], \(\vartheta\) a tame character with chosen modulus \(Q\) (a finite set of places outside which its tame part is trivial; the tame part may also be trivial at places of \(Q\), and \(Q\) is the exact support only for a [[?lean:New.Data.Twist|twist]]); below \(Q\) always means this chosen set, \(q=\mathrm{N}Q\), and \(\mathfrak{q}\) the
[[proofs/grh/upper-seesaw/support-of-unfolding-stages|twist idele]]. For \(j\le m-1\) let
\(G_{j,f}\) be the [[?c:Finite adele ring of a number field|finite adelic]] unitary group of \(Y_j\), \(K_j\) the stabiliser of the standard
lattice, \(J_j\le K_j\) the [[?lean:New.Data.levelY|level]] of elements reducing to \(1\) at the
chosen places and at \(Q\), and \(R_{j,f}\) the finite Bessel subgroup of the grading of \(Y_j\).

**Definition.** A finite set \(T\subseteq G_{j,f}/J_j\) is a **stage cut** if, with \(m_T\) the
[[proofs/grh/upper-seesaw/cover-multiplicity|cover multiplicity]] for \(S=R_{j,f}\), \(A=K_j\):

1. \(T\) is stable under \(R_{j,f}\cap K_j\);
2. every \(x\) with \(xJ_j\in T\) is integral at all places not dividing \(q\);
3. \(m_T(xJ_j)\) divides a power of \(q\) for \(xJ_j\in T\);
4. \(m_T(xJ_j)\ne0\) whenever the orbit of \(x\) is
   [[proofs/grh/upper-seesaw/lattice-bounds-induction-step|bounded]] for \((\mathfrak{q},j)\).

**Lemma.** For every \(j\le m-1\) a stage cut exists. Define the **cut points** \(\Omega_j\) as the
set of classes of the elements of the chosen level for \(j=0\), and a chosen stage cut for
\(j\ge1\); and the **cut multiplicity** \(\mu_j\) as \(1\) for \(j=0\) and \(m_{\Omega_j}\) for
\(j\ge1\). Then:

* points over \(\Omega_j\) are integral away from \(q\), and \(\mu_j\) divides a power of \(q\) on
  \(\Omega_j\);
* for \(b\) in the level of \(U(X_j)\), translation by the image of \(b\) in \(G_{j,f}\) permutes
  \(\Omega_j\); for every finite point \(b\) of \(U(X_j)\) it preserves \(\mu_j\);
* if \(Q=\emptyset\), every finite set of classes modulo \(J_k\) (\(k<m\)) consisting of points
  integral everywhere has at most \(\mathcal{C}=M^{fn_m^{2}}\) elements.

## Proof

(Outline.) *Powers.* If \(x\) is integral at all places outside \(Q\cup\bar Q\), there is \(n\)
with \((xux^{-1})^{q^{n}}\in K_j\) for all \(u\in J_j\): outside \(Q\cup\bar Q\) the conjugate is
integral; at \(w\in Q\cup\bar Q\), \(u\equiv1\), high \(q\)-th powers of \(u\) are as close to
\(1\) as desired (lifting the exponent; \(q\) is divisible by the residue characteristic), and
conjugation by \(x\) keeps elements close enough to \(1\) integral.

*Existence.* Finitely many cosets \(cK_j\), with \(c\) supported on \(Q\cup\bar Q\), meet all
\(R_{j,f}\)-orbits that are bounded for \((\mathfrak q,j)\) (asserted; a finiteness statement for
lattices between \(\bar{\mathfrak q}^{j}\Lambda\) and \(\mathfrak q^{-j}\Lambda\) from
`Lib/Weil/Periods/LatticeBounds`). Let \(D\) be their union, a compact set whose points are
integral away from \(q\). Apply
[[proofs/grh/upper-seesaw/cut-with-multiplicities-dividing-powers|the cut lemma]] with
\(S=R_{j,f}\), \(A=K_j\), \(J=J_j\), \(B\) the group of points integral away from \(q\), and \(W\)
= "the orbit is bounded".

*Properties.* For \(j=0\) the image of the compact chosen level in the discrete quotient is finite.
For \(j=0\): \(xJ_0\in\Omega_0\) iff \(x\) lies in the chosen level (as \(J_0\) is contained in the chosen level), and the image of the level of \(X_0\) lies in the chosen level ([[proofs/grh/upper-seesaw/unfolding-stages|property 4 of the functions of the unfolding]]), a group; so translation by it permutes \(\Omega_0\), and the multiplicity is identically \(1\). For \(j\ge1\): the image of \(U(X_j)\) lies in the Bessel subgroup, and the image of the level of \(X_j\) lies in
\(K_j\) ([[proofs/grh/upper-seesaw/glued-level-congruences|glued level]]), so stability is property 1 of a stage cut, and the
invariance of the multiplicity under every element of the Bessel subgroup is property 1 of the [[proofs/grh/upper-seesaw/cover-multiplicity|cover multiplicity]]. If
\(Q=\emptyset\), the points lie in \(K_k\) and \(J_k\) contains the principal congruence subgroup
modulo \(\pi_M\), so the set injects into \(K_k\) modulo that subgroup, of order at most the number
of matrices modulo \(\pi_M\). \(\blacksquare\)

## References

1. Lean: `New.Data.exists_isStageCut`, `New.Data.cutPoints`, `New.Data.cutMultiplicity` and the lemmas listed in the front matter, in `src/New/UpperBound/Seesaw/Cut.lean`.

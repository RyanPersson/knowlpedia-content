+++
id = "proofs/grh/upper-seesaw/support-of-unfolding-stages"
title = "Support of the unfolding functions for ramified source forms"
kind = "theorem"
summary = "For a ramified source form, a point where the j-th unfolding function does not vanish has, at graded points of its Bessel orbit, a lattice sandwiched between the standard one scaled by the j-th powers of the twist idele."
aliases = ["support lemma", "twist idele"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.unfoldStage_eq_zero_of_scalingGenerator", "New.Data.map_stringMapFin_latticePlus_gradingY", "New.Data.notMem_Q_of_mem_piNPlaces", "New.Data.unfoldStage_eq_zero_of_latticeSplitsAt", "New.Data.hasLatticeBounds_of_unfoldStage_ne_zero"]
lean_files = ["src/New/UpperBound/Seesaw/UnfoldingStages.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/upper-seesaw/unfolding-stages|the functions of the unfolding]]
\(\mathcal{W}_j\) on \(G_j=U(Y_j)(\mathbb{A})\). Let \(Q\) be the chosen modulus of the tame character \(\vartheta\) (its tame part is trivial outside \(Q\) but may also be trivial at places of \(Q\); the bounds below use this \(Q\), not the set of places of actual ramification) and \(\mathfrak{q}\) the **twist idele**: the chosen generator of
the [[?lean:New.Data.twistModulus|modulus of the twist]] (the chosen places times \(Q\)) divided by
the [[?lean:New.Data.chosenIdele|chosen idele]]; it is a [[?c:Uniformizer|uniformiser]] at the places of \(Q\) and a
unit elsewhere.

**Theorem (support).** Let \(\varphi\) be a
[[?lean:New.Data.ramifiedSourceForms|ramified source form]] and let \(y_0\) lie in the chosen level.
Let \(1\le j\le m-1\), and suppose \(\mathcal{W}_j(a,x)\ne0\) for an archimedean point \(a\) and a
finite point \(x\) of \(U(Y_j)\). Then for every \(r'\) in the finite Bessel subgroup such that the
lattice of \(r'x\) is graded, \(r'x\) has the
[[proofs/grh/upper-seesaw/lattice-bounds-induction-step|lattice bounds]] \((\mathfrak{q},j)\):
\[
\bar{\mathfrak{q}}^{\,j}\Lambda^{-}\subseteq\Lambda^{-}_{r'x}\qquad\text{and}\qquad \mathfrak{q}^{\,j}\Lambda^{-}_{r'x}\subseteq\Lambda^{-}.
\]

**Complement (vanishing).** Let \(\varphi\) be ramified, \(2j+2\le m-1\), and \(w\) a place
dividing \(\pi_N\). If the lattice of the finite point \(x\) of \(U(Y_{2j+2})\)
[[proofs/grh/upper-seesaw/lattice-splitting-and-scalings|splits along \(X_{2j+2}\) at \(w\)]], then
\(\mathcal{W}_{2j+2}(\gamma\cdot(a,x))=0\) for all \(\gamma\in R_{2j+2}\) and all archimedean \(a\).

## Proof

*Preliminaries.* (i) \(\mathfrak q\) has the valuations stated: the modulus is \((\pi_M)\) times
the product of the distinct primes of \(Q\), and the chosen idele has the valuations of \(\pi_M\)
([[proofs/grh/upper-seesaw/tower-lattice-data|lattice data of the tower]]). Places above \(N\) are
not in \(Q\), so \(\mathfrak q\) is a unit at the places of \(P\cup\bar P\), \(P\) the places
dividing \(\pi_N\).

(ii) ([[proofs/grh/upper-seesaw/point-datum-periods|Periods of the point datum]].) *The point datum is fixed by \(\varrho_f(\varpi_{\mathfrak m}x)\) for integral \(x\)*, where
\(\varpi_{\mathfrak m}\) is the generator of the modulus. By
[[proofs/grh/upper-seesaw/schrodinger-operator-admissible|the Schrödinger operator lemma]] (with
\(g=0\), \(q=1\), \(d=\varpi_{\mathfrak m}\)) the point datum is a combination of translates
\(\varrho_f(t)v_0\) with \(\bar\varpi_{\mathfrak m}t\) integral. For such \(t\),
\(\psi\bigl((\varpi_{\mathfrak m}x)^{*}\!\cdot t\bigr)=1\) by self-duality of the standard lattice,
so \(\varrho_f(\varpi_{\mathfrak m}x)\) commutes with \(\varrho_f(t)\)
([[?lean:New.Space.finHeisenbergOp_comm|commutation law]]), and it fixes \(v_0\) because
\(\varpi_{\mathfrak m}x\) is integral.

(iii) \(\operatorname{sh}(\Lambda^{+})=a\,\Lambda^{-}\) between the stages \(k\) and \(k+1\) of the
tower, by [[proofs/grh/upper-seesaw/shift-of-string-lattice|the shift of the string lattices]]
applied to the lattice data of the tower (scales \((a/\bar a)^{\lfloor(s+2)/2\rfloor}\) for the
string lengths \(s=m-1-k\) and \(s-1\); same constant; \(c\) with the valuations of \(a\bar a\)).

*Complement.* Let \(z_w\) be the [[?lean:New.Data.scalingGenerator|scaling generator at \(w\)]]:
an integral adele of norm one that is \(1\) outside \(w,\bar w\). Since \(w\ne\bar w\) and the
lattice of \(x\) splits at \(w\), part 3 of
[[proofs/grh/upper-seesaw/lattice-splitting-and-scalings|the splitting lemma]] shows that
\(x^{-1}\sigma_{z_w}x\) lies in the maximal compact subgroup at \(w\) (integral, trivial off
\(w,\bar w\)). The places \(w,\bar w\) are neither chosen places nor in \(Q\), so this subgroup is
contained in the level \(J_{2j+2}\). Now take \((a,x)\) as the outer variable of index \(2j+2\)
(the function \(\mathcal{W}_{2j+2}\) does not depend on it). By
[[proofs/grh/upper-seesaw/unfolding-stage-as-coefficient-of-chain|part 1 of the coefficient
theorem]],
\[
\mathcal{W}_{2j+2}\bigl(\gamma\cdot(a,x)\bigr)=\mathcal{W}^{R}_{2j+2}(\gamma)=\text{source function of }\bigl(l,\Theta_{j+1}(\vartheta,y')\varphi\bigr)\text{ at }\gamma ,
\]
with \(y'\) equal to \(y\) except \(y'_{2j+2}=x\). By part 3 of the same theorem, the Weil operator
of \((1,z_w)\) on the second factor fixes \(E_j(\vartheta,y')\). For a ramified \(\varphi\) this
forces \(\Theta_{j+1}(\vartheta,y')\varphi=0\)
([[?lean:New.Data.doubleLiftChain_eq_zero_of_ramified|the chain of double lifts kills ramified
forms when the scaling at \(w\) fixes the last datum]]), and the source function of the zero form
is \(0\).

*Support.* Strong induction on \(k=j-1\ge0\); write \(\mathcal{Y}_k\) for the grading of \(Y_k\).

*Step 1.* By definition
\(\mathcal{W}_{k+1}(a,x)=\int_{[R_k]}\mathcal{W}^{R}_k(\gamma)\,c_{\operatorname{sh}}(F_k^{g};\gamma,(a,x))\,d\gamma\ne0\),
so there is \(\gamma\in R_k\) with \(\mathcal{W}^{R}_k(\gamma)\ne0\) and
\(c_{\operatorname{sh}}(F_k;\gamma g_k,(a,x))\ne0\) (the moved datum at \(\gamma\) is the datum at
\(\gamma g_k\)).

*Step 2.* The orbit of the finite part \(p\) of \(\gamma g_k\) is bounded for \((\mathfrak q,k)\):
there is \(r\) in the finite Bessel subgroup with graded lattice \(\Lambda_{rp}\) and the bounds
\((\mathfrak q,k)\). For \(k=0\): the finite part of \(\gamma^{-1}\) lies in the finite Bessel
subgroup and \((\gamma^{-1})_f\,p=y_0\) stabilises the standard lattice, so
[[proofs/grh/upper-seesaw/lattice-bounds-induction-step|part 3 of the sandwich proposition]]
applies (bounds with exponent \(0\)). For \(k\ge1\): \(\mathcal{W}^{R}_k(\gamma)=\mathcal{W}_k(\gamma g_k)\ne0\),
so by the induction hypothesis every translate of \(p\) with graded lattice has the bounds
\((\mathfrak q,k)\), and part 3 of the sandwich proposition gives the bounded orbit.

*Step 3 (frequency).* The real and finite factors of the datum \(F_k\) are a Fock vector and the
point datum, which by (ii) is fixed by \(\varrho_f(\varpi_{\mathfrak m}x)\), \(x\) integral. By
[[proofs/grh/upper-seesaw/shift-maps-lattices|part 2 of the frequency theorem]] with
\(b=\varpi_{\mathfrak m}\) and the graded points \(rp\) and \(r'x\):
\[
(\bar\varpi_{\mathfrak m}/\alpha)\,\operatorname{sh}\bigl(\Lambda^{+}_{rp}\bigr)\subseteq\Lambda^{-}_{r'x},
\qquad \bar\varpi_{\mathfrak m}/\alpha=\bar{\mathfrak q}/a ,
\]
since \(\mathfrak q=\varpi_{\mathfrak m}/\varpi\) and \(a=\alpha/\bar\varpi\).

*Step 4 (sandwich).* By (iii), Step 3 and the upper bound
\(\mathfrak q^{k}\Lambda^{-}_{rp}\subseteq\Lambda^{-}\) of Step 2, part 1 of the sandwich proposition
gives the lower bound \(\bar{\mathfrak q}^{\,k+1}\Lambda^{-}\subseteq\Lambda^{-}_{r'x}\) at stage
\(k+1\).

*Step 5 (dichotomy).* By (i) and part 2 of the sandwich proposition for the grading of
\(Y_{k+1}\), either \(r'x\) has the bounds \((\mathfrak q,k+1)\) — the claim — or the string length
\(m-2-k\) is odd and the lattice of \(r'x\) splits at some \(w\in P\). In the second case
\(k=2j+1\) is odd, and the complement, applied to the point \(r'x\) and
\(\gamma=(1,r')^{-1}\in R_{k+1}\), gives
\(\mathcal{W}_{k+1}(a,x)=\mathcal{W}_{k+1}\bigl((1,r')^{-1}(a,r'x)\bigr)=0\), a contradiction.
\(\blacksquare\)

## References

1. Lean: `New.Data.hasLatticeBounds_of_unfoldStage_ne_zero`, `New.Data.unfoldStage_eq_zero_of_latticeSplitsAt`, `New.Data.unfoldStage_eq_zero_of_scalingGenerator` and the lemmas listed in the front matter, in `src/New/UpperBound/Seesaw/UnfoldingStages.lean`.

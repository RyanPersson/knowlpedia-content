+++
id = "proofs/grh/upper-seesaw/double-unfolding-integral"
title = "Two unfolding steps: Bessel integrals of constant terms as a double theta integral"
kind = "theorem"
summary = "The integral over two Bessel subgroups of an equivariant function times two constant terms at the shifts equals an integral over U(X) of a theta integral over U(X') of the joined datum, translated by the stacked string map and cut down along the double lift splitting."
aliases = ["double unfolding step"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.DoubleLiftData.exists_integral_constTermAtStringMap_mul_eq", "New.Seesaw.DoubleLiftData.constTerm_mul_constTerm_eq_inv_mul_zeroTerm", "New.Seesaw.DoubleLiftData.exists_add_eq_homAtPoint_stackedStringMap", "New.Seesaw.formAdjoint_stackedStringMap_mul_stackedStringMap", "New.Seesaw.DoubleLiftData.zeroTerm_stackedStringMap_planes", "New.Seesaw.constTermAtStringMap_unipotent_mul_right", "New.Seesaw.constTermAtStringMap_unipotent_mul_left", "New.Seesaw.mul_constTermAtStringMap_unipotent_mul", "New.Seesaw.integral_theta_tripleWeil_eq_lift_comp", "New.Seesaw.arrowProduct_integrated_polyVector", "New.Seesaw.integrable_algFormCoeff_mul_theta_tripleWeil", "New.Seesaw.formAdjoint_fromRows"]
lean_files = ["src/New/UpperBound/Seesaw/UnfoldingStages.lean"]
proof_status = "outline"
+++

Let \(\mathcal{D}\) be [[proofs/grh/upper-seesaw/double-lift-data|double lift data]] for gradings
\(Y,Y',Y''\) of \(V,V',V''\) (definite parts \(X,X',X_0\); target \(X''\); homomorphism
\(\epsilon\)), with shifts \(T\colon V\to V'\), \(T'\colon V'\to V''\). Let \(R_Y,R_{Y'}\) be the
[[?lean:New.Grading.besselGroup|Bessel subgroups]], with quotient measures modulo rational points.
For characters \(a,b\) of the norm-one adeles let \(c_T(f;g,r)\) be the
[[?lean:New.Grading.constTermAtStringMap|constant term at the shift]] of the Weil translate of
\(f\) by \((g,r)\), normalised by the [[?lean:New.rankTwist|rank twist]] of \(a\) (resp. \(b\) for
\(T'\)).

**Theorem.** There is a constant \(z\in\mathbb{C}\), depending only on \(\mathcal{D}\) (it is \(\kappa\kappa'/z_0\) in the notation of the proof), such that
for all characters \(a,b\), all \(f\in\mathcal{S}(\operatorname{Hom}(V,V'))\),
\(f'\in\mathcal{S}(\operatorname{Hom}(V',V''))\), all adelic points \(k\) of \(U(X_0)\), and every
continuous function \(W\) on \(R_Y\) that is
[[?lean:New.Grading.IsEquivariant|equivariant]] (invariant under rational points and transforming
by the unipotent character under the [[?c:Unipotent radical|unipotent radical]]):
\[
\int_{R_{Y'}}\!\int_{R_Y}W(g)\,c_T(f;g,r)\,c_{T'}(f';r,k)\,dg\,dr
=\int_{[U(X)]}W(g)\Bigl(z\int_{[U(X')]}\theta\bigl(W_{a,b}(g,r,\epsilon(k))\,Z_{\mathcal{D}}\,\varrho(T^{*},T')(f\ast f')\bigr)\,dr\Bigr)dg .
\]
Here \(f\ast f'\) is the joined datum on \(\operatorname{Hom}(V',V^{-}\oplus V'')\),
\(\varrho(T^{*},T')\) the Heisenberg translation by the stacked string map,
\(Z_{\mathcal{D}}\) the zero term along the splitting of \(\mathcal{D}\), \(W_{a,b}\) the triple
Weil operator of the definite spaces, \(\theta\) the [[?c:Theta functional|theta functional]], and \([U(\cdot)]\) the
adelic points modulo rational points.

**Complement (double theta integrals are composite lifts).** Let families \(k_o,k'_o\) compute the
[[?lean:New.Space.IsThetaLift|theta lifts]] of algebraic forms \(X\to X'\) and \(X'\to X''\) for the
rank twists of the characters \(a_o,b_o\) (the lift between spaces uses \(a_o\upsilon^{\lfloor r/2\rfloor}\), resp. \(b_o\upsilon^{\lfloor r/2\rfloor}\), at a space of rank \(r\), \(\upsilon\) the fixed character of the Weil data), and let \(L_o(\Phi\otimes\Phi')=k'_o(\Phi')\circ k_o(\Phi)\). For every Fock
vector \(u\) of \(\operatorname{Hom}(X',X^-\oplus X'')\) and every linear form \(t\) on the values of
forms on \(U(X)\) there is a linear form \(t''\) such that, for all \(o\), finite data \(y\), forms
\(\varphi\) and \(g\in U(X'')(\mathbb{A})\),
\[
\int_{[U(X)]}t(\varphi(x))\int_{[U(X')]}\theta\bigl(W_{a_o,b_o}(x,r,g)\,(u\otimes y^{\ast})\bigr)\,dr\,dx
=t''\bigl(L_o(y)\varphi\,(g)\bigr),
\]
where \(y^{\ast}\) is the join of \(y\), and for an adelic point \(x=(x_\infty,x_f)\) the symbol \(t(\varphi(x))\) denotes the adelic coefficient \(t\bigl(\rho(x_\infty)^{-1}\varphi(x_f)\bigr)\) of the algebraic form \(\varphi\) (a vector-valued function on finite points; \(\rho\) the conjugate Weyl representation at infinity); likewise \(t''(\cdot(g))\) on the right.

## Proof

(Outline; the structure below was checked against the Lean proof line by line, the three library inputs named in it are asserted.) *Product of constant terms.* The theta functional of a join factors:
\(\theta(f\ast f')=z_0\,\theta(f)\theta(f')\) with \(z_0\ne0\) (asserted; a property of the join in
`Lib/Weil/DualPair/TwoEdges`). A map \(V'\to V^-\oplus V''\) of positive degree is a pair
\((a^{*},a')\) with \(a,a'\) of positive degree, so the product of the constant terms of \(f\) at
\(w\) and \(f'\) at \(w'\) is \(z_0^{-1}\) times the value at \(0\) of the zero term, along the
grade zero splitting, of the join of the two translates.

*Absorbing unipotents.* For \(n\) in the unipotent radical of \(Y'\), \(c_T(f;g,nr)\) is the
constant term at \(n^{-1}T\) and \(c_{T'}(f';nr,k)\) the constant term at \(T'n\); for \(n\) in the
unipotent radical of \(Y\), the constant term at \(Tn\), whose character cancels that of \(W\)
(here \(s\) odd is used). The stacked string map is [[?c:Isotropic subspace|isotropic]],
\((T^{*},T')^{*}(T^{*},T')=-TT^{*}+T'^{*}T'=0\), so translations by it compose without phase; and
\((T^{*},T')(n-1)\) is the sum of a map of positive degree and the map sending \(X'\) into the
isotropic half of the planes with matrix \(c_{Y'}\) times the block of \(n-1\) with rows the grade
one vectors of the double lift data and columns \(X'\).

*Integration.* A general lemma on Bessel integrals (asserted;
`Grading.integral_besselMeasure_eq_of_mean` in `Lib/Weil/Periods/Unfolding`, which produces constants \(\kappa\) for \(Y\) and \(\kappa'\) for \(Y'\)) turns the integral over a
Bessel group of a function of the form \(\phi(nx)=F_x(\text{row of }n-1)\) into a constant times
the integral over \([U(X)]\) of the mean of \(F_x\). Applied to \(Y\), the characters cancel;
applied to \(Y'\), the mean over the rows is the mean over the isotropic half of the planes, which
turns the zero term along the grade zero splitting into \(Z_{\mathcal{D}}\). Finally
[[proofs/grh/upper-seesaw/double-lift-evaluation-equivariant|equivariance of the zero term]]
moves the group action out as the triple Weil operator at \((g,r,\epsilon(k))\).

*Complement.* The families given by a linear form \(t''\) form a finite-dimensional, hence closed,
space, and the left side is continuous in \(u\); so it suffices to treat Fock polynomials, which are
sums of products \(PQ\) of a polynomial on \(\operatorname{Hom}(X,X')\) and one on
\(\operatorname{Hom}(X',X'')\). For a product \(PQ\) and a pure finite tensor \(y=\Phi\otimes\Phi'\), the datum \(PQ\otimes y^{\ast}\) is the join of the two pure tensors \(P\otimes\Phi\) and \(Q\otimes\Phi'\); the theta functional of a join is \(z_0\) times the product of the theta functionals, the triple Weil operator is the join of the two pair actions, and the double integral becomes the iterated [[?c:Theta lift|theta lift]] \(k'_o(\Phi')\circ k_o(\Phi)\) with \(Q\) replaced by \(z_0Q\). Both sides are additive in \(y\), so the identity extends from pure tensors to all finite tensors. \(\blacksquare\)

## References

1. Lean: `New.Seesaw.DoubleLiftData.exists_integral_constTermAtStringMap_mul_eq`, `New.Seesaw.integral_theta_tripleWeil_eq_lift_comp` and the lemmas listed in the front matter, in `src/New/UpperBound/Seesaw/UnfoldingStages.lean`.

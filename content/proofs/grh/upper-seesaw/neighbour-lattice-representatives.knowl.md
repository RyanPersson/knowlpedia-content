+++
id = "proofs/grh/upper-seesaw/neighbour-lattice-representatives"
title = "Representatives of the neighbour lattice modulo its integral points"
kind = "theorem"
summary = "Sums of a neighbour translation and a representative of the away quotient represent the neighbour lattice modulo the standard lattice uniquely; the away quotient has order dividing the number of matrices modulo beta."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.existsUnique_sub_neighbourCosetRep_mem", "New.Seesaw.existsUnique_add_neighbourTranslation_mem", "New.Seesaw.exists_add_neighbourTranslation_mem_iff", "New.Seesaw.exists_class_star_idem_mul_mem_iff", "New.Seesaw.neighbourTranslation_mem_neighbourLattice", "New.Seesaw.neighbourCosetRep_mem_neighbourLattice", "New.Seesaw.mem_neighbourLattice_iff_of_mem_vanishingAbove", "New.Seesaw.awayLattice_le_weightedTranslations", "New.Seesaw.card_awayLatticeQuotient_dvd"]
lean_files = ["src/New/UpperBound/Seesaw/NeighbourLattice.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/upper-seesaw/neighbour-lattice|the neighbour lattice]] \(\mathcal{N}\):
\((P,N,\pi)\) split squarefree, \(\kappa\) a scaling at \(M\) for \((N,\beta,\delta)\),
\(L=\widehat{\mathcal{O}}_E^{\,I\times X'}\), \(j=1_P\), \(\gamma=1+A\rho\rho^{*}\),
\(u=(\gamma\operatorname{diag}\kappa)\otimes1\). Assume in addition that \(N\) is prime and that the
[[algebra-fields-galois/place-of-global-field|places]] of \(E\) above \(N\) are exactly those of
\(P\cup\bar P\), all split of degree one and unramified
([[?lean:New.IsSplitLevel|split level]]).

**Theorem.**

1. An element \(x\) vanishing at \(P\cup\bar P\) lies in \(\mathcal{N}\) iff
   \(\bar\kappa_{i}x_{i,a}\) is integral for all \((i,a)\).
2. \(\mathcal{N}^{\mathrm{aw}}\subseteq T_n\bigl((\beta_i)_{(i,a)}\bigr)\) for every \(n\), where
   \(\beta_i=\beta\) on the first block and \(\bar\beta\) on the second
   ([[proofs/grh/upper-seesaw/translation-groups|weighted translations]]); and the order of the
   away quotient divides \(\lvert\widehat{\mathcal{O}}_E/(\beta)\rvert^{\lvert I\times X'\rvert}\).
3. Every neighbour translation \(n(y)\) lies in \(\mathcal{N}\).
4. For every \(x\in\mathcal{N}\) there is exactly one residue family \(y\) such that \(x+n(y)\) is
   integral at all places of \(P\cup\bar P\).
5. For every \(z\in\mathcal{N}\) there is exactly one pair \((y,q)\), with
   \(y\colon X'\to(\mathbb{Z}/N)^{P}\) and \(q\) a class of the away quotient, such that
   \(z-(n(y)+t_q)\in L\).

## Proof

(1) Let \(x\) vanish at \(P\cup\bar P\). Since \(A\) is supported on \(P\cup\bar P\), \(Ax_{i,a}=0\)
and \(\gamma\) acts trivially on the columns of \(x\); so \(u\cdot x=(\kappa_ix_{i,a})\). The
matrix \(\bar\kappa x\) also vanishes above \(N\), and \(u\cdot(\bar\kappa x)=\kappa\bar\kappa x=x\)
because \(\kappa_i\bar\kappa_i=1\). As \(u\) is injective, \(x\in u\cdot L\) iff
\(\bar\kappa x\in L\).

(2) For \(x\in\mathcal{N}^{\mathrm{aw}}\), \(\beta_ix_{i,a}=(\beta_i\kappa_i)(\bar\kappa_ix_{i,a})\)
is a product of two integral adeles (the first by the definition of a scaling at \(M\)), so it is
integral at every place. For the order, consider the additive map
\[
r\colon\mathcal{N}^{\mathrm{aw}}\to(\widehat{\mathcal{O}}_E/(\beta))^{I\times X'},\qquad x\mapsto\bigl(\overline{\bar\kappa_ix_{i,a}}\bmod\beta\bigr)_{(i,a)} .
\]
If \(r(x)=0\) then \(\overline{\bar\kappa_ix_{i,a}}=\beta z\) with \(z\) integral, hence
\(x_{i,a}=\bar\beta\kappa_i\bar z\), which is integral since \(\bar\beta\kappa_i\) is. So
\(\ker r\subseteq\mathcal{N}^{\mathrm{aw}}\cap L\), and the order of
\(\mathcal{N}^{\mathrm{aw}}/(\mathcal{N}^{\mathrm{aw}}\cap L)\) divides the index of \(\ker r\),
which is the order of the image of \(r\), a subgroup of the finite group of matrices modulo
\(\beta\); conclude by [[?c:Lagrange's theorem|Lagrange's theorem]]. (The away quotient is finite
because \(\mathcal{N}\cap L\) has finite index in \(\mathcal{N}=uL\); see
[[proofs/grh/upper-seesaw/zero-term-lattice|the zero term lattice]], part 2.)

*A local statement.* Let \(t\in\mathbb{A}_{E,f}\). There is a residue family
\(y_0\in(\mathbb{Z}/N)^{P}\) such that for all \(y\):
\[
\bar j\bigl(\bar\pi^{-1}t+\eta\,\overline{y/N}\bigr)\in\widehat{\mathcal{O}}\iff\bigl(\bar jt\in\widehat{\mathcal{O}}\ \text{and}\ y=y_0\bigr).\tag{*}
\]
Indeed, the map \(w\mapsto\eta\bar w\) preserves integrality in both directions, because
\(\eta\,\overline{\eta\bar w}=\eta\bar\eta\,w=-w\) and \(\eta\) is integral. It sends the left
expression to \(j(z-y/N)\) with \(z=\eta\pi^{-1}\bar t\), using \(\eta\bar\eta=-1\). For a split
level there is \(y_0\) with: \(j(z-y/N)\) integral iff \(jNz\) integral and \(y=y_0\)
([[?lean:New.IsSplitLevel.exists_sub_residueOverN_mem_iff|residues modulo a split prime]]: at each
\(w\in P\) the residue field is \(\mathbb{Z}/N\) and \(N\) is a uniformiser). Finally
\(jNz=\bar\pi\cdot\eta\,\overline{\bar jt}\) (as \(N=\pi\bar\pi\)), and conversely
\(\eta\,\overline{\bar jt}=\overline{(1-j)\pi^{-1}}\cdot jNz\) where \((1-j)\pi^{-1}\) is integral
(\(\pi\) is a unit off \(P\)); so \(jNz\) is integral iff \(\bar jt\) is.

*Columns at \(\bar P\).* At the places of \(\bar P\) one has \(j=0\), so
\(\langle\rho,x\rangle=x_e\) and \(A=\bar\pi^{-1}-1\); moreover \(n(y)=\rho\cdot\eta\,\overline{y/N}\)
there, since \(\rho_{e''}\cdot\eta=\bar\eta\eta=-1\). Hence, column by column,
\[
\bar j\bigl(\gamma x+n(y)\bigr)_{i,a}=\bar jx_{i,a}+\rho_i\Bigl(\bar j\bigl(\bar\pi^{-1}x_{e,a}+\eta\,\overline{y_a/N}\bigr)-\bar jx_{e,a}\Bigr).
\]
Taking \(i=e\) (\(\rho_e=1\)) and applying \((*)\) to \(t=x_{e,a}\) for each column \(a\): there is
\(y_0\) such that \(\gamma x+n(y)\) is integral at \(\bar P\) iff \(x\) is integral at \(\bar P\)
and \(y=y_0\). (If the left side holds, the row \(e\) gives \(y=y_0\) and \(\bar jx_{e,a}\)
integral; then all entries differ from those of \(\bar jx\) by integral adeles, \(\rho\) being
integral. The converse is the same computation.)

*At \(P\).* If \(jz\) is integral then so is \(j(\gamma z+n(y))\): \(jn(y)=0\), and
\(j(\gamma z)_{i}=jz_i+(\pi-1)\,c\,\rho_i\) with \(c=jz_e+\eta jz_{e''}\) integral.

(3) Choose \(x\) with \(\gamma x=-n(y)\) (\(\gamma\) is invertible). Then \(\gamma x+n(y)=0\) is
integral at \(\bar P\), so \(x\) is integral at \(\bar P\). Put \(x_0=-\bar jx\in L\). Since
\(\kappa=1\) at the places above \(N\), \(\kappa x_0=x_0\), and
\(u\cdot x_0=\gamma x_0=-\bar j\gamma x=\bar jn(y)=n(y)\), as \(n(y)\) is supported at \(\bar P\).

(4) Let \(x=u\cdot x_0\) with \(x_0\in L\), and \(z=\kappa x_0\), so \(x=\gamma z\). Above \(N\)
the factors \(\kappa\) are \(1\), so \(z\) is integral at \(P\) and at \(\bar P\). By the statement
at \(P\), \(\gamma z+n(y)\) is integral at \(P\) for every \(y\); by the statement at \(\bar P\) it
is integral at \(\bar P\) for exactly one \(y\).

(5) Let \(e=1_{P\cup\bar P}=j+\bar j\). The element \(e z\) lies in \(\mathcal{N}\) (\(u\) is
linear over the adeles), so \(z'=z-ez\in\mathcal{N}^{\mathrm{aw}}\). For a pair \((y,q)\), using
that \(n(y)\) is supported above \(N\) and \(t_q\) vanishes there,
\[
z-(n(y)+t_q)=-e\bigl(-z+n(y)\bigr)+\bigl(z'-t_q\bigr),
\]
where the first summand is supported above \(N\) and the second vanishes there. So the left side
is in \(L\) iff \(e(-z+n(y))\in L\) and \(z'-t_q\in L\). The second condition says that \(q\) is
the class of \(z'\); the first, by (4) applied to \(-z\in\mathcal{N}\), holds for exactly one
\(y\). \(\blacksquare\)

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Seesaw/NeighbourLattice.lean`.

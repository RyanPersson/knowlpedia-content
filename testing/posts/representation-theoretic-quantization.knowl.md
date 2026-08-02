+++
id = "posts/representation-theoretic-quantization"
title = "Symplectic symmetries and representation-theoretic quantization"
kind = "document"
summary = "A knowlified discussion connecting symplectic group actions, quantization maps, moment maps, and derived unitary representations."
aliases = ["Representation-theoretic notation for quantization", "Symplectic symmetry quantization conversation"]
domains = ["mathematical-physics", "lie-groups", "differential-geometry"]
+++

The proposed description of quantization combines three different structures:

1. a finite-dimensional [[fiber-bundles/lie-group|Lie group]] acting on a classical phase space by [[differential-geometry/symplectomorphism|symplectomorphisms]];
2. a [[lie-groups/strongly-continuous-unitary-representation|unitary]] or [[lie-groups/projective-unitary-representation|projective unitary representation]] of that group on a [[linear-algebra/hilbert-space|Hilbert space]];
3. the [[lie-groups/derived-representation-on-smooth-vectors|derived Lie-algebra representation]], whose self-adjoint generators represent classical observables.

Standard [[mathematical-physics/geometric-quantization|geometric quantization]] distinguishes the representation of symplectic symmetries from the [[mathematical-physics/quantization-map|quantization map]] that sends classical observables to operators.

## The classical symmetry group

Let \((M,\omega)\) be a finite-dimensional [[differential-geometry/symplectic-manifold|symplectic manifold]]. Its [[differential-geometry/symplectomorphism-group|symplectomorphism group]] is
\[
\operatorname{Symp}(M,\omega)
=\{\phi\in\operatorname{Diff}(M):\phi^*\omega=\omega\}.
\]
A finite-dimensional subgroup is more precisely specified by a finite-dimensional Lie group \(G\) and a smooth [[algebra-groups/group-homomorphism|group homomorphism]]
\[
\alpha:G\longrightarrow\operatorname{Symp}(M,\omega),
\qquad
\alpha(gh)=\alpha(g)\circ\alpha(h).
\]
If \(\alpha\) is injective, one may identify \(G\) with its image. Equivalently, \(G\) acts smoothly on \(M\) by \((g,m)\mapsto\alpha(g)(m)\). The adjective “finite-dimensional” refers to \(G\), not to \(M\) or to the quantum Hilbert space.

## The group-level representation

The quantum symmetry representation has the form
\[
U_\hbar:G\longrightarrow\mathcal U(\mathscr H_\hbar),
\]
where \(\mathscr H_\hbar\) is a complex Hilbert space, \(U_\hbar\) is usually strongly continuous, \(\hbar>0\), and
\[
U_\hbar(gh)=U_\hbar(g)U_\hbar(h).
\]

In quantum mechanics the natural object is often only a projective unitary representation
\[
\overline U_\hbar:G\longrightarrow\operatorname{PU}(\mathscr H_\hbar),
\qquad
\operatorname{PU}(\mathscr H_\hbar)
=\mathcal U(\mathscr H_\hbar)/\{zI: z\in U(1)\}.
\]
After choosing representatives,
\[
U_\hbar(g)U_\hbar(h)=\sigma_\hbar(g,h)U_\hbar(gh),
\]
where \(\sigma_\hbar:G\times G\to U(1)\) is a group \(2\)-cocycle. Equivalently, one can pass to a [[algebra-groups/central-extension|central extension]]
\[
1\longrightarrow U(1)\longrightarrow\widetilde G_\hbar
\longrightarrow G\longrightarrow1
\]
and obtain a genuine unitary representation of \(\widetilde G_\hbar\).

This phenomenon occurs naturally in [[mathematical-physics/prequantization|prequantization]]: a lifted Hamiltonian group action induces a genuine representation of the lifted group and can induce only a projective representation of the original group.

## Why an arbitrary representation is not sufficient

An arbitrary unitary representation of \(G\) does not by itself encode \((M,\omega)\). One also needs a relation between classical observables and quantum operators.

Let \(\mathcal A\subseteq C^\infty(M,\mathbb R)\) be a \(G\)-invariant Poisson subalgebra containing the constants, and let \(\mathscr D_\hbar\subseteq\mathscr H_\hbar\) be a dense \(U_\hbar(G)\)-invariant subspace. A quantization map is a real-linear map
\[
Q_\hbar:\mathcal A\longrightarrow\operatorname{End}(\mathscr D_\hbar)
\]
whose values are [[functional-analysis/symmetric-operator|symmetric operators]], with conditions such as
\[
Q_\hbar(1)=I|_{\mathscr D_\hbar},
\qquad
[Q_\hbar(f),Q_\hbar(g)]=i\hbar Q_\hbar(\{f,g\}).
\]
Covariance relates the classical and quantum actions:
\[
U_\hbar(g)Q_\hbar(f)U_\hbar(g)^{-1}
=Q_\hbar\!\left(f\circ\alpha(g^{-1})\right).
\]
Thus pullback of classical observables corresponds to conjugation of quantum observables.

The [[mathematical-physics/groenewold-van-hove-theorem|Groenewold–Van Hove theorem]] explains why the exact commutator rule cannot generally be imposed on all of \(C^\infty(M,\mathbb R)\). One instead restricts the Poisson subalgebra, asks for a semiclassical asymptotic relation, or uses deformation quantization. A representation-theoretic quantization therefore involves at least the tuple
\[
(\mathscr H_\hbar,\mathscr D_\hbar,U_\hbar,Q_\hbar),
\]
not merely \(U_\hbar\).

## Hamiltonian group actions and moment maps

Fix the conventions
\[
\iota_{X_f}\omega=-df,
\qquad
\{f,g\}=\omega(X_f,X_g)=X_f(g),
\]
where \(X_f\) is the [[differential-geometry/hamiltonian-vector-field|Hamiltonian vector field]] of \(f\).

For \(X\in\mathfrak g=T_eG\), define the [[differential-geometry/infinitesimal-generator-lie-action|fundamental vector field]] by
\[
X_M(m)=\left.\frac{d}{dt}\right|_{t=0}
\alpha(\exp_G(-tX))(m).
\]
With these signs, both \(f\mapsto X_f\) and \(X\mapsto X_M\) are Lie-algebra homomorphisms.

An equivariant [[differential-geometry/hamiltonian-lie-group-action|Hamiltonian \(G\)-action]] has a [[differential-geometry/comoment-map|comoment map]]
\[
J:\mathfrak g\longrightarrow C^\infty(M,\mathbb R),
\qquad X\longmapsto J_X,
\]
satisfying
\[
X_{J_X}=X_M,
\qquad
\{J_X,J_Y\}=J_{[X,Y]}.
\]
The corresponding [[fiber-bundles/moment-map|moment map]] \(\mu:M\to\mathfrak g^*\) is defined by
\[
\langle\mu(m),X\rangle=J_X(m).
\]

## The derived Lie-algebra representation

For a strongly continuous unitary representation, the [[lie-groups/smooth-vector-unitary-representation|space of smooth vectors]] is
\[
\mathscr H_\hbar^\infty
=\{\psi\in\mathscr H_\hbar:g\mapsto U_\hbar(g)\psi
\text{ is smooth}\}.
\]
The derived representation is
\[
dU_\hbar:\mathfrak g\longrightarrow
\operatorname{End}(\mathscr H_\hbar^\infty),
\qquad
dU_\hbar(X)\psi
=\left.\frac{d}{dt}\right|_{t=0}U_\hbar(\exp_G(tX))\psi,
\]
and satisfies
\[
dU_\hbar([X,Y])=[dU_\hbar(X),dU_\hbar(Y)].
\]

The infinitesimal operators are generally unbounded and skew-symmetric on the smooth domain; by [[lie-groups/stone-theorem-one-parameter-unitary-groups|Stone's theorem]], their closures are skew-adjoint generators. The corresponding self-adjoint observables, in the present convention, are
\[
\widehat J_\hbar(X)=i\hbar\,dU_\hbar(X).
\]
They obey
\[
[\widehat J_\hbar(X),\widehat J_\hbar(Y)]
=i\hbar\widehat J_\hbar([X,Y]),
\qquad
Q_\hbar(J_X)=i\hbar\,dU_\hbar(X).
\]

Equivalently, with the rescaled commutator
\[
[A,B]_\hbar=\frac{1}{i\hbar}(AB-BA),
\]
the map \(X\mapsto i\hbar dU_\hbar(X)\) preserves Lie brackets. The natural codomain is \(\operatorname{End}(\mathscr H_\hbar^\infty)\), not generally the bounded-operator algebra \(\mathcal B(\mathscr H_\hbar)\). Bounded infinitesimal generators arise under the stronger assumption of norm continuity.

## The case of one Hamiltonian

Let \(H_{\mathrm{cl}}\in C^\infty(M,\mathbb R)\) be a [[differential-geometry/hamiltonian-function|classical Hamiltonian]] whose Hamiltonian vector field is complete. Its [[differential-geometry/hamiltonian-flow|global flow]] satisfies
\[
\Phi_{H_{\mathrm{cl}}}^{t+s}
=\Phi_{H_{\mathrm{cl}}}^{t}\circ\Phi_{H_{\mathrm{cl}}}^{s},
\]
and defines a one-parameter group in the Hamiltonian diffeomorphism group. Its image is isomorphic to
\[
\mathbb R/K_{H_{\mathrm{cl}}},
\qquad
K_{H_{\mathrm{cl}}}
=\{t\in\mathbb R:\Phi_{H_{\mathrm{cl}}}^t=\operatorname{id}_M\}.
\]

A quantization assigns the self-adjoint [[stat-mech-quantum/quantum-hamiltonian|quantum Hamiltonian]]
\[
\widehat H=Q_\hbar(H_{\mathrm{cl}}).
\]
Quantum time evolution is the strongly continuous one-parameter unitary group
\[
U_{H_{\mathrm{cl}}}(t)
=\exp\!\left(-\frac{it}{\hbar}\widehat H\right).
\]
Its derived representation satisfies
\[
dU_{H_{\mathrm{cl}}}(a)
=-\frac{ia}{\hbar}\widehat H,
\qquad
\widehat H=i\hbar\,dU_{H_{\mathrm{cl}}}(1)
\]
on the appropriate domain. The usual terminology is “quantization of the Hamiltonian” or “unitary time evolution generated by the Hamiltonian operator,” rather than “quantization by energy.”

## Example: the symplectic and metaplectic groups

Let \(V=\mathbb R^{2n}\) with its standard [[shale-paper/symplectic-form|symplectic form]] \(\omega_0\). The [[lie-groups/symplectic-group|linear symplectic group]] acts by symplectomorphisms:
\[
\operatorname{Sp}(2n,\mathbb R)
\longrightarrow\operatorname{Symp}(V,\omega_0),
\qquad A\longmapsto(v\mapsto Av).
\]
For \(A\in\mathfrak{sp}(2n,\mathbb R)\), the associated quadratic Hamiltonian is
\[
q_A(v)=\frac12\omega_0(Av,v).
\]

On \(L^2(\mathbb R^n)\), this action is only projective for the symplectic group. It becomes the genuine [[lie-groups/metaplectic-representation|metaplectic representation]] after passing to the [[lie-groups/metaplectic-group|metaplectic double cover]]
\[
1\longrightarrow\{\pm1\}
\longrightarrow\operatorname{Mp}(2n,\mathbb R)
\longrightarrow\operatorname{Sp}(2n,\mathbb R)
\longrightarrow1.
\]
Its derived representation preserves the [[functional-analysis/schwartz-space|Schwartz space]]:
\[
dU_{\operatorname{Mp}}:
\mathfrak{sp}(2n,\mathbb R)
\longrightarrow\operatorname{End}(\mathcal S(\mathbb R^n)).
\]
The self-adjoint operators \(i\hbar dU_{\operatorname{Mp}}(A)\) are quadratic differential operators quantizing the \(q_A\). This is a direct example of a finite-dimensional symplectic symmetry group whose quantization is a Hilbert-space representation of a central covering group.

## The complete dictionary

The representation-theoretic relationships can be summarized as
\[
\begin{aligned}
G&\xrightarrow{\alpha}\operatorname{Symp}(M,\omega),\\
\mathfrak g&\xrightarrow{J}
\bigl(C^\infty(M,\mathbb R),\{\mathord\cdot,\mathord\cdot\}\bigr),\\
G&\xrightarrow{U_\hbar}\mathcal U(\mathscr H_\hbar)
\quad\text{or}\quad
G\xrightarrow{\overline U_\hbar}\operatorname{PU}(\mathscr H_\hbar),\\
\mathfrak g&\xrightarrow{dU_\hbar}
\operatorname{End}(\mathscr H_\hbar^\infty),\\
Q_\hbar(J_X)&=i\hbar\,dU_\hbar(X).
\end{aligned}
\]
The last equality is the formal relation between classical Hamiltonian generators and infinitesimal generators of the quantum representation.

## References

1. N. M. J. Woodhouse, *Geometric Quantization*, 2nd ed., Oxford University Press, 1992. [Publisher record](https://global.oup.com/academic/product/geometric-quantization-9780198502708). Relevant: symplectic actions, prequantization, and polarizations.
2. V. S. Varadarajan, *Geometry of Quantum Theory*, 2nd ed., Springer, 1985. [DOI record](https://doi.org/10.1007/978-0-387-49386-2). Relevant: projective unitary representations and multipliers.
3. G. B. Folland, *Harmonic Analysis in Phase Space*, Princeton University Press, 1989. [Publisher record](https://press.princeton.edu/books/paperback/9780691085289/harmonic-analysis-in-phase-space). Relevant: the symplectic group and metaplectic representation.
4. M. J. Gotay, “On the Groenewold–Van Hove Problem for \(\mathbb R^{2n}\),” *Journal of Mathematical Physics* 40 (1999), 2107–2116. [arXiv record](https://arxiv.org/abs/math-ph/9809015). Relevant: the obstruction to exact quantization of all polynomial observables.

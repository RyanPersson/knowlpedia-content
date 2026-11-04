+++
id = "mathematical-physics/gamma-matrices"
title = "Gamma matrices"
kind = "definition"
summary = "Matrices representing Clifford multiplication in a chosen basis of a spinor module."
aliases = ["Dirac gamma matrices", "Clifford matrices"]
domains = ["mathematical-physics", "differential-geometry"]
section_mode = "progressive"
prerequisites = ["linear-algebra/quadratic-form", "differential-geometry/spinor-module", "differential-geometry/clifford-module", "linear-algebra/matrix"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((V,g)\) be a finite-dimensional real or complex [[linear-algebra/quadratic-form|quadratic space]] with
basis \(e_a\), and let
\(c:\operatorname{Cl}(V,g)\to\operatorname{End}(\Delta)\) be a
[[differential-geometry/spinor-module|spinor module]] written in a basis of
\(\Delta\). The **gamma matrices** are
\[
\gamma_a=c(e_a).
\]
Using the geometric Clifford convention \(v^2=-g(v,v)1\), they satisfy
\[
\gamma_a\gamma_b+\gamma_b\gamma_a=-2g_{ab}I.
\]
Thus gamma matrices are the basis-dependent matrices of
[[differential-geometry/clifford-module|Clifford multiplication]], not
additional invariant geometric objects.

## Raised indices

Writing \(g^{ab}\) for the inverse matrix, set
\(\gamma^a=g^{ab}\gamma_b\). Contracting gamma matrices with the components of
a vector or covector is the
[[mathematical-physics/clifford-slash-notation|Clifford slash notation]].

## Minkowski-signature convention

For the Lorentzian knowls in this collection, take
\[
\eta=\operatorname{diag}(-1,+1,+1,+1).
\]
Under the geometric convention used here,
\[
\gamma_0^2=+I,
\qquad
\gamma_j^2=-I\quad(j=1,2,3).
\]
Many physics texts instead use the opposite metric signature
\(\eta_{\mathrm{phys}}=\operatorname{diag}(+1,-1,-1,-1)\) together with
\[
\{\gamma^\mu,\gamma^\nu\}=+2\eta_{\mathrm{phys}}^{\mu\nu}I.
\]
With \(\eta_{\mathrm{phys}}=-\eta\), this has the same numerical right-hand
side as the convention in the core. If one changes only the Clifford sign
while holding the metric fixed, multiplying all complex gamma matrices by
\(i\) passes between the two relations. Metric signature and Clifford sign
must therefore be recorded separately.

## Worked example: the Dirac representation

Work on \(\mathbb R^{1,3}\) with coordinates \(x^0=t,x^1,x^2,x^3\),
metric \(\eta=\operatorname{diag}(-1,1,1,1)\), and complex spinor module
\(\Delta=\mathbb C^4\). Write \(I_n\) for the \(n\times n\) identity matrix
and \(i^2=-1\). The **Pauli matrices** used in this construction are
\[
\sigma^1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\sigma^2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
\sigma^3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
Define the raised-index matrices by \(2\times2\) blocks:
\[
\gamma^0=\begin{pmatrix}I_2&0\\0&-I_2\end{pmatrix},\qquad
\gamma^j=\begin{pmatrix}0&\sigma^j\\-\sigma^j&0\end{pmatrix}
\quad(j=1,2,3).
\]
Thus all four matrices are explicitly
\[
\gamma^0=\begin{pmatrix}
1&0&0&0\\0&1&0&0\\0&0&-1&0\\0&0&0&-1
\end{pmatrix},\qquad
\gamma^1=\begin{pmatrix}
0&0&0&1\\0&0&1&0\\0&-1&0&0\\-1&0&0&0
\end{pmatrix},
\]
\[
\gamma^2=\begin{pmatrix}
0&0&0&-i\\0&0&i&0\\0&i&0&0\\-i&0&0&0
\end{pmatrix},\qquad
\gamma^3=\begin{pmatrix}
0&0&1&0\\0&0&0&-1\\-1&0&0&0\\0&1&0&0
\end{pmatrix}.
\]

To check the relations directly, matrix multiplication gives
\((\sigma^j)^2=I_2\) and
\[
\sigma^1\sigma^2=i\sigma^3=-\sigma^2\sigma^1,\qquad
\sigma^2\sigma^3=i\sigma^1=-\sigma^3\sigma^2,\qquad
\sigma^3\sigma^1=i\sigma^2=-\sigma^1\sigma^3.
\]
Consequently \(\sigma^j\sigma^k+\sigma^k\sigma^j=2\delta_{jk}I_2\),
where \(\delta_{jk}\) is \(1\) when \(j=k\) and \(0\) otherwise.
Block multiplication now gives
\[
(\gamma^0)^2=I_4,\qquad
\gamma^0\gamma^j=\begin{pmatrix}0&\sigma^j\\\sigma^j&0\end{pmatrix}
=-\gamma^j\gamma^0,
\]
\[
\gamma^j\gamma^k=
-\begin{pmatrix}\sigma^j\sigma^k&0\\0&\sigma^j\sigma^k\end{pmatrix}.
\]
These identities prove all the Clifford anticommutation relations:
\[
\{\gamma^\mu,\gamma^\nu\}
:=\gamma^\mu\gamma^\nu+\gamma^\nu\gamma^\mu
=-2\eta^{\mu\nu}I_4\quad(\mu,\nu=0,1,2,3).
\]
In particular, the spatial squares are \(-I_4\). A concrete mixed product is
\[
\gamma^1\gamma^2
=-i\begin{pmatrix}\sigma^3&0\\0&\sigma^3\end{pmatrix}
=\operatorname{diag}(-i,i,-i,i),\qquad
\gamma^2\gamma^1=-\gamma^1\gamma^2.
\]

To connect this example with the geometric definition, take
\(e_\mu=\partial/\partial x^\mu\) and set
\(c(e_\mu)=\gamma_\mu=\eta_{\mu\nu}\gamma^\nu\), summing over \(\nu\).
Thus \(\gamma_0=-\gamma^0\) and \(\gamma_j=\gamma^j\).
Using the metric identification of covectors with vectors,
\(c(dx^\mu)=c((dx^\mu)^\sharp)=\gamma^\mu\); the verified relations
therefore give a representation of the geometric Clifford algebra.
With \(\eta_{\mathrm{phys}}=-\eta\), the same numerical raised-index
matrices satisfy \(\{\gamma^\mu,\gamma^\nu\}=2\eta_{\mathrm{phys}}^{\mu\nu}I_4\).
No factor of \(i\) is needed when changing both metric signature and Clifford
sign in this way. Lowered indices must, however, use the metric of the chosen
convention. The corresponding differential equation is expanded in the
[[mathematical-physics/dirac-equation|Dirac equation]] knowl.

## Change of basis and spin covariance

Changing the basis of the spinor module conjugates every gamma matrix
simultaneously. A spin transformation \(s\) satisfies
\[
\rho(s)c(v)\rho(s)^{-1}=c(svs^{-1}),
\]
so the matrices transform compatibly with the orthogonal action on \(V\).
Different-looking gamma-matrix realizations can therefore describe equivalent
Clifford representations.

## Related constructions

In even dimension, the normalized product of all gamma matrices represents
the [[differential-geometry/chirality-operator|chirality operator]]. The
normalization is convention-dependent, whereas the resulting grading of the
complex spin representation is invariant.

## References

1. H. Blaine Lawson Jr. and Marie-Louise Michelsohn, *Spin Geometry*,
   Princeton University Press, 1989. [DOI
   record](https://doi.org/10.1515/9781400883912). Relevant: Chapter I.
2. Daniel S. Freed, *Five Lectures on Supersymmetry*, American Mathematical
   Society, 1999. Relevant: Lectures 1–2.
3. Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum
   Field Theory*, Addison–Wesley, 1995. Relevant: Sections 3.1–3.4 for the
   common physics sign convention.

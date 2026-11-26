+++
id = "proofs/grh/spanning-mainterm/product-of-sieve-systems"
title = "A finite product of sieve systems is a sieve system"
kind = "lemma"
summary = "Sieve systems on finitely many copies of the complex numbers and one more sieve system multiply to a sieve system on the product ring."
aliases = ["SieveSystem.pi", "product of sieve systems"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.SieveSystem.pi", "New.posSemidef_prod_mul", "New.norm_prod_mul_le_prod_mul", "New.headAt"]
lean_files = ["src/New/Spanning/MainTerm/SieveSystem.lean"]
proof_status = "full"
+++

**Lemma.** Let \((u,\iota,n,J,\psi,B_0,\Lambda,\beta)\) be a
[[proofs/grh/spanning-mainterm/sieve-system|sieve system]] of length \(n\) on a commutative
ring \(C\) whose measure is [[?c:S-finite measure|s-finite]], with entries in \(U\). Let \(\tau\)
be a finite set, and for each \(v\in\tau\) let
\((u',\iota',n,J'_v,\mathrm{w},B'_v,\Lambda',\gamma_v)\) be a sieve system of the same length
\(n\) on \(\mathbb C\) (with Lebesgue measure) with entries in \(\mathbb C^\times\), where

- \(u'(z)=z\) for \(z\ne0\) and \(u'(0)=1\),
- \(\mathrm{w}(c)=\exp(c-\bar c)\),
- \(\iota'\colon\mathbb C^\times\to\mathbb C\) and the weights \(\Lambda'_i\) are the same for all \(v\).

For a head \(p\) with entries in \((\mathbb C^\times)^\tau\times U\) write \(p^{(v)}\) for
the head of its components at \(v\) and \(p^{(U)}\) for the head of its components in \(U\). Then
the following data are a sieve system of length \(n\) on the ring \(\mathbb C^\tau\times C\)
(product measure) with entries in \((\mathbb C^\times)^\tau\times U\):

\[
\begin{aligned}
  &\text{entry map } (x,c)\mapsto\bigl((u'(x_v))_v,\ u(c)\bigr),\qquad
  \text{back map } (y,t)\mapsto\bigl((\iota'(y_v))_v,\ \iota(t)\bigr),\\
  &\mathbf J_i(p,q)=\prod_{v\in\tau}J'_{v,i}\bigl(p^{(v)},q^{(v)}\bigr)\cdot J_i\bigl(p^{(U)},q^{(U)}\bigr),\qquad
  \boldsymbol\psi(x,c)=\prod_{v}\mathrm w(x_v)\cdot\psi(c),\\
  &\mathbf B_0=\prod_v B'_v\cdot B_0,\qquad
  \boldsymbol\Lambda_i(p)=\prod_v\Lambda'_i\bigl(p^{(v)}\bigr)\cdot\Lambda_i\bigl(p^{(U)}\bigr),\qquad
  \boldsymbol\beta(x,c)=\prod_v\gamma_v(x_v)\cdot\beta(c).
\end{aligned}
\]

## Proof

Each of the six axioms is checked factor by factor.

*Value at zero.* \(\mathrm w(0)=1\) and \(\psi(0)=1\), so \(\boldsymbol\psi(0)=1\).

*Recursion and decay.* Fix \(i\le n\), heads \(p,q\) and \(\xi=((\xi_v)_v,\xi_C)\). Put
\[
  g_v(z)=\mathrm w(\xi_vz)\,J'_{v,i+1}\bigl(p^{(v)}[i\mapsto u'(z)],q^{(v)}[i\mapsto u'(z)]\bigr),\qquad
  g_C(c)=\psi(\xi_Cc)\,J_{i+1}\bigl(p^{(U)}[i\mapsto u(c)],q^{(U)}[i\mapsto u(c)]\bigr).
\]
Replacing the entry at position \(i\) of a head commutes with taking components, so the function
\(f_\xi\) of axiom 2 for the product data is \(f_\xi(x,c)=\prod_v g_v(x_v)\cdot g_C(c)\). Each
\(g_v\) and \(g_C\) is integrable by axiom 2 of its system, hence the product of functions of
separate variables is integrable for the product measure, and by
[[measure-theory/fubinis-theorem|Fubini's theorem]]
\[
  \int f_\xi\;=\;\prod_v\int_{\mathbb C}g_v\cdot\int_Cg_C .
\]
If \(\xi=0\), every \(\xi_v\) and \(\xi_C\) is \(0\), each factor is the corresponding \(J_i\) by
the recursion in its system, and the product is \(\mathbf J_i(p,q)\). If \(\xi\) is a unit of
the product ring, then every \(\xi_v\) is a unit of \(\mathbb C\) and \(\xi_C\) a unit of \(C\);
the decay bounds of the factors multiply (the modulus of a product is the product of the moduli)
and give \(\lvert\int f_\xi\rvert\le\boldsymbol\beta(\xi)\boldsymbol\Lambda_i(p)\boldsymbol\Lambda_i(q)\)
after reordering the factors.

*Positivity.* Let \((a_j)_{j\in\kappa}\) be finitely many heads with common entry \(t=((t_v)_v,t_U)\)
at position \(n\). Then the heads \(a_j^{(v)}\) have the common entry \(t_v\) and the heads
\(a_j^{(U)}\) the common entry \(t_U\) at position \(n\), so each matrix
\(\bigl(J'_{v,n+1}(a_j^{(v)},a_l^{(v)})\bigr)\) and \(\bigl(J_{n+1}(a_j^{(U)},a_l^{(U)})\bigr)\) is
positive semidefinite. The matrix of \(\mathbf J_{n+1}\) is their entrywise
([[linear-algebra/hadamard-product|Hadamard]]) product, which is positive semidefinite by the
[[?c:Schur product theorem|Schur product theorem]], applied by induction on the number of
factors.

*Continuity.* \(\mathbf J_{n+1}\) is a finite product of continuous functions composed with the
continuous maps that take components of heads.

*Mass and off-diagonal bound.* The bounds \(\lvert J'_{v,0}\rvert\le B'_v\), \(\lvert J_0\rvert\le B_0\)
multiply. For \(i<n\), if \(\boldsymbol\xi=\boldsymbol\iota(p_i)-\boldsymbol\iota(q_i)\) is a
unit, its components \(\iota'(p^{(v)}_i)-\iota'(q^{(v)}_i)\) and \(\iota(p^{(U)}_i)-\iota(q^{(U)}_i)\)
are units, the off-diagonal bounds of the factors apply, and their product is the required
bound. \(\blacksquare\)

## References

1. Lean: `New.SieveSystem.pi`, with `New.posSemidef_prod_mul` (Schur's product theorem for
   finitely many kernels) and `New.norm_prod_mul_le_prod_mul`, in
   `src/New/Spanning/MainTerm/SieveSystem.lean`.

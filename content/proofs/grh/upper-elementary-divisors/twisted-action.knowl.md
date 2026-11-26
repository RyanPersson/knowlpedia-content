+++
id = "proofs/grh/upper-elementary-divisors/twisted-action"
title = "Twisted action of GL_k(W) on forms"
kind = "construction"
summary = "The action of GL_k(W) on polynomials in the variables x_{b,s} through the maps of a Frobenius cycle, by g on even letters and by the inverse transpose on odd letters."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.letterMatrix", "New.FrobeniusCycle.polyAction", "New.FrobeniusCycle.letterRep", "New.FrobeniusCycle.polyAction_X", "New.FrobeniusCycle.polyAction_polyOfCoeffs", "New.FrobeniusCycle.letterRep_map"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/TwistingData.lean"]
+++

Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,R)\) and \(k\ge 0\). For \(g\in \mathrm{GL}_k(W)\) ([[?c:General linear group over a commutative ring|general linear group]]) and a letter \(s\) put
\[
g_s=\begin{cases}\iota_s(g) & s\text{ even},\\ \iota_s\bigl({}^{t}g^{-1}\bigr) & s\text{ odd},\end{cases}\qquad g_s\in M_k(R),
\]
the maps \(\iota_s\) being applied entrywise. Then \(g\mapsto g_s\) is multiplicative. The **twisted action** of \(g\) on the [[algebra-rings/polynomial-ring|polynomial ring]] \(R[x_{b,s}]\) is the \(R\)-algebra endomorphism
\[
g\cdot x_{c,s}=\sum_{b=0}^{k-1}(g_s)_{b,c}\,x_{b,s}.
\]
For \(n\ge 0\), the **twisted representation** is the multiplicative map \(\rho_n\colon \mathrm{GL}_k(W)\to M_{\mathcal{E}(N,k,n)}(R)\),
\[
\rho_n(g)=\bigotimes_{s\in\mathbb{Z}/N}\operatorname{Sym}^{n}(g_s),
\]
the [[?c:Kronecker product of matrices|Kronecker product]] over the letters of the \(n\)-th [[?c:Symmetric power of a matrix|symmetric powers]]: \(\operatorname{Sym}^n(A)_{\beta,\alpha}\) is the coefficient of \(x^{\beta}\) in the image of \(x^{\alpha}\) under the substitution \(x_c\mapsto\sum_b A_{b,c}x_b\), and \(\rho_n(g)_{\beta,\alpha}=\prod_s\operatorname{Sym}^n(g_s)_{\beta_s,\alpha_s}\).

## Properties

**Compatibility.** For every coefficient vector \(F\colon\mathcal{E}(N,k,n)\to R\),
\[
g\cdot\Bigl(\sum_\alpha F_\alpha x^{\alpha}\Bigr)=\sum_\beta\bigl(\rho_n(g)F\bigr)_\beta\,x^{\beta}.
\]
*Proof.* The action substitutes linearly inside each letter, and \(x^{\alpha}=\prod_s x_s^{\alpha_s}\), where \(x_s^{\alpha_s}\) involves only the variables of the letter \(s\). The image of \(x_s^{\alpha_s}\) is homogeneous of degree \(n\) in the variables of \(s\), hence equals \(\sum_{\beta_s}\operatorname{Sym}^n(g_s)_{\beta_s,\alpha_s}x_s^{\beta_s}\). Multiplying over \(s\) and expanding the product of sums gives \(g\cdot x^{\alpha}=\sum_\beta\rho_n(g)_{\beta,\alpha}x^{\beta}\); now sum against \(F_\alpha\). \(\square\)

**Base change.** For a ring homomorphism \(\varphi\colon R\to R'\), the twisted representation of \(\varphi_*T\) is \(\varphi(\rho_n(g))\), entrywise.

**Convention.** Matrices act on coefficient vectors, so they are the transposes of the matrices substituted in the variables: for both parities the translate of a polynomial \(h\) in the letter \(s\) is \(h\circ {}^{t}g_s\).

## References

1. Lean: `New.FrobeniusCycle.letterMatrix`, `New.FrobeniusCycle.polyAction`, `New.FrobeniusCycle.letterRep`, `New.FrobeniusCycle.polyAction_X`, `New.FrobeniusCycle.polyAction_polyOfCoeffs`, `New.FrobeniusCycle.letterRep_map` in `src/New/UpperBound/ElementaryDivisors/TwistingData.lean`.

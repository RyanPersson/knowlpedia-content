+++
id = "proofs/grh/upper-elementary-divisors/levels-of-substitution-operator"
title = "Filtration levels of the entries of a substitution operator"
kind = "lemma"
summary = "If the factors have levels given by differences of potentials up to a loss u, the entries of row beta of the substitution operator have level the weight of beta for the last potentials minus N n k (l+2) u."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.substitutionOperator_mem", "New.adjugate_transpose_mem", "New.symPowMatrix_mem", "New.reverse_prod_map_range_mem", "New.FrobeniusCycle.parityCofactor_mem", "New.FrobeniusCycle.degree_le_of_coeff_substitutionOperator"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean"]
proof_status = "full"
+++

**Lemma.** Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] with \(N\ge1\), \(G\) a [[proofs/grh/upper-elementary-divisors/gauss-filtration|real filtration]] of a commutative ring \(R\), and \(\psi\) factors as in the [[proofs/grh/upper-elementary-divisors/substitution-operator|substitution operator]] \(\mathcal{S}=\mathcal{S}(r,\ell,n;\psi)\). Let \(u\ge0\) and let \(\alpha_{s,d}\in\mathbb{R}^{k}\) (**potentials**; \(s\in\mathbb{Z}/N\), \(d\in\mathbb{N}\)) satisfy \(\sum_b\alpha_{s,d}(b)=0\), \(\lvert\alpha_{s,0}(b)\rvert\le u\), and
\[
(\psi_{s,d})_{b,c}\in G_{\alpha_{s,d+1}(b)-\alpha_{s,d}(c)-u}\qquad\text{for all }s,\ d\le\ell,\ b,c .
\]
Put \(x(b,s)=\pm\alpha_{s,\ell+\delta_r(b,s)}(b)\), with \(+\) for even and \(-\) for odd \(s\). Then for all \(\beta,\gamma\in\mathcal{E}(N,k,n)\),
\[
\mathcal{S}_{\beta,\gamma}\in G_{t},\qquad t=\sum_{b,s}\beta_s(b)\,x(b,s)-N\,n\,k\,(\ell+2)\,u .
\]

**Corollary (degrees).** For the Frobenius factors \(\Psi\) over \(O\), every monomial \(X^{\nu}\) occurring in an entry of \(\mathcal{S}(r,\ell,n;\Psi)\) has degree at most \(N\,n\,k\,(\ell+2)\,P^{\ell}\) in the variables of each copy \(j\).

## Proof

*Products.* By induction on \(m\le\ell+1\), every entry of row \(b\) of \(\psi_{s,m-1}\cdots\psi_{s,0}\) lies in \(G_{\alpha_{s,m}(b)-(m+1)u}\): for \(m=0\) the entries of the identity are in \(G_0\subseteq G_{\alpha_{s,0}(b)-u}\); in the step, \((\psi_{s,m})_{b,y}\cdot(\text{entry of row }y)\in G_{\alpha_{m+1}(b)-\alpha_m(y)-u+\alpha_m(y)-(m+1)u}\). In particular the level is at least \(\alpha_{s,m}(b)-v\) with \(v=(\ell+2)u\).

*Cofactors.* If the entries of row \(b\) of \(M\) lie in \(G_{y_b-v}\) with \(\sum_by_b=0\), \(v\ge0\), then the entries of row \(b\) of \({}^t\!\operatorname{adj}M\) lie in \(G_{-y_b-kv}\): the cofactor at \((b,c)\) is a signed sum of products of one entry from each row \(i\ne b\), of level \(\sum_{i\ne b}(y_i-v)=-y_b-(k-1)v\). For even \(s\), \(G_{y_b-v}\subseteq G_{y_b-kv}\) (\(k\ge1\)). So row \(b\) of the letter matrix \(\Sigma_s\) has level \(x(b,s)-K\), \(K=k(\ell+2)u\).

*Symmetric powers and Kronecker product.* If row \(b\) of \(M\) has level \(y_b\), the entry \(\operatorname{Sym}^n(M)_{\beta,\gamma}\) (the coefficient of \(x^{\beta}\) in \(\prod_c(\sum_bM_{b,c}x_b)^{\gamma_c}\)) has level \(\sum_b\beta(b)y_b\): give \(x_b\) the weight \(-y_b\); each linear form has Gauss level \(0\), hence so has the product. For \(\beta_s\) of degree \(n\) this is \(\sum_b\beta_s(b)x(b,s)-nK\). Multiplying over the \(N\) letters gives \(t\).

*Corollary.* Let \(G\) be the Gauss filtration over the \(0\)-adic filtration with weight \(-1\) on the variables of the copy \(j\) and \(0\) on the others; \(f\in G_{-t}\) means that all monomials of \(f\) have degree \(\le t\) in the copy \(j\). The entries of \(\Psi_{s,d}\), \(d\le\ell\), lie in \(G_{-P^{\ell}}\). Apply the lemma with \(\alpha=0\), \(u=P^{\ell}\). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.substitutionOperator_mem`, `New.adjugate_transpose_mem`, `New.symPowMatrix_mem`, `New.reverse_prod_map_range_mem`, `New.FrobeniusCycle.parityCofactor_mem`, `New.FrobeniusCycle.degree_le_of_coeff_substitutionOperator` in `src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean`.

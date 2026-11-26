+++
id = "proofs/grh/derivatives-vacuum/jet-series-of-product-of-linear-forms"
title = "Jet series of a theta function that is a product of functions of linear forms"
kind = "lemma"
summary = "If the entire theta function of f at scale c is a product of entire functions of one variable composed with linear forms, then the jet series of f is the product of their Taylor series evaluated at those forms, and the theta value is the product of their values at 0."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Space.jetSeries_eq_prod_of_entireTheta_smul", "New.Space.jetSeries_eq_prod", "New.Space.theta_eq_prod_of_entireTheta_smul", "New.Space.entireTheta_zero", "New.taylorAtZero_prod_comp_mul", "New.mvPowerSeries_eq_of_forall_line"]
lean_files = ["src/New/Derivatives/Vacuum/TightFrames.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/taylor-series-on-a-line-from-jet-series|the lemma on Taylor series along lines]]. For an entire function \(G\colon\mathbb{C}\to\mathbb{C}\) let \(T(G)\in\mathbb{C}[\![X]\!]\) be its Taylor series at \(0\), and for \(\mu\in Z\) let \(\ell_\mu=\sum_p\mu_pX_p\) be the linear form with coefficients \(\mu\); \(\mu\cdot z=\sum_p\mu_pz_p\).

**Lemma.** Let \(I\) be a finite set, \(G_i\colon\mathbb{C}\to\mathbb{C}\) (\(i\in I\)) functions, \(c\in\mathbb{C}\), \(\mu_i\in Z\), and \(f\in\mathcal{S}(V)\) such that
\[ \Theta_f(c\,z)=\prod_{i\in I}G_i(\mu_i\cdot z)\qquad\text{for all }z\in Z. \]

1. (Any signs.) \(\theta(f)=\prod_iG_i(0)\).
2. If all signs of \(V\) are \(+1\), \(f\) lies in the finite part of \(V\) and every \(G_i\) is entire, then
\[ J_c(f)=\prod_{i\in I}T(G_i)(\ell_{\mu_i}) \]
in \(\mathbb{C}[\![X_p]\!]\), where \(T(G_i)(\ell_{\mu_i})\) is the substitution of \(\ell_{\mu_i}\) for \(X\).

## Proof

1. Put \(z=0\): \(\Theta_f(0)=\theta(\varrho(0)f)e^{0}=\theta(f)\).

2. *Two power series in finitely many variables over \(\mathbb{C}\) that agree on every line agree.* For \(v\in Z\), restricting \(S\) to the line through \(v\) means substituting \(X_p\mapsto v_pX\). The coefficient of \(X^N\) in the restriction is \(S_N(v)\), the value at \(v\) of the homogeneous component of degree \(N\) of \(S\), a polynomial. If the restrictions of \(S\) and \(S'\) agree for all \(v\), then \(S_N\) and \(S'_N\) take the same values on \(\mathbb{C}^{\Sigma\times n}\), hence are equal polynomials (\(\mathbb{C}\) is infinite), for every \(N\).

*Restriction of both sides.* Fix \(v\). By [[proofs/grh/derivatives-vacuum/taylor-series-on-a-line-from-jet-series|the line lemma]] the restriction of \(J_c(f)\) is the Taylor series of
\[ t\mapsto\Theta_f(c\,t\,v)=\prod_iG_i\bigl((\mu_i\cdot v)\,t\bigr). \]
The Taylor series of \(t\mapsto G(\kappa t)\) is \(T(G)(\kappa X)\), and the Taylor series of a finite product of entire functions is the product of the Taylor series (induction on the number of factors, by the Leibniz rule). So the restriction of the left side is \(\prod_iT(G_i)((\mu_i\cdot v)X)\). On the right side, restriction is a ring homomorphism compatible with substitution, and it sends \(\ell_{\mu_i}\) to \((\mu_i\cdot v)X\); so the restriction of the right side is the same product.

## Remarks

The Lean file also records the uniform version: if the product formula holds for all \(c\) with coefficients \(\mu_{c,i}\), then both conclusions hold for all \(c\).

## References

1. Lean: `New.Space.jetSeries_eq_prod_of_entireTheta_smul`, `New.Space.jetSeries_eq_prod`, `New.Space.theta_eq_prod_of_entireTheta_smul`, `New.Space.entireTheta_zero`, `New.taylorAtZero_prod_comp_mul`, `New.mvPowerSeries_eq_of_forall_line` in `src/New/Derivatives/Vacuum/TightFrames.lean`.

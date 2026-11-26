+++
id = "proofs/grh/derivatives-divisibility/frobenius-congruence-for-theta"
title = "Frobenius congruence for the theta function"
kind = "theorem"
summary = "At a prime p that does not split in K, theta(pi_p z) equals theta(z)^(q_p) times 1 + pi_p H with H an integral series in y; consequently q_p g(z) - g(pi_p z) lies in pi_p O[[y]] for g = -log theta."
aliases = ["Frobenius congruence", "Frobenius congruence for -log theta"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CMLattice.exists_rescale_theta_eq_pow_mul_one_add_smul", "New.CMLattice.exists_negLogTheta_frobenius_congruence", "New.CMLattice.exists_rescale_theta_eq_pow_mul_aeval", "New.CMLattice.norm_piPrime_mul_coeff_negLogTheta_le_one", "New.CMLattice.norm_coeff_smul_negLogTheta_sub_rescale_le", "New.norm_piPrime_le_rpow", "New.norm_primeNorm", "New.norm_piPrime_le_norm_mul_succ", "New.odd_primeNorm", "New.ne_two_of_chiK_ne_one"]
lean_files = ["src/New/Derivatives/FormalGroup/FrobeniusCongruence.lean"]
proof_status = "full"
+++

**Theorem (Frobenius congruence).** Let \(d\equiv7\pmod 8\) be a prime, \(C\) a CM lattice for \(K=\mathbb{Q}(\sqrt{-d})\) with theta function \(\theta\) and \(g=-\log\theta\) (notation of the [[proofs/grh/derivatives-divisibility/cm-curve-setting|CM lattice]]), and let \(p\) be a prime with \(\chi_K(p)\ne1\), with a \(p\)-adic place \(\iota_p\). Write \(\pi=\iota_p(\pi_p)\) and \(q=q_p\) (see the [[proofs/grh/derivatives-divisibility/p-adic-setting|\(p\)-adic setting]]). Then, in \(\mathbb{C}_p[[z]]\):

1. there is \(H\in\mathcal{O}[[y]]\) with \(\theta(\pi z)=\theta(z)^{q}\,(1+\pi H)\);
2. there is \(G\in\mathcal{O}[[y]]\) with \(q\,g(z)-g(\pi z)=\pi\,G\).

## Proof

*Preliminaries.* The prime \(2\) splits in \(K\), so \(p\ge3\); hence \(q\) (which is \(p\) or \(p^2\)) is odd, and \(\lvert\pi\rvert=p^{-v(\pi_p)}\le p^{-1/2}\le p^{-1/(p-1)}\). Also \(q=\pm\pi^2\) (\(q=p^2=\pi^2\) if \(p\) is inert, \(q=p=-\pi^2\) if \(p=d\)), so \(\lvert q\rvert=\lvert\pi\rvert^2\).

*Step 1: \(\theta(\pi z)=\theta^{q}R(x)\) for a polynomial \(R\in\mathbb{C}_p[X]\) with \(2\deg R<q\).* The number \(\pi_p\) lies in \(\mathcal{O}_K\) and \(\pi_p\bar\pi_p=q\), so \(z\mapsto\pi_pz\) maps \(\Lambda\) into itself and is an [[?lean:New.CMLattice.IsIsogeny|isogeny of degree \(q\)]]. Therefore \(f(z)=\theta(\pi_pz)\) is a [[?lean:New.CMLattice.sections|section of degree \(q\)]] (a theta function for \(\Lambda\) of that degree), it is even because \(\theta\) is, and its values at torsion points are [[?lean:New.CMLattice.HasIntegralValues|integral]] at \(\iota_p\), because those of \(\theta\) are and this property [[?lean:New.CMLattice.HasIntegralValues.comp_isogeny|passes to the composition with an isogeny]]. By the [[?lean:New.CMLattice.exists_polynomial_of_even|expansion of even sections with integral torsion values]], the Taylor series of \(f\) is \(\theta^{q}R(x)\) for a polynomial \(R\) of degree at most \(q/2\); as \(q\) is odd, \(2\deg R<q\).

*Step 2: \(R(x)=\exp(q\,g(z)-g(\pi z))\).* This follows from \(\theta=\exp(-g)\): \(\exp(qg)\,\theta(\pi z)=\exp(qg)\theta^qR(x)=R(x)\).

*Step 3: \(\lvert\pi\rvert\,\lvert g_n\rvert\le1\) for the coefficients \(g_n\) of \(g\) with \(n<q\).* We have \(g_0=g_1=0\). For \(n=2\): \(\lvert\iota_p(\sqrt{-d})\cdot 2g_2\rvert\le1\) (fact 5 of the setting), \(\lvert2\rvert=1\), and \(\lvert\pi\rvert\le\lvert\iota_p\sqrt{-d}\rvert\) (equality if \(p=d\); otherwise \(\sqrt{-d}\) is a unit). For \(n=k+3\): comparing the coefficients of \(z^{k+1}\) in \(g''=g''(0)+x\) gives \((k+3)(k+2)\,g_{k+3}=x_{k+1}\), and \(\lvert x_{k+1}\rvert\le1\) because \(x\in\mathcal{O}[[y]]\) and \(k+1<q\) (facts 1, 2). It remains to see \(\lvert\pi\rvert\le\lvert(k+3)(k+2)\rvert\) when \(k+3<q\): one of the two consecutive integers is prime to \(p\); the other, \(m\) say, satisfies \(0<m<q\), so \(v_p(m)\le1\) if \(q=p^2\) (and then \(\pi=p\)), and \(v_p(m)=0\) if \(q=p\).

*Step 4.* For \(n<q\) the coefficient of \(z^n\) in \(h=q\,g(z)-g(\pi z)\) is \((q-\pi^n)g_n\). It vanishes for \(n\le1\); for \(n\ge2\), \(\lvert q-\pi^n\rvert\le\lvert\pi\rvert^2\), so by Step 3 it has norm at most \(\lvert\pi\rvert\).

*Step 5.* Since \(\lvert\pi\rvert\le p^{-1/(p-1)}\), \(h(0)=0\), and \(\pi\) divides the coefficients of \(h\) below the degree \(q\), [[?lean:New.norm_coeff_expSubst_sub_one_le|the same holds for \(\exp(h)-1\)]]. By Step 2, the coefficients of \((R-1)(x)\) below the degree \(q\) have norm at most \(\lvert\pi\rvert\).

*Step 6.* The series \(x=z^2+\cdots\) is integral below the degree \(q\). In degree \(2i\) only the powers \(x^j\), \(j\le i\), contribute to \((R-1)(x)\), and \(x^i\) contributes with coefficient \(1\); so by [[?lean:New.norm_coeff_le_of_aeval|induction on \(i\)]] the coefficients of \(R-1\) satisfy \(\lvert(R-1)_i\rvert\le\lvert\pi\rvert\) whenever \(2i<q\), that is, for all \(i\le\deg R\). Hence
\[
H=\pi^{-1}(R-1)(x)=\sum_{i\le\deg R}\pi^{-1}(R-1)_i\,x^i\in\mathcal{O}[[y]],
\]
because \(x\in\mathcal{O}[[y]]\), and \(\theta(\pi z)=\theta^qR(x)=\theta^q(1+\pi H)\). This is 1.

*Step 7 (2).* Put \(G=\pi^{-1}h\); then \(G(0)=0\) and \(\exp(\pi G)=R(x)=1+\pi H\) with \(H\in\mathcal{O}[[y]]\). As \(\pi\ne0\) and \(\lvert\pi\rvert\le p^{-1/(p-1)}\), fact 7 of the setting (taking logarithms: \(G=\pi^{-1}\log(1+\pi H)\) is an integral series in \(H\)) gives \(G\in\mathcal{O}[[y]]\). \(\blacksquare\)

## References

1. Lean: `New.CMLattice.exists_rescale_theta_eq_pow_mul_one_add_smul`, `New.CMLattice.exists_negLogTheta_frobenius_congruence` and the lemmas before them in `src/New/Derivatives/FormalGroup/FrobeniusCongruence.lean`.

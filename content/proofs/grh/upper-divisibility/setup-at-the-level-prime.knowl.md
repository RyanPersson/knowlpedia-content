+++
id = "proofs/grh/upper-divisibility/setup-at-the-level-prime"
title = "The places Sigma_N, the lattices L_j and the module A' at the prime N"
kind = "definition"
summary = "At p = N: the conjugates of the induced places, the diagonal points that carry the standard lattice to L_j and its dual, the action of GL at these places in a basis of L_j, and the module of forms that a power of U_p makes integral."
aliases = ["Sigma_N", "non-induced places", "diagonal point at N", "up-integral forms"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.nonInducedPlaces", "New.Data.isSplitLevel_nonInducedPlaces", "New.Data.diagPoint", "New.Data.diagPointN", "New.Data.dualPointN", "New.Data.conjEmbedGL", "New.Data.formRepAtN", "New.Data.upIntegralForms", "New.Data.map_adeleExtension_diagPoint"]
lean_files = ["src/New/UpperBound/Divisibility/SetupAtLevel.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] with level prime \(N=\pi_N\bar\pi_N\), and fix an embedding \(\iota\colon\mathbb{C}\to\mathbb{C}_N\). For \(\tau\in\Phi\) let \(w_\tau\) be the [[proofs/grh/upper-divisibility/marked-set-of-primes|prime of \(E\) above \(N\) induced by \(\tau\)]].

- \(\Sigma_N=\{\overline{w_\tau}:\tau\in\Phi\}\), the set of the conjugates of the induced places.
- For a stage \(j\) and a set \(S\) of places, \(\delta_j(S)\in G_f(X_j)\) is the point supported above \(N\) whose component at \(w\in\Sigma_N\) is \(\operatorname{diag}(1,\dots,1,N)\) if \(w\in S\) and \(1\) otherwise (the component at \(\bar w\) being determined by unitarity).
- \(\delta_j=\delta_j(\{w:w\mid\pi_N\})\) and \(\delta_j^{\vee}=\delta_j\cdot\delta_j(\Sigma_N)^{-1}\). At \(\Sigma_N\), \(\delta_j\) carries the standard lattice to the lattice \(L_j\) of integral vectors whose last coordinate is divisible by \(\pi_N\), and \(\delta_j^{\vee}\) carries it to the dual lattice \(L_j^{\vee}\).
- For a matrix \(a\in\mathrm{GL}(X_j)\) over the product \(\prod_{w\in\Sigma_N}E_w\), let \(\langle a\rangle_j=\delta_j\,\tilde a\,\delta_j^{-1}\in G_f(X_j)\), where \(\tilde a\) is the unitary adelic point supported above \(N\) with components \(a\) at \(\Sigma_N\): "\(a\) read in a basis of \(L_j\)". Forms on \(X_j\) become a representation \(\rho_j\) of \(\mathrm{GL}(X_j)(\prod_{w\in\Sigma_N}E_w)\) by right translation by \(\langle a\rangle_j\).
- Let \(U=U_N\) be the [[?lean:New.IsSplitLevel.upOperator|operator \(U_p\)]] of the representation \(\rho_0\), and \(\varrho\) the number with \(m=2\varrho+2\). The module \(\mathcal A'\) of **up-integral forms** consists of the forms \(\varphi\) on \(X_0\) such that \(U^{\varrho+1}\varphi\) is a source form whose values are integral at base point \(\delta_0\) (gauge of \(U^{\varrho+1}\varphi(g)\) at \(g\delta_0\) at most \(1\) for all \(g\)); it is a module over \(O_\iota=\{z:\lvert\iota z\rvert_N\le1\}\) and does not depend on the twist.

**Proposition.** \(\Sigma_N\) is a [[?lean:New.IsSplitLevel|split level]] for \(N\): its places lie above \(N\), are unramified of residue degree one, and of each pair \(w,\bar w\) of places above \(N\) exactly one lies in \(\Sigma_N\). Moreover, read in \(\mathbb{C}_N\) through \(\iota\circ\tau\circ\mathrm{conj}\) (the component at \(\overline{w_\tau}\)), the point \(\delta_j(S)\) is \(\operatorname{diag}(1,\dots,1,N)\) if \(\overline{w_\tau}\in S\) and \(1\) otherwise.

## Proof

\(N\equiv1\bmod q_2^2\), so \(N\) splits completely in \(E\): every place above \(N\) has residue degree one and \(N\) is a uniformiser there ([[?lean:New.Parameters.q_eq_of_modEq_one|`q_eq_of_modEq_one`]], [[?lean:New.Data.v_N_eq_exp_neg_one|`v_N_eq_exp_neg_one`]], quoted). The induced places \(w_\tau=\tau\cdot w_1\) form one orbit of \(\Phi=\operatorname{Gal}(E/K)\), which contains no conjugate pair because \(N\) splits in \(K\) ([[?lean:New.Parameters.smul_ne_star|`smul_ne_star`]], quoted); and every place above \(N\) is in this orbit or conjugate to a member ([[?lean:New.Parameters.exists_smul_eq_or_star|`exists_smul_eq_or_star`]], quoted). The last statement holds because \(\iota\circ\tau\circ\mathrm{conj}\) factors through the completion at \(\overline{w_\tau}\in\Sigma_N\). \(\blacksquare\)

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Divisibility/SetupAtLevel.lean`.

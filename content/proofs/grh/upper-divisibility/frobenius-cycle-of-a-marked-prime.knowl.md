+++
id = "proofs/grh/upper-divisibility/frobenius-cycle-of-a-marked-prime"
title = "The Frobenius cycle of a marked prime"
kind = "proposition"
summary = "The a-places inducing a marked prime or its conjugate form one orbit under the place named by -p^(o_0), and the corresponding embeddings of the valuation ring form a Frobenius cycle with exponent o_0."
aliases = ["letter embedding"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsMarked.exists_frobeniusCycle", "New.Data.exists_orbit_of_mem_aPlaces", "New.Data.dvd_letterEmbedding_sub_pow", "New.Data.letterEmbedding", "New.Data.embeddingToward", "New.Data.IsExceptional.card_residueField", "New.Data.not_isUnit_natCast_embValRing"]
lean_files = ["src/New/UpperBound/Divisibility/MarkOperator.lean"]
proof_status = "outline"
+++

Let \(D\) be [[?lean:New.Data|admissible data]], \(p\) a prime, \(\iota\colon\mathbb{C}\to\mathbb{C}_p\) an embedding, \(O_\iota=\{z\in\mathbb{C}:\lvert\iota z\rvert_p\le1\}\), \(g=u(-p)\in\Phi\) the place named by \(-p\) and \(o_0=o_0(p)\). For a prime \(\mathfrak l\) of \(E\) with valuation ring \(W\subset E\) and a place \(\sigma\) with \(w_\sigma\in\{\mathfrak l,\bar{\mathfrak l}\}\), the **letter embedding** \(\lambda_\sigma\colon W\to O_\iota\) is the restriction of \(\sigma\) if \(w_\sigma=\mathfrak l\), and of \(\sigma\circ\mathrm{conj}\) otherwise; in both cases it induces \(\mathfrak l\), so it maps \(W\) into \(O_\iota\).

**Proposition.**

1. (**Orbit.**) Suppose \(\chi_K(p)=-1\) and \(o_0\) is odd. Let \(\tau\) be an a-place and \(N\) the order of \(g^{o_0}\). Then \(t(i)=g^{o_0i}\tau\), \(i\in\mathbb{Z}/N\), is injective, satisfies \(t(i+1)=u(-p^{o_0})\,t(i)\), and its image is exactly the set of a-places \(\sigma\) with \(w_\sigma\in\{w_\tau,\overline{w_\tau}\}\).
2. (**Frobenius congruence.**) Suppose \(\chi_K(p)=-1\), \(\bar{\mathfrak l}\ne\mathfrak l\), \(e\) is odd, \(\sigma'=u(-p^{e})\sigma\), and both \(\sigma,\sigma'\) induce \(\mathfrak l\) or \(\bar{\mathfrak l}\). Then for all \(x\in W\): \(\lambda_{\sigma'}(x)\equiv\lambda_\sigma(x)^{p^{e}}\pmod{p\,O_\iota}\).
3. (**Cycle.**) Let \(\Lambda\) be a [[proofs/grh/upper-divisibility/marked-set-of-primes|marked set]], \(\mathfrak l\in\Lambda\), let the order of \(g\) be \(o_0N\), and let \(t\colon\mathbb{Z}/N\to\Phi\) satisfy \(t(i+1)=u(-p^{o_0})t(i)\) and \(w_{t(i)}\in\{\mathfrak l,\bar{\mathfrak l}\}\). Then the maps \(\lambda_{t(i)}\) form a [[?lean:New.FrobeniusCycle|Frobenius cycle]] with \(N\) letters on \(W\) with values in \(O_\iota\), with prime \(p\), exponent \(o_0\) (so \(P=p^{o_0}\)), and with the letter \(i\) even exactly when \(w_{t(i)}=\mathfrak l\).

## Proof

(1) Injectivity holds since \(g^{o_0}\) has order \(N\); the recursion since \(u(-p^{o_0})=g^{o_0}\) for odd \(o_0\). By the [[proofs/grh/upper-divisibility/orbits-at-an-exceptional-prime|description of orbits]] (which uses only that \(p\) is inert), the places inducing \(w_\tau\) or its conjugate are the \(g^{i}\tau\); and \(g^{i}\tau\) is an a-place iff the class of \(g\) modulo \(q_0\) has \(i\)-th power \(1\), iff \(o_0\mid i\).

(2) Let \(\rho\) be the automorphism of \(E\) attached to the place \(u(-p^{e})\). The source proves ([[?lean:New.Parameters.natCast_dvd_pow_sub_galOfPlaceInt_star|`natCast_dvd_pow_sub_galOfPlaceInt_star`]], quoted) that for \(p\) inert in \(K\) and odd \(e\), \(\rho(\bar a)\equiv a^{p^{e}}\pmod{p\mathcal O_E}\) for all \(a\in\mathcal O_E\); that is, \(\rho(a)\equiv\bar a^{\,p^{e}}\). Since \(e\) is odd, \(w_{\sigma'}=\overline{w_\sigma}\), so exactly one of \(\lambda_\sigma,\lambda_{\sigma'}\) involves conjugation; with \(\sigma'=\sigma\circ\rho\) this gives \(\lambda_{\sigma'}(\bar a)=\lambda_\sigma(\rho(a))\) for \(a\in\mathcal O_E\) in both cases. Reducing modulo \(p\) (the quotient \(O_\iota/p\) has characteristic \(p\), since \(p\) is not a unit of \(O_\iota\)): \(\lambda_{\sigma'}(\bar a)\equiv\lambda_\sigma(\bar a)^{p^{e}}\). As \(a\mapsto\bar a\) is onto \(\mathcal O_E\), the two ring maps \(W\to O_\iota/p\), namely \(\lambda_{\sigma'}\) and the \(p^{e}\)-th power of \(\lambda_\sigma\), agree on \(\mathcal O_E\), hence on its localisation \(W\).

(3) The requirements of a Frobenius cycle: \(p\) is prime; \(P=p^{o_0}\ge p\ge13\ge5\) (a non-split prime is at least \(13\)); a square root of \(p\) exists in \(\mathbb{C}\) and lies in \(O_\iota\); the congruence is (2) with \(e=o_0\); parities alternate because multiplication by \(u(-p^{o_0})\) exchanges \(\mathfrak l\) and \(\bar{\mathfrak l}\ne\mathfrak l\); and the residue field of \(W\) has \(p^{o_0N}=P^{N}\) elements by the [[proofs/grh/upper-divisibility/orbits-at-an-exceptional-prime|norm of primes above an exceptional \(p\)]]. \(\blacksquare\)

*Status.* The congruence \(\rho(\bar a)\equiv a^{p^{e}}\) for the automorphism named by \(-p^{e}\) is quoted from another file.

## References

1. Lean: `New.Data.IsMarked.exists_frobeniusCycle`, `New.Data.exists_orbit_of_mem_aPlaces`, `New.Data.dvd_letterEmbedding_sub_pow` in `src/New/UpperBound/Divisibility/MarkOperator.lean`.

+++
id = "proofs/grh/upper-divisibility/elementary-divisors-of-the-scaled-hecke-operator-given-a-frobenius-cycle"
title = "Elementary divisor bound for the scaled Hecke operator, given a Frobenius cycle"
kind = "theorem"
summary = "Given a Frobenius cycle matching the a-places above a marked prime, the scaled Hecke operator is onto on integral source forms modulo p^j up to a colength bounded by (3c + theta j) times the dimension."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Columns.isOntoUpToColength_scaledHeckeOperator_of_frobeniusCycle"]
lean_files = ["src/New/UpperBound/Divisibility/HeckeEdges.lean"]
proof_status = "outline"
+++

**Theorem.** Let \(D\) be [[?lean:New.Data|admissible data]], \(p\) a prime, \(\iota\colon\mathbb{C}\to\mathbb{C}_p\), \(O_\iota=\{z\in\mathbb{C}:\lvert\iota z\rvert_p\le1\}\), \(\Lambda\) a [[proofs/grh/upper-divisibility/marked-set-of-primes|marked set]] and \(\mathfrak l\in\Lambda\), with valuation ring \(W\subset E\). Let \(N\ge1\) and let \(T\) be a [[?lean:New.FrobeniusCycle|Frobenius cycle]] with \(N\) letters on \(W\) with values in \(O_\iota\), with prime \(p\) (so \(p\) is not a unit of \(O_\iota\)), such that:

- a bijection \(t\) from \(\mathbb{Z}/N\) to the set \(Q=\{\sigma\in\Phi_a:w_\sigma\in\{\mathfrak l,\bar{\mathfrak l}\}\}\) is given;
- the map \(\iota_s\) of the letter \(s\) is the restriction to \(W\) of the embedding \(t(s)\) if \(s\) is even, and of \(t(s)\circ\mathrm{conj}\) if \(s\) is odd;
- \(A_{\mathfrak l}=a\cdot\lvert\{s:\ s\text{ even}\}\rvert\);
- the size conditions hold for \(k\), \(a\), \(\mathfrak r=\mathfrak r(p)\) and a real \(\theta\): \(0<\mathfrak r\), \(2\mathfrak r\le k\), \(0<\theta\le1\), \(a^{4}\le q\) and \((Nk\log q/\theta)^{5}P^{3\mathfrak r}\le a\), where \(q=P^{N}\).

Let \(\widetilde T_{\mathfrak l}=p^{A_{\mathfrak l}}T_{\mathfrak l,\mathfrak r}\) be the [[proofs/grh/upper-divisibility/scaled-hecke-operator|scaled Hecke operator]] and \(\mathcal M\) the \(O_\iota\)-module of integral source forms. Then for every \(j_0\in\mathbb{N}\): \(\widetilde T_{\mathfrak l}\mathcal M\subset\mathcal M\), and there is a natural number
\[
e\le\bigl(3c+\theta j_0\bigr)\dim_{\mathbb{C}}\mathcal S,\qquad c=Na\Bigl(P^{-2\mathfrak r}+\frac{\mathfrak r^{2}}{kP}\Bigr),
\]
such that the [[?lean:New.ColengthDvd|colength]] of \(\widetilde T_{\mathfrak l}\mathcal M+p^{j_0}\mathcal M\) in \(\mathcal M\) divides \(p^{e}\): every finite family \(\varphi_1,\dots,\varphi_n\in\mathcal M\) is carried into \(\widetilde T_{\mathfrak l}\mathcal M+p^{j_0}\mathcal M\) by a square matrix over \(O_\iota\) whose determinant divides \(p^{e}\). (In the source: \(\widetilde T_{\mathfrak l}\) is [[?lean:New.IsOntoUpToColength|onto up to colength]] \((3c+\theta j_0)\dim\mathcal S\) modulo \(p^{j_0}\).)

## Proof

The statement is the [[?lean:New.FrobeniusCycle.elementary_divisors|theorem on elementary divisors of an edge Hecke operator]] (another area), once \(\widetilde T_{\mathfrak l}\) on \(\mathcal M\) is identified with an edge Hecke operator. This identification is what is proved here.

1. *Preliminaries.* By the [[proofs/grh/upper-divisibility/properties-of-marked-sets|properties of marked sets]], \(\bar{\mathfrak l}\ne\mathfrak l\), \(p\) is a uniformiser at \(\mathfrak l\), and the level \(K_0\) of stage \(0\) is maximal at \(\mathfrak l\); \(K_0\) is free; and \(\mathfrak r<k\) by the size conditions.
2. *Edges.* Choose [[proofs/grh/upper-divisibility/hecke-cosets-as-edges|edge data]] \((\rho_x,o,\gamma_e,u_e,g_e)\) for \(K_0\), \(\mathfrak l\) and \(r=\mathfrak r\). By the knowl on the [[proofs/grh/upper-divisibility/hecke-operator-as-a-sum-over-edges|sum over edges]], an edge is determined by its origin \(o(e)\) and the coset \(g_e^{-T}\mathcal P_r\) of the inverse transpose of its change of basis (equivalently by the coset \(\mathcal P_rg_e^{T}\) on the other side), and
\[
(\widetilde T_{\mathfrak l}\varphi)(\rho_x)=p^{A_{\mathfrak l}}\sum_b\varrho(\gamma_{(x,b)})\varphi(\rho_{o(x,b)}).
\]
3. *The matrix of an edge.* On the weight space of \(X_0\) (no determinant twist at stage \(0\)) \(\varrho(\gamma)\) is the Schur matrix of the family \(((\tau\circ\mathrm{conj})(\gamma))_\tau\). By the [[proofs/grh/upper-divisibility/action-of-an-edge-on-the-variables|lemma on the action of an edge]]: with the splitting \(J\) for \(Q\), with \(c_s=p\) for even \(s\) and \(1\) for odd \(s\) (so that \((\prod_sc_s)^{a}=p^{A_{\mathfrak l}}\)), and with \(\gamma_e^{-1}=g_e\,d^{-1}\beta^{-1}\),
\[
p^{A_{\mathfrak l}}\,\varrho(\gamma_e)_{ij}=m_e{}_{\,J(i)_2,J(j)_2}\cdot\bigl(\mathrm{Let}_a(g_e)\,\mathrm{Dep}\,\mathrm{Let}_a(\beta^{-1})\bigr)_{J(j)_1,J(i)_1},
\]
where \(m_e\) is the Schur matrix of \(\gamma_e\) at the places outside \(Q\). This \(m_e\) is invertible over \(O_\iota\): for an a-place \(\tau\notin Q\) the prime \(\overline{w_\tau}\) is above \(p\) and different from \(\mathfrak l,\bar{\mathfrak l}\), where \(\gamma_e\) is integral (part 4 of the knowl on edges).
4. *The module.* By the [[proofs/grh/upper-divisibility/integral-source-forms-as-families-of-integral-vectors|lemma on integral source forms]], \(F\mapsto\varphi_F\) identifies \(\mathcal M\) with families of integral vectors indexed by the classes; by 2 and 3 it intertwines \(\widetilde T_{\mathfrak l}\) with the [[?lean:New.FrobeniusCycle.edgeHeckeOperator|edge Hecke operator]] of the edge coordinates (origin \(o\), change of basis \(g_e\) at the origin, \(\beta^{-1}\) at the terminus, transition \(m_e\)).
5. *Dimension.* \(\dim\mathcal S\) is the number of classes times the dimension of the weight space, the rank of the module of families.

The quoted theorem, applied to these edge coordinates, gives the claim. \(\blacksquare\)

*Status.* The theorem on elementary divisors of an edge Hecke operator is the main input and is not proved in this area; steps 1 to 5 were checked against the Lean proof.

## References

1. Lean: `New.Columns.isOntoUpToColength_scaledHeckeOperator_of_frobeniusCycle` in `src/New/UpperBound/Divisibility/HeckeEdges.lean`; `New.FrobeniusCycle.elementary_divisors` in `src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean`.

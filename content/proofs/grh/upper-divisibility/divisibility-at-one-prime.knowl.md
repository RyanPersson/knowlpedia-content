+++
id = "proofs/grh/upper-divisibility/divisibility-at-one-prime"
title = "Divisibility of the composite lift at one prime"
kind = "theorem"
summary = "At each prime there is a module of source forms of colength at most allowedLoss(p) times the dimension on whose ramified members the composite lift has valuation at least gain(p) minus allowedLoss(p)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.exists_colengthDvd_gaugeLe_compositeLift", "New.Data.mem_smallNonsplitPrimes_iff_isSmallNonsplit", "New.Data.chiK_eq_one_or_le_of_notMem_smallNonsplitPrimes"]
lean_files = ["src/New/UpperBound/Divisibility/LocalDivisibility.lean"]
proof_status = "outline"
+++

**Theorem.** Let \(D\) be [[?lean:New.Data|admissible data]], \(p\) a prime and \(\iota\colon\mathbb{C}\to\mathbb{C}_p\) an embedding, with \(O_\iota\) the ring of \(p\)-integral complex numbers, \(\mathcal M\) the \(O_\iota\)-module of integral source forms and \(\operatorname{al}(p)\) the [[proofs/grh/upper-divisibility/allowed-loss|allowed loss]]. There are a natural number \(l\le\operatorname{al}(p)\dim_{\mathbb{C}}\mathcal S\) and an \(O_\iota\)-submodule \(S\) of the source forms such that:

1. every finite family in \(\mathcal M\) is carried into \(S\) by a square matrix over \(O_\iota\) whose determinant divides \(p^{l}\);
2. for every twist \(\vartheta\) whose modulus has norm prime to \(p\), every [[?lean:New.Data.IsChainDatum|chain datum]] \(\Psi\) for \(\vartheta\), and every \(\varphi\in S\) that is a [[proofs/grh/upper-divisibility/ramified-source-forms|ramified source form]], the [[?lean:New.Data.compositeLift|composite lift]] \(C_{\vartheta,\Psi}(\varphi)\) has gauge at most \(p^{\operatorname{al}(p)-\operatorname{gain}(p)}\) at base point \(1\).

## Proof

Four cases. In the first three \(p\ne N\), and the composite lift is the restricted chain of a weak chain datum ([[proofs/grh/upper-divisibility/chain-datum-as-a-weak-chain-datum|expanding the gluing]]).

*(i) \(p\ne N\), and \(p\) split in \(K\) or \(p\ge x_1\).* Here \(\operatorname{al}(p)=0\) and \(\operatorname{gain}(p)=0\) ([[proofs/grh/upper-divisibility/prime-sum-grouped-by-primes|vanishing of the gain]]). Also \(p\ne d\): \(d<x_1\) and \(\chi_K(d)=0\ne1\), so \(d\) is a small non-split prime. Take \(l=0\), \(S=\mathcal M\); the chain keeps integrality ([[proofs/grh/upper-divisibility/valuation-of-chains-at-unmarked-primes|part 1]]).

*(ii) \(p<x_1\) non-split, not exceptional.* \(\operatorname{al}(p)=2\operatorname{loss}(p)\). Take \(l=0\), \(S=\mathcal M\). The valuation is at least \(\operatorname{gain}-\operatorname{loss}-m\operatorname{coll}_p(\emptyset)\) ([[proofs/grh/upper-divisibility/valuation-of-chains-at-unmarked-primes|part 2]]) and \(m\operatorname{coll}_p(\emptyset)\le\operatorname{loss}(p)\) for non-exceptional \(p\) ([[proofs/grh/upper-divisibility/collision-sum-bound|collision sum]]).

*(iii) \(p<x_1\) exceptional.* \(\operatorname{al}(p)=2\operatorname{loss}(p)\). Choose a [[proofs/grh/upper-divisibility/full-mark-exists|full mark]] \(\Lambda\) and take \(S=Y^{m}\mathcal M+p^{j_p}\mathcal M\). By the theorem on [[proofs/grh/upper-divisibility/valuation-and-colength-at-a-full-mark|valuation and colength at a full mark]], the colength exponent is \(l\le\operatorname{loss}(p)\dim\mathcal S\le2\operatorname{loss}(p)\dim\mathcal S\), and the valuation on \(S\) is at least \(\operatorname{gain}-2\operatorname{loss}\).

*(iv) \(p=N\).* \(N\) is not a small non-split prime (\(N\ge x_1\)), \(\operatorname{al}(N)=2mfb\), and \(\operatorname{gain}(N)=0\). Take \(S\) the source forms lying in the module \(\mathcal A'\) of [[proofs/grh/upper-divisibility/setup-at-the-level-prime|up-integral forms]]. Its [[proofs/grh/upper-divisibility/colength-of-the-up-integral-forms|colength]] exponent in \(\mathcal M\) is \(l\le mfb\dim\mathcal S\), and on its ramified members the composite lift has gauge at most \(N^{2mfb}\) ([[proofs/grh/upper-divisibility/valuation-of-the-composite-lift-at-n|valuation at \(N\)]]).

Ramification of \(\varphi\) is used only in case (iv). \(\blacksquare\)

*Status.* Complete relative to the cited knowls (which are outlines).

## Remarks

In case (iii) \(S\) is contained in \(\mathcal M\); in case (iv) the members of \(S\) need not be integral, which is why the statement speaks of a module of source forms and the [[proofs/grh/upper-divisibility/local-divisibility-of-the-composite-lift|final theorem]] intersects with the integral ramified forms.

## References

1. Lean: `New.Data.exists_colengthDvd_gaugeLe_compositeLift` in `src/New/UpperBound/Divisibility/LocalDivisibility.lean`.

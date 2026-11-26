+++
id = "proofs/grh/upper-elementary-divisors/frobenius-cycle"
title = "Frobenius cycle"
kind = "definition"
summary = "A prime power P, ring maps from a local ring indexed by Z/N that are successive P-th powers modulo p, alternating parities, and a square root of p."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle", "New.FrobeniusCycle.P", "New.FrobeniusCycle.q", "New.FrobeniusCycle.map", "New.FrobeniusCycle.frobenius_pow_congr", "New.Exponents"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/TwistingData.lean"]
+++

Let \(N\ge 1\) be an integer, \(W\) a commutative [[algebra-commutative/local-ring|local ring]] and \(R\) a commutative ring. A **Frobenius cycle** \(T\) for \((N,W,R)\) consists of

- a prime number \(p\) and an integer \(f\ge 0\) with \(P:=p^{f}\ge 5\);
- for every **letter** \(s\in\mathbb{Z}/N\) a [[algebra-rings/ring-homomorphism|ring homomorphism]] \(\iota_s\colon W\to R\);
- for every letter \(s\) a **parity**, even or odd;
- an element \(w\in R\);

such that

1. \(w^{2}=p\) in \(R\);
2. \(\iota_{s+1}(x)\equiv \iota_s(x)^{P} \pmod{pR}\) for all \(s\in\mathbb{Z}/N\) and \(x\in W\);
3. the letters \(s\) and \(s+1\) have opposite parities, for every \(s\);
4. the [[algebra-commutative/residue-field|residue field]] of \(W\) is finite with \(q:=P^{N}\) elements.

## Remarks

- Iterating axiom 2 gives \(\iota_{s+n}(x)\equiv\iota_s(x)^{P^{n}} \pmod{pR}\) for all \(n\ge 0\): if \(u\equiv v \pmod p\) then \(u^{P}\equiv v^{P}\pmod p\), since \(u-v\) divides \(u^{P}-v^{P}\). For \(n=N\) this reads \(\iota_s(x)\equiv\iota_s(x)^{q}\pmod p\).
- Axiom 3 forces \(N\) to be even when \(N\ge 1\) is such that a cycle exists (the parities alternate around \(\mathbb{Z}/N\)); the Lean structure does not state this separately.
- **Base change.** If \(\varphi\colon R\to R'\) is a ring homomorphism, then \((p,f,\varphi\circ\iota_s,\text{parities},\varphi(w))\) is a Frobenius cycle for \((N,W,R')\), written \(\varphi_*T\).
- **Variables and exponents.** Throughout this chapter one fixes \(k\ge 0\) and uses the variables \(x_{b,s}\), \(b\in\{0,\dots,k-1\}\), \(s\in\mathbb{Z}/N\). For \(n\ge 0\) the set \(\mathcal{E}(N,k,n)\) of **exponents** consists of the families \(\beta=(\beta_s)_{s\in\mathbb{Z}/N}\) with \(\beta_s\in\mathbb{N}^{k}\) of total degree \(n\); to \(\beta\) corresponds the monomial \(x^{\beta}=\prod_{b,s}x_{b,s}^{\beta_s(b)}\), homogeneous of degree \(n\) in the variables of each letter. A **coefficient vector** is a function \(F\colon\mathcal{E}(N,k,n)\to R\); its **form** is \(\sum_\beta F_\beta x^{\beta}\).
- In the elements of the Lean structure, \(R\) is not assumed to have characteristic \(0\); the cycle is used both over a valuation ring of characteristic \(0\) and over a field of characteristic \(p\) (where \(w=0\)).

## References

1. Lean: `New.FrobeniusCycle`, `New.FrobeniusCycle.P`, `New.FrobeniusCycle.q`, `New.FrobeniusCycle.map`, `New.FrobeniusCycle.frobenius_pow_congr`, `New.Exponents` in `src/New/UpperBound/ElementaryDivisors/TwistingData.lean`.

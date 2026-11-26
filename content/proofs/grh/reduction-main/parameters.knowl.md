+++
id = "proofs/grh/reduction-main/parameters"
title = "The parameters q0 and d, and the moduli q1 and q2"
kind = "definition"
summary = "A multiple q0 of 18480 and a prime d congruent to q0/2 - 1 modulo q0; with them the numbers l0(s), the tower degree, q1(s) and q2(s)."
aliases = ["Parameters", "parameters of the proof", "tower degree", "q1", "q2"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters", "New.l₀", "New.towerDeg", "New.Parameters.q₁", "New.Parameters.q₂", "New.Parameters.K", "New.mul_lt_l₀", "New.l₀_le_mul", "New.towerDeg_eq", "New.Parameters.instPrimeSevenModEight", "New.Parameters.sixty_four_lt_d", "New.Parameters.dvd_d_add_one_div_four_of_dvd_q₁", "New.Parameters.chiK_eq_one_of_dvd", "New.Parameters.thirteen_le_of_chiK_ne_one", "New.Parameters.q₁_mul_d_dvd_q₂", "New.Parameters.coprime_q₁_d", "New.Parameters.d_pow_ne_neg_one"]
lean_files = ["src/New/Reduction/Data/FieldsAndPlaces.lean"]
+++

The **parameters** \(P=(q_0,d)\) of the proof are two natural numbers such that

1. \(18480=16\cdot3\cdot5\cdot7\cdot11\) divides \(q_0\);
2. \(d\) is a prime number;
3. \(q_0\mid 2(d+1)\) and \(q_0\nmid d+1\).

Condition (3) forces \(q_0\ne0\) and, \(q_0\) being even, is equivalent to \(d\equiv q_0/2-1\pmod{q_0}\). The parameters determine the [[algebra-fields-galois/imaginary-quadratic-field|imaginary quadratic field]] \(K=\mathbb Q(\sqrt{-d})\subset\mathbb C\) and the character \(\chi_K(n)=\bigl(\tfrac nd\bigr)\), the [[?c:Legendre symbol|Legendre symbol]] modulo \(d\).

For a natural number \(s\) (the *tower exponent*) define

\[
l_0(s)=3^{\lfloor\log_3s\rfloor+4},\qquad \operatorname{towerDeg}(s)=3^{\lfloor\log_3s\rfloor+5}\,2^{s}=3\,l_0(s)\,2^s,
\]
\[
q_1(s)=q_0\cdot\operatorname{towerDeg}(s),\qquad q_2(s)=(q_0d)^{s+6},
\]
with the convention \(\lfloor\log_3 0\rfloor=0\).

## Properties

1. \(27s<l_0(s)\) for all \(s\), and \(l_0(s)\le81s\) for \(s\ge1\); so for \(s\ge1\), \(l_0(s)\) is the least power of \(3\) above \(27s\).
2. \(d\equiv7\pmod 8\), and \(d>64\).
3. Every prime \(p\mid q_1(s)\) divides \(q_0\), divides \((d+1)/4\), and satisfies \(\chi_K(p)=1\) (it splits in \(K\)).
4. A prime \(p\) with \(\chi_K(p)\ne1\) is at least \(13\).
5. \(q_1(s)\,d\) divides \(q_2(s)\), and \(\gcd(q_1(s),d)=1\).
6. No power of \(d\) is \(\equiv-1\pmod{q_0}\).

## Proof

(1) With \(e=\lfloor\log_3s\rfloor\), \(s<3^{e+1}\) gives \(27s<3^{e+4}\); and \(3^e\le s\) for \(s\ge1\) gives \(3^{e+4}\le81s\).

(2) \(16\mid q_0\mid2(d+1)\) gives \(8\mid d+1\). Also \(2(d+1)\) is a positive multiple of \(q_0\ge18480\), so \(d\ge9239\).

(3) The primes dividing \(\operatorname{towerDeg}(s)\) are among \(2,3\), which divide \(q_0\); so \(p\mid q_0\mid2(d+1)=8\cdot\frac{d+1}4\). If \(p\mid8\) then \(p=2\), and \(\frac{d+1}4\) is even by (2); otherwise \(p\mid\frac{d+1}4\). Hence \(4p\mid d+1\), i.e. \(d\equiv4p-1\pmod{4p}\). The [[?c:Jacobi symbol|Jacobi symbol]] \(\bigl(\frac pd\bigr)\) depends on the odd number \(d\) only modulo \(4p\) (quadratic reciprocity), so \(\bigl(\frac pd\bigr)=\bigl(\frac p{4p-1}\bigr)=\bigl(\frac{4p}{4p-1}\bigr)=\bigl(\frac1{4p-1}\bigr)=1\), using that \(4\) is a square and \(4p\equiv1\pmod{4p-1}\).

(4) The primes below \(13\) divide \(18480\), hence \(q_0\) and \(q_1(0)\); apply (3).

(5) \(6\mid q_0d\), \(\lfloor\log_3s\rfloor\le s\), so \(3^{\lfloor\log_3s\rfloor+5}2^s\mid(3\cdot2)^{s+5}\mid(q_0d)^{s+5}\), and \(q_1(s)d=q_0d\cdot\operatorname{towerDeg}(s)\mid(q_0d)^{s+6}\). If the prime \(d\) divided \(q_1(s)\), (3) would give \(\chi_K(d)=1\), but \(\chi_K(d)=0\).

(6) In \(\mathbb Z/q_0\): \(2(d+1)=0\), \(d+1\ne0\), and \(d=2w+1\) is odd, so \(d^2-1=(d+1)\cdot2w=0\). Thus the powers of \(d\) are \(1\) and \(d\). \(d\ne-1\) by hypothesis; and \(1=-1\) would give \(2=0\), hence \(d+1=2(w+1)=0\).

## References

1. Lean: `New.Parameters`, `New.l₀`, `New.towerDeg`, `New.Parameters.q₁`, `New.Parameters.q₂`, `New.Parameters.K` and the lemmas listed in the front matter, in `src/New/Reduction/Data/FieldsAndPlaces.lean`. The exponent \(\varepsilon\) of the scales is not a parameter; it enters only [[proofs/grh/reduction-main/data-exist|the existence of the data]].

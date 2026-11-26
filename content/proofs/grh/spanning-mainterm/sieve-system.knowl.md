+++
id = "proofs/grh/spanning-mainterm/sieve-system"
title = "Sieve system"
kind = "definition"
summary = "A family of forms on pairs of heads over a ring with a measure, each the integral of the next over a common entry, with a positive top form and bounds for twisted integrals."
aliases = ["SieveSystem", "axioms of the sieve"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.SieveSystem", "New.SieveSystem.integrable_mul_update", "New.SieveSystem.integrable_update", "New.SieveSystem.integral_update", "New.SieveSystem.norm_integral_mul_update_le"]
lean_files = ["src/New/Spanning/MainTerm/SieveSystem.lean"]
+++

Let \(C\) be a [[algebra-rings/commutative-ring|commutative ring]] carrying a measure
(a [[measure-theory/measure-space|measure space]] structure, written \(dc\)), and let \(U\) be a
[[topology/topological-space|topological space]], the space of *entries*. A **head** is a
sequence \(p=(p_0,p_1,\dots)\) of entries; for a head \(p\), an index \(i\) and an entry \(t\)
write \(p[i\mapsto t]\) for the head that agrees with \(p\) except that its entry at position
\(i\) is \(t\).

Let there be given maps \(u\colon C\to U\) and \(\iota\colon U\to C\), a natural number \(n\),
functions \(J_i\colon U^{\mathbb N}\times U^{\mathbb N}\to\mathbb C\) (\(i\ge 0\), the *forms*),
a function \(\psi\colon C\to\mathbb C\), a real number \(B_0\), functions
\(\Lambda_i\colon U^{\mathbb N}\to\mathbb R\) (the *weights*) and a function
\(\beta\colon C\to\mathbb R\) (the *decay*). These data form a **sieve system of length \(n\)**
if the following six conditions hold.

1. \(\psi(0)=1\).
2. (**Recursion and decay.**) For every \(i\le n\), all heads \(p,q\) and every \(\xi\in C\),
   the function
   \[
     f_\xi(c)\;=\;\psi(\xi c)\,J_{i+1}\bigl(p[i\mapsto u(c)],\,q[i\mapsto u(c)]\bigr)
   \]
   is [[?c:Integrable function|integrable]] on \(C\); for \(\xi=0\) its integral is
   \(\int_C f_0(c)\,dc=J_i(p,q)\); and if \(\xi\) is a [[algebra-rings/unit|unit]] of \(C\), then
   \[
     \Bigl\lvert \int_C f_\xi(c)\,dc\Bigr\rvert\;\le\;\beta(\xi)\,\Lambda_i(p)\,\Lambda_i(q).
   \]
3. (**Positivity of the top form.**) For every finite family of heads \((a_j)_{j\in\kappa}\)
   that have one common entry at position \(n\), the matrix
   \(\bigl(J_{n+1}(a_j,a_l)\bigr)_{j,l\in\kappa}\) is
   [[linear-algebra/positive-semidefinite-matrix|positive semidefinite]] (hermitian with
   nonnegative quadratic form).
4. (**Continuity of the top form.**) \(J_{n+1}\) is continuous on
   \(U^{\mathbb N}\times U^{\mathbb N}\) with the product topology.
5. (**Mass.**) \(\lvert J_0(p,q)\rvert\le B_0\) for all heads \(p,q\).
6. (**Off-diagonal bound.**) For every \(i<n\) and all heads \(p,q\): if
   \(\xi=\iota(p_i)-\iota(q_i)\) is a unit of \(C\), then
   \[
     \lvert J_{i+1}(p,q)\rvert\;\le\;\beta(\xi)\,\Lambda_{i+1}(p)\,\Lambda_{i+1}(q).
   \]

## Immediate consequences

Taking \(\xi=0\) in condition 2 and using \(\psi(0)=1\): for \(i\le n\) the function
\(c\mapsto J_{i+1}(p[i\mapsto u(c)],q[i\mapsto u(c)])\) is integrable and

\[
  \int_C J_{i+1}\bigl(p[i\mapsto u(c)],q[i\mapsto u(c)]\bigr)\,dc \;=\; J_i(p,q).
\]

So each form but the top one is the integral of the next one over a common entry at the next
position, and \(J_0\) is the total *mass*.

## Remarks

- No relation between \(u\) and \(\iota\) is required. In the applications \(U\) is the group of
  units of \(C\), \(u\) sends a unit to itself and a non-unit to \(1\), and \(\iota\) is
  \(x\mapsto x^{-1}\), multiplied by a constant at the finite places.
- The function \(\psi\) is an additive character in the applications, but only \(\psi(0)=1\) is
  required.
- \(C\) is a place or a product of places:
  [[proofs/grh/spanning-mainterm/product-of-sieve-systems|sieve systems multiply]].

## References

1. Lean: `New.SieveSystem` and the lemmas `integrable_mul_update`, `integrable_update`,
   `integral_update`, `norm_integral_mul_update_le` in
   `src/New/Spanning/MainTerm/SieveSystem.lean`.

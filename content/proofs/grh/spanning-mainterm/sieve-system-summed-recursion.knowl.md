+++
id = "proofs/grh/spanning-mainterm/sieve-system-summed-recursion"
title = "The recursion of a sieve system summed over pairs of heads"
kind = "lemma"
summary = "The sum of the forms J(i+1) over all pairs from a finite family of heads with a common entry is integrable in that entry, integrates to the sum of the forms J(i), and has twisted integrals bounded by the decay times the squared sum of the weights."
aliases = ["SieveSystem.integrable_and_integral_sum_update"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.SieveSystem.integrable_and_integral_sum_update", "New.SieveSystem.integrable_sum_update", "New.SieveSystem.integral_sum_update", "New.SieveSystem.norm_integral_mul_sum_update_le"]
lean_files = ["src/New/Spanning/MainTerm/SieveSystem.lean"]
proof_status = "full"
+++

**Lemma.** Let \((u,\iota,n,J,\psi,B_0,\Lambda,\beta)\) be a
[[proofs/grh/spanning-mainterm/sieve-system|sieve system]] on \(C\), let \(i\le n\), and let
\((a_p)_{p\in\tau}\) be a finite family of heads. Put

\[
  F(c)\;=\;\sum_{p\in\tau}\sum_{q\in\tau}J_{i+1}\bigl(a_p[i\mapsto u(c)],\,a_q[i\mapsto u(c)]\bigr)\qquad(c\in C).
\]

Then:

1. \(F\) is integrable on \(C\);
2. \(\displaystyle\int_CF(c)\,dc=\sum_{p,q\in\tau}J_i(a_p,a_q)\);
3. for every unit \(\xi\) of \(C\),
   \(\displaystyle\Bigl\lvert\int_C\psi(\xi c)F(c)\,dc\Bigr\rvert\le\beta(\xi)\Bigl(\sum_{p\in\tau}\Lambda_i(a_p)\Bigr)^{2}\).

## Proof

By axiom 2 of a sieve system each summand of \(\psi(\xi c)F(c)\) is integrable in \(c\) for every
\(\xi\), in particular for \(\xi=0\), where \(\psi(0)=1\); a finite sum of integrable functions
is integrable, which gives 1. Integrating term by term and using the recursion
\(\int_CJ_{i+1}(a_p[i\mapsto u(c)],a_q[i\mapsto u(c)])\,dc=J_i(a_p,a_q)\) gives 2. For a unit
\(\xi\), integrating term by term and applying the decay bound of axiom 2 to each pair,

\[
  \Bigl\lvert\int_C\psi(\xi c)F(c)\,dc\Bigr\rvert
  \le\sum_{p,q}\beta(\xi)\Lambda_i(a_p)\Lambda_i(a_q)
  =\beta(\xi)\Bigl(\sum_p\Lambda_i(a_p)\Bigr)^2 . \qquad\blacksquare
\]

## References

1. Lean: `New.SieveSystem.integrable_sum_update`, `New.SieveSystem.integral_sum_update`,
   `New.SieveSystem.norm_integral_mul_sum_update_le`, collected in
   `New.SieveSystem.integrable_and_integral_sum_update`, in
   `src/New/Spanning/MainTerm/SieveSystem.lean`.

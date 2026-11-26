+++
id = "proofs/grh/spanning-mainterm/sieve-system-sum-nonneg-and-lower-semicontinuous"
title = "Sums of a sieve system over heads with a common entry are nonnegative and lower semicontinuous"
kind = "lemma"
summary = "In a sieve system, the sum of J(i+1) over all pairs from finitely many heads with a common entry at position i is a nonnegative real number, lower semicontinuous in a parameter wherever the heads are continuous."
aliases = ["SieveSystem.sum_nonneg", "SieveSystem.lowerSemicontinuousAt_sum", "SieveSystem.sum_nonneg_and_lowerSemicontinuousAt"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.SieveSystem.sum_nonneg", "New.SieveSystem.lowerSemicontinuousAt_sum", "New.SieveSystem.sum_nonneg_and_lowerSemicontinuousAt"]
lean_files = ["src/New/Spanning/MainTerm/SieveSystem.lean"]
proof_status = "full"
+++

**Lemma.** Let \((u,\iota,n,J,\psi,B_0,\Lambda,\beta)\) be a
[[proofs/grh/spanning-mainterm/sieve-system|sieve system]] on \(C\) with entries in \(U\), and
let \(i\le n\).

1. (**Nonnegativity.**) If \((a_p)_{p\in\tau}\) is a finite family of heads that all have the
   same entry at position \(i\), then
   \[
     \sum_{p\in\tau}\sum_{q\in\tau}J_{i+1}(a_p,a_q)
   \]
   is a real number \(\ge0\).
2. (**Lower semicontinuity.**) Suppose moreover that \(C\) carries a
   [[?c:First-countable space|first-countable]] topology. Let \(b_y=(b_{y,p})_{p\in\tau}\) be
   finite families of heads depending on \(y\in C\) such that for each \(y\) all the heads
   \(b_{y,p}\) have the same entry at position \(i\). Put
   \(F(y)=\sum_{p,q}J_{i+1}(b_{y,p},b_{y,q})\ge0\). If \(x\in C\) is a point at which every map
   \(y\mapsto b_{y,p}\) (into \(U^{\mathbb N}\) with the product topology) is continuous, then
   \(F\) is [[?c:Lower semicontinuous function|lower semicontinuous]] at \(x\).

In the Lean source, statement 2 is formulated for the function \(y\mapsto\operatorname{Re}F(y)\)
regarded as a function with values in \([0,\infty]\); by statement 1 this is the same function.

## Proof

Both statements are proved by descending induction on \(i\), from \(i=n\) down.

**1.** For \(i=n\): the heads have a common entry at position \(n\), so by axiom 3 the matrix
\(A=(J_{n+1}(a_p,a_q))_{p,q}\) is positive semidefinite, and the sum is the value
\(\mathbf 1^{*}A\,\mathbf 1\ge0\) of its quadratic form at the vector \(\mathbf 1=(1,\dots,1)\).

For \(i<n\), assuming the statement for \(i+1\): by the
[[proofs/grh/spanning-mainterm/sieve-system-summed-recursion|summed recursion]] at position
\(i+1\le n\),
\[
  \sum_{p,q}J_{i+1}(a_p,a_q)=\int_C\sum_{p,q}J_{i+2}\bigl(a_p[i+1\mapsto u(z)],a_q[i+1\mapsto u(z)]\bigr)\,dz .
\]
For each \(z\) the heads \(a_p[i+1\mapsto u(z)]\) have the common entry \(u(z)\) at position
\(i+1\), so the integrand is \(\ge0\) by the induction hypothesis, and so is its integral. (The
hypothesis that the \(a_p\) have a common entry at position \(i\) is not used in this step: it
is needed only at the top.)

**2.** For \(i=n\): \(J_{n+1}\) is continuous (axiom 4) and the maps \(y\mapsto b_{y,p}\) are
continuous at \(x\), so \(F\) is continuous at \(x\), hence lower semicontinuous there.

For \(i<n\), assuming the statement for \(i+1\): put
\[
  G(y,z)=\sum_{p,q}J_{i+2}\bigl(b_{y,p}[i+1\mapsto u(z)],b_{y,q}[i+1\mapsto u(z)]\bigr).
\]
By 1, \(G(y,z)\ge0\); by the summed recursion, \(G(y,\cdot)\) is integrable and
\(F(y)=\int_CG(y,z)\,dz\). For fixed \(z\), the heads \(b_{y,p}[i+1\mapsto u(z)]\) have the
common entry \(u(z)\) at position \(i+1\) and depend continuously on \(y\) at \(x\), so by the
induction hypothesis \(y\mapsto G(y,z)\) is lower semicontinuous at \(x\), that is
\(G(x,z)\le\liminf_{y\to x}G(y,z)\). Therefore, by
[[measure-theory/fatous-lemma|Fatou's lemma]] (in its form for a
[[?c:Limit inferior|limit inferior]] along the neighbourhood filter of \(x\), which is countably
generated because \(C\) is first-countable),
\[
  F(x)=\int_CG(x,z)\,dz\le\int_C\liminf_{y\to x}G(y,z)\,dz\le\liminf_{y\to x}\int_CG(y,z)\,dz=\liminf_{y\to x}F(y),
\]
which is lower semicontinuity of \(F\) at \(x\). \(\blacksquare\)

## References

1. Lean: `New.SieveSystem.sum_nonneg`, `New.SieveSystem.lowerSemicontinuousAt_sum`, collected in
   `New.SieveSystem.sum_nonneg_and_lowerSemicontinuousAt`, in
   `src/New/Spanning/MainTerm/SieveSystem.lean`.

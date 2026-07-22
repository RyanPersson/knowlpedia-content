Let \(K\) be a division ring and \(G\) a group. The group algebra \(K[G]\) consists of finite formal sums
\[
a=\sum_{g\in G}a_g g,
\]
with coefficients \(a_g\in K\). Addition is coefficientwise, and multiplication extends the group law bilinearly:
\[
\left(\sum_g a_g g\right)\left(\sum_h b_h h\right)
=\sum_{g,h}a_gb_h(gh).
\]

A nonzero element \(a\) of a ring is a zero divisor if there is a nonzero \(b\) with \(ab=0\) or \(ba=0\). A group is torsion-free when \(g^n=e\), for an integer \(n\ge1\), implies \(g=e\).

## Conjecture

If \(K\) is a division ring and \(G\) is torsion-free, then the group algebra \(K[G]\) has no nonzero zero divisors. Equivalently,
\[
ab=0\quad\Longrightarrow\quad a=0\ \text{or}\ b=0
\]
for all \(a,b\in K[G]\).

The torsion-free hypothesis is necessary: if \(g\ne e\) has finite order \(n\), then
\[
(1-g)(1+g+\cdots+g^{n-1})=0,
\]
which visibly produces zero divisors when the two factors are nonzero.

## Known boundary

The conjecture is known for substantial classes of torsion-free groups, including orderable groups, but remains open in general. It is closely related to other conjectures about units and idempotents in group rings.

## Formal source

This page follows `FormalConjectures/Wikipedia/Kaplansky.lean`, which states the result for a division ring of coefficients and a torsion-free group.

+++
id = "algebra-commutative/i-adic-topology"
title = "\\(I\\)-adic topology"
kind = "definition"
summary = "The linear topology on a ring or module whose neighborhoods of zero are the powers of an ideal."
aliases = ["adic topology", "I-adic topology", "ideal-adic topology"]
domains = ["algebra-commutative", "algebra-rings"]
section_mode = "progressive"
+++

Let \(A\) be a [[algebra-rings/commutative-ring|commutative ring]] and
\(I\subseteq A\) an [[algebra-rings/ideal|ideal]]. The **\(I\)-adic topology**
on \(A\) is the ring topology for which
\[
A\supseteq I\supseteq I^2\supseteq\cdots
\]
is a neighborhood basis of \(0\). Thus a sequence \(a_j\) converges to \(0\)
exactly when, for every \(N\), it eventually lies in \(I^N\).

For an \(A\)-module \(M\), the \(I\)-adic topology similarly has
\(\{I^NM\}_{N\geq0}\) as a neighborhood basis of \(0\).

## Separation and completion

The topology on \(A\) is separated (Hausdorff) precisely when
\[
\bigcap_{N\geq0}I^N=0.
\]
Separatedness does not by itself mean that every Cauchy system has a limit.
The [[algebra-commutative/i-adic-completion|\(I\)-adic completion]]
\(\widehat A=\varprojlim A/I^N\) measures and remedies that second issue,
subject to a general-ring subtlety about which topology is placed on the
completion.

## Continuous maps

If \(B\) has its \(J\)-adic topology, a [[algebra-rings/ring-homomorphism|ring homomorphism]]
\(\varphi:A\to B\) is continuous exactly when, for every \(m\), there is an
\(n\) such that
\[
\varphi(I^n)\subseteq J^m.
\]
The common sufficient condition \(\varphi(I)\subseteq J\) makes this immediate.
Continuity is the condition needed for homomorphisms between formal power
series rings and formal spectra.

## Examples

- The \(0\)-adic topology is discrete.
- The \(x\)-adic topology on
  [[algebra-rings/formal-power-series-ring|\(R[[x]]\)]] records agreement to
  increasing order in \(x\).
- For \(A=\mathbb Z\) and \(I=(p)\), completion produces the ring of
  [[shared-foundations/p-adic-integers|\(p\)-adic integers]].

## References

1. The Stacks Project Authors, “Topological rings and modules.” [Section 15.37, Tag 07E7](https://stacks.math.columbia.edu/tag/07E7). Relevant: Definition 15.37.1 and the discussion of \(I\)-adic topologies.
2. Hideyuki Matsumura, *Commutative Ring Theory*, Cambridge University Press, 1986. Relevant: Section 8, completions.

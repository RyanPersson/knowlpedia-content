+++
id = "operator-algebras/lower-semicontinuous-trace"
title = "Lower semicontinuous trace"
kind = "definition"
summary = "An extended-valued tracial weight on a C-star algebra that is lower semicontinuous in the norm topology."
aliases = ["lower-semicontinuous C-star trace", "lsc C-star trace"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. A
**lower semicontinuous trace** is a map
\(\tau:A_+\to[0,+\infty]\) that is additive, positively homogeneous, and
satisfies
\[
\tau(x^*x)=\tau(xx^*)\qquad(x\in A),
\]
and whose sublevel sets
\(\{a\in A_+:\tau(a)\leq c\}\) are norm closed for every \(c\geq0\).
Equivalently, \(a_n\to a\) in norm with \(a_n,a\geq0\) implies
\(\tau(a)\leq\liminf_n\tau(a_n)\). Values of \(+\infty\) are allowed.
Neither dense definition, semifiniteness, faithfulness, nor boundedness is
part of the term unless explicitly added.

## Equivalent approximation formula

For \(a\in A_+\), lower semicontinuity is equivalent to
\[
\tau(a)=\sup_{\varepsilon>0}\tau\bigl((a-\varepsilon)_+\bigr),
\]
where \((a-\varepsilon)_+\) is obtained by
[[operator-algebras/continuous-functional-calculus|continuous functional calculus]]. This formula is especially useful in nonunital algebras and in
comparison theory. The tracial identity also implies invariance under unitary
conjugation in the [[operator-algebras/unitization|unitization]].

## Domains and extra adjectives

The finite positive domain is
\[
\mathfrak m_\tau^+=\{a\in A_+:\tau(a)<\infty\}.
\]
The trace is **densely defined** when this cone is norm dense in \(A_+\).
Semifiniteness is an order-density requirement and is a separate condition;
compare [[operator-algebras/semifinite-weight|semifinite weights]]. A bounded
[[operator-algebras/trace-cstar-algebra|trace on a \(C^*\)-algebra]] is finite
everywhere and automatically lower semicontinuous, but lower semicontinuous
traces need not be bounded.

## Examples

The canonical [[operator-algebras/operator-trace|operator trace]] on
\(K(H)_+\), allowed to take \(+\infty\), is a densely defined lower
semicontinuous trace: finite-rank positive operators lie in its finite domain
and are norm dense in \(K(H)_+\). On \(C_0(X)\), integration
\[
\tau(f)=\int_X f\,d\mu
\]
against a positive Radon measure gives an extended lower semicontinuous trace.
Commutativity makes the tracial identity automatic.

**Warning.** A lower semicontinuous \(2\)-quasitrace is not a trace by
definition: additivity on arbitrary positive pairs is the potentially missing
axiom.

## References

1. Gert K. Pedersen, \(C^*\)-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [Publisher record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §§5.2 and 5.6 on lower-semicontinuous weights, traces, and their finite ideals.
2. Leonel Robert, “On the Comparison of Positive Elements of a \(C^*\)-Algebra by Lower Semicontinuous Traces,” 2008. [arXiv record](https://arxiv.org/abs/0806.1570). Relevant: Introduction for the extended trace convention and §2 for lower-semicontinuous trace comparison.

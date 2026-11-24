+++
id = "arithmetic-geometry/iterated-theta-lifts"
title = "Iterated global theta lifts"
kind = "construction"
summary = "A succession of global theta lifts in which the output on each group supplies the input on the next dual pair."
aliases = ["chain of theta lifts", "iterated theta lift"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/theta-lift", "langlands/automorphic-form"]
+++

An **iterated global theta lift** applies a sequence of [[arithmetic-geometry/theta-lift|global theta lifts]] to an [[langlands/automorphic-form|automorphic form]]. Choose groups \(G_0,\ldots,G_m\) such that each adjacent pair admits the theta correspondence, together with a theta kernel for each pair. Starting with \(f_0\) on \(G_0\), set \(f_j=\Theta_j(f_{j-1})\) on \(G_j\) whenever the defining pairing exists. The integer \(m\) counts the lifts.

## Two successive lifts

For three compatible unitary groups \(G_0,G_1,G_2\), the first integral pairs \(f_0\) with a kernel on \(G_0\times G_1\), leaving a form \(f_1\) on \(G_1\). The second pairs \(f_1\) with a kernel on \(G_1\times G_2\). If \(f_1\) vanishes, the second lift is zero as well. Even when \(f_1\ne0\), convergence of the second pairing and nonvanishing of its output require hypotheses.

## References

- Wee Teck Gan, [Automorphic forms and the theta correspondence, §§3.6–3.9, global theta lifting and nonvanishing](https://swc-math.github.io/aws/2022/2022GanNotes.pdf).

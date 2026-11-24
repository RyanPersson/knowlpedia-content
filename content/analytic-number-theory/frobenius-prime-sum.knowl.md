+++
id = "analytic-number-theory/frobenius-prime-sum"
title = "Character decomposition of a Frobenius prime sum"
kind = "identity"
summary = "Finite Fourier inversion expresses a sum over selected Frobenius elements as a linear combination of character-weighted prime sums."
aliases = ["Frobenius indicator expansion"]
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/finite-fourier-inversion", "analytic-number-theory/galois-character", "algebra-fields-galois/frobenius-unramified"]
+++

Let \(E/\mathbb Q\) be a finite abelian extension with Galois group \(G\). For each prime \(p\) in a finite set \(S\) of unramified primes, choose a weight \(b_p\) and write \(g_p\) for its [[algebra-fields-galois/frobenius-unramified|Frobenius element]]. Given \(C\subseteq G\), [[analytic-number-theory/finite-fourier-inversion|finite Fourier inversion]] of its indicator gives
\[
\sum_{\substack{p\in S\\g_p\in C}}b_p
=\sum_{\chi\in\widehat G}
\widehat{\mathbf 1_C}(\chi)\sum_{p\in S}b_p\,\chi(g_p),
\qquad
\widehat{\mathbf 1_C}(\chi)=\frac{1}{|G|}\sum_{g\in C}\overline{\chi(g)}.
\]
The outer sum runs over the [[analytic-number-theory/galois-character|characters of \(G\)]]. The identity selects precisely the primes whose Frobenius lies in \(C\).

## Inert primes in a quadratic field

In a quadratic field the nontrivial character takes value \(1\) at split primes and \(-1\) at [[arithmetic-geometry/inert-prime|inert primes]]. The inert-prime indicator is therefore \((1-\chi(g_p))/2\). For \(E=\mathbb Q(i)\) and \(S=\{3,5,7\}\), this formula retains \(b_3+b_7\) and cancels \(b_5\).

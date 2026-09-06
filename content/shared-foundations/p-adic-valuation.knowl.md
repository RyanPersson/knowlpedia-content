+++
id = "shared-foundations/p-adic-valuation"
title = "p-adic valuation"
kind = "knowl"
summary = "The exponent of a prime in an integer, extended to a valuation on rational numbers."
aliases = ["p-adic valuation", "prime-adic valuation"]
domains = ["shared-foundations", "algebra-fields-galois"]
prerequisites = ["shared-foundations/rational-numbers"]
dependency_review_count = 1
+++

Fix a prime \(p\). For a nonzero integer \(m\), the **\(p\)-adic valuation** \(v_p(m)\) is the unique nonnegative integer \(r\) such that \(p^r\mid m\) but \(p^{r+1}\nmid m\). Set \(v_p(0)=+\infty\), and extend to nonzero [[shared-foundations/rational-numbers|rational numbers]] by
\[
v_p(a/b)=v_p(a)-v_p(b).
\]

It satisfies \(v_p(xy)=v_p(x)+v_p(y)\) and \(v_p(x+y)\ge\min\{v_p(x),v_p(y)\}\). The associated absolute value is \(|0|_p=0\) and \(|x|_p=p^{-v_p(x)}\) for \(x\ne0\); it defines the \(p\)-adic topology on \(\mathbb Q\).

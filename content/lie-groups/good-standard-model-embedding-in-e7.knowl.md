+++
id = "lie-groups/good-standard-model-embedding-in-e7"
title = "Good Standard Model embedding in e7"
kind = "definition"
summary = "The distinguished automorphism class of regular embeddings of the complexified Standard Model Lie algebra in e7 used in the three-generation construction."
aliases = ["good embedding of the Standard Model Lie algebra in e7", "good gSM subalgebra of e7"]
domains = ["lie-groups", "mathematical-physics"]
section_mode = "progressive"
+++

Let
\[
\mathfrak g_{\mathrm{SM}}\cong
\mathfrak{sl}_3(\mathbb C)\oplus\mathfrak{sl}_2(\mathbb C)\oplus\mathbb C
\]
be the [[mathematical-physics/standard-model-lie-algebra|complexified Standard Model Lie algebra]]. A **good Standard Model embedding in \(\mathfrak e_7\)** is an embedding
\(\iota:\mathfrak g_{\mathrm{SM}}\hookrightarrow\mathfrak e_7\) carried by an automorphism of [[lie-groups/exceptional-lie-algebra-e7|\(\mathfrak e_7\)]] to the [[lie-groups/regular-lie-subalgebra|regular]] embedding obtained by
[[lie-groups/removing-a-simple-root|successively removing simple roots]] down the exceptional chain and then taking the relevant [[lie-groups/maximal-levi-subalgebra|maximal Levi subalgebra]] of \(\mathfrak{sl}_5\).

Thus “good” specifies an automorphism class of embeddings, not merely an abstract subalgebra isomorphic to \(\mathfrak g_{\mathrm{SM}}\).

## Equivalent construction through SU(5)

Start with the block-diagonal [[mathematical-physics/georgi-glashow-su5-embedding|Standard Model embedding in \(SU(5)\)]], pass to complex [[lie-groups/lie-algebra|Lie algebras]]
\[
\mathfrak g_{\mathrm{SM}}\subset\mathfrak{sl}_5(\mathbb C),
\]
and embed \(\mathfrak{sl}_5\) as a regular \(A_4\)-subalgebra of \(\mathfrak e_7\). All \(A_4\) [[lie-groups/root-subsystem|root subsystems]] of \(E_7\) lie in one Weyl-group orbit, so this gives the same automorphism class.

## Why the qualification matters

An abstract inclusion of a copy of \(\mathfrak{sl}_3\oplus\mathfrak{sl}_2\oplus\mathbb C\) in \(\mathfrak e_7\) need not have the centralizers and [[lie-groups/branching-rule-for-lie-representations|branching rules]] used in the three-generation construction. The adjective “good” records the regular-position hypothesis from which the [[lie-groups/generation-sl3-in-e7|generation \(\mathfrak{sl}_3\)]], [[lie-groups/standard-sl6-in-e7|standard \(\mathfrak{sl}_6\)]], and subsequent decompositions follow.

## Dependence on choices

The definition is invariant under automorphisms of \(\mathfrak e_7\). Choosing a particular representative embedding is still necessary to regard the constructed algebras as literal subalgebras rather than only as conjugacy classes. Later choices of [[lie-groups/cartan-subalgebra|Cartan subalgebra]] and roots are additional and are not part of “goodness.”

## References

1. John C. Baez, “Three Generations in E7,” 2026, §2. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
2. Toshio Oshima, “A Classification of Subsystems of a Root System,” 2006, especially the tables of subsystem orbits. [arXiv:math/0611904](https://arxiv.org/abs/math/0611904).
3. E. B. Dynkin, “Semisimple Subalgebras of Semisimple Lie Algebras,” *American Mathematical Society Translations*, Series 2, 6 (1957), 111–244.

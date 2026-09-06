+++
id = "operator-algebras/group-cstar-algebra-discrete-group"
title = "Group C*-algebras of a discrete group"
kind = "definition"
summary = "The full and reduced C*-completions of the complex group algebra of a discrete group."
aliases = ["discrete group C*-algebra", "C*(Gamma)", "C_r*(Gamma)"]
domains = ["operator-algebras", "algebra-representation-theory"]
prerequisites = ["algebra-representation-theory/group-algebra", "real-analysis/supremum-norm"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\Gamma\) be a discrete group and
\(\mathbb C[\Gamma]\) its
[[algebra-representation-theory/group-algebra|complex group algebra]], with
\(\delta_g^*=\delta_{g^{-1}}\). Its **full group \(C^*\)-algebra**
\(C^*(\Gamma)\) is the completion in the [[real-analysis/supremum-norm|supremum norm]] over all unitary
representations of \(\Gamma\). Its **reduced group \(C^*\)-algebra**
\(C_r^*(\Gamma)\) is the completion in the norm induced by the left regular
representation on \(\ell^2(\Gamma)\). The phrase “group
\(C^*\)-algebra” is therefore ambiguous unless the full or reduced
completion is specified.

## Concrete construction

For a finitely supported function \(f:\Gamma\to\mathbb C\), write
\(f=\sum_g f(g)\delta_g\). The left [[algebra-representation-theory/regular-representation|regular representation]] acts by
\[
\lambda(f)\xi(s)=\sum_{g\in\Gamma}f(g)\xi(g^{-1}s).
\]
Completing \(\lambda(\mathbb C[\Gamma])\) in [[linear-algebra/operator-norm|operator norm]] gives
[[operator-algebras/reduced-group-cstar-algebra|\(C_r^*(\Gamma)\)]]. Taking
the supremum over the integrated forms of all unitary representations gives
[[operator-algebras/full-group-cstar-algebra|\(C^*(\Gamma)\)]].

## Comparison of the completions

Because the regular representation is among the representations used in the
full norm, the identity on \(\mathbb C[\Gamma]\) extends to a canonical
surjective \(*\)-homomorphism
\[
C^*(\Gamma)\longrightarrow C_r^*(\Gamma).
\]
It is an isomorphism exactly when \(\Gamma\) is
[[harmonic-analysis/amenable-locally-compact-group|amenable]]. Hence the two
constructions agree for finite, abelian, and more generally amenable discrete
groups, but not for [[algebra-groups/free-group|free groups]] on at least two generators.

## Examples and conventions

For \(\Gamma=\mathbb Z\), Fourier transform identifies both completions with
\(C(\mathbb T)\). For a finite group, the group \(C^*\)-algebra is a
finite-dimensional direct sum of matrix algebras determined by the
[[algebra-representation-theory/irreducible-representation|irreducible representations]]. Both completions are unital for every discrete
group, with unit \(\delta_e\). The notation \(C^*(\Gamma)\) conventionally
means the full completion, whereas \(C_r^*(\Gamma)\) always means the reduced
one.

## References

1. Nathanial P. Brown and Narutaka Ozawa, \(C^*\)-Algebras and Finite-Dimensional Approximations, American Mathematical Society, 2008. [AMS DOI record](https://doi.org/10.1090/gsm/088). Relevant: §§2.5–2.6 on discrete group \(C^*\)-algebras and amenability.
2. Kenneth R. Davidson, \(C^*\)-Algebras by Example, American Mathematical Society, 1996. [AMS DOI record](https://doi.org/10.1090/fim/006). Relevant: examples of full and reduced group \(C^*\)-algebras.

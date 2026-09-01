+++
id = "operator-algebras/extension-to-multiplier-algebras"
title = "Extension of a nondegenerate homomorphism to multiplier algebras"
kind = "theorem"
summary = "A nondegenerate homomorphism between C*-algebras extends uniquely to a unital strictly continuous homomorphism of their multiplier algebras."
aliases = ["strict extension theorem", "multiplier extension theorem"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/nondegenerate-star-homomorphism", "operator-algebras/multiplier-algebra", "operator-algebras/strict-topology"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(A\) and \(B\) be
[[operator-algebras/cstar-algebra|\(C^*\)-algebras]]. Every
[[operator-algebras/nondegenerate-star-homomorphism|nondegenerate
\(*\)-homomorphism]] \(\varphi:A\to M(B)\) into the
[[operator-algebras/multiplier-algebra|multiplier algebra]] of \(B\) has a
unique unital
\(*\)-homomorphism
\[
\overline{\varphi}:M(A)\longrightarrow M(B)
\]
whose restriction to \(A\subseteq M(A)\) is \(\varphi\). The extension is
continuous from the [[operator-algebras/strict-topology|strict topology]] on
\(M(A)\) to the strict topology on \(M(B)\). It is characterized by
\[
\overline{\varphi}(m)\varphi(a)b=\varphi(ma)b
\]
for \(m\in M(A)\), \(a\in A\), and \(b\in B\). Thus nondegeneracy is precisely
the hypothesis that makes the extension canonical and unital.

## Construction and uniqueness

The dense subspace \(\operatorname{span}\varphi(A)B\) of \(B\) determines the
left action of a multiplier \(m\) by
\[
\overline{\varphi}(m)\bigl(\varphi(a)b\bigr)=\varphi(ma)b.
\]
The corresponding right-multiplier relation makes this formula independent of
the chosen expression and yields an element of
[[operator-algebras/multiplier-algebra|\(M(B)\)]]. Density gives uniqueness.
Equivalently, for any
[[operator-algebras/approximate-identity|approximate identity]] \((e_i)\) of
\(A\),
\[
\overline{\varphi}(m)=\operatorname*{strict\,lim}_i\varphi(me_i).
\]

## Functorial consequences

If \(\psi:B\to M(C)\) is nondegenerate, the composite used in the
nonunital category is \(\overline{\psi}\circ\varphi:A\to M(C)\), and its
multiplier extension is
\(\overline{\psi}\circ\overline{\varphi}\). A [[operator-algebras/nondegenerate-star-homomorphism|nondegenerate representation]]
\(\pi:A\to B(H)=M(\mathcal K(H))\) therefore extends uniquely to \(M(A)\).
These formulas are fundamental in covariant representations and crossed
products.

## Scope and near-miss

**Warning.** Nondegeneracy cannot simply be omitted. If \(A\) is unital and
\(\varphi(1_A)\ne1_{M(B)}\), any extension agreeing with \(\varphi\) remains
nonunital; the theorem's unital conclusion fails. Also, strict continuity is
the natural conclusion: norm continuity alone neither describes strict limits
of approximate identities nor determines their multiplier unit.

## References

1. E. Christopher Lance, *Hilbert C*-Modules: A Toolkit for Operator Algebraists*, Cambridge University Press, 1995. [DOI record](https://doi.org/10.1017/CBO9780511526206). Relevant: Proposition 2.1 on extension of nondegenerate homomorphisms.
2. Dana P. Williams, *Crossed Products of C*-Algebras*, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: Appendix A on multiplier algebras and nondegenerate homomorphisms.

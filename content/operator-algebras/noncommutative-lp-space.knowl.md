+++
id = "operator-algebras/noncommutative-lp-space"
title = "Noncommutative L^p space"
kind = "definition"
summary = "Haagerup's weight-independent Lp space constructed from homogeneous measurable operators in a crossed product."
aliases = ["Lp space of a von Neumann algebra", "Haagerup Lp space"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/normal-semifinite-faithful-weight", "operator-algebras/continuous-core-von-neumann-algebra", "operator-algebras/von-neumann-crossed-product", "operator-algebras/modular-automorphism-group", "operator-algebras/dual-action-von-neumann-crossed-product", "operator-algebras/tau-measurable-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]],
choose a [[operator-algebras/normal-semifinite-faithful-weight|normal semifinite faithful weight]] \(\varphi\), and form the
[[operator-algebras/continuous-core-von-neumann-algebra|continuous core]]
\(N=M\rtimes_{\sigma^\varphi}\mathbb R\), a
[[operator-algebras/von-neumann-crossed-product|von Neumann crossed product]],
by its
[[operator-algebras/modular-automorphism-group|modular automorphism group]].
Write \(\theta\) for the
[[operator-algebras/dual-action-von-neumann-crossed-product|dual action]] and
\(\tau\) for the canonical trace on \(N\). For \(0<p<\infty\), the
**Haagerup noncommutative \(L^p\) space** is
\[
L^p(M)=\{x:x\text{ is }\tau\text{-measurable and affiliated with }N,\quad
\theta_s(x)=e^{-s/p}x\text{ for every }s\in\mathbb R\}.
\]
One sets \(L^\infty(M)=M\). Different choices of \(\varphi\) give canonically
isometric spaces. The homogeneity condition selects exactly the operators of
integrability degree \(p\) inside the measurable crossed-product algebra.
Here [[operator-algebras/tau-measurable-operator|\(\tau\)-measurability]] is
computed in the crossed product \(N\).

## Independence and basic structure

The crossed product and trace depend on the auxiliary weight, but the
homogeneous subspaces do not, up to their canonical identifications. For
\(1\leq p\leq\infty\), \(L^p(M)\) is a [[linear-algebra/banach-space|Banach space]]; \(L^1(M)\) identifies
isometrically with the predual \(M_*\), and \(L^2(M)\) gives the standard-form
[[linear-algebra/hilbert-space|Hilbert space]] of \(M\). Multiplication of affiliated operators yields Hölder
maps \(L^p(M)L^q(M)\subseteq L^r(M)\) when
\(1/r=1/p+1/q\).

## Relation to familiar \(L^p\) spaces

If \(M\) is commutative, the construction recovers classical \(L^p\) of the
corresponding measure class. If \(M\) is semifinite with a faithful normal
semifinite
[[operator-algebras/faithful-normal-semifinite-trace|trace]], it is canonically
isometric to the
[[operator-algebras/tracial-noncommutative-lp-space|tracial noncommutative \(L^p\) space]]. Thus Haagerup's construction extends the tracial theory rather
than replacing its formulas in the semifinite case. It remains available for
type III algebras, where no faithful normal semifinite trace exists on \(M\)
itself.

## Conventions and scope

**Warning.** “Noncommutative \(L^p\) space” can refer to several equivalent
models, including Haagerup, spatial-derivative, and interpolation
constructions. This knowl uses the Haagerup crossed-product model. The
homogeneity exponent and the scaling rule for the canonical trace both change
sign if the opposite convention for the dual action is adopted; the paired
choices describe the same space. The operators defining \(L^p(M)\) are
[[operator-algebras/affiliated-operator|affiliated]] with the crossed product
\(N\), not generally with \(M\).

## References

1. Uffe Haagerup, “\(L^p\)-Spaces Associated with an Arbitrary von Neumann Algebra,” in *Algèbres d’opérateurs et leurs applications en physique mathématique*, Colloques Internationaux du CNRS 274, CNRS, 1979, 175–184. [Institutional scan](https://math.berkeley.edu/~pavlov/scans/haagerup.pdf). Relevant: the crossed-product construction, weight independence, and identifications at \(p=1,2,\infty\).
2. Marianne Terp, *\(L^p\) Spaces Associated with von Neumann Algebras*, Notes, Mathematical Institute, Copenhagen University, 1981. [Institutional scan](https://www.fuw.edu.pl/~kostecki/scans/terp1981.pdf). Relevant: Chapters I–II on tracial measurable operators and the Haagerup construction.

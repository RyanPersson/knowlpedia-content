+++
id = "noncommutative-geometry/entire-cyclic-cohomology"
title = "Entire cyclic cohomology"
kind = "definition"
summary = "A Z/2-graded cyclic cohomology of Banach algebras whose infinite cochain sequences satisfy a factorial analytic-growth condition."
aliases = ["entire (b,B)-cohomology", "HE cohomology"]
domains = ["noncommutative-geometry", "operator-algebras", "algebra-homological"]
section_mode = "progressive"
+++

Let \(A\) be a unital [[functional-analysis/banach-algebra|Banach algebra]], and let \(C^n_{\mathrm{cont}}(A)\) be its continuous \((n+1)\)-linear cochains. An even cochain sequence \(\phi=(\phi_{2k})_{k\geq0}\) is **entire** when
\[
\sum_{k\geq0}\frac{\|\phi_{2k}\|}{k!}z^k
\]
has infinite radius of convergence; here the cochain norm is the supremum on the product of unit balls. The odd condition uses \(\phi_{2k+1}\) similarly. These sequences form a \(\mathbb Z/2\)-graded complex under \(b+B\). Its cohomology is the **entire cyclic cohomology** \(HE^0(A)\oplus HE^1(A)\).

## Why this is a distinct completion

The factorial condition allows infinitely many nonzero cochain components while controlling their analytic growth. By contrast, [[noncommutative-geometry/periodic-cyclic-cohomology|periodic cyclic cohomology]] is represented by the direct-sum totalization of the periodic \((b,B)\)-bicomplex, hence by finite-support sequences in that model. An unrestricted direct product is too large and can have pathological or even trivial cohomology. Entire cyclic cohomology selects an intermediate analytic completion preserved by \(b+B\).

Equivalent presentations use normalized cochains, completed entire chains and their continuous duals, or factorial weights such as \(\lfloor n/2\rfloor!\). The weights may differ by degree conventions but must define the same intended bornological growth class.

## Theta summability and the JLO character

A [[noncommutative-geometry/theta-summable-spectral-triple|theta-summable spectral triple]] yields the Jaffe–Leśniewski–Osterwalder cochain. Heat operators regularize its multilinear expressions, and simplex-volume estimates give the required factorial control. The JLO cochain is an entire cyclic cocycle whose class is an analytic Chern character. This extends finite-degree characters arising from strict Schatten summability to a heat-kernel setting.

The resulting class pairs with suitable \(K\)-theory classes and is stable under the perturbations and homotopies allowed by the theta-summable theory.

## Locally convex and bornological versions

For a locally convex algebra, the norm condition is replaced by uniform estimates on every bounded subset. A complete bornological formulation packages precisely which multilinear maps and completions are admissible. These extensions are important for smooth function algebras and for bivariant analytic cyclic theory.

**Warning.** “Entire,” “analytic,” and “local” [[noncommutative-geometry/cyclic-cohomology|cyclic cohomology]] are related but distinct theories. Their completions have different functorial and excision properties. One must also distinguish the cohomological complex of multilinear functionals from the dual homological complex of completed chains.

## References

1. A. Connes, “Entire Cyclic Cohomology of Banach Algebras and Characters of \(\theta\)-Summable Fredholm Modules,” *K-Theory* 1 (1988), 519–548. [DOI record](https://doi.org/10.1007/BF00533785). Relevant: the entire cochain growth condition and the character of a theta-summable Fredholm module.
2. A. Jaffe, A. Leśniewski, and K. Osterwalder, “Quantum K-Theory. I. The Chern Character,” *Communications in Mathematical Physics* 118 (1988), 1–14. [DOI record](https://doi.org/10.1007/BF01218474). Relevant: the heat-kernel entire cocycle now called the JLO character.
3. R. Meyer, “Analytic Cyclic Cohomology,” 1999. [arXiv record](https://arxiv.org/abs/math/9906205). Relevant: complete bornological algebras, analytic completions, and comparison with entire cyclic cohomology.

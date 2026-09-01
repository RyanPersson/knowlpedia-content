+++
id = "convex-analysis/convexity-preserved-under-affine-composition"
title = "Convexity Preserved Under Affine Composition"
kind = "knowl"
summary = "Precomposition of a convex function with an affine map preserves convexity."
aliases = ["convexity-preserved-under-affine-composition", "Convexity Preserved Under Affine Composition"]
domains = ["convex-analysis"]
prerequisites = ["convex-analysis/affine-mapping", "linear-algebra/vector-space", "convex-analysis/convex-function-via-epigraph"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "convex-analysis/convexity-preserved-under-affine-composition.md"
+++

Let \(B:X\to Y\) be an [[convex-analysis/affine-mapping|affine mapping]] between real [[linear-algebra/vector-space|vector spaces]], and let \(f:Y\to\overline{\mathbb R}\) be a [[convex-analysis/convex-function-via-epigraph|convex function]]. Then \(f\circ B\) is convex on \(X\).

## Proof idea

Use \(B(\lambda x+(1-\lambda)y)=\lambda B(x)+(1-\lambda)B(y)\) for \(0\leq\lambda\leq1\), then apply convexity of \(f\).

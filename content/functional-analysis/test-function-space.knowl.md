+++
id = "functional-analysis/test-function-space"
title = "Test-function space"
kind = "definition"
summary = "The LF-space of compactly supported smooth functions on an open subset of Euclidean space."
aliases = ["test function", "compactly supported smooth function", "C_c^\\infty", "C_c^infinity", "D(Omega)", "space D(U)", "compactly supported smooth test functions"]
domains = ["functional-analysis", "distribution-theory", "real-analysis"]
prerequisites = ["linear-algebra/vector-space", "topology/compact-set", "functional-analysis/lf-space", "functional-analysis/inductive-limit-locally-convex-spaces"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

For an open set \(\Omega\subseteq\mathbb R^n\), the **test-function space**
is
\[
\mathcal D(\Omega)=C_c^\infty(\Omega),
\]
the [[linear-algebra/vector-space|vector space]] of smooth functions whose supports are
[[topology/compact-set|compact]] subsets of \(\Omega\), equipped with its
canonical [[functional-analysis/lf-space|LF topology]]. Choose compact sets
\(K_j\subseteq\operatorname{int}K_{j+1}\) exhausting \(\Omega\), and let
\(\mathcal D_{K_j}(\Omega)\) consist of functions supported in \(K_j\), with
the seminorms
\[
p_m(\varphi)=
\max_{|\alpha|\leq m}\sup_{x\in K_j}
\left|\partial^\alpha\varphi(x)\right|.
\]
Then \(\mathcal D(\Omega)\) carries the locally convex
[[functional-analysis/inductive-limit-locally-convex-spaces|inductive-limit
topology]] of the spaces \(\mathcal D_{K_j}(\Omega)\). This topology, not
only the underlying set, is part of the definition.

## Convergence

A sequence \(\varphi_\nu\) converges to \(0\) in
\(\mathcal D(\Omega)\) exactly when all its supports lie in one fixed compact
\(K\Subset\Omega\) and every
[[real-analysis/partial-derivative|partial derivative]] converges uniformly
to \(0\) there. Supports that drift toward infinity or toward the boundary do
not converge in the test-function topology merely because the functions and
their derivatives converge pointwise.

## Continuous functionals

A linear functional on \(\mathcal D(\Omega)\) is continuous exactly when its
restriction to each fixed-support space \(\mathcal D_K(\Omega)\) is
continuous. The resulting
[[functional-analysis/topological-dual|topological dual]] is the space of
[[functional-analysis/distribution|distributions]] on \(\Omega\). This is
why distribution theory must specify the LF topology: algebraic linear
functionals on \(C_c^\infty(\Omega)\) are far more numerous.

## Comparison with Schwartz space

When \(\Omega=\mathbb R^n\), every test function is a Schwartz function, and
\(\mathcal D(\mathbb R^n)\) is dense in
[[functional-analysis/schwartz-space|\(\mathcal S(\mathbb R^n)\)]]. The two
spaces are nevertheless different: test functions have compact support,
whereas Schwartz functions may have full support but must decay rapidly
together with all derivatives.

## References

- [Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, §§1.1–1.2 (Springer, 2003)](https://doi.org/10.1007/978-3-642-61497-2)
- [François Trèves, *Topological Vector Spaces, Distributions and Kernels*, Chapter 21 (Academic Press, 1967)](https://books.google.com/books?id=dugpcQAACAAJ)

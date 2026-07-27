+++
id = "convex-analysis/convexity-on-a-convex-subset-via-extension"
title = "Convexity on a convex subset via extension"
kind = "knowl"
summary = "A function on a convex set is convex exactly when its extension by positive infinity is convex."
aliases = ["convexity-on-a-convex-subset-via-extension", "Convexity on a convex subset via extension"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/convexity-on-a-convex-subset-via-extension.md"
+++

Let \(X\) be a real vector space, let \(\Omega\subseteq X\) be a nonempty [[convex-analysis/convex-set|convex set]], and let \(f:\Omega\to\mathbb R\).

Define the extension \(\widetilde f:X\to(-\infty,+\infty]\) by
\[
\widetilde f(x)=
\begin{cases}
f(x), & x\in\Omega,\\
+\infty, & x\notin\Omega.
\end{cases}
\]

The function \(f\) is **convex on \(\Omega\)** if \(\widetilde f\) is a [[convex-analysis/convex-function-via-epigraph|convex function]] on \(X\). Equivalently, for all \(x,y\in\Omega\) and \(\lambda\in[0,1]\),
\[
f(\lambda x+(1-\lambda)y)\le \lambda f(x)+(1-\lambda)f(y).
\]

## Interpretation

Extending by \(+\infty\) packages the domain constraint into an extended-real function without changing the convexity inequality on \(\Omega\).

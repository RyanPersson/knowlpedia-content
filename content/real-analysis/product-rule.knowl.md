+++
id = "real-analysis/product-rule"
title = "Product rule for derivatives"
kind = "definition"
summary = "The derivative of a product differentiates each factor once while retaining the other."
aliases = ["Leibniz product rule"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/derivative", "real-analysis/limit-of-a-function-at-a-point"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For functions [[real-analysis/derivative|differentiable]] at \(x\), the **product rule** is
\[
(fg)'(x)=f'(x)g(x)+f(x)g'(x).
\]
To prove it, write the difference quotient as
\[
\frac{f(x+h)-f(x)}h g(x+h)
+f(x)\frac{g(x+h)-g(x)}h
\]
and use continuity of the differentiable function \(g\).

## Partial and bilinear versions

Holding the other variables fixed gives \(\partial_j(fg)=(\partial_j f)g+f\partial_jg\). More generally, for a fixed continuous bilinear map \(B\),
\(\partial_jB(u,v)=B(\partial_j u,v)+B(u,\partial_jv)\).
This includes dot products, cross products, outer products and matrix multiplication. The order of factors is retained when the product is noncommutative.

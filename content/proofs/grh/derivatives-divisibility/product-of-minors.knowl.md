+++
id = "proofs/grh/derivatives-divisibility/product-of-minors"
title = "Product of minors attached to a filling"
kind = "definition"
summary = "The polynomial P_y(z): the product, over the columns of a family of diagrams, of the minor of z_tau y_tau on the rows that a filling puts into the column and on the first h columns."
aliases = ["product of minors", "minor product P_y", "column counts", "number of boxes"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.minorProd"]
lean_files = ["src/New/Derivatives/Divisibility/Count.lean"]
+++

**Definition (product of minors).** Let \(\Phi\), \(n\), \(n'\) be finite sets and \(R\) a commutative ring. Let \(\kappa\colon\Phi\times\mathbb{N}\to\mathbb{N}\) be **column counts**: \(\kappa(\tau,h)\) is the number of columns of height \(h\) of a diagram at the place \(\tau\); only the heights \(h<N:=\lvert n'\rvert\) are used, and the **number of boxes** is \(B=\sum_{\tau}\sum_{h<N}h\,\kappa(\tau,h)\). A **filling** \(i'\) assigns to every place \(\tau\), height \(h<N\), column \(j<\kappa(\tau,h)\) and box \(b<h\) a *row* \(i'(\tau,h,j,b)\in n'\). Let \(y_{\tau,a,k}\in R\) for \(\tau\in\Phi\), \(a\in n\), \(k\ge0\), read as matrices \(y_\tau\) with rows \(a\in n\) and columns \(k\). In variables \(z_{(\tau,b,a)}\), the entries of matrices \(z_\tau\) of size \(n'\times n\), the **product of minors** is the polynomial
\[
P_y(z)=\prod_{\tau\in\Phi}\ \prod_{h<N}\ \prod_{j<\kappa(\tau,h)}\ \det\Bigl(\sum_{a\in n}y_{\tau,a,k}\;z_{(\tau,\,i'(\tau,h,j,b),\,a)}\Bigr)_{0\le b,k<h}\ \in R[z] ,
\]
that is, for each column, the minor of the product \(z_\tau y_\tau\) on the rows of the column and on the first \(h\) columns. It is homogeneous of degree \(B\) in \(z\).

## Remarks

In the source, fillings are the members of [[?lean:New.WeylIndex|the index set of the standard fillings]], a chosen set of fillings whose minor products form a basis of the corresponding space of semi-invariants; the definition above uses only the underlying map \(i'\). Conversely to what one might expect, it is \(P_y\) that expands as a linear combination of the entries of a row of the Schur matrix, with coefficients given by minors evaluated at \(y\); over a general ring the entries are not combinations of the \(P_y\). Over \(\mathbb{C}_p\) one still finds, for each entry, an integral \(y\) for which the jet along \(P_y\) is at least as large in norm; see [[proofs/grh/derivatives-divisibility/schur-entry-to-minor-product|from Schur entries to products of minors]].

## References

1. Lean: `New.minorProd` in `src/New/Derivatives/Divisibility/Count.lean`; `New.boxes` in `src/Lib/Weil/Construction/ThetaJets.lean`.

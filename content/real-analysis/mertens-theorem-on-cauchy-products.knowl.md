+++
id = "real-analysis/mertens-theorem-on-cauchy-products"
title = "Mertens theorem on Cauchy products"
kind = "knowl"
summary = "The Cauchy product of two convergent series converges to the product of their sums if one series converges absolutely."
aliases = ["mertens-theorem-on-cauchy-products", "Mertens theorem on Cauchy products"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/mertens-theorem-on-cauchy-products.md"
+++

Let \(\sum_{n=0}^\infty a_n\) and \(\sum_{n=0}^\infty b_n\) be convergent real or complex [[real-analysis/series|series]]. Define their [[real-analysis/cauchy-product|Cauchy product]] by
\[
c_n=\sum_{k=0}^n a_kb_{n-k}.
\]
If at least one of the two series [[real-analysis/absolutely-convergent-series|converges absolutely]], then \(\sum_{n=0}^\infty c_n\) converges and
\[
\sum_{n=0}^\infty c_n
=\left(\sum_{n=0}^\infty a_n\right)
 \left(\sum_{n=0}^\infty b_n\right).
\]

## Remarks

This result justifies multiplying power series and many other formal series manipulations when absolute convergence is present.

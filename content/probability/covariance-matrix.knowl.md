+++
id = "probability/covariance-matrix"
title = "Covariance matrix"
kind = "definition"
summary = "The matrix of centered pairwise products of a random vector with finite second moment."
aliases = ["variance-covariance matrix"]
domains = ["probability"]
section_mode = "progressive"
prerequisites = ["probability/random-vector", "probability/covariance", "measure-theory/averaged-second-moment-matrix", "linear-algebra/outer-product"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a random vector \(X=(X_1,\ldots,X_d)\) with finite second moment, its **covariance matrix** is
\[
\operatorname{Cov}(X)=\mathbb E[(X-\mathbb EX)(X-\mathbb EX)^T].
\]
Its \((i,j)\) entry is the scalar [[probability/covariance|covariance]] \(\operatorname{Cov}(X_i,X_j)\). Equivalently, it is \(\mathbb E[XX^T]-(\mathbb EX)(\mathbb EX)^T\).

## Positivity and degeneracy

For every \(a\), \(a^T\operatorname{Cov}(X)a=\operatorname{Var}(a\cdot X)\ge0\). It is positive definite precisely when no nonzero linear combination \(a\cdot X\) is almost surely constant. The deterministic choice of a probability average on a torus gives the same matrix construction for a periodic vector field.

## Velocity fluctuations

[[fluid-dynamics/reynolds-averaging-stress|Reynolds averaging stress]] is the covariance matrix of a fluctuating velocity. Its sign in a momentum equation depends on which side contains the tensor divergence.

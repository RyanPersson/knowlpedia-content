+++
id = "real-analysis/global-maximum-global-minimum"
title = "Global maximizer and global minimizer"
kind = "definition"
summary = "A point where a function attains its maximum or minimum value on its entire domain."
aliases = ["global-maximum-global-minimum", "Global maximum and global minimum"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/global-maximum-global-minimum.md"
prerequisites = []
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(f:E\to\mathbb{R}\) and let \(a\in E\).

- The point \(a\) is a **global maximizer** (or **absolute maximizer**) of
  \(f\) on \(E\) if
  \[\forall x\in E,\ f(x)\le f(a).\]
  The value \(f(a)\) is then the **global maximum** (or **absolute
  maximum**) of \(f\) on \(E\).

- The point \(a\) is a **global minimizer** (or **absolute minimizer**) of
  \(f\) on \(E\) if
  \[\forall x\in E,\ f(a)\le f(x).\]
  The value \(f(a)\) is then the **global minimum** (or **absolute
  minimum**) of \(f\) on \(E\).

## Remarks

Global extrema are stronger than local extrema and need not exist in general. The [[topology/extreme-value-theorem|extreme value theorem]] states that continuous real-valued functions on compact spaces attain both a global maximum and a global minimum.

## Examples

- On \(E=[0,1]\), \(f(x)=x\) has global minimizer \(0\), global maximizer
  \(1\), minimum value \(0\), and maximum value \(1\).
- On \(E=(0,1)\), \(f(x)=x\) has no global maximizer or minimizer and no
  maximum or minimum value.
- On \(E=\mathbb{R}\), \(f(x)=x^2\) has global minimizer \(0\) and minimum
  value \(0\), but no global maximizer or maximum value.

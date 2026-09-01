+++
id = "algebra-rings/minimal-polynomial-field"
title = "Minimal polynomial over a field"
kind = "knowl"
summary = "The unique monic irreducible polynomial over K annihilating a given algebraic element."
aliases = ["minimal-polynomial-field", "Minimal polynomial over a field"]
domains = ["algebra-rings"]
prerequisites = ["algebra-rings/irreducible-polynomial"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-rings/minimal-polynomial-field.md"
+++

Let \(K\subseteq L\) be fields and let \(\alpha\in L\) be algebraic over \(K\). The **minimal polynomial of \(\alpha\) over \(K\)** is the unique monic [[algebra-rings/irreducible-polynomial|irreducible polynomial]] \(m_{\alpha,K}(x)\in K[x]\) such that \(m_{\alpha,K}(\alpha)=0\).

## Remarks

It generates the kernel of the evaluation map \(K[x]\to L\), \(f\mapsto f(\alpha)\), and determines the simple extension \(K(\alpha)\) up to \(K\)-isomorphism.

## Examples

- Over \(\mathbb Q\), the minimal polynomial of \(\sqrt2\) is \(x^2-2\).
- Over \(\mathbb R\), the minimal polynomial of \(i\) is \(x^2+1\).
- If \(\alpha\in K\), then the minimal polynomial is \(x-\alpha\).

---
title: "Cayley-Hamilton Theorem"
description: "Every linear operator satisfies its own characteristic polynomial"
---

**Cayley-Hamilton Theorem**: Let $T$ be a {{< knowl id="linear-operator" text="linear operator" >}} on a finite-dimensional vector space $V$ over a field $F$, and let $\chi_T(t)$ be its {{< knowl id="characteristic-polynomial" text="characteristic polynomial" >}}. Then
$$
\chi_T(T)=0,
$$
meaning that when $\chi_T(t)$ is expanded as a polynomial $\chi_T(t)=t^n+c_{n-1}t^{n-1}+\cdots+c_0$, one has
$$
T^n+c_{n-1}T^{n-1}+\cdots+c_0 I=0
$$
as operators on $V$ (where $I$ is the identity operator and $0$ is the zero operator).

A key consequence is that the {{< knowl id="minimal-polynomial" text="minimal polynomial" >}} of $T$ divides $\chi_T$.

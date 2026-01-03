---
title: "Linearity in the integrator (Riemann–Stieltjes)"
description: "Integrability and the integral are linear with respect to linear combinations of integrators"
---

Let $f:[a,b]\to\mathbb{R}$ and let $\alpha,\beta:[a,b]\to\mathbb{R}$ be functions of {{< knowl id="bounded-variation" text="bounded variation" >}}. Suppose the {{< knowl id="riemann-stieltjes-integral" text="Riemann–Stieltjes integrals" >}} $\int_a^b f\,d\alpha$ and $\int_a^b f\,d\beta$ exist. Let $c,d\in\mathbb{R}$ and define a new integrator
$
\gamma=c\alpha+d\beta.
$

**Proposition**: The integral $\int_a^b f\,d\gamma$ exists and
$
\int_a^b f\,d(c\alpha+d\beta)=c\int_a^b f\,d\alpha+d\int_a^b f\,d\beta.
$

This is the "integrator-side" linearity of the Riemann–Stieltjes integral. Together with integrand-side linearity, it makes $\int f\,d\alpha$ bilinear in $(f,\alpha)$ (within the class where the integral exists).

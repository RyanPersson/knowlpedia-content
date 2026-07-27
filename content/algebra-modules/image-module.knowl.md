+++
id = "algebra-modules/image-module"
title = "Image of a module homomorphism"
kind = "knowl"
summary = "The submodule consisting of all values attained by a module homomorphism."
aliases = ["image-module", "Image of a module homomorphism"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/image-module.md"
+++

Let \(f:M\to N\) be a [[algebra-modules/module-homomorphism|module homomorphism]]. The **image** of \(f\) is
\[
\operatorname{im}(f)=\{f(m): m\in M\}\subseteq N.
\]
It is a [[algebra-modules/submodule|submodule]] of \(N\).

## Properties

The map \(f\) is surjective if and only if \(\operatorname{im}(f)=N\). For consecutive module homomorphisms \(M\xrightarrow{f}N\xrightarrow{g}P\), exactness at \(N\) means \(\operatorname{im}(f)=\ker(g)\); see [[algebra-modules/exactness-via-kernels-images|exactness via kernels and images]].

## Examples

- For \(f:\mathbb Z\to\mathbb Z\) given by \(f(n)=2n\), the image is \(2\mathbb Z\).
- For the projection \(\pi:R^2\to R\), \(\pi(a,b)=a\), the image is all of \(R\).
- The image of the zero homomorphism is \(\{0\}\).

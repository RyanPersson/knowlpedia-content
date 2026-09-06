+++
id = "algebra-modules/kernels-are-submodules"
title = "Kernels are submodules"
kind = "knowl"
summary = "The kernel of a module homomorphism is a submodule of its domain."
aliases = ["kernels-are-submodules", "Kernels are submodules"]
domains = ["algebra-modules"]
prerequisites = ["algebra-modules/submodule", "algebra-modules/kernel-module"]
dependency_review_count = 1
legacy_source_path = "algebra-modules/kernels-are-submodules.md"
+++

Let \(f:M\to N\) be a homomorphism of \(R\)-modules. Its kernel
\[
\ker(f)=\{m\in M:f(m)=0\}
\]
is an \(R\)-[[algebra-modules/submodule|submodule]] of \(M\).

Indeed, if \(x,y\in\ker(f)\) and \(r\in R\), then \(f(x+y)=0\) and
\(f(rx)=rf(x)=0\). Thus the [[algebra-modules/kernel-module|kernel]] is the
canonical submodule used to form the
[[algebra-modules/quotient-module|quotient by the kernel]].

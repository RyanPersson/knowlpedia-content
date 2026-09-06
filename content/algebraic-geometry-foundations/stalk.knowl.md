+++
id = "algebraic-geometry-foundations/stalk"
title = "Stalk"
kind = "knowl"
summary = "The collection of germs near one point of a sheaf."
aliases = ["stalk", "germ at a point"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/sheaf", "topology/topological-space"]
dependency_review_count = 1
legacy_source_path = "algebraic-geometry-foundations/stalk.md"
+++

Let \(\mathcal F\) be a [[algebraic-geometry-foundations/sheaf|sheaf]] on a [[topology/topological-space|topological space]] \(X\), and let \(x\in X\). The **stalk** \(\mathcal F_x\) is the collection of germs of sections of \(\mathcal F\) near \(x\). Concretely, a germ is represented by a pair \((U,s)\), where \(U\) is an open neighborhood of \(x\) and \(s\in\mathcal F(U)\). Two representatives \((U,s)\) and \((V,t)\) define the same germ if \(s\) and \(t\) agree on some neighborhood of \(x\) contained in \(U\cap V\).

Thus the stalk forgets behavior away from \(x\) while retaining everything visible arbitrarily close to it. For the sheaf of continuous real-valued functions, \(\mathcal F_x\) consists of germs of continuous functions at \(x\). For a [[algebraic-geometry-foundations/structure-sheaf|structure sheaf]] on an [[algebraic-geometry-foundations/affine-scheme|affine scheme]], the stalk at a prime \(\mathfrak p\) is the local ring \(A_{\mathfrak p}\).

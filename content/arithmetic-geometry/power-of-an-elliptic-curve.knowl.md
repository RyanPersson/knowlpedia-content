+++
id = "arithmetic-geometry/power-of-an-elliptic-curve"
title = "Power of an elliptic curve"
kind = "construction"
summary = "The product Eⁿ of n copies of an elliptic curve, with addition in each coordinate."
aliases = ["powers of an elliptic curve", "elliptic curve power"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/elliptic-curve", "arithmetic-geometry/abelian-variety"]
+++

For an [[algebraic-geometry-foundations/elliptic-curve|elliptic curve]] \(E/k\) and an integer \(n\ge1\), its **\(n\)th power** \(E^n\) is the product of \(n\) copies of \(E\) over \(k\). Its points over an extension \(K/k\) are \(n\)-tuples in \(E(K)^n\). Coordinatewise addition makes it an [[arithmetic-geometry/abelian-variety|abelian variety]] of dimension \(n\).

## How to read the post

For instance, \(E^2\) has points \((P,Q)\), while multiplication by two sends a single point \(P\) to \(2P\) on \(E\). An abelian variety described as a power “up to isogeny” admits an [[arithmetic-geometry/isogeny|isogeny]] to such a product over the field under consideration.

+++
id = "langlands/ind-scheme"
title = "Ind-scheme"
kind = "definition"
summary = "A functor presented as a filtered colimit of schemes, usually along closed immersions."
aliases = ["ind-algebraic scheme"]
domains = ["langlands", "algebraic-geometry-foundations"]
section_mode = "progressive"
+++

An **ind-scheme** over a field \(k\) is a functor on \(k\)-algebras admitting
a presentation
\[
X\simeq\varinjlim_i X_i
\]
by schemes \(X_i\) whose transition maps are closed immersions. It is
**ind-projective** if the \(X_i\) can be chosen projective.

The presentation is not part of the object: two filtered systems define the
same ind-scheme when their colimit functors are isomorphic.

## References

1. Alexander Beilinson and Vladimir Drinfeld, *Chiral Algebras*, American
   Mathematical Society, 2004, §7.11.

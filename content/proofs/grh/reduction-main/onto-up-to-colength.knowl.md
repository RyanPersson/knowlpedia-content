+++
id = "proofs/grh/reduction-main/onto-up-to-colength"
title = "Endomorphism onto up to a bounded colength"
kind = "definition"
summary = "An endomorphism that keeps a submodule M and is onto on M modulo p^n up to a colength dividing p^l with l at most c."
aliases = ["onto up to colength", "IsOntoUpToColength"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsOntoUpToColength"]
lean_files = ["src/New/Reduction/Lattices/Colength.lean"]
+++

Let \(O\) be a [[?c:commutative ring|commutative ring]], \(V\) an \(O\)-[[algebra-modules/module|module]], \(M\subseteq V\) a [[?c:submodule|submodule]], \(p\in O\), \(n\ge 0\) an integer, \(y:V\to V\) an \(O\)-[[?c:linear map|linear]] endomorphism and \(c\) a real number. We say that **\(y\) is onto on \(M\) modulo \(p^n\) up to colength \(c\)** if

1. \(y(M)\subseteq M\), and
2. there is an integer \(l\ge 0\) with \(l\le c\) such that [[proofs/grh/reduction-main/colength-divides|\(\operatorname{colen}\bigl(M,\ y(M)+p^nM\bigr)\mid p^l\)]].

## Properties

The bounds \(c\) add under composition: see [[proofs/grh/reduction-main/onto-up-to-colength-product|products of endomorphisms onto up to colength]]. Over a discrete valuation ring the condition bounds the length of \(M/(y(M)+p^nM)\): see [[proofs/grh/reduction-main/colength-bounds-length|colength bounds a length]].

## References

1. Lean: `New.IsOntoUpToColength` in `src/New/Reduction/Lattices/Colength.lean`.

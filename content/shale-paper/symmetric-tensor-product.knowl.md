+++
id = "shale-paper/symmetric-tensor-product"
title = "Symmetric Tensor Product (·)_s"
kind = "knowl"
summary = "The symmetrization of a pure tensor, obtained by averaging over all permutations of its factors."
aliases = ["symmetric-tensor-product", "Symmetric Tensor Product (·)_s"]
domains = ["shale-paper"]
legacy_source_path = "shale-paper/symmetric-tensor-product.md"
+++

Let \(H\) be a complex Hilbert space and let \(x_1,\dots,x_n\in H\). Their **symmetric tensor** is the symmetrization
\[
(x_1\otimes\cdots\otimes x_n)_s=\frac1{n!}\sum_{\pi\in S_n} x_{\pi(1)}\otimes\cdots\otimes x_{\pi(n)}.
\]
It belongs to the subspace of \(H^{\otimes n}\) fixed by permutations of the tensor factors.

## Remarks

Symmetric tensors span the \(n\)-particle symmetric tensor power; these powers form the [[shale-paper/symmetric-fock-space|symmetric Fock space \(S(H)\)]] used for Fock–Cook quantization.

## Examples

- For \(n=2\), \((x\otimes y)_s=\tfrac12(x\otimes y+y\otimes x)\).

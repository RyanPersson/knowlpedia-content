+++
id = "nonassociative-algebra/spin8-stabilizer-of-an-albert-algebra-frame"
title = "Spin(8) stabilizer of an Albert-algebra frame"
kind = "theorem"
summary = "The pointwise stabilizer in compact F_4 of a labelled Albert-algebra Jordan frame is Spin(8)."
aliases = ["Albert algebra frame stabilizer", "Spin(8) in F4", "Jordan frame isotropy in F4"]
domains = ["nonassociative-algebra", "lie-groups"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/exceptional-jordan-algebra", "nonassociative-algebra/jordan-frame", "lie-groups/half-spin-representation", "lie-groups/spin8-triality"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(J=H_3(\mathbb O)\) be the compact real [[nonassociative-algebra/exceptional-jordan-algebra|Albert algebra]], let
\(F_4=\operatorname{Aut}(J)\), and let \((e_1,e_2,e_3)\) be a labelled
[[nonassociative-algebra/jordan-frame|Jordan frame]]. Its **pointwise
stabilizer** is
\[
\{g\in F_4:g(e_i)=e_i\text{ for }i=1,2,3\}\cong\mathrm{Spin}(8).
\]
Moreover, \(F_4\) acts transitively on labelled Jordan frames.

## Triality action

For the standard frame, the decomposition
\[
J=\mathbb R e_1\oplus\mathbb R e_2\oplus\mathbb R e_3
\oplus\xi_{12}(\mathbb O)\oplus\xi_{23}(\mathbb O)
\oplus\xi_{31}(\mathbb O)
\]
is invariant under the frame stabilizer. The three eight-dimensional
off-diagonal summands carry, in a suitable ordering, the vector, left half-spin,
and right [[lie-groups/half-spin-representation|half-spin representations]] of \(\mathrm{Spin}(8)\). Their coupled
action is [[lie-groups/spin8-triality|Spin(8) triality]].

## Pointwise versus setwise stabilizers

The qualifier “pointwise” is essential. If a frame is regarded as an unordered
set, its setwise stabilizer is
\[
\mathrm{Spin}(8)\rtimes S_3.
\]
The quotient \(S_3\) permutes \(e_1,e_2,e_3\) and acts on \(\mathrm{Spin}(8)\)
through the outer automorphisms associated with triality. Thus the unqualified
statement “the setwise stabilizer is \(\mathrm{Spin}(8)\)” is false. Its
[[lie-groups/identity-component-of-a-lie-group|identity component]] is the pointwise \(\mathrm{Spin}(8)\).

## References

1. Ichirô Yokota, *Exceptional Lie Groups*, 2009, Theorem 2.7.1. [arXiv:0902.0431](https://arxiv.org/abs/0902.0431).
2. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026, Lemma 5. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
3. John F. Adams, *Lectures on Exceptional Lie Groups*, University of Chicago Press, 1996, Chapters 1–3. [Publisher record](https://press.uchicago.edu/ucp/books/book/chicago/L/bo3627754.html).

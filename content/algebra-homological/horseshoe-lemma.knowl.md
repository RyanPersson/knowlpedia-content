+++
id = "algebra-homological/horseshoe-lemma"
title = "Horseshoe lemma"
kind = "knowl"
summary = "Given a short exact sequence of modules, compatible projective (or injective) resolutions can be spliced to produce a resolution of the middle module."
aliases = ["horseshoe-lemma", "Horseshoe lemma"]
domains = ["algebra-homological"]
legacy_source_path = "algebra-homological/horseshoe-lemma.md"
+++

Let \(R\) be a ring and
\[
0 \longrightarrow A \xrightarrow{i} B \xrightarrow{p} C \longrightarrow 0
\]
a [[algebra-modules/short-exact-sequence|short exact sequence]] of \(R\)-modules. Given projective resolutions \(P_\bullet^A\to A\) and \(P_\bullet^C\to C\), the **horseshoe lemma** provides a projective resolution \(P_\bullet^B\to B\) and a short exact sequence of chain complexes
\[
0\to P_\bullet^A\to P_\bullet^B\to P_\bullet^C\to 0
\]
such that \(P_n^B\cong P_n^A\oplus P_n^C\) in every degree \(n\).

## Projective construction

More explicitly, suppose
\[
\cdots \to P_1^A \to P_0^A \to A \to 0,
\qquad
\cdots \to P_1^C \to P_0^C \to C \to 0
\]
are resolutions by [[algebra-modules/projective-module|projective modules]]. The lemma constructs
\[
\cdots \to P_1^B \to P_0^B \to B \to 0,
\]
whose augmentation maps recover the original short exact sequence. The differentials on the degreewise direct sums are chosen compatibly with the maps \(i\) and \(p\).

## Injective version

Dually, given injective resolutions of \(A\) and \(C\), one constructs an injective resolution of \(B\) with \(I^n_B\cong I^n_A\oplus I^n_C\) and a short exact sequence of cochain complexes
\[
0 \to I^\bullet_A \to I^\bullet_B \to I^\bullet_C \to 0.
\]
See [[algebra-homological/injective-resolution|injective resolution]] and [[algebra-modules/injective-module|injective modules]].

## Why it matters

The horseshoe lemma underlies functorial constructions of the long exact sequences in [[algebra-homological/tor|Tor]] and [[algebra-homological/ext|Ext]] (see [[algebra-homological/long-exact-sequence-tor|long exact sequence for Tor]] and [[algebra-homological/long-exact-sequence-ext|long exact sequence for Ext]]), and is a standard way to build resolutions needed to compute derived functors (see [[algebra-homological/derived-functor|derived functor]]).

## Example

In \(\mathbf{Ab}\), the sequence
\[
0 \to \mathbb Z/2 \to \mathbb Z/6 \to \mathbb Z/3 \to 0.
\]
is exact. Applying the lemma to the standard projective resolutions
\[
0\to \mathbb Z \xrightarrow{\cdot 2} \mathbb Z \to \mathbb Z/2 \to 0,\qquad
0\to \mathbb Z \xrightarrow{\cdot 3} \mathbb Z \to \mathbb Z/3 \to 0.
\]
produces a resolution of \(\mathbb Z/6\) with
\[
P_1^B\cong\mathbb Z\oplus\mathbb Z,\qquad
P_0^B\cong\mathbb Z\oplus\mathbb Z.
\]
This resolution is generally not minimal, but its compatibility with the original exact sequence is what is useful in homological arguments.

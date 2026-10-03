+++
id = "discrete-structures/cayley-graph"
title = "Cayley graph"
kind = "definition"
summary = "The graph of multiplication by selected generators of a group."
aliases = ["Cayley digraph", "right Cayley graph"]
domains = ["discrete-structures"]
section_mode = "progressive"
prerequisites = ["algebra-groups/group", "discrete-structures/directed-graph"]
dependency_heuristic = "transcript-connections-semantic-v1"
dependency_review_count = 1
+++
For a [[algebra-groups/group|group]] \(G\) and a subset \(S\subseteq G\), the **right Cayley [[discrete-structures/directed-graph|directed graph]]** \(\operatorname{Cay}(G,S)\) has vertex set \(G\) and an edge labelled \(s\) from \(g\) to \(gs\) for every \(g\in G\), \(s\in S\).

When \(S=S^{-1}\) and \(1\notin S\), the **undirected Cayley graph** joins distinct vertices \(g,h\) when \(g^{-1}h\in S\); opposite directed edges are treated as one undirected edge. This gives a simple graph of degree \(|S|\) when \(S\) is finite.

## Connectedness

For the undirected convention, paths from \(1\) give words in \(S\). Thus the graph is connected exactly when \(S\) generates \(G\). Left multiplication by any element of \(G\) is a graph automorphism, since it preserves \(g^{-1}h\).

For example, \(G=\mathbb Z/m\mathbb Z\) and \(S=\{1,-1\}\) give the cycle on \(m\) vertices when \(m\ge3\).

## Conventions

Left Cayley graphs use edges \(g\mapsto sg\). Generating multisets, the identity generator, and directed generators can produce multiplicities or loops, so those conventions must be specified separately. Some finite Cayley graphs satisfy the [[discrete-structures/ramanujan-graph|Ramanujan spectral bound]].

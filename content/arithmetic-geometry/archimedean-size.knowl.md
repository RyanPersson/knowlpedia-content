+++
id = "arithmetic-geometry/archimedean-size"
title = "Archimedean size"
kind = "definition"
summary = "The magnitude at a real or complex embedding, measured by the ordinary absolute value or its logarithm."
aliases = ["archimedean norm"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/field-embedding", "algebra-fields-galois/norm-field"]
+++

For a nonzero number \(a\) in a number field \(K\), an **archimedean size** is \(|\sigma(a)|\) at a real or complex [[algebra-fields-galois/field-embedding|embedding]] \(\sigma:K\hookrightarrow\mathbb C\). Adding the logarithms over all embeddings, counting both members of each complex pair, gives \(\log|N_{K/\mathbb Q}(a)|\), the logarithm of the absolute [[algebra-fields-galois/norm-field|field norm]].

## A complex pair

The embeddings of \(\mathbb Q(i)\) send \(2+i\) to \(2+i\) and \(2-i\). Both absolute values are \(\sqrt5\), so their logarithms add to \(\log 5\). A vector or a section in the post has a specified norm at each archimedean place. These norms play the same measuring role as the absolute values in the scalar example.

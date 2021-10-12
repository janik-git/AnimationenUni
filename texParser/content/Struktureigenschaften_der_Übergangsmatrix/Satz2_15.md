---
 title: "Satz2_15"
 mathjax : true
---
[\[Folgerung Dynkin Formel, (LR), (LT)\]]{#Folgerung Dynkin Formel, (LR), (LT)
label="Folgerung Dynkin Formel, (LR), (LT)"} Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine irreduzible $(\nu,P)$-Markovkette
mit Zustandsraum E.

-   Falls $\emptyset \neq A \subsetneq E$ und $h: E \to [0, \infty)$
    existieren mit
    $$(Lh)(x) \leq 0 \quad \forall x \in A^{C} \quad und \quad h(y) < \inf_{z \in A} h(z) \: für \: ein \: y \in E \qquad (LT)$$
    so gilt
    $$\mathbb{P}_{y}[S_{A} < \infty] \leq \dfrac{h(y)}{\inf_{z \in A} h(z)} < 1$$
    Insbesondere ist jeder Zustand $y \in E$ transient.

-   Falls eine endliche Menge $\emptyset \neq A \subsetneq E$ und
    $h: E \to [0, \infty)$ existieren mit
    $$(Lh)(x) \leq 0 \quad \forall x \in A^{C} \quad und \quad \vert \lbrace x \: : \: h(x) \leq c \rbrace \vert < \infty \quad c \geq 0 \qquad (LR)$$
    so gilt $\mathbb{P}_{x}[S_{A}< \infty] = 1$ für alle $x \in E$.
    Insbesondere ist jeder Zustand $y \in E$ rekurrent.

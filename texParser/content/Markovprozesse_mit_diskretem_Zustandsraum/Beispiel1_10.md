---
 title: "Beispiel1_10"
 mathjax : true
---
Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ eine $(\nu,P)$-Markovkette auf
$E = \lbrace 1,2,3,4 \rbrace$, deren stochastische Matrix durch
folgenden Übergangsgraphen beschrieben wird

. ![Übergangsgraph des stochastischen Prozesses](beispiel22 "fig:")

Im folgenden soll die Eintrittswahrscheinlichkeit in den Zustand
$\lbrace 4 \rbrace$, d.h.
$$h_{\lbrace    4 \rbrace}(x) := \mathbb{P}_{x}[T_{\lbrace 4 \rbrace} < \infty], \: x \in E$$
bestimmt werden. Nach Satz
[\[Dirichletsatz\]](#Dirichletsatz){reference-type="ref"
reference="Dirichletsatz"} genügt es dazu, die minimale Lösung des
Dirichletproblems mit $A=\lbrace 4 \rbrace$ zu berechnen. Betrachte
somit folgendes Gleichungssystem. $$\begin{aligned}
     I. \quad h_{\lbrace 4 \rbrace}(1) &= c          & II. \quad h_{\lbrace 4 \rbrace}(2) &= \dfrac{1}{2}(h_{\lbrace 4 \rbrace}(1) + h_{\lbrace 4 \rbrace}(3))  \,  \\ 
  III. \quad h_{\lbrace 4 \rbrace}(3) &= \dfrac{1}{2}(h_{\lbrace 4 \rbrace}(2) + h_{\lbrace 4 \rbrace}(4))   & IV. \quad h_{\lbrace    4 \rbrace}(1) &= 1.\end{aligned}$$

::: center
$\Leftrightarrow$
$h_{\lbrace 4 \rbrace} = (c, \dfrac{2}{3}c + \dfrac{2}{3}, \dfrac{1}{3}c + \dfrac{5}{6},1)^{T}$
:::

Folglich besitzt obiges Gleichungssystem erst durch die
Minimalitätsbedingung eine eindeutige Lösung. Wähle hierzu $c=0$. Dann
folgt

::: center
$h_{\lbrace 4 \rbrace}(2) = \mathbb{P}_{2}[T_{\lbrace 4 \rbrace} < \infty] = \dfrac{2}{3}$
und
$h_{\lbrace 4 \rbrace}(3) = \mathbb{P}_{3}[T_{\lbrace 4 \rbrace} < \infty] = \dfrac{5}{6}$
:::

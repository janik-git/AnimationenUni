---
 title: "Kolmogorov_s_Zykelbedingung"
 mathjax : true
---
[\[Kolmogorov\'s Zykelbedingung\]]{#Kolmogorov's Zykelbedingung
label="Kolmogorov's Zykelbedingung"} Sei $P = (p(x,y))_{x,y \in E}$ eine
irreduzible, stochastische Matrix. Ein Maß $\pi$ auf E ist genau dann
reversibel bzgl. $P$, wenn

-   $p(x,y)>0 \quad \Rightarrow \quad p(y,x)>0 \qquad \forall \: x,y \in E$

-   für jeden Zykel $x_{0},x_{1},...,x_{n}$ mit $x_{n} = x_{0}$ und
    $\prod_{i=1}^{n} p(x_{i},x_{i-1})>0$ gilt
    $$\prod_{i=1}^{n} \dfrac{p(x_{i-1},x_{i})}{p(x_{i},x_{i-1})} = 1$$

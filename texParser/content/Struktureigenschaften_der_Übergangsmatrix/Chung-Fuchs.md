---
 title: "Chung-Fuchs"
 mathjax : true
---
[\[Chung-Fuchs\]]{#Chung-Fuchs label="Chung-Fuchs"} Sei
$(X_{n})_{n \in \mathbb{N}_{0}}$ eine irreduzible Irrfahrt auf
$E = \mathbb{Z}^{d}$ mit $p(x,y) = \mu (y-x), \: \: x,y \in E$, wobei
$\mu$ ein Wahrscheinlichkeitsmaß auf E ist. Bezeichne mit $\varphi$ die
charakteristische Funktion von $\mu$, d.h.
$$\varphi(t) = \int_{\mathbb{R}^{d}} e^{i \langle t,x \rangle} \mu (\diff x ) = \sum_{x \in E} e^{i \langle t,x \rangle} p(0,x) \quad , \qquad t \in [-\pi, \pi)^{d}$$
Die Markovkette $(X_{n})_{n \in \mathbb{N}_{0}}$ ist genau dann
rekurrent, wenn
$$\lim_{\lambda \uparrow 1} \int_{[-\pi, \pi)^{d}} \Re (\dfrac{1}{1-\lambda \varphi(t)}) \diff t  = \infty$$

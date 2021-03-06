---
 title: "Beispiel1_4"
 mathjax : true
---
Sei $(Y_{n})_{n \in \mathbb{N}_{0}}$ eine Folge von unabhängigen
Zufallsvariablen mit Werten in E. Setze
$(X_{n})_{n \in \mathbb{N}_{0}} := \max \lbrace Y_{0},...,Y_{n} \rbrace, \: n \in \mathbb{N}_{0}$.
Dabei besitzt $(X_{n})_{n \in \mathbb{N}_{0}}$ die Markoveigenschaft,
denn für jedes $n \in \mathbb{N}_{0}$ und $x_{0},...,x_{n+1} \in E$ mit
$\mathbb{P}[X_{0} = x_{0},...,X_{n} = x_{n}]>0$ gilt
$$\mathbb{P}[X_{n+1} = x_{n+1} \: | \: X_{0} = x_{0},...,X_{n} = x_{n}]$$
$$= \mathbb{P}[\max\lbrace x_{n}, Y_{n+1} \rbrace = x_{n+1} \: | \: X_{0} = x_{0},...,X_{n} = x_{n}]$$
$$= \mathbb{P}[\max\lbrace x_{n}, Y_{n+1} \rbrace 
= x_{n+1}]$$
$$= \mathbb{P}[\max\lbrace x_{n}, Y_{n+1} \rbrace = x_{n+1} \: | \: X_{n} = x_{n}]$$
$$= \mathbb{P}[X_{n+1} = x_{n+1} \: | \: X_{n} = x_{n}]$$

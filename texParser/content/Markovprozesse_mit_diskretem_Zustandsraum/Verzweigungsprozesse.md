---
 title: "Verzweigungsprozesse"
 mathjax : true
---
Sei $X_{n}$ die Anzahl der Individuen in der n-ten Generation. Jedes
Individuum der n-ten Generation wird unabhängig von allen anderen in der
folgenden Generation mit Wahrscheinlichkeit $\mu(y)$ mit
$y \in \mathbb{N}_{0}$ Nachkommen ersetzt. Dann lässt sich
$(X_{n})_{n \in \mathbb{N}_{0}}$ durch eine Markovkette auf
$E = \mathbb{N}_{0}$ mit Übergangsmatrix $P =(p(x,y))_{x,y \in E}$
$$p(x,y) = \mu^{*x}(y) = \sum_{y_{1} +...+ y_{x} = y} \: \mu(y_{1})... \mu(y_{2}) \qquad \mathrm{mit} \: \mu^{*0}(y) = \mathbbm{1}_{\lbrace 0 \rbrace}(y)$$
[Frage?]{style="color: red"} Woher kommt die Faltung?\
\
Sei $({X_{n}}^{(i)})_{n,i \in \mathbb{N}_{0}}$ eine Folge u.i.v.
Zufallsvariablen mit $\mathbb{P}[{X_{n}}^{(i)} = k] = \mu(k)$. Setze
$$X_{0} = x \qquad  \mathrm{und}  \qquad X_{n} = \sum_{i = 1}^{x_{n-1}} X_{n-1}^{(i)}$$
Dann gilt
$$\mathbb{P}[X_{n+1} = x_{n+1} \: | \: X_{0} = x_{0},...,X_{n} = x_{n}] = \mathbb{P}[X_{n}^{1}+...+X_{n}^{(x_{n})} = x_{n+1}]$$
$$= \mu^{*x_{n}}[x_{n+1}] = p(x_{n},x_{n+1}).$$

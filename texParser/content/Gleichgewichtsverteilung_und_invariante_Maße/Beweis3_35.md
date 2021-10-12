---
 title: "Beweis3_35"
 mathjax : true
---
$"\Rightarrow"$ Da $\pi$ reversibel bzgl. $P$ ist, ist folglich $\pi$
ein invariantes Maß. Da $P$ zudem irreduzibel ist, so folgt aus
Bemerkung $\ref{Auflistende Bemerkung zu invarianten Maßen}$ c), dass
$\pi(x) > 0$ für alle $x \in E$\
\
: $p(x,y)>0 \quad \Rightarrow \quad p(y,x)>0$\
\
Sei also $p(x,y)>0$. Dann ergibt sich aus der \"detailed balance\"
$\:$Bedingung
$$p(y,x) = \dfrac{\pi(y)}{\pi(y)} p(y,x) = \underbrace{\dfrac{\pi(x)}{\pi(y)}}_{>0} \underbrace{p(x,y)}_{>0} > 0.$$
Betrachte nun $x_{0},...,x_{n} \in E$ mit $x_{n} = x_{0}$ und
$\prod_{i=1}^{n} p(x_{i},x_{i-1})>0$ .\
\
: $\prod_{i=1}^{n} \dfrac{p(x_{i-1},x_{i})}{p(x_{i},x_{i-1})} = 1$\
\
Wiederum ergibt sich aus der \"detailed balance\" Bedingung
$$\prod_{i=1}^{n} \dfrac{p(x_{i-1},x_{i})}{p(x_{i},x_{i-1})} = \prod_{i=1}^{n} \dfrac{\pi(x_{i-1})}{\pi(x_{i-1})} \dfrac{p(x_{i-1},x_{i})}{p(x_{i},x_{i-1})} = \prod_{i=1}^{n} \dfrac{\pi(x_{i})}{\pi(x_{i-1})} = \dfrac{\pi(x_{n})}{\pi(x_{0})} \stackrel{x_{0} = x_{n}}{=} 1$$
$"\Leftarrow"$ Für ein festes $z \in E$ setze $\pi(z) = 1$. Aus der
Irreduzibilität von $P$ folgt, dass zu jedem $x \in E$ ein
$n \in \mathbb{N}$ existiert mit $p_{n}(z,x) > 0$. Fo0lglich existieren
$x_{0},...,x_{n} \in E$ mit
$$x_{0} = z \quad, \: x_{n} = x \quad und  \quad \prod_{i=1}^{n} p(x_{i},x_{i-1})>0.$$
Definiere
$$\pi(x) = \prod_{i=1}^{n} \dfrac{p(x_{i-1},x_{i})}{p(x_{i},x_{i-1})}$$\
\
: $\pi(x)$ ist unabhängig vom gewählten Pfad\
\
Sei $(x_{0}',...,x_{m}')$ ein weiterer Pfad in E mit
$x_{0}' = z, \: x_{m}' = x$ und $\prod_{j=1}^{m} p(x_{j}',x_{j-1}')>0$.
Dann folgt aus (i), dass auch $\prod_{j=1}^{m} p(x_{j-1}',x_{j}')>0$.
Setze $$(y_{0},...,y_{n+m}) = (x_{0},...,x_{n},x_{m-1}',...,x_{0}')$$
Dann gilt
$$y_{0} = y_{n+m} = z \quad und \quad \prod_{i=1}^{n+m} p(y_{i},y_{i-1}) \stackrel{x_{n}'=x_{n}}{=} \prod_{i=1}^{n} p(x_{i},x_{i-1})  \prod_{j=1}^{m} p(x_{j-1}',x_{j}')>0$$
Also folgt aus (ii)
$$\pi(x) = \prod_{i=1}^{n} \dfrac{p(x_{i-1},x_{i})}{p(x_{i},x_{i-1})} = \prod_{j=1}^{m} \dfrac{p(x_{j-1}',x_{j}')}{p(x_{j}',x_{j-1}')} \cdot \underbrace{\prod_{i=1}^{n+m} \dfrac{p(y_{i-1},y_{i})}{p(y_{i},y_{i-1})}} _{=1} = \prod_{j=1}^{m} \dfrac{p(x_{j-1}',x_{j}')}{p(x_{j}',x_{j-1}')}$$
Folglich ist $\pi(x)$ unabhängig vom gewählten Pfad.\
\
: $\pi(x)p(x,y) = \pi(y) p(y,x)$\
\
Falls $p(x,y)=0$, so ist aufgrund von (i) auch $p(y,x)=0$ und die
Aussage ist trivial. sei nun also $p(x,y)>0$. Dann ist wegen (i) auch
$p(y,x)>0$. Zudem gilt
$$\pi(x)p(x,y) = \prod_{i=1}^{n} \dfrac{p(x_{i-1},x_{i})}{p(x_{i},x_{i-1})}  \cdot p(x,y)$$
$$= \prod_{i=1}^{n} \dfrac{p(x_{i-1},x_{i})}{p(x_{i},x_{i-1})}  \cdot \dfrac{p(x,y)}{p(y,x)} \cdot p(y,x) = \pi(y)p(y,x),$$
da mit $x_{n+1}:= y$ der Pfad $(x_{0},...,x_{n},x_{n+1})$ die
Eigenschaft hat, dass $x_{0} = z, \: x_{n+1} = y$ und
$\prod_{i=1}^{n+1} p(x_{i},x_{i-1})>0$.

---
 title: "Beweis3_36"
 mathjax : true
---
-   Da K eine rekurrente, kommunizierende Klasse ist, so folgt aus Satz
    $\ref{irreduzibel, y rekurrent -> Px=1 , y transient -> Px<1 }$,
    dass
    $$\mathbb{P}_{x}[S_{\lbrace y \rbrace} < \infty] = 1 \qquad \forall \: x,y \in K$$
    Bezeichne wieder mit $S_{\lbrace x \rbrace}^{k}$ die k-te Treffzeit
    des Zustandes $x \in E$, d.h.
    $$S_{\lbrace x \rbrace}^{0} := 0 \qquad und \qquad S_{\lbrace x \rbrace}^{k} := \inf \lbrace n > S_{\lbrace x \rbrace}^{k-1} \: : \: X_{n} = x \rbrace \qquad , \quad k \in \mathbb{N}.$$
    Dann folgt aus der starken Markoveigenschaft (Satz
    $\ref{starke Markoveigenschaft}$) für $x,y \in K$ mit $x \neq y$ und
    $k \in \mathbb{N}$
    $$\mathbb{P}_{x}[S_{\lbrace x \rbrace}^{k} < S_{\lbrace y \rbrace}] = \mathbb{P}_{x}[S_{\lbrace x \rbrace}^{k} < S_{\lbrace y \rbrace}, S_{\lbrace x \rbrace}^{k-1} < S_{\lbrace y \rbrace}]$$
    $$= \mathbb{P}_{x}[S_{\lbrace x \rbrace}^{k-1} < S_{\lbrace y \rbrace}]\cdot \mathbb{P}_{x}[S_{\lbrace x \rbrace}^{k} < S_{\lbrace y \rbrace} \: | \: \underbrace{S_{\lbrace x \rbrace}^{k-1} < S_{\lbrace y \rbrace}}_{\in \mathfrak{F}_{S_{\lbrace x \rbrace}^{k-1}}^{X}}, X_{S_{\lbrace x \rbrace}^{k-1}} = x, S_{\lbrace x \rbrace}^{k-1}< \infty]$$
    $$\stackrel{\mathrm{Satz} \: \ref{starke Markoveigenschaft}}{=} \mathbb{P}_{x}[S_{\lbrace x \rbrace}^{k-1} < S_{\lbrace y \rbrace}] \cdot \mathbb{P}_{x}[S_{\lbrace x \rbrace} < S_{\lbrace y \rbrace}]$$\
    $$= \: \: ... \: \:$$\
    $$= \mathbb{P}_{x}[S_{\lbrace x \rbrace} < S_{\lbrace y \rbrace}]^{k}$$
    Angenommen
    $\mathbb{P}_{x}[S_{\lbrace y \rbrace} < S_{\lbrace x \rbrace}]=0$.
    Dann gilt, da $S_{\lbrace x \rbrace}^{k}(\omega) \geq k$ für alle
    $\omega \in \Omega$,
    $$\mathbb{P}_{x}[k < S_{\lbrace y \rbrace}] \geq \mathbb{P}_{x}[S_{\lbrace x \rbrace}^{k} < S_{\lbrace y \rbrace}] = \left( 1 - \underbrace{\mathbb{P}_{x}[S_{\lbrace y \rbrace} < S_{\lbrace x \rbrace}}_{=0}] \right)^{k} = 1$$
    Also,
    $$0 = \mathbb{P}_{x}[S_{\lbrace y \rbrace} = \infty] = \lim_{k \to \infty} \mathbb{P}_{x}[k < S_{\lbrace y \rbrace}] \geq 1 \quad \lightning$$
    Folglich ist
    $\mathbb{P}_{x}[S_{\lbrace y \rbrace} < S_{\lbrace x \rbrace}]>0.$\
    \
    : Für $x,y \in K$ mit $x \neq y$ gilt
    $$\mathbb{E}_{x}[\sum_{n=0}^{S_{\lbrace x \rbrace}-1} \mathbbm{1}_{X_{n} = y}] = \dfrac{\mathbb{P}_{x}[S_{\lbrace y \rbrace } < S_{\lbrace x \rbrace}]}{\mathbb{P}_{y}[S_{\lbrace x \rbrace } < S_{\lbrace y \rbrace}]}$$
    zunächst einmal folgt aus der starken Markoveigenschaft für
    $N \in \mathbb{N}$ und $z \in E$
    $$\mathbb{P}_{z}[X_{S_{\lbrace y \rbrace} + n} = y, n < S_{\lbrace x \rbrace} \wedge N - S_{\lbrace y \rbrace}, S_{\lbrace y \rbrace} < S_{\lbrace x \rbrace} \wedge N]$$
    $$= \mathbb{P}_{z}[S_{\lbrace y \rbrace} < S_{\lbrace x \rbrace} \wedge N] \mathbb{P}_{z}[X_{S_{\lbrace y \rbrace} + n} = y, n < S_{\lbrace x \rbrace} \wedge N - S_{\lbrace y \rbrace} \: | \: X_{\lbrace y \rbrace} = y,S_{\lbrace y \rbrace} < S_{\lbrace x \rbrace} \wedge N]$$
    $$\stackrel{\mathrm{Satz \: \ref{starke Markoveigenschaft}}}{=} \mathbb{P}_{z}[S_{\lbrace y \rbrace} < S_{\lbrace x \rbrace} \wedge N] \mathbb{P}_{y}[X_{n} = y, n < S_{\lbrace x \rbrace} \wedge N] \qquad \forall \: n \in \mathbb{N}_{0}$$
    Daraus folgt
    $$\mathbb{E}_{x}[\sum_{n=0}^{S_{\lbrace x \rbrace} \wedge N -1}  \mathbbm{1}_{X_{n} = y}] = \mathbb{E}_{x}[\sum_{n=S_{\lbrace y \rbrace}}^{S_{\lbrace x \rbrace} \wedge N -1}  \mathbbm{1}_{X_{n} = y} \mathbbm{1}_{S_{\lbrace y \rbrace} < S_{\lbrace x \rbrace} \wedge N}]$$
    $$= \sum_{n=0}^{\infty} \mathbb{P}_{x}[X_{S_{\lbrace y \rbrace} + n}=y,n<S_{\lbrace x \rbrace} \wedge N - S_{\lbrace y \rbrace}, S_{\lbrace y \rbrace} < S_{\lbrace x \rbrace} \wedge N]$$
    $$= \mathbb{P}_{x}[S_{\lbrace y \rbrace} < S_{\lbrace x \rbrace} \wedge N]= \sum_{n=0}^{\infty} \mathbb{P}_{x}[X_{n}=y,n<S_{\lbrace x \rbrace} \wedge N]$$
    $$= \mathbb{P}_{x}[S_{\lbrace y \rbrace} < S_{\lbrace x \rbrace} \wedge N]\mathbb{E}_{y}[\sum_{n=0}^{S_{\lbrace x \rbrace} \wedge N -1}  \mathbbm{1}_{X_{n} = y}]$$
    sowie
    $$\mathbb{E}_{y}[\sum_{n=0}^{S_{\lbrace x \rbrace} \wedge N -1}  \mathbbm{1}_{X_{n} = y}] = 1 + \mathbb{E}_{y}[\sum_{n=S_{\lbrace y \rbrace}}^{S_{\lbrace x \rbrace} \wedge N -1}  \mathbbm{1}_{X_{n} = y} \mathbbm{1}_{S_{\lbrace y \rbrace} < S_{\lbrace x \rbrace} \wedge N}]$$
    $$= 1 + \sum_{n=0}^{\infty} \mathbb{P}_{y}[X_{S_{\lbrace y \rbrace} + n}=y,n<S_{\lbrace x \rbrace} \wedge N - S_{\lbrace y \rbrace}, S_{\lbrace y \rbrace} < S_{\lbrace x \rbrace} \wedge N]$$
    $$= 1 + \mathbb{P}_{y}[S_{\lbrace y \rbrace} < S_{\lbrace x \rbrace} \wedge N]= \sum_{n=0}^{\infty} \mathbb{P}_{x}[X_{n}=y,n<S_{\lbrace x \rbrace} \wedge N]$$
    $$= 1 + \mathbb{P}_{y}[S_{\lbrace y \rbrace} < S_{\lbrace x \rbrace} \wedge N]\mathbb{E}_{y}[\sum_{n=0}^{S_{\lbrace x \rbrace} \wedge N -1}  \mathbbm{1}_{X_{n} = y}]$$
    $$\Leftrightarrow \mathbb{E}_{y}[\sum_{n=0}^{S_{\lbrace x \rbrace} \wedge N -1}  \mathbbm{1}_{X_{n} = y}] = \dfrac{1}{ \mathbb{P}_{y}[S_{\lbrace x \rbrace} \wedge N < S_{\lbrace y \rbrace}]}$$
    Aus der monotonen Konvergenz und der Stetigkeit der Maße
    $\mathbb{P}_{x}$ und $\mathbb{P}_{y}$ ergibt sich
    $$\mathbb{E}_{x}[\sum_{n=0}^{S_{\lbrace x \rbrace} -1}  \mathbbm{1}_{X_{n} = y}] \stackrel{\mathbb{P}_{x}[S_{\lbrace x \rbrace} < \infty]=1}{=} \lim_{N \to \infty} \mathbb{E}_{x}[\sum_{n=0}^{S_{\lbrace x \rbrace} \wedge N -1}  \mathbbm{1}_{X_{n} = y}]$$
    $$= \lim_{N \to \infty} \dfrac{\mathbb{P}_{x}[S_{\lbrace y \rbrace} < S_{\lbrace x \rbrace} \wedge N ]}{\mathbb{P}_{y}[S_{\lbrace x \rbrace} \wedge N < S_{\lbrace y \rbrace}]} \stackrel{\mathbb{P}_{x}[S_{\lbrace x \rbrace} < \infty]=1}{=} \dfrac{\mathbb{P}_{x}[S_{\lbrace y \rbrace} < S_{\lbrace x \rbrace}]}{\mathbb{P}_{y}[S_{\lbrace x \rbrace} < S_{\lbrace y \rbrace}]}$$
    Insbesondere ist $\mu_{x}(x) =1$ nach Definition.
    $\mu_{x}(y) \in (0, \infty)$ für alle $y \in K$ und $\mu_{x}(y) = 0$
    für alle $y \in K^{C}$, da in diesem Fall $p_{n}(x,y) = 0$ für alle
    $n \in \mathbb{N}$.

-   Für $y \in K^{C}$ folgt wegen $z \not\rightarrow y$ für alle
    $z \in K$
    $$\sum_{z \in E} \mu_{x}(z)p(z,y) = \sum_{z \in K}\mu_{x}(z)p(z,y) = 0 = \mu_{x}(y)$$
    Sei also nun $y \in K$. Da $x \in K$ nach Voraussetzung rekurrent
    ist, gilt
    $$\mu_{x}(y) = \mathbb{E}_{x}[\sum_{n=0}^{S_{\lbrace x \rbrace}}  \mathbbm{1}_{X_{n} = y}] + \mathbb{P}_{x}[X_{0} = y] - \mathbb{P}_{x}[X_{S_{\lbrace x \rbrace}} = y, S_{\lbrace x \rbrace} < \infty]  \qquad (\star)$$
    $$= \sum_{n=1}^{\infty} \mathbb{P}_{x}[X_{n}=y, S_{\lbrace x \rbrace} \geq n] + \mathbbm{1}_{x=y} \left( 1 - \underbrace{\mathbb{P}_{x}[S_{\lbrace x \rbrace} < \infty]}_{=1} \right)$$
    $$= \sum_{n=1}^{\infty} \sum_{z \in E}\mathbb{P}_{x}[X_{n}=y, X_{n-1} = z, S_{\lbrace x \rbrace} \geq n]$$
    $$= \sum_{n=1}^{\infty} \sum_{z \in K}\mathbb{P}_{x}[X_{n-1} = z, S_{\lbrace x \rbrace} \geq n]\mathbb{P}_{x}[X_{n}=y \: | \: X_{n-1} = z, S_{\lbrace x \rbrace} \geq n]$$
    Da
    $\lbrace S_{\lbrace x \rbrace} \geq n \rbrace = {\lbrace S_{\lbrace x \rbrace} \leq n-1 \rbrace}^{C} \in \mathfrak{F}^{X}_{n-1}$,
    folgt aus Satz $\ref{vorangegangene und zukünftige Ereignisse}$
    $$= \sum_{n=1}^{\infty} \sum_{z \in K}\mathbb{P}_{x}[X_{n-1} = z, S_{\lbrace x \rbrace} - 1 \geq n-1]\mathbb{P}_{z}[X_{1}=y]$$
    $$= \sum_{z \in K} p(z,y)\mathbb{E}_{x}[\sum_{n=0}^{S_{\lbrace x \rbrace}-1}  \mathbbm{1}_{X_{n} = z}]$$
    $$= \sum_{z \in K} p(z,y) \mu_{x}(z)$$ Also ist $\mu_{x}$ invariant
    bzgl. $P$.

-   Sei $\lambda$ ein invariantes Maß bzgl. $P$ auf E mit
    $\lambda(x) = 1$ für ein $x \in K$ und $\lambda(y) = 0$ für alle
    $y \in K^{C}$.\
    \
    :
    $\quad \lambda(y) \geq \sum_{n=1}^{N} \mathbb{P}_{x}[S_{\lbrace x \rbrace} \geq n, X_{n} = y] \qquad \forall y \in K \quad \forall N \in \mathbb{N}$\
    \
    **IA** $N=1 \: : \:$ Da $\lambda$ invariant ist, gilt für alle
    $y \in K$
    $$\lambda(y) = \sum_{z \in E} \lambda(z)p(z,y) \geq \underbrace{\lambda(x)}_{=1}p(x,y) = \mathbb{P}_{x}[X_{1}=y] = \mathbb{P}_{x}[S_{\lbrace x \rbrace} \geq 1, X_{1} = y]$$\
    **IS** $N \to N+1 \: : \:$ Für $y \in K$ gilt\
    \
    $$\lambda(y) = \sum_{z \in E} \lambda(z)p(z,y) = \sum_{z \in K \setminus \lbrace x \rbrace} \lambda(z)p(z,y) + \lambda(x)p(x,y)$$
    $$\stackrel{\mathrm{IV}}{\geq} \sum_{z \in K \setminus \lbrace x \rbrace} \sum_{n=1}^{N} \mathbb{P}_{x}[S_{\lbrace x \rbrace} \geq n, X_{n} = z]p(z,y) + \mathbb{P}_{x}[S_{\lbrace x \rbrace} \geq 1, X_{1} = y]$$
    Da
    $\lbrace S_{\lbrace x \rbrace} \geq n + 1 \rbrace = {\lbrace S_{\lbrace x \rbrace} \leq n \rbrace}^{C} \in \mathfrak{F}^{X}_{n}$
    gilt für alle $z \in K \setminus \lbrace x \rbrace$
    $$\mathbb{P}_{x}[S_{\lbrace x \rbrace} \geq n+1, X_{n} = z, X_{n+1} = y]$$
    $$= \mathbb{P}_{x}[S_{\lbrace x \rbrace} \geq n+1, X_{n} = z] \mathbb{P}_{x}[ X_{n+1} = y \: | \: X_{n} = z, S_{\lbrace x \rbrace} \geq n+1]$$
    $$\stackrel{\mathrm{Satz} \:\ref{vorangegangene und zukünftige Ereignisse}}{=} \mathbb{P}_{x}[S_{\lbrace x \rbrace} \geq n+1, X_{n} = z] \mathbb{P}_{z}[ X_{1} = y]$$
    $$\stackrel{z \neq x}{=} \mathbb{P}_{x}[S_{\lbrace x \rbrace} \geq n, X_{n} = z]p(z,y)$$
    Daraus folgt
    $$\lambda(y) \geq \sum_{z \in K \setminus \lbrace x \rbrace} \sum_{n=1}^{N} \mathbb{P}_{x}[S_{\lbrace x \rbrace} \geq n+1, X_{n} = z, X_{n+1}=y] + \mathbb{P}_{x}[S_{\lbrace x \rbrace} \geq 1, X_{1} = y]$$
    $$=  \sum_{n=1}^{N} \mathbb{P}_{x}[S_{\lbrace x \rbrace} \geq n+1, X_{n+1}=y] + \mathbb{P}_{x}[S_{\lbrace x \rbrace} \geq 1, X_{1} = y]$$
    $$= \sum_{n=1}^{N+1} \mathbb{P}_{x}[S_{\lbrace x \rbrace} \geq n, X_{n}=y]$$\
    : $\lambda = \mu_{x}$\
    \
    Zunächst einmal folgt aus der monotonen Konvergenz, dass
    $$\lambda(y) \geq \lim_{N \to \infty} \sum_{n=1}^{N} \mathbb{P}_{x}[S_{\lbrace x \rbrace} \geq n, X_{n}=y] = \mathbb{E}_{x}[\sum_{n=1}^{S_{\lbrace x \rbrace}}  \mathbbm{1}_{X_{n} = y}] = \mu_{x}(y)$$
    Insbesondere ist $\lambda - \mu_{x}$ ein invariantes Maß mit
    $(\lambda - \mu_{x})(y)=0$ für alle
    $y \in K^{C} \cup \lbrace x \rbrace$. Für
    $y \in K \setminus \lbrace x \rbrace$ gibt es, da
    $x \leftrightarrow y$, ein $n \in \mathbb{N}$ mit $p_{n}(y,x)>0$.
    Daraus folgt
    $$0 = (\lambda - \mu_{x})(x) = \sum_{z \in E} \underbrace{(\lambda - \mu_{x})(z)}_{\geq 0}p_{n}(z,x) \geq (\lambda - \mu_{x})(y)\underbrace{p_{n}(y,x)}_{>0}$$
    Folglich ist $(\lambda - \mu_{x})(y)=0$ für jedes
    $y \in K \setminus \lbrace x \rbrace$. Also $\lambda = \mu_{x}$

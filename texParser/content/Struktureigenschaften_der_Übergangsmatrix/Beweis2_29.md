---
 title: "Beweis2_29"
 mathjax : true
---
Zunächst einmal ist
$\lbrace T \leq n-1 \rbrace \in \mathfrak{F}_{n-1}^{X}$ für jedes
$n \in \mathbb{N}$. Weiterhin gilt
$$\mathbb{P}_{x}[X_{T \wedge n} = y] = \mathbb{P}_{x}[X_{T \wedge n} = y, T \leq n - 1] + \mathbb{P}_{x}[X_{T \wedge n} = y, T > n - 1]$$
$$= \mathbb{P}_{x}[X_{T} = y, T \leq n-1] + \sum_{z \in E} \mathbb{P}_{x}[X_{n-1}=z, T > n-1]\mathbb{P}_{x}[X_{n}=y \:| \: \underbrace{T > n-1}_{\in \mathfrak{F}_{n-1}^{X}}, X_{n-1} = z]$$
$$= \mathbb{P}_{x}[X_{T} = y, T \leq n-1] + \sum_{z \in E} \mathbb{P}_{x}[X_{n-1}=z, T > n-1]p(z,y)$$
Daraus folgt
$$\mathbb{E}_{x}[f(X_{T \wedge n})] = \sum_{y \in E} f(y) \mathbb{P}_{x}[X_{T \wedge n}=y]$$
$$= \sum_{y \in E} f(y) \mathbb{P}_{x}[X_{T} = y, T \leq n-1] + \sum_{z \in E} (Pf)(z) \mathbb{P}_{x}[X_{n-1}=z, T > n-1]$$
$$= \mathbb{E}_{x}[f(X_{T \wedge (n-1)}) \mathbbm{1}_{T \leq n-1}] + \mathbb{E}_{x}[(Pf)(X_{n-1})\mathbbm{1}_{T > n-1}]$$
Daraus ergibt sich dann aber
$$\mathbb{E}_{x}[f(X_{T \wedge n})] = \mathbb{E}_{x}[f(X_{T \wedge (n-1)})] + \mathbb{E}_{x}[(Lf)(X_{n-1})\mathbbm{1}_{T > n-1}]$$
Induktiv folgt somit
$$\mathbb{E}_{x}[f(X_{T \wedge n})] - f(x) = \sum_{k=1}^{n} \mathbb{E}_{x}[(Lf)(X_{k-1})\mathbbm{1}_{T > k-1}]$$
$$= \mathbb{E}_{x}[\sum_{k=0}^{n-1} (Lf)(X_{k})\mathbbm{1}_{T > k}] = \mathbb{E}_{x}[\sum_{k=0}^{T \wedge n-1} (Lf)(X_{k})]$$
Da nach Vorraussetzung f beschränkt ist und $\mathbb{E}_{x}[T]<\infty$
ist, so folgt aus dem Satz von Lebesgue
$$\mathbb{E}_{x}[f(X_{T})] - f(x) = \lim_{n \to \infty} \mathbb{E}_{x}[f(X_{T \wedge n})] - f(x)$$
$$= \lim_{n \to \infty} \mathbb{E}_{x}[\sum_{k=0}^{(T \wedge n)-1} (Lf)(X_{k})] =  \mathbb{E}_{x}[\sum_{k=0}^{T-1} (Lf)(X_{k})].$$

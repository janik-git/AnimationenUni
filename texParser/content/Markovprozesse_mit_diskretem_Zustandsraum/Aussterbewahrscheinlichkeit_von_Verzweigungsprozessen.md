---
 title: "Aussterbewahrscheinlichkeit_von_Verzweigungsprozessen"
 mathjax : true
---
Sei $(X_{n})_{n \in \mathbb{N}_{0}}$ ein Verzweigungsprozess, d.h.
$(X_{n})_{n \in \mathbb{N}_{0}}$ ist eine Markovkette mit Zustandsraum
$E = \mathbb{N}_{0}$ und Übergangsmatrix $P = (p(x,y))_{x,y \in E}$
$$p(x,y) = \mu^{*x}(y) \qquad \mathrm{mit} \: \mu^{*0}(y) := \mathbbm{1}_{\lbrace 0 \rbrace}(y)$$
wobei $\mu$ eine gegebene Wahrscheinlichkeitsverteilung auf E ist.\
\
[Ziel]{.ul}: Berechne
$\mathbb{P}_{x}[T_{\lbrace 0 \rbrace} < \infty ], \: x \in E$ (=
Aussterbewahrscheinlichkeit)\
[Beh.]{.ul}: Für alle $n \in \mathbb{N}_{0}$ gilt
$\mathbb{P}_{x}[X_{n} = 0] = \mathbb{P}_{1}[X_{n} = 0]^{x}$, $x \in E$\
\
Beweis durch vollständige Induktion über n.\
\
**IA** $n=0$ :
$\mathbb{P}_{x}[X_{0} = 0] = \mathbbm{1}_{\lbrace x \rbrace}(0) = \mathbb{P}_{1}[X_{0} = 0]^{x}$,
$(0^{0} = 1)$\
**IS** $n \to n+1$ : Es gilt nun aber
$$\mathbb{P}_{x}[X_{n+1} = 0] = \sum_{y \in E} \mathbb{P}[X_{n+1} = 0, X_{1} = y \: | \: X_{0} = x]$$
$$=\sum_{y \in E} \mathbb{P}[X_{1} = y \: | \: X_{0} = x] \cdot \mathbb{P}[X_{n+1} = 0 \: | \: X_{0} = x, X_{1} = y ]$$
$$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=}   \sum_{y \in E} p(x,y) \cdot \mathbb{P}_{y}[X_{n} = 0]$$
Nach Induktionsvoraussetzung gilt weiterhin
$$\sum_{y \in E} p(x,y) \cdot \mathbb{P}_{y}[X_{n} = 0] \stackrel{\mathrm{IV}}{=}  \sum_{y \in E} \mu^{*x}(y) \cdot \mathbb{P}_{1}[X_{n} = 0]^{y}$$
$$\sum_{y \in E} \sum_{y_{1} +....+ y_{x} = y} \mu(y_{1}) \cdot ... \cdot \mu(y_{x}) \mathbb{P}_{1}[X_{n} = 0]^{y_{1}+...+y_{x}}$$
$$= \sum_{y_{1},...,y_{x} \geq 0 } \mu(y_{1}) \mathbb{P}_{1}[X_{n} = 0]^{y_{1}} \cdot...\cdot \mu(y_{x}) \mathbb{P}_{1}[X_{n} = 0]^{y_{x}}$$
$$= (\sum_{z \geq 0} \mu(z) \mathbb{P}_{1}[X_{n} = 0]^{z})^{x}$$
$$\stackrel{\mathrm{IV}}{=} (\sum_{z \in E} p(1,z) \mathbb{P}_{z}[X_{n} = 0])^{x}$$
$$\stackrel{\mathrm{Satz} \: \ref{vorangegangene und zukünftige Ereignisse}}{=}   \mathbb{P}_{1}[X_{n+1} = 0]^{x}$$
Da $\lbrace T_{\lbrace 0 \rbrace} \leq n \rbrace$ =
$\lbrace X_{n} = 0 \rbrace$ für alle $n \in \mathbb{N}_{0}$ und
$\lbrace T_{\lbrace 0 \rbrace}  \leq n \rbrace$ $\uparrow$
$\bigcup_{k=0}^{\infty}$ $\lbrace T_{\lbrace 0 \rbrace} \leq k \rbrace$
$=$ $\lbrace T_{\lbrace 0 \rbrace} < \infty \rbrace$ für $n \to \infty$
folgt aus der Stetigkeit von $\mathbb{P}_{x}$
$$\mathbb{P}_{x}[T_{\lbrace 0 \rbrace} < \infty] = \lim_{n \to \infty} \mathbb{P}_{x}[X_{n} = 0] = \lim_{n \to \infty} \mathbb{P}_{1}[X_{n} = 0]^{x} = \mathbb{P}_{1}[T_{\lbrace 0 \rbrace} < \infty]^{x}$$
Folglich gilt
$h_{\lbrace 0 \rbrace}(x) = h_{\lbrace 0 \rbrace}(1)^{x} =: q^{x}$ für
alle $x \in E$. Im folgenden soll $q \in [0,1]$ bestimmt werden. Da nach
Satz $\ref{Dirichletsatz}$ $h_{\lbrace 0 \rbrace}$ die kleinste,
nichtnegative Lösung des Dirichletproblems ist, gilt
$$(Lh_{\lbrace 0 \rbrace})(1) = 0 \: \Leftrightarrow \: q = h_{\lbrace 0 \rbrace}(1) = \sum_{y \in E} \mu(y) \cdot  h_{\lbrace 0 \rbrace}(1)^{y} = G_{\mu}(q),$$
wobei $$G_{\mu}(s) := \sum_{y \in E} \mu(y) s^{y}, \: s \in [0,1]$$ Die
erzeugende Funktion von $\mu$ ist. Also ist q ein Fixpunkt der Gleichung
$$s = G_{\mu}(s)$$ Ist nun $\overline{q}$ ein weiterer Fixpunkt, so
genügt die Funktion $h(x) := \overline{q}^{x}$ ebenfalls dem
Dirichletproblem. Dann folgt aus Satz
[\[Dirichletsatz\]](#Dirichletsatz){reference-type="ref"
reference="Dirichletsatz"}
$$\overline{q} = h(1) \geq  h_{\lbrace 0 \rbrace}(1) = q,$$ d.h. q ist
der kleinste, nichtnegative Fixpunkt der Gleichung $s = G_{\mu}(s)$.\
\
Nachfolgend soll der kleinste nichtnegative Fixpunkt der Gleichung
$s = G_{\mu}(s)$ genauer analysiert werden. Da $\mu$ ein
Wahrscheinlichkeitsmaß auf E ist, gilt
$$G_{\mu}(1) = \sum_{y \in E} \mu(y) = 1$$ Falls $\mu$ entweder linear
$(\mu(0) + \mu(1) = 1)$ oder strikt konvex mit
$$G'_{\mu}(1) = \lim_{s \uparrow 1} G'_{\mu}(s) = \lim_{s \uparrow 1} \sum_{ k \geq 1} k \cdot \mu(k) \cdot s^{k-1} = \sum_{ k \geq 0} k \cdot \mu(k) < \infty$$
so gilt

. ![Fixpunktanalyse](beispiel24 "fig:")

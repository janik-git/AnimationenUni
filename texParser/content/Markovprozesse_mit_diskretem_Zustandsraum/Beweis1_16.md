---
 title: "Beweis1_16"
 mathjax : true
---
Für $x \in E$ definiere
$$S_{\lbrace x \rbrace}^{0} := 0 \quad und \quad S_{\lbrace x \rbrace}^{k} := \inf \lbrace n > S_{\lbrace x \rbrace}^{k-1} \: : \: X_{n} = x \rbrace \: , \quad k \in \mathbb{N}$$
Dann gilt für alle $k \in \mathbb{N}$
$$\lbrace V_{ \lbrace x \rbrace} > k \rbrace \cap \lbrace X_{0} = x \rbrace = \lbrace S_{\lbrace x \rbrace}^{k} < \infty \rbrace \cap \lbrace X_{0} = x \rbrace .$$
Aus der starken Markoveigenschaft folgt somit
$$\mathbb{P}_{x}[V_{ \lbrace x \rbrace} > k+1 \: | \: V_{ \lbrace x \rbrace} > k] = \mathbb{P}_{\lbrace x \rbrace}[S_{\lbrace x \rbrace}^{k+1} < \infty \: | \: S_{\lbrace x \rbrace}^{k} < \infty]$$
$$= \mathbb{P}_{x}[S_{\lbrace x \rbrace}^{k+1} < \infty \: | \: X_{S_{\lbrace x \rbrace}^{k}} = x, S_{\lbrace x \rbrace}^{k} < \infty]$$
$$= \mathbb{P}_{\nu}[\inf \lbrace n>0 \: : \: X_{S_{\lbrace x \rbrace}^{k} + n} = x \rbrace + S_{\lbrace x \rbrace}^{k} < \infty  \: | \: X_{0} = x,X_{S_{\lbrace x \rbrace}^{k}} = x, S_{\lbrace x \rbrace}^{k} < \infty]$$
$$\stackrel{\mathrm{Satz} \: \ref{starke Markoveigenschaft}}{=} \mathbb{P}_{x}[S_{\lbrace x \rbrace}^{1} < \infty]$$
Daraus folgt dann
$$\mathbb{P}_{x}[V_{x} > k] = \prod_{l=1}^{k-1} \mathbb{P}_{x}[V_{x} > l + 1 \: | \: V_{x} > l] \cdot \mathbb{P}_{x}[V_{x} > 1] \stackrel{\mathrm{Satz} \: \ref{starke Markoveigenschaft}}{=} \mathbb{P}_{x}[S_{\lbrace x \rbrace}^{1} < \infty]^{k}.$$
Weiterhin gilt im Falle
$\mathbb{P}_{x}[S_{\lbrace x \rbrace}^{1} < \infty] < 1$
$$\mathbb{E}_{x}[V_{x}] = \sum_{k=0}^{\infty}\mathbb{P}_{x}[V_{x} > k] = 1 + \sum_{k=1}^{\infty}\mathbb{P}_{x}[V_{x} > k] = 1 + \sum_{k=1}^{\infty}\mathbb{P}_{x}[S_{\lbrace x \rbrace}^{1} < \infty]^{k}$$
$$= \dfrac{1}{1-\mathbb{P}_{x}[S_{\lbrace x \rbrace}^{1} < \infty]} = \dfrac{1}{\mathbb{P}_{x}[S_{\lbrace x \rbrace}^{1} = \infty]}$$

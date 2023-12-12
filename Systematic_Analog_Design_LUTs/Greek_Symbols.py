# %% 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Here is a list of Greek letters and their corresponding LaTeX commands:

# Table

# Letter	LaTeX Command
# Alpha	\\alpha
# Beta	\\beta
# Gamma	\\gamma
# Delta	\\delta
# Epsilon	\\epsilon
# Zeta	\\zeta
# Eta	\\eta
# Theta	\\theta
# Iota	\\iota
# Kappa	\\kappa
# Lambda	\\lambda
# Mu	\\mu
# Nu	\\nu
# Xi	\\xi
# Omicron	\\omicron
# Pi	\\pi
# Rho	\\rho
# Sigma	\\sigma
# Tau	\\tau
# Upsilon	\\upsilon
# Phi	\\phi
# Chi	\\chi
# Psi	\\psi
# Omega	\\omega
# You can find a more comprehensive list of mathematical symbols and their LaTeX commands on Overleaf1 or LaTeX-Tutorial.com2. I hope this helps!
# https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols
# https://latex-tutorial.com/symbols/greek-alphabet/
# https://quickref.me/latex

# %% 
# Greek letters
# {\displaystyle \alpha A}	\alpha A	{\displaystyle \nu N}	\nu N
# {\displaystyle \beta B}	\beta B	{\displaystyle \xi \Xi }	\xi \Xi
# {\displaystyle \gamma \Gamma }	\gamma \Gamma	{\displaystyle oO\;}	o O
# {\displaystyle \delta \Delta }	\delta \Delta	{\displaystyle \pi \Pi }	\pi \Pi
# {\displaystyle \epsilon \varepsilon E\;}	\epsilon \varepsilon E	{\displaystyle \rho \varrho P\;}	\rho \varrho P
# {\displaystyle \zeta Z}	\zeta Z	{\displaystyle \sigma \,\!\Sigma \;}	\sigma \Sigma
# {\displaystyle \eta H}	\eta H	{\displaystyle \tau T}	\tau T
# {\displaystyle \theta \vartheta \Theta }	\theta \vartheta \Theta	{\displaystyle \upsilon \Upsilon }	\upsilon \Upsilon
# {\displaystyle \iota I}	\iota I	{\displaystyle \phi \varphi \Phi }	\phi \varphi \Phi
# {\displaystyle \kappa K}	\kappa K	{\displaystyle \chi X}	\chi X
# {\displaystyle \lambda \Lambda \;}	\lambda \Lambda	{\displaystyle \psi \Psi }	\psi \Psi
# {\displaystyle \mu M}	\mu M	{\displaystyle \omega \Omega }	\omega \Omega
# Arrows
# {\displaystyle \leftarrow }	\leftarrow	{\displaystyle \Leftarrow }	\Leftarrow
# {\displaystyle \rightarrow }	\rightarrow	{\displaystyle \Rightarrow \;}	\Rightarrow
# {\displaystyle \leftrightarrow }	\leftrightarrow	{\displaystyle \rightleftharpoons }	\rightleftharpoons
# {\displaystyle \uparrow }	\uparrow	{\displaystyle \downarrow }	\downarrow
# {\displaystyle \Uparrow \;}	\Uparrow	{\displaystyle \Downarrow }	\Downarrow
# {\displaystyle \Leftrightarrow \;}	\Leftrightarrow	{\displaystyle \Updownarrow }	\Updownarrow
# {\displaystyle \mapsto }	\mapsto	{\displaystyle \longmapsto \;}	\longmapsto
# {\displaystyle \nearrow }	\nearrow	{\displaystyle \searrow }	\searrow
# {\displaystyle \swarrow }	\swarrow	{\displaystyle \nwarrow }	\nwarrow
# {\displaystyle \leftharpoonup }	\leftharpoonup	{\displaystyle \rightharpoonup }	\rightharpoonup
# {\displaystyle \leftharpoondown }	\leftharpoondown	{\displaystyle \rightharpoondown }	\rightharpoondown		
# Miscellaneous symbols
# {\displaystyle \infty \;\;}	\infty	{\displaystyle \forall \;}	\forall
# {\displaystyle \Re }	\Re	{\displaystyle \Im }	\Im
# {\displaystyle \nabla }	\nabla	{\displaystyle \exists }	\exists
# {\displaystyle \partial }	\partial	{\displaystyle \nexists }	\nexists
# {\displaystyle \emptyset }	\emptyset	{\displaystyle \varnothing \;}	\varnothing
# {\displaystyle \wp }	\wp	{\displaystyle \complement }	\complement
# {\displaystyle \neg }	\neg	{\displaystyle \cdots }	\cdots
# {\displaystyle \square }	\square	{\displaystyle \surd }	\surd
# {\displaystyle \blacksquare }	\blacksquare	{\displaystyle \triangle }	\triangle
# Binary Operation/Relation Symbols
# {\displaystyle \times }	\times	{\displaystyle \cdot }	\cdot
# {\displaystyle \div }	\div	{\displaystyle \cap }	\cap
# {\displaystyle \cup }	\cup	{\displaystyle \neq \;}	\neq
# {\displaystyle \leq }	\leq	{\displaystyle \geq }	\geq
# {\displaystyle \in }	\in	{\displaystyle \perp \;}	\perp
# {\displaystyle \notin }	\notin	{\displaystyle \subset }	\subset
# {\displaystyle \simeq }	\simeq	{\displaystyle \approx }	\approx
# {\displaystyle \wedge }	\wedge	{\displaystyle \vee }	\vee
# {\displaystyle \oplus \;}	\oplus	{\displaystyle \otimes }	\otimes
# {\displaystyle \Box }	\Box	{\displaystyle \boxtimes }	\boxtimes
# {\displaystyle \equiv }	\equiv	{\displaystyle \cong }	\cong

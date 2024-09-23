""" 
A *congruência de Zeller* é um algoritmo inventado pelo matemático alemão Julius Christian Zeller 
(1822–1899) para calcular o dia da semana para qualquer dia do calendário. Para o nosso calendário, 
o calendário Gregoriano, a congruência de Zeller é dada por:
$$h=\left(q+\left\lfloor \frac{13(m+1)}{5}\right\rfloor+K+\left\lfloor\frac{K}{4}\right\rfloor+\left\lfloor\frac{J}{4}\right\rfloor-2J\right) \mod 7$$
em que $h$ é o dia da semana ($0 =$ Sábado, $1 =$ Domingo, ...), $q$ é o dia do mês, $m$ é o mês ($3 =$ março, $4 =$ abril, ..., $14 =$ fevereiro) – 
os meses de janeiro e fevereiro são contados como os meses $13$ e $14$ do ano anterior, $K$ é o ano do século (ano $\mod 100$), $J$ é o século 
$\left(\lfloor ano/100\rfloor\right)$. Esta expressão utiliza a função matemática, chão, denotada por $\lfloor\cdot\rfloor$, a qual converte um número real $x$
no maior número inteiro menor ou igual a $x$. A definição formal desta função é $\lfloor x\rfloor = \max\{m\in\mathbb Z\,|\,m\leq x\}$.
A expressão utiliza também a função módulo, em que $a\mod b$ representa o resto da divisão inteira de $a$ por $b$ (i.e., $a\%b$). 

Escreva uma função em **Python**, chamada `dia_da_semana`, que recebe três inteiros 
correspondentes a um dia, um mês e um ano e que devolve o dia da semana em que calha essa data. 
A sua função pode utilizar outras funções auxiliares a definir por si. 
Por exemplo

```Python
dia_da_semana(18, 1, 2014)
'sabado'
```"""
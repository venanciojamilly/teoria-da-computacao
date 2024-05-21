[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Oq4HJ_Kz)
# Exercício Prático 02 (EP02)

Este repositório apresenta um template para a execução do EP02. O objetivo é construir Máquinas de Turing usando a biblioteca [automata-lib](https://pypi.org/project/automata-lib/) de Python.
Documentação detalhada da api encontra-se no [repositório](https://caleb531.github.io/automata/) do GitHub.

**Observações Gerais:**

* Não altere a estrutura do repositório ou modifique nomes dos arquivos ou folders;

* Não altere arquivos da pasta test ou workflows;

* Não altere os nomes das variáveis que definem os autômatos ou expressões regulares solicitados, visto que esta atividade será avaliada através de testes automáticos;

* As soluções devem ser implementadas exclusivamente usando a biblioteca **automata-lib** ou **re** conforme solicitado em cada questão;

* Organize o código de forma consistente para facilitar sua legibilidade. Por exemplo, evite espaçamentos entre linhas ou identação inconsistentes; use nomes significativos;

* Cada grupo deverá realizar este trabalho de forma individual apresentando sua própria resposta. As respostas serão inspecionadas visualmente e mecanicamente com ferramentas especializadas. Nesta inspeção, caso seja detectada cópia de resposta, o(s) grupo(s) envolvido(s) sofrerão penalidade na nota e poderão ficar com nota 0;

* É importante salientar que é de responsabilidade do grupo manter o sigilo sobre sua solução. Para tal, não deixe sua solução em locais de visibilidade pública e acesso trivial;

* O trabalho deve ser realizado estritamente em grupo. A realização e entrega individual será penalizada com diminuição de 30% do valor da nota. Casos excepcionais, tais como assistência domiciliar ou desistência/indisponibilidade de membro(s) do grupo devem ser comunicados com antecedência.

Entrega:

* Realizar push com a versão final do repositório;
* Confira o status da execução automática dos testes na aba Actions no GitHub;
* Caso seu projeto contenha algum erro de compilação, nenhum teste será executado e, portanto, não poderá ser corrigido;
* A participação de cada membro será comprovada através do histórico de edições e *commits* do repositório. A nota será dada apenas para aqueles que editarem efetivamente o repositório utilizando o *login* específico atribuído no Team do github (conta vinculada ao seu @ccc.ufcg.edu.br);
* Caso o repositório seja editado após o prazo para entrega, a atividade será considerada como reposição.

## Questão 01

Construa uma Máquina de Turing Determinística (DTM) que recebe como entrada uma cadeia de símbolos no alfabeto $\Sigma = $`{a,b,A,B}` e converte todos os símbolos maiúsculos para minúsculos. Considere que o caracter branco é representado por `.`.

Como exemplo, considere a seguinte entrada `AAaBB`. A máquina deve produzir a seguinte cadeia na saída ao parar no estado de aceitação: `aaabb`. A saída pode conter símbolos branco antes ou após a cadeia. Por exemplo, `aaabb..`.

Arquivos: 
* src/Q01.py (local onde o dfa deve ser definido)
* test/test_Q01.py

Execução dos testes automáticos: 

      python -m unittest -v test/test_Q01.py

## Questão 02

Construa uma Máquina de Turing Determinística (DTM), que recebe uma expressão sobre o alfabeto $\Sigma = $ `{a,b,+}`, onde `+` representa a operação de concatenação de cadeias, e realiza concatenação das cadeias presentes na expressão. Por exemplo, para entrada `a+bb+ab+a`, a máquina deve produzir `abbaba`. Símbolos branco antes ou após a cadeia podem ocorrer.
A máquina considera que a cadeia vazia é representada pela ausência de símbolos. Desta forma a entrada `a++b` é válida e deve produzir a seguinte saída: `ab`.
Considere que o caracter branco é representado por `.`.

Arquivos: 
* src/Q02.py (local onde o nfa deve ser definido)
* test/test_Q02.py

Execução dos testes automáticos: 

      python -m unittest -v test/test_Q02.py


## Questão 03

Construa uma Máquina de Turing Multifita (MNTM) com 2 fitas que seja equivalente a máquina da questão (02).
O resultado da computação deve estar na fita 2 quando a máquina parar. Considere que o caracter branco é representado por `.`.

Arquivos: 
* src/Q03.py (local onde o nfa deve ser definido)
* test/test_Q03.py

Execução dos testes automáticos: 

      python -m unittest -v test/test_Q03.py

# Questão 04

Construa uma Máquina de Turing Multifita (MNTM) com 2 fitas sobre o alfabeto $\Sigma =$ `{a, b, #}` que recebe como entrada uma cadeia `s#w`, onde $s$ e $w$ são cadeias em `{a,b}*` e para em um estado de aceitação se $s$ for uma subcadeia de $w$. Caso contrário, para em um outro estado qualquer que não seja de aceitação.

Por exemplo, para a entrada `ab#aaaabaaab`, a máquina deve parar em um estado de aceitação. No entanto, para a entrada `ab#aaaaaaa`, a máquina para em um estado que não é de aceitação.
Considere que o caracter branco é representado por `.`.

Arquivos: 
* src/Q04.py (local onde o nfa deve ser definido)
* test/test_Q04.py

Execução dos testes automáticos: 

      python -m unittest -v test/test_Q04.py


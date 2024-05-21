[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/0EL-SkU_)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14153209&assignment_repo_type=AssignmentRepo)
# Exercício Prático 01 (EP01)

Este repositório apresenta um template para a execução do EP01. O objetivo é construir automatos usando a biblioteca [automata-lib](https://pypi.org/project/automata-lib/) e implementar expressões regulares usando a biblioteca [re](https://docs.python.org/3/library/re.html) de python.

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

Em algumas linguagens de programação, comentários aparecem entre delimitadores como `/#` e `#/`. Seja $C$ uma linguagem de comentários corretamente delimitados. Uma cadeia $w$ pertence a $C$ se inicia com `/#` e termina com `#/`, mas não pode conter `#` ou `/` como subcadeia intermediária. Considere que $\Sigma$ = {`l`, `n`, `b`, `/`, `#`}, onde `l` representa letras, `n` representa dígitos numéricos, `b` representa espaço em branco.
Construa um DFA que reconhece $C$ usando a biblioteca **automata-lib**.


Exemplos de cadeias de $C$:

      '/#blllb#/'
      '/##/'
      '/#ll#/'
      '/#bbbb#/'
      '/#lbblnlllb#/'
      '/#bbblnn#/'
      '/#nnnnnn#/'

Exemplos de cadeias que não pertencem a $C$:

      '#/bbbl#/'
      '/#bbllllnn#/bbbll#/'
      '/#llll#/#'
      '/#bbblllbnn#/bb'
      '/#bbllnn#b#/'
      ''
Arquivos: 
* src/Q01.py (local onde o dfa deve ser definido)
* test/test_Q01.py

Execução dos testes automáticos: 

      python -m unittest -v test/test_Q01.py

## Questão 02

Para a linguagem regular da questão 01, escreva uma expressão regular que a gera usando a biblioteca **re** de python. Neste caso, substitua `l` por `[a-zA-Z]`, `n` por `[0-9]` e `b` por `\s
`

Exemplos de cadeias da linguagem:


    /# abc #/
    /##/
    /#9ab#/
    /#   #/
    /#a z123 #/
    /#   g75#/
    /#123456#/

Arquivos: 
* src/Q02.py (local onde o nfa deve ser definido)
* test/test_Q02.py

Execução dos testes automáticos: 

      python -m unittest -v test/test_Q02.py


## Questão 03

Considere uma máquina de vendas de pacotes de balas do tipo `S`, `P` e `B`. Cada pacote custa 3 reais. Para que a venda seja realizada, é necessário que o usuário insira a quantidade de fichas de 1 real ou 2 reais com valor exato de um pacote e depois pressione o botão correspondente ao tipo de bala desejado. Podem ser inseridas as seguintes combinações de ficha:  (2,1) ,  (1,2)  ou  (1,1,1) . Caso um valor maior ou menor seja inserido, o produto selecionado não poderá ser entregue. Construa um NFA que modela um controlador para esta máquina usando a biblioteca **automata-lib**. O NFA recebe uma sequência de eventos e determina se a máquina pode liberar a venda de um produto, aceitando ou não a sequência. Considere o seguinte alfabeto:  $\Sigma$ ={`1`,`2`,`B`,`P`,`S`}. O controlador deve ignorar eventos relativos ao pressionamento dos botões de seleção dos produtos intercalos com a inserção de moedas. O último evento deve ser sempre relativo a seleção do produto.

As cadeias `21B`, `111S`, `12P`, `1S2P` e `SBP111S` são exemplos de cadeias que devem ser aceitas. Por outro lado, as cadeias `21`, `22B`, `121E`, `2`, `BB`, `S`, `11BB`, `111B1`, `11P1` são exemplos de cadeias que não devem ser aceitas.

Arquivos: 
* src/Q03.py (local onde o nfa deve ser definido)
* test/test_Q03.py

Execução dos testes automáticos: 

      python -m unittest -v test/test_Q03.py

# Questão 04

Considere que endereços de email podem ser definidos de acordo com a seguinte expressão regular: 

$L(L \cup N \cup S)^*@(L \cup N)^+PLLLPLL$

onde $L$ representa letras, $N$ dígito numérico, $S$ símbolos válidos, $P$ representa o caracter `.`.
Construa um NFA que reconhece emails que atendem a este padrão usando a biblioteca **automata-lib**. Considere $\Sigma$ = {`L`, `N`, `S`, `@`, `P`}.

São exemplos de emails aceitos pelo NFA:

        'LLLL@LLL.LLL.LL'
        'L@L.LLL.LL'
        'LN@NNN.LLL.LL'
        'LS@LN.LLL.LL'
        'LSNN@N.LLL.LL'
        'LLLLLLLNNN@LNL.LLL.LL'
        'LLLNSSS@LLLLLLLLL.LLL.LL'

Arquivos: 
* src/Q04.py (local onde o nfa deve ser definido)
* test/test_Q04.py

Execução dos testes automáticos: 

      python -m unittest -v test/test_Q04.py


# Questão 05

Para a linguagem regular da questão 04, escreva uma expressão regular que a gera usando a biblioteca **re** de python. Neste caso, substitua $L$ por `[a-z]`, $N$ por `[0-9]`, $P$ por `\.` e $S$ por `_`.

São exemplos de emails válidos segundo a expressão:

       'abcd@aaa.xxx.ra'
       'g@d.daf.df'
       'f4@356.ghj.ds'
       'a_@d6g.dsf.df'
       'a_77@5.das.hf'
       'daagafa5656@f3f.das.fs'
       'fas35___@ghhdhght.fgd.ht'

Arquivos: 
* src/Q05.py (local onde o nfa deve ser definido)
* test/test_Q05.py

Execução dos testes automáticos: 

      python -m unittest -v test/test_Q05.py

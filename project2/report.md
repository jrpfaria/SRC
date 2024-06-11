# Comportamento normal

Ao analisar o ficheiro data8.parquet, fizemos algumas observações sobre o comportamento normal da rede e dos servidores presentes.

## Estatísticas gerais
- Considerando os protocolos, houveram 108093 flows por UDP e 790707 por TCP;
- Todos os flows para a porta 53 (DNS) são UDP, e vice-versa;
- Todos os flows para a porta 443 (HTTP) são TCP, e vice-versa;
- Aproximadamente 12% dos flows foram de DNS;
- No total, houveram 9019873641 bytes (9 GB) de upload;
- No total, houveram 83198921759 bytes (83 GB) de download;
- O ratio de download/upload total foi aproximadamente 9:1;
- O primeiro flow acontece ás 04:04:47;
- O último flow acontece ás 23:33:13;
- A distribuição dos flows durante o tempo segue mais ou menos uma distribuição binomial, com centro ás 13:11:45;

## Servidores na rede
Existem apenas 6 IPs da própria rede interna que podem ser encontrados como destino de flows. Estes são:
- 192.168.108.224
- 192.168.108.225
- 192.168.108.226
- 192.168.108.231
- 192.168.108.237
- 192.168.108.238

Dois destes IPs (192.168.108.224 e 192.168.108.231) só são usados para DNS, e são os únicos que são usados para tal. Podemos conclúir que são os servidores de DNS da rede. É difícil dizer o que são os outros IPs, mas visto que nenhum IP desta lista é alguma vez a origem de um flow, podemos concluír que todos estes são servidores da rede (já que apenas respondem a pedidos).

Existem no total 266430 flows com destino a algum destes IPs. Cada um dos servidores de DNS é destino de 20% destes flows. O resto dos flows está mais ou menos igualmente distribuído pelos restantes servidores.

O upload total feito para cada servidor de DNS foi aproximadamente 10 MB. Por outro lado, para os outros servidores, este número é 452 MB.
Para o download total observa-se uma diferença semelhante entre os dois grupos de servidores. Foram feitos 25 MB de download de cada servidor de DNS, e 4 GB de cada um dos restantes.

## Países de destino
Foram encontrados 36 países diferentes de destino. Os destinos mais comuns em termos de número de flows são os Estados Unidos, a própria rede interna, e Portugal.

//inserir gráficos aqui

###########################################

## DNS Servers
Dois IPs que, para além de serem os destinos mais comuns, são acessados exclusivamente na porta 53 com o protocolo UDP, e são os únicos acessados pela porta 53
- 192.168.108.224
- 192.168.108.231

Passaram a haver o dobro dos pedidos a estes servers no test8, apesar do upload e download se manterem iguais.
No data8, o IP que fazia mais pedidos para estes servers fazia 0.01499634573% dos pedidos.
No test8, o IP 192.168.108.97 faz 36% dos pedidos, o 192.168.108.169 faz 12% dos pedidos, e o 192.168.108.55 faz pouco menos que 1%.

Ao investigar mais a fundo estes IPs, percebemos o seguinte:
- o 192.168.108.97 tem um número de flows mais ou menos constante desde as 06:45h até ás 20:30h, com um número mais ou menos constante de pedidos por hora. // TODO
- aproximadamente 90% do tráfego gerado por este IP é destinado à porta 53 dos DNS Servers internos (distribuido igualmente por estes dois servidores)
- para o 192.168.108.169, também 90% do tráfego é feito para a porta 53 dos servidores de DNS internos
- neste caso, o tráfego é feito aproximadamente das 08:40h ás 14:10h, também a um ritmo constante // TODO

## Outros Servers Internos
Existem outros 4 IPs internos que são acessados normalmente. Estes são:
- 192.168.108.225
- 192.168.108.226
- 192.168.108.237
- 192.168.108.238

No test8, são acessados 3 novos IPs internos:
- 192.168.108.20
- 192.168.108.164
- 192.168.108.191

O ratio de up/down dos flows com estes destinos são aproximadamente 1:1. Todo o trágefo com estes destinos tens esse mesmo conjunto de IPs como origem, e é feito por TCP na porta 443, no entanto estes IPs são a origem de tráfego com muitos outros IPs externos.

## Tempo entre pedidos para cada source IP
Em situações normais, o tempo médio entre pedidos para um determinado source IP pode ir de 3,5 segundos a 20,8 segundos. No entanto, podemos observar duas exceções, onde os tempo médio está à volta dos 0,6 segundos:
- 192.168.108.97
- 192.168.108.169
Estes são os mesmos IPs que fazem um grande número de pedidos aos servidores de DNS, por isso são extremamente suspeitos!!!!!!!!!!!!!

## Ratio de download/upload em HTTPS/TCP
Tanto num dia normal como no dia do testX, o normal é cada IP ter um ratio total de download/upload entre 8 e 10. No entanto, os seguintes IPs têm ratios fora do expectado (upload relativamente maior do que o comum):
- 192.168.108.140  0.057944
- 192.168.108.206  0.125438
- 192.168.108.138  2.313692
- 192.168.108.110  3.719782
- 192.168.108.46   3.903700

## Upload total
Os seguintes IPs apresentam um download total muito maior do que os outros:
- 192.168.108.110     221472872 (221MB)
- 192.168.108.140    6988278568 (7GB)
- 192.168.108.206    2992019743 (3GB)

O esperado, tanto no data8 como no test8, seria um valor até 150MB de upload total. Estes três IPs também estão na lista de IPs com um ratio abnormal de download/upload.

Algumas observações que fizemos:
- para o IP 192.168.108.140, todos os seus grandes uploads foram feitos para o IP 13.107.42.20, que é um IP do Microsoft Azure
- este IP está muito mais ativo nas horas em que os outros IPs estão menos ativos. Está mais ativo das 06:30h ás 10:00h, e das 17:30h ás 19:00h. Nos outros horários, está praticamente inativo
- para o IP 192.168.108.206, todos os seus grandes uploads foram feitos para o IP 142.250.184.145, que é um IP da Google (na Bulgária)
- este IP está ativo das 10:00h ás 16:00h, não apresentando mais nenhuma atividade nas restantes horas
- para o IP 192.168.108.110, todos os seus grandes uploads foram feitos para o IP 104.244.42.1, que é um IP do Twitter
- este IP tem uma atividade mais ou menos constante das 08:20h ás 19:00h
- este IP tem um ratio abnormal de download/upload no Twitter. seria esperado uma maior quantidade de downloads comparado a uploads

## Países

No data8, existem 36 países diferentes nos destinos dos flows. No test8, existem 60 países.

Os novos países são: Armenia, Austria, Bangladesh, Belize, Cambodia, Czech Republic, Dominica, Europe, Greece, Iran, Islamic Republic of, Isle of Man, Kazakhstan, Kyrgyzstan, Lebanon, Malaysia, Moldova, Republic of, Myanmar, Oman, Palestinian Territory, Romania, Russian Federation, Taiwan, Thailand, Turkmenistan, Ukraine, Uzbekistan

Todo o tráfego para estes países é gerado por estes IPs (associados ao número de flows):
- 192.168.108.116     14
- 192.168.108.168      3
- 192.168.108.178      6
- 192.168.108.179      2
- 192.168.108.182      1
- 192.168.108.209      2
- 192.168.108.29      17
- 192.168.108.36     776
- 192.168.108.77      14
- 192.168.108.88       3
- 192.168.108.94       2
- 192.168.108.95     555

Podemos observar que dois dos IPs geram a maioria dos flows para estes países:
- 192.168.108.36     776
- 192.168.108.95     555

Também são estes que geram a maior quantidade de upload:
- 192.168.108.36     12698610 (12MB)
- 192.168.108.95      9488480 (9MB)

E download:
- 192.168.108.36     108196407 (108MB)
- 192.168.108.95      81414226 (81MB)

Além disso, se removermos desta lista os países Malásia, "Europa", Omã e Taiwan, vemos que apenas estes dois IPs geram o tráfego para todos os outros países. Podemos observar que existe apenas um IP que é origem de flows para "Europe", outro para Oman, e outro para Taiwan. No entanto, existem 7 IPs diferentes que contactam a Malásia (não considerando os dois IPs descritos acima), um país que não era destino de flows no dataset original.
- 192.168.108.77       7294751
- 192.168.108.29       1314011
- 192.168.108.116      1229535
- 192.168.108.88        461221
- 192.168.108.94        296566
- 192.168.108.182       127540
- 192.168.108.179       109059

A maioria do tráfego para a Malásia acontece das 14:00h ás 18:20h. Todo o tráfego é feito para 2 AS: Facebook e Microsoft.

# AS
No data8, são acessadas 42 AS diferentes. No test8, são acessadas 459 novas AS.
Todos os acessos a estas novas AS são feitas pelos IPs definidos anteriormente:
- 192.168.108.36 861
- 192.168.108.95 652
Aqui os IPs estão associados com o número de flows.

# Timestamps

Existem apenas dois IPs que utilizam a rede antes das 05:00h ou depois das 20:00h:
- 192.168.108.208     24
- 192.168.108.88     395

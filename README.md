# timvoip
Script per estrarre l'IP numerico dei proxy VOIP di TIM
Utile per configurare il voip dei fritzbox con la vdsl


Prerequisiti: python-dnspython
```shell
sudo apt-get install python-dnspython
```

Uso:
```shell
python timvoip.py -h
usage: timvoip.py [-h] [--verbose] [--nameserver NAMESERVER] --sip SIP

TIM SIP proxy IP address extractor

optional arguments:
  -h, --help            show this help message and exit
  --verbose
  --nameserver NAMESERVER
                        nameserver
  --sip SIP             sip proxy
```
Es.
```shell
python timvoip.py --sip=XXX.co.imsw.telecomitalia.it
priority 20 : 1.2.3.4
priority 10 : 5.6.7.8
```

Se usate un nameserver ( dns ) non tim, es. 8.8.8.8 di Google o altri, occorre specificare il nameserver ufficiale nello script affinchè vengano risolti gli indirizzi.  
Il nameserver ufficiale viene visualizzato dal fritzbox nella pagina internet > monitor online

Es.
```shell
python timvoip.py --sip=XXXXX.co.imsw.telecomitalia.it --nameserver=85.37.17.58
priority 20 : 1.2.3.4
priority 10 : 5.6.7.8
```



Per configurare la linea voip quindi tim vi dice:

I dati che hai richiesto per configurare il tuo modem sono:
Numero linea **PP NNNNNNNN**  
outboundProxy :	**PPPP.co.imsw.telecomitalia.it**  
sipKey :	**XXXXXXXXXXXXXXX**  

Sul fritz vanno messi i seguenti parametri per la linea

Nome utente: **+39PPNNNNNN**  
Password: **XXXXXX**  
Registrar: **telecomitalia.it:5060**  
Server proxy **1.2.3.4** ( *priorità 10 o 20, estratto con lo script python a partire da outboundProxy* )  

Riferimenti:  
https://www.voip-info.org/dns-srv/  
https://anders.com/cms/263/Tutorial/SIP/DNS/SRV/djbdns  




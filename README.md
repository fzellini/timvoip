# timvoip
script per estrarre l'IP numerico dei proxy VOIP di TIM

Utile per configurare il voip dei fritzbox con la vdsl

Prerequisiti: python-dnspython
sudo apt-get install python-dnspython

Uso:
python timvoip.py -h
usage: timvoip.py [-h] [--verbose] [--nameserver NAMESERVER] --sip SIP

TIM SIP proxy IP address extractor

optional arguments:
  -h, --help            show this help message and exit
  --verbose
  --nameserver NAMESERVER
                        nameserver
  --sip SIP             sip proxy

Es.

python timvoip.py --sip=XXX.co.imsw.telecomitalia.it
priority 20 : 1.2.3.4
priority 10 : 5.6.7.8


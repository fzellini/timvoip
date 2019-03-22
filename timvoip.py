# sudo apt-get install python-dnspython

import dns
import dns.resolver
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='TIM SIP proxy IP address extractor')
    parser.add_argument("--verbose",action='store_true')
    parser.add_argument("--nameserver",help="nameserver",default="85.37.17.58",required=False)
    parser.add_argument("--sip",help="sip proxy",required=True)

    args = parser.parse_args()

    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [args.nameserver]
    srv_rec =  resolver.query("_sip._udp."+args.sip,'SRV')

    for srv in srv_rec:
        a_rec  =  resolver.query(srv.target,'A')
        for a in a_rec:
            print ("priority {} : {}".format(srv.priority,a))


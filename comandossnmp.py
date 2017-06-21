import os
import commands


interface = raw_input()
ip = raw_input()
#### RECUPERA O NOME DA INTERFACE E A QUANTIDADE DE BYTES QUE SAI DELA ####
horas = commands.getoutput('snmpget -v 2c -c public '+ip+' RFC1213-MIB::sysUpTime.0 | cut -d ":" -f4 | cut -d ":" -f4 | cut -d" " -f3')
minutos = commands.getoutput('snmpget -v 2c -c public '+ip+' RFC1213-MIB::sysUpTime.0 | cut -d : -f5')
segundos = commands.getoutput('snmpget -v 2c -c public '+ip+' RFC1213-MIB::sysUpTime.0 | cut -d ":" -f6 | cut -d "." -f1')

os.system('snmpget -v 2c -c public '+ip+' RFC1213-MIB::ifDescr.'+interface+' | cut -d ":" -f4 | tr -d " "')
os.system('snmpget -v 2c -c public '+ip+' RFC1213-MIB::ifOutOctets.'+interface+' | cut -d : -f4 | tr -d " "')
os.system('snmpget -v 2c -c public '+ip+' RFC1213-MIB::ifInOctets.'+interface+' | cut -d : -f4 | tr -d " "')
os.system('snmpwalk -v 2c -c public '+ip+' RFC1213-MIB::ifSpeed.'+interface+' | cut -d : -f4 | tr -d " "')
os.system('snmpwalk -v 2c -c public '+ip+' RFC1213-MIB::ifType.'+interface+' | cut -d : -f4 | tr -d " "')


## MENSAGENS ICMP ENTRADA E SAIDA ##
os.system('snmpwalk -v 2c -c public '+ip+' RFC1213-MIB::icmpInMsgs | cut -d "=" -f2 | cut -d ":" -f2 | tr -d " "')
os.system('snmpwalk -v 2c -c public '+ip+' RFC1213-MIB::icmpOutMsgs | cut -d "=" -f2 | cut -d ":" -f2 | tr -d " "')

## TCP ##
os.system('snmpwalk -v 2c -c public '+ip+' RFC1213-MIB::tcpMaxConn | cut -d "=" -f2 | cut -d ":" -f2 | tr -d " "')
os.system('snmpwalk -v 2c -c public '+ip+' RFC1213-MIB::tcpRetransSegs | cut -d "=" -f2 | cut -d ":" -f2 | tr -d " "')

## UDP ##
os.system('snmpwalk -v 2c -c public '+ip+' RFC1213-MIB::udpInDatagrams | cut -d "=" -f2 | cut -d ":" -f2 | tr -d " " ')
os.system('snmpwalk -v 2c -c public '+ip+' RFC1213-MIB::udpOutDatagrams | cut -d "=" -f2 | cut -d ":" -f2 | tr -d " " ')

print horas+"h"+minutos+"m"+segundos+"s"


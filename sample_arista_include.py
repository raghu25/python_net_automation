'''
HERE I USE JINJA2 TEMPLATE TO GENERATE THE FOLLOWING SAMPLE ARISTA CONFIG 

MAIN TEMPLATE IS STORED IN EXTERNAL JINJA2 file 'arista_template.j2'. THIS TEMPLATE USES JINJA2 INCLUDE TO PARSE ADDITIONAL TEMPLATES
FIRST TEMPLATE CONSISTS USERNAME STATEMENTS 'arista_users.j2' AND SECOND TEMPLATE HAS SNMP STATEMENTS 'snmp.j2'.


!
hostname desmoines-sw4
!
ntp server 10.10.10.24
!
snmp-server contact Raghu
snmp-server location Des Moines, IA
snmp-server community foo ro SNMP
!
spanning-tree mode mstp
!
aaa authorization exec default local
!
no aaa root
!
username local privilege 15 secret 5 abDD09yW.NIR8d2Lh0
username admin privilege 15 secret 5 abDD09yW.NIR8d2Lh0
!
clock timezone America/Chicago
!
interface Ethernet1
   spanning-tree portfast
   spanning-tree cost 1
!
interface Ethernet2
!
interface Ethernet3
!
interface Ethernet4
!
interface Ethernet5
!
interface Ethernet6
!
interface Ethernet7
!
interface Management1
   shutdown
!
interface Vlan1
   ip address 10.10.88.31/24
!
ip route 0.0.0.0/0 10.10.88.1
!
ip routing
!
management api http-commands
   no shutdown
!
!
end
'''

from __future__ import print_function, unicode_literals
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

device_vars = {
    'snmp_location': 'Des Moines, IA',
    'snmp_contact': 'Raghu',
    'snmp_community': 'foo',
}

template_file = 'arista_template.j2'
template = env.get_template(template_file)
print(template.render(device_vars))

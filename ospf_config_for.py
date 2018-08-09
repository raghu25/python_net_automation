#!/usr/bin/env python


from __future__ import print_function, unicode_literals
import jinja2

'''
generating configuration template with jinja2 template in external file 'ospf_config_for.j2' uses for loop for more than one network statements
'''
filename = 'ospf_conifg_for.j2'
with open(filename) as f:
	ospf_template = f.read()

ospf_networks = [
	{
	'network' : '10.120.88.0',
	'wildcard' : '0.0.0.255',
	'area': 0,
	},
	{
	'network' : '172.31.255.28',
	'wildcard' : '0.0.0.0',
	'area': 1,
	},
]

ospf_vars = {
    'process_id' : 40,
	'ospf_networks': ospf_networks,
	'loopback0_addr': '172.33.253.1',
	'loopback0_mask' : '255.255.255.255',
}

template = jinja2.Template(ospf_template)
output = template.render(**ospf_vars)
print(output)
f.close()

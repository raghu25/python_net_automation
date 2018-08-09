from __future__ import print_function, unicode_literals
import jinja2
'''
generating configuration template with jinja2 template in external file 'ospf_config.j2'
'''
filename = 'ospf_config.j2'
with open(filename) as f:
	ospf_template = f.read()
	

ospf_vars = {
	'process_id' : 40,
	'network' : '10.120.88.0',
	'wildcard' : '0.0.0.255',
	'area_id' : 0,
	'loopback0_addr': '172.33.253.1',
	'loopback0_mask' : '255.255.255.255',
}
template = jinja2.Template(ospf_template)
output = template.render(**ospf_vars)
print(output)
f.close()

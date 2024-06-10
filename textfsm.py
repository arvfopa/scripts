import textfsm
from tabulate import tabulate

with open('dns_t_1column.txt') as template, open('dns_stat.txt') as dnsstat:
    re_table = textfsm.TextFSM(template)
    header = re_table.header
    result = re_table.ParseText(dnsstat.read())
    tabulated = (tabulate(result, headers=header))
    print(tabulated)

with open('fsmtabulated.txt', mode='w', newline='') as file:
    file.write(tabulated)

#coding:utf-8


template_variables = dict(
    title=u'OPS',
    name=u'OPS管理平台',
)

DATABASES = dict(
    DB='ops',
    USERNAME='root',
    PASSWORD='123456',
    HOST='10.1.72.66',
    PORT=3306,
)

ADD_HOST_LIST = ["server_ip", "public_ip", "idc_name", "mem_size", "disk_size", "cpu_num",
                 "server_rack", "sn", "server_type", "os", "project_name", "server_status", "server_contact", "comment"]
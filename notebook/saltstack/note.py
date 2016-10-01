定义grains数据

1.在被控端主机定制grains数据
在/etc/salt/minon,中参数default_include: minion.d/*.conf
/etc/salt/minion.d/hostinfo.conf

grains:
  roles:
    - webserver
    - memcache
  deployment: datacenter4
  cabinet: 13

2.主控端扩展模块定制grains数据


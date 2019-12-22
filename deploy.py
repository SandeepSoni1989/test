connect('weblogic' , 'weblogic123' , 't3://localhost:7010')
appname ="TestServerKrishna"
application="E:\TestServerKrishna.war"
deploy(appname,application,tartgets='MServer-1')
exit()
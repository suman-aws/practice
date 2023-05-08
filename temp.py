env = ['ABC INT', 'ABC INT']
host = []
for e in env:
    if 'QA' in e:
        host.append(  'qa.example.com')
    elif 'PROD' in e:
        host.append( 'prod.example.com')
    else:
        host.append( 'int.example.com')

print(host[0])
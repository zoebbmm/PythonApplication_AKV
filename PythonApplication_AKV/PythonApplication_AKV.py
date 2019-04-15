from OpenSSL import crypto
import os
from azure.keyvault import KeyVaultClient, KeyVaultAuthentication
from azure.common.credentials import ServicePrincipalCredentials
import wincertstore


# Get cert from windows cert store
for storename in ("CA", "ROOT"):
    with wincertstore.CertSystemStore("My") as store:
        for cert in store.itercerts(usage=wincertstore.SERVER_AUTH):
            if(cert.get_name() == "VSTSICMSync-TEST"):
                print(cert.get_name())

# Get secret from AKV
subscription_id = '4743ef1d-749f-46e9-ae08-c6c2ea7f22f6'
credentials = ServicePrincipalCredentials(
    client_id = '7c748035-c78e-4e6c-bd3e-fce22259fce3',
    secret = 'DTvlMWXC/vR9fHhKzjeftSiw1vWJq1fMQc1A0ueuY0I=',
    tenant = '72f988bf-86f1-41af-91ab-2d7cd011db47'
)
token = credentials.token
client = KeyVaultClient(KeyVaultAuthentication(token['token_type'], token['access_token']))
secrets = client.get_secrets('https://vstsicmsync-test.vault.azure.net/')
print(secrets)


# Get cert by privay key and password
cert_file = "C:\\Users\\zhowe\\Desktop\\Certs\\python-eat-vstsicmsync-test.pfx"
#print(os.path.isfile(cert_file))
cert = crypto.load_pkcs12(open(cert_file, 'rb').read(), "666666").get_certificate()
subject = cert.get_subject()
print(subject)
serial = cert.get_serial_number()
print(serial)
serial_hex = '{0:#0{1}x}'.format(serial, 4) 
print(serial_hex) 

#cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())
#subject = cert.get_subject()
#print(subject)


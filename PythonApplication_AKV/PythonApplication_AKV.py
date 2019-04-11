from OpenSSL import crypto
import os

# Get cert by privay key and password
cert_file = "C:\\Users\\zhowe\\Desktop\\Certs\\python-eat-vstsicmsync-test.pfx"
print(os.path.isfile(cert_file))
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


    
#from azure.keyvault import KeyVaultClient, KeyVaultAuthentication
#from azure.common.credentials import ServicePrincipalCredentials
#from azure.keyvault import KeyVaultId

#def auth_callback(server, resource, scope):
#    credentials = ServicePrincipalCredentials(
#        client_id = '7c748035-c78e-4e6c-bd3e-fce22259fce3',
#        secret = 'DTvlMWXC/vR9fHhKzjeftSiw1vWJq1fMQc1A0ueuY0I=',
#        tenant = 'from azure.keyvault import KeyVaultId',
#    )
#    token = credentials.token
#    return token['token_type'], token['access_token']

#client = KeyVaultClient(KeyVaultAuthentication(auth_callback))

#secret_bundle = client.get_secret('https://vstsicmsync-test.vault.azure.net/', 'VstsPat', secret_version=KeyVaultId.version_none)

#print(secret_bundle.value)

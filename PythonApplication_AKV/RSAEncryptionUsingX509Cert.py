import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from OpenSSL import crypto
import os
import wincertstore
import atexit
import ssl
import sys
import logging
import base64
from pyasn1.codec.der import decoder
from hashlib import sha256

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
for storename in ("CA", "ROOT", "My"):
    logger.info("Gathering information from store: %s" % storename)
    with wincertstore.CertSystemStore(storename) as store:
        storecerts = {}
        for cert in store.itercerts(usage=None):
            #if(cert.get_name() == "VSTSICMSync-TEST"):
            certName = cert.get_name()
            logger.info("Processing certificate: %s" % certName)
            # get pem
            pem = cert.get_pem()
            # Convert to .der, and decode it in order to get cert thumbprint
            encodedDer = ''.join(pem.split("\n")[1:-2])
            logger.info("Encoded der certificate: %s" % encodedDer)
            der = base64.b64decode(encodedDer)
            logger.info("Dncoded der certificate: %s" % der)
            h = sha256()
            h.update(der)
            # get thumbprint
            thumbprint = h.hexdigest()
            certificateInfo = {
                    "Name": certName,
                    "Thumbprint": thumbprint,
                    "PEM": pem
                }
            logger.info("Detailed Cert Info: %s" % certificateInfo)
            

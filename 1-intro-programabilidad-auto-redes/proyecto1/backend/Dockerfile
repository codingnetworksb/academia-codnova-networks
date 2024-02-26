FROM python:3.9

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

COPY my_openssl_config.txt /tmp/my_openssl_config.txt


RUN sed  -i '1i openssl_conf = default_conf' /etc/ssl/openssl.cnf && \
    sed -i -e '$a[default_conf]\n\nssl_conf = ssl_sect\n\n[ssl_sect]\n\nsystem_default = system_default_sect\n\n[system_default_sect] \nMinProtocol = TLSv1.0\nCipherString = DEFAULT:@SECLEVEL=1' /etc/ssl/openssl.cnf



CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"] 

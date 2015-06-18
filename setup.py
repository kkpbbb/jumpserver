from setuptools import setup

setup(
    name="jumpserver",
    version="2.0.0",
    packages = find_packages(),
    install_requires=[
        "sphinx-me==0.3",
        "django==1.6",
        "python-ldap==2.4.19",
        "pycrypto==2.6.1",
        "paramiko==1.15.2",
        "ecdsa==0.13",
        "MySQL-python==1.2.5",
        "django-uuidfield==0.5.0",
        "psutil==2.2.1",
    ],
    
)

import os, threading
os.system("chmod +x init.sh")
os.system("./init.sh")
os.system("python litwallet.py create")
os.system("python litwallet.py news")
os.system("python litwallet.py us")
os.system("lt --subdomain cyan-mirrors-smile-34-86-111-132 --port 5000")
# sPyChat

### Python setup

To properly use this python-modules some additional libraries have to be
installed beforehand. This can be easily accomplished with the commands below.

```
virtualenv -p python3 .
source bin/activate
pip install pycrypto
pip install pycap
```

### Run demo

This software ships with two demo-scripts containing a sample implementation of
an encrypted communication. To test them, just enter the commands below.

```
python3 bob.py
python3 alice.py
```

**WARNING: The provided secure protocol implementation is just for exercise
purposes and should not be used in real world implementations because of some
major vulnerabilities (They were requested in the problem statement.)!**

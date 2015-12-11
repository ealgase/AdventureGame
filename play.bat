set /P world="Which world? (1) Tutorial, and (2) base. "
if %world%=="1" python3 tutorial.py
else python3 worlds/base.py

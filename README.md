# fms 
 
######Version: 0.1.0-SNAPSHOT

FMS works as the fontman client application's backend. All the tasks like 
installing fonts, updating font cache are covered by this application. FMS 
uses a SQLite database to store data, you can find it under "data" directory 
under fms home directory.
<br><br>

#####Requirements

Make sure you have `python 3` and `pip` installed. Then install 
following packages.

```bash
pip install flask
pip install requests
pip install sqlalchemy
``` 

additionally for windows platforms,

```bash
pip install pypiwin32
```

#####Run for the first time

To initialize the application data, if you are running it for the first time,

```bash
python fms.py init
```


#####Run fms

```bash
python fms.py start
```

Once the flask application started you can start using fontman-gui, 
fontman-client frontend.

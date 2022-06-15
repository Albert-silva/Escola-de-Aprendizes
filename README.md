# Escola de Aprendizes API

Sistema de escola desenvolvido na float academy


## Prerequeriments

- Python >= 3.6
- Banco de Dados MySQL >= 5.6

## Install

### Clone of the project
```
    git clone git@github.com:Albert-silva/Escola-de-Aprendizes.git

```
```
    cd Escola-de-Aprendizes
```

### Install dependencias

```
    cd api/

```
```
    pip3 install -r requirements.txt

```
## Running

Access the `db` folder and execute `setup.sql` file in your database.

then, running in command line:

```
FLASK_APP=api/app.py flask run
```

open http://localhost:5000/
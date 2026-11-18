import psycopg2 as pg

url = "[bootstrap.pypa.io](https://bootstrap.pypa.io/get-pip.py)"
resposta = pg.get(url, timeout=30)
resposta.raise_for_status()

with open("get-pip.py", "wb") as psycopg2:
    psycopg2.write(resposta.content):

import io
import os
import gdstk
import boto3
import boto3.session
import hashlib
from dotenv import load_dotenv
import pymysql

load_dotenv()
boto3.setup_default_session(profile_name="gdslib")

path = "taper.gds"

gds = gdstk.read_gds(path)


def gds_content(path: str) -> bytes:
    with open(path, "rb") as file:
        bts = file.read()
    return bts


def gds_hash(path: str) -> str:
    content = gds_content(path)
    hex = hashlib.md5(content).hexdigest()
    return hex
    # val = int(hex, 16)
    # return val


def gds_name(path: str) -> str:
    return os.path.split(path)[-1]

print(os.getenv("PS_HOST", ""))
print(os.getenv("PS_DATABASE", ""))
print(os.getenv("PS_USERNAME", ""))
print(os.getenv("PS_PASSWORD", ""))
print(os.getenv("PS_SSL_CERT", ""))

conn = pymysql.connect(
    host=os.getenv("PS_HOST", ""),
    database=os.getenv("PS_DATABASE", ""),
    user=os.getenv("PS_USERNAME", ""),
    password=os.getenv("PS_PASSWORD", ""),
    ssl_ca=os.getenv("PS_SSL_CERT", ""),
)

cursor = conn.cursor()

name = gds_name(path)
hash = gds_hash(path)
#query = f"INSERT INTO GdsFile (name, hash) VALUES ('{name}', '{hash}')"
#cursor.execute(query)
#conn.commit()

query = "SELECT * FROM GdsFile LIMIT 10"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows: print(row)

cursor.close()
conn.close()

s3_client = boto3.client("s3")
s3_client.upload_file(path, "gdslib", f"gds/{hash}")

print(f"name: {name}")
print(f"hash: {hash}")
print(f"gds: {gds_content(path)}")

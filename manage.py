import io
import os
import boto3
import boto3.session
import hashlib
from dotenv import load_dotenv
import pymysql
from pathlib import Path

load_dotenv()
s3_client = boto3.client("s3")
#boto3.setup_default_session(profile_name="gdslib")

def get_file(hash: int):
    with conn.cursor() as cursor:
        cursor.execute('SELECT name, hash FROM GdsFile WHERE hash=%s', hash)
        filename, hash = cursor.fetchone()
        s3_client.download_file("gdslib", f"gds/{hash}", filename)
        if Path(filename).exists():
            return filename
        return None


def get_list():
    with conn.cursor() as cursor:
        cursor.execute("SELECT name, hash FROM GdsFile LIMIT 15")
        rows = cursor.fetchall()
        return rows

def upload_file(file):
    with conn.cursor() as cursor:
        name = gds_name(file.filename)
        contents = file.file.read()
        hash = gds_hash(contents)
        query = "INSERT INTO GdsFile (name, hash) VALUES (%s, %s)"
        cursor.execute(query,(name, hash))
        s3_client.upload_file(file.filename, "gdslib", f"gds/{hash}")
        return True

def delete_file(filehash):
    with conn.cursor() as cursor:
        query = f"DELETE FROM GdsFile WHERE hash=%s"
        cursor.execute(query, filehash)
    s3_client.delete_object(Bucket="gdslib", Key=f"gds/{filehash}")


def gds_hash(content: bytes) -> str:
    hex = hashlib.md5(content).hexdigest()
    return hex
    # val = int(hex, 16)
    # return val


def gds_name(path: str) -> str:
    return os.path.split(path)[-1]

def debug_env():
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



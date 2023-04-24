import boto3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("profile")
parser.add_argument("what")
args = parser.parse_args()

session = boto3.setup_default_session(profile_name=args.profile)
client = boto3.client("sts")
identity = client.get_caller_identity()
account = identity.get("Account")
region = client.meta.region_name

if args.what == "account":
    print(account)
elif args.what == "region":
    print(client.meta.region_name)
else:
    pass


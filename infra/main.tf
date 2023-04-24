// Providers
terraform {
  backend "s3" {
    bucket = "flaport-infra"
    key    = "gdslib"
    region = "us-west-2"
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.36.1"
    }
  }
}

provider "aws" {
  region  = "us-west-2"
  profile = "gdslib" // defined in ~/.aws/config
}

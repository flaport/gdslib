// S3 bucket where gdslib blobs are stored
resource "aws_s3_bucket" "gdslib_bucket" {
  bucket = "gdslib"
}

resource "aws_s3_bucket_public_access_block" "gdslib_public" {
  bucket = aws_s3_bucket.gdslib_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

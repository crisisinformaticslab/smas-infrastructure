###################
# DynamoDB Tables #
###################

resource "aws_dynamodb_table" "smasInstances" {
  name         = "smas-instances-${var.namespace}"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "userID"
  range_key    = "smasID"

  attribute {
    name = "userID"
    type = "S"
  }

  attribute {
    name = "smasID"
    type = "S"
  }

  server_side_encryption {
    enabled = true
  }

  tags = {
    Project = var.app_name
    Stage   = var.stage
  }
}


resource "aws_dynamodb_table" "smasAPIKeys" {
  name         = "smas-apikeys-${var.namespace}"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "userID"

  attribute {
    name = "userID"
    type = "S"
  }


  server_side_encryption {
    enabled = true
  }

  tags = {
    Project = var.app_name
    Stage   = var.stage
  }
}

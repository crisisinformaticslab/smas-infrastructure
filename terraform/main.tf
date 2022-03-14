#############
# Providers #
#############
provider "aws" {
  region  = var.region
  profile = "smas"
}

#############
# Variables #
#############
variable "region" {
  # NOTE: If changed, you must uncomment virginia provider alias above
  default = "us-west-2"
}

variable "app_name" {
  default = "smas"
}

variable "namespace" {
  default = "smas-dev"
}

variable "stage" {
  # e.g. development, testing, production
  default = "development"
}

# variable "notifier_fn_arn" {
#   # Output from serverless
#   default = "arn:aws:lambda:us-east-2:659400527649:function:services-dev-notifier"
# }

variable "site_domain" {
  # Your Domain Name used for S3 bucket + Cloudfront distro
  default = "smas-byu"
}

variable "cognito_role_external_id" {
  # Some unique ID that cognito can use for SMS verification
  default = "smas-unique-238478238"
}

# Permission Boundary ARN for BYU's AWS Cloud infrastructure
variable "permissions_boundary" {
  default = "arn:aws:iam::901232515713:policy/iamRolePermissionBoundary"
}

variable "dept_vpc_id" {
  description = "VPC ID of the dept assigned by BYU OIT"
  default     = "vpc-0d155f9604f8734b8"
}

variable "byu_public_subnet" {
  description = "BYU public subnet in the above vpc"
  default     = "subnet-06b7240727409ff31"
}

variable "byu_private_subnet" {
  description = "BYU private subnet in the above vpc"
  default     = "subnet-06c5aab932000dfe6"
}


# BELOW params are for DEV account
# Permission Boundary ARN for BYU's AWS Cloud infrastructure
# variable "permissions_boundary" {
#   default = "arn:aws:iam::980881292263:policy/iamRolePermissionBoundary"
# }

# variable "dept_vpc_id" {
#   description = "VPC ID of the dept assigned by BYU OIT"
#   default     = "vpc-057175f829f9e74b2"
# }

# variable "byu_public_subnet" {
#   description = "BYU public subnet in the above vpc"
#   default     = "subnet-050f8f212a3bee8a8"
# }

# variable "byu_private_subnet" {
#   description = "BYU private subnet in the above vpc"
#   default     = "subnet-04ea1b1ec5d896375"
# }





###########################
# Additional Data Sources #
###########################

# Used by Cloudfront distribution
# data "aws_acm_certificate" "website" {
#   # NOTE: uncomment if you changed default provider region
#   provider = "aws.virginia"
#   domain   = var.site_domain

#   statuses    = ["ISSUED"]
#   most_recent = true
# }

# data "aws_route53_zone" "website" {
#   name = "${var.site_domain}."
# }

###########
# Outputs #
###########

# locals {
#   awsexports = <<AWSEXPORTS

# // Warning: This file is automatically generated. It will be overwritten.
# // Stage: ${var.stage}

# const awsmobile = {
#     "aws_project_region": "${var.region}",
#     "aws_appsync_region": "${var.region}",
#     "aws_cognito_region": "${var.region}",
#     "aws_cognito_identity_pool_id": "${aws_cognito_identity_pool.main.id}",
#     "aws_user_pools_id": "${aws_cognito_user_pool.main.id}",
#     "aws_user_pools_web_client_id": "${aws_cognito_user_pool_client.web.id}",
#     "aws_appsync_graphqlEndpoint": "${aws_appsync_graphql_api.main.uris["GRAPHQL"]}",
#     "aws_appsync_authenticationType": "AMAZON_COGNITO_USER_POOLS",
# };

# export default awsmobile;
# AWSEXPORTS
# }

# output "aws-exports-file" {
#   value = local.awsexports
# }

# output "user_pool_id" {
#   value = aws_cognito_user_pool.main.id
# }
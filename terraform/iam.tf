# IAM for serverless stack
data "aws_iam_policy_document" "api-gateway-assume-role" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["apigateway.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "serverless-cloudwatch-role" {
  name                 = "${var.namespace}-serverless-cloudwatch-role"
  assume_role_policy   = data.aws_iam_policy_document.api-gateway-assume-role.json
  permissions_boundary = var.permissions_boundary

}

# Attach Push to cloudwatch policy
resource "aws_iam_role_policy_attachment" "serverless-cloudwatch-role-polify" {
  role       = aws_iam_role.serverless-cloudwatch-role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonAPIGatewayPushToCloudWatchLogs"
}

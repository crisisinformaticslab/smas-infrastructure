# Supporting Infrastructure for Serverless Stack


# Security Group for launching lambda in

# resource "aws_security_group" "lambda-sg" {
#   name   = "${var.namespace}-lambda-sg"
#   vpc_id = var.dept_vpc_id
#   egress {
#     protocol    = "-1"
#     from_port   = 0
#     to_port     = 0
#     cidr_blocks = ["0.0.0.0/0"]
#   }
# }

# output "lambda-sg" {
#   value = aws_security_group.lambda-sg.id
# }

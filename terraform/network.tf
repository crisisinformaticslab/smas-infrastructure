# network.tf

# resource "aws_eip" "nat" {
#   vpc = true
# }


# resource "aws_nat_gateway" "ngw" {
#   subnet_id     = var.byu_public_subnet
#   allocation_id = aws_eip.nat.id

# }

# resource "aws_route" "public_igw" {
#   route_table_id         = aws_route_table.public.id
#   destination_cidr_block = "0.0.0.0/0"
#   gateway_id             = aws_internet_gateway.igw.id
# }

# resource "aws_route" "private_ngw" {
#   route_table_id         = aws_route_table.private.id
#   destination_cidr_block = "0.0.0.0/0"
#   nat_gateway_id         = aws_nat_gateway.ngw.id
# }

# resource "aws_security_group" "http" {
#   name        = "http"
#   description = "HTTP traffic"
#   vpc_id      = var.dept_vpc_id

#   ingress {
#     from_port   = 80
#     to_port     = 80
#     protocol    = "TCP"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   tags = {
#     resource-creator-email = "rfun11@byu.edu"
#   }
# }



# resource "aws_security_group" "ssh" {
#   name        = "ssh_from_home"
#   description = "SSH for Rohits home IP"
#   vpc_id      = var.dept_vpc_id

#   ingress {
#     from_port   = 22
#     to_port     = 22
#     protocol    = "TCP"
#     cidr_blocks = ["136.36.10.129/32"]
#   }

#   tags = {
#     resource-creator-email = "rfun11@byu.edu"
#   }
# }

# resource "aws_security_group" "https" {
#   name        = "https"
#   description = "HTTPS traffic"
#   vpc_id      = var.dept_vpc_id

#   ingress {
#     from_port   = 443
#     to_port     = 443
#     protocol    = "TCP"
#     cidr_blocks = ["0.0.0.0/0"]
#   }
# }

# resource "aws_security_group" "egress-all" {
#   name        = "egress_all"
#   description = "Allow all outbound traffic"
#   vpc_id      = var.dept_vpc_id

#   egress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }
#   tags = {
#     resource-creator-email = "rfun11@byu.edu"
#   }
# }


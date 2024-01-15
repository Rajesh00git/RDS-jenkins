resource "aws_db_instance" "mydb" {
    instance_class = "db.t3.micro"
    engine = "mysql"
    engine_version = "8.0.35"
    allocated_storage = 20
    identifier = "jenkinsdb"
    storage_type = "gp2"
    username = "rajesh"
    password = "rajesh!123"
    publicly_accessible = true
    skip_final_snapshot = true
    tags = {
      name = "myjenkinsdb"
    }

}
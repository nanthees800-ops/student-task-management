terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "student_app" {
  name = "student-task-app:v1"

  build {
    context = "../"
  }
}

resource "docker_container" "student_container" {
  name  = "student-task-terraform"
  image = docker_image.student_app.image_id

  ports {
    internal = 8000
    external = 8002
  }
}

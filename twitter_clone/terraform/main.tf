terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}


provider "docker" {}

resource "docker_network" "twitter_net" {
  name = "twitter_net"
}

resource "docker_volume" "postgres_data" {
  name = "postgres_data"
}

resource "docker_container" "postgres" {
  name  = "postgres"
  image = "postgres:14"

  env = [
    "POSTGRES_USER=myuser",
    "POSTGRES_PASSWORD=mypass",
    "POSTGRES_DB=mydb"
  ]

  volumes {
    volume_name    = docker_volume.postgres_data.name
    container_path = "/var/lib/postgresql/data"
  }

  networks_advanced {
    name = docker_network.twitter_net.name
  }
}


resource "docker_image" "backend" {
  name = "twitter_clone_backend:latest"

  build {
    context = "${path.module}/.."
  }
}

resource "docker_container" "backend" {
  name  = "backend"
  image = docker_image.backend.name

  env = [
    "APP_PORT=${var.backend_port}"
  ]

  ports {
    internal = var.backend_port
    external = var.backend_port
  }

  networks_advanced {
    name = docker_network.twitter_net.name
  }

  depends_on = [
    docker_container.postgres
  ]
}

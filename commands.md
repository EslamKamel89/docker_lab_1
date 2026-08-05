# Docker Commands Reference

This document contains the Docker commands used throughout the course.

Placeholders:

- `{image_name}` — Docker image name (e.g. `node-app-image`)
- `{container_name}` — Docker container name (e.g. `node-app-container`)
- `{host_port}` — Port on your machine
- `{container_port}` — Port exposed by the application inside the container
- `{host_directory}` — Local project directory
- `{container_directory}` — Directory inside the container

---

## Build an Image

```bash
docker build -t {image_name} .
```

### Flags

| Flag | Description                                                    |
| ---- | -------------------------------------------------------------- |
| `-t` | Assign a name (tag) to the image.                              |
| `.`  | Build context (current directory containing the `Dockerfile`). |

Example:

```bash
docker build -t node-app-image .
```

---

## Run a Container

```bash
docker run \
  --rm \
  --name {container_name} \
  -v "{host_directory}":{container_directory} \
  -p {host_port}:{container_port} \
  -d \
  -it \
  {image_name}
```

### Flags

| Flag     | Description                                                       |
| -------- | ----------------------------------------------------------------- |
| `--rm`   | Automatically remove the container after it stops.                |
| `--name` | Assign a custom container name.                                   |
| `-v`     | Mount a local directory into the container (bind mount).          |
| `-p`     | Publish a host port to a container port (`host:container`).       |
| `-d`     | Run the container in detached (background) mode.                  |
| `-it`    | Start the container in interactive mode with a terminal attached. |

Example:

```bash
docker run \
  --rm \
  --name node-app-container \
  -v "$(pwd)":/app \
  -p 80:80 \
  -d \
  -it \
  node-app-image
```

> **Note:** In practice, `-d` (detached) and `-it` (interactive terminal) are usually used for different scenarios. They can technically be combined, but most applications use one or the other.

---

## Start an Existing Container

```bash
docker start -a -i {container_name}
```

### Flags

| Flag | Description                                   |
| ---- | --------------------------------------------- |
| `-a` | Attach your terminal to the container output. |
| `-i` | Keep STDIN open for interaction.              |

Example:

```bash
docker start -a -i node-app-container
```

---

## Attach to a Running Container

```bash
docker attach {container_name}
```

Connect your terminal to a running container's main process.

Example:

```bash
docker attach node-app-container
```

---

## View Container Logs

```bash
docker logs {container_name}
```

Display the logs produced by a container.

Example:

```bash
docker logs node-app-container
```

---

## List Containers

### Running Containers

```bash
docker ps
```

Display only the containers that are currently running.

Example:

```bash
docker ps
```

### All Containers

```bash
docker ps -a
```

Display both running and stopped containers.

Example:

```bash
docker ps -a
```

---

## Remove Containers

Remove one container:

```bash
docker rm {container_name}
```

Remove multiple containers:

```bash
docker rm {container_1} {container_2} {container_3}
```

Examples:

```bash
docker rm node-app-container
```

```bash
docker rm container1 container2 container3
```

> **Note:** Containers must be stopped before they can be removed.

---

## List Images

```bash
docker images
```

Display all images stored locally.

Example:

```bash
docker images
```

---

## Remove Images

Remove one or more images:

```bash
docker rmi {image_name}
```

```bash
docker rmi {image_1} {image_2} {image_3}
```

Examples:

```bash
docker rmi node-app-image
```

```bash
docker rmi image1 image2 image3
```

> **Note:** An image cannot be removed while it is still being used by any container (running or stopped).

---

## Remove Unused Images

```bash
docker image prune
```

Remove images that are no longer being used.

Example:

```bash
docker image prune
```

---

## Inspect an Image

```bash
docker image inspect {image_name}
```

Display detailed metadata about an image, including its configuration, layers, exposed ports, environment variables, and operating system.

Example:

```bash
docker image inspect node-app-image
```

---

## Copy Files Between Host and Container

### Copy a File from the Host to a Container

```bash
docker cp {host_file_path} {container_name}:{container_file_path}
```

Copy a file or directory from your local machine into a running or stopped container.

Example:

```bash
docker cp doc/notes.txt node-app-container:/
```

### Copy a File from a Container to the Host

```bash
docker cp {container_name}:{container_file_path} {host_file_path}
```

Copy a file or directory from a container to your local machine.

Example:

```bash
docker cp node-app-container:/notes.txt ./doc/notes.txt
```

> **Note:** `docker cp` works with both running and stopped containers. If the destination directory already exists, the copied file is placed inside it. If the destination file does not exist, Docker creates it.

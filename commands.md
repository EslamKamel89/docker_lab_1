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

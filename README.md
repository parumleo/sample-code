# Docker API Environment Configuration Demo

This Flask REST API demonstrates how Docker environment variables can change application behavior without rebuilding the image.

## 1. Build the image

Run from this project folder:

```bash
docker build -t config-api-demo .
```

## 2. Run configuration A

```bash
docker run --name config-api-a -p 5000:5000 -e APP_ENV=development -e APP_MESSAGE="Hello from development" -e FEATURE_STATUS=enabled config-api-demo
```

In Postman, send:
- `GET http://localhost:5000/config` — shows development settings.
- `GET http://localhost:5000/hello` — returns HTTP 200 and the development message.

## 3. Run configuration B

Stop and remove configuration A:

```bash
docker stop config-api-a
docker rm config-api-a
```

Run the same image with different settings:

```bash
docker run --name config-api-b -p 5000:5000 -e APP_ENV=testing -e APP_MESSAGE="Hello from testing" -e FEATURE_STATUS=disabled config-api-demo
```

In Postman, send:
- `GET http://localhost:5000/config` — shows testing settings.
- `GET http://localhost:5000/hello` — returns HTTP 403 and a feature-disabled error.

## 4. Compare the results

| Request | Configuration A | Configuration B |
|---|---|---|
| `GET /config` | Development settings | Testing settings |
| `GET /hello` | HTTP 200 | HTTP 403 |

The Docker image remains the same; only environment variables change.

## Useful Docker commands

```bash
docker ps
docker logs config-api-b
docker stop config-api-b
docker rm config-api-b
```

Use port 5000 on your computer and `http://localhost:5000` as the Postman base URL. This is a learning demo, not production-ready.

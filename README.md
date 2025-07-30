# ticket-analyzer

## First Time Setup - Pull Ollama Models

- Install certificates so you can pull Ollama models: `docker exec -it ollama sh -c "apk add --no-cache ca-certificates || apt-get update && apt-get install -y ca-certificates && update-ca-certificates"`
- Install Gemma 2b (general reasoning): `docker exec -it ollama ollama pull gemma:2b`
- Install LLaVA (document parsing): `docker exec -it ollama ollama pull llava:latest`

## Running Application

- On first execution, and any time changing docker-compose.yaml or Dockerfile: `docker compose build`
- `docker compose up`

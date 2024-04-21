# Flask API Mirror

This is a simple Flask API that mirrors a word provided as a query parameter and also provides a health check endpoint.

## Running the API

### Prerequisites
- Python 3.9 or higher
- Docker

### Running with Docker

1. Clone this repository.
2. Navigate to the project directory.

```bash
 docker build -t swisspine .
 docker run -d -p 80:4004 swisspine:latest
```
## Endpoints

- `/api/mirror?word={word}` - Mirrors the provided word.
- `/api/health` - Health check endpoint.



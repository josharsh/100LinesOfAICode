# First time setup

```bash
$ cp .env.example .env
```

# Edit .env with your API key

```bash 
$ docker-compose up -d
```

# Run any tool

```bash 
$ docker compose exec tools python week-recap/recap.py
$ docker compose exec tools python commit_ai/commit.py
```

# Interactive shell

```bash
$ docker compose exec tools bash
```

# Stop

```bash 
$ docker compose down
```

# For development 

use the following command to make a temprary .env file based on the .env.example.

```bash 
$ cp .env.example .env 
```


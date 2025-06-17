# TeamSpeak WG Auth Bot

A TeamSpeak bot that responds to commands and welcomes users when they join the server.

## Quick Start with Docker

1. Create a `.env` file in the project root with your TeamSpeak server credentials:
```env
TS_SERVER_QUERY_USERNAME=YourQueryUsername
TS_SERVER_QUERY_PASSWORD=YourQueryPassword
TS_ADDRESS=your.teamspeak.server
TS_PORT=10011
TS_NICKNAME=Your Bot Name
TS_PROTOCOL=raw
```

2. Build and start the container:
```bash
docker-compose up --build
```

3. To run in the background:
```bash
docker-compose up -d
```

4. View logs:
```bash
docker-compose logs -f
```

5. Stop the bot:
```bash
docker-compose down
```

## Available Commands

- `!hello` - Bot responds with a greeting

## Automatic Actions

- Sends a welcome message when a user joins the server

## Troubleshooting

1. **No console output**
   - Check Docker logs: `docker-compose logs -f`
   - Verify environment variables are set correctly

2. **Bot not connecting**
   - Verify your TeamSpeak server query credentials in `.env`
   - Check if the server is running and accessible
   - Ensure the port is correct and open

3. **Container issues**
   - Check container status: `docker-compose ps`
   - View detailed logs: `docker-compose logs --tail=100`
   - Restart container: `docker-compose restart` 
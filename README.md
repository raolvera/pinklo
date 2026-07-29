# Emoji Drop 3D - 360 Space Edition

A playful 3D plinko-style game built with Three.js, Cannon.js, HTML, and CSS. Players can rotate the board, drop metallic balls or emojis, earn multipliers, and compete on a live leaderboard.

## Features

- 3D rotating plinko board with animated pegs and multiplier boxes
- Responsive desktop, tablet, and mobile layouts
- Drop metallic balls or real emoji payloads
- Floating animated emoji effects and billboarding labels
- Local Python server for leaderboard API support

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- 3D Graphics: Three.js
- Physics: Cannon.js
- Backend: Python `http.server`

## Run Locally

1. Open a terminal in the project folder
2. Start the local server:

```bash
python server.py
```

3. Open the game in your browser:

```text
http://127.0.0.1:8000/index.html
```

## Play on GitHub Pages

The game is also ready to be published as a GitHub Pages site so others can play it directly from a URL.

### What to do

1. Open your repository on GitHub
2. Go to Settings → Pages
3. Under "Build and deployment", choose "GitHub Actions"
4. Push to the `master` branch and wait for the workflow to finish

Once deployed, the site will be available at:

```text
https://<your-username>.github.io/pinklo/
```

Note: the Python leaderboard backend is only used when running locally. On GitHub Pages, the game uses the built-in demo leaderboard so the experience still works as a static site.

## Project Structure

- `index.html` — the full game UI, 3D scene, and game logic
- `server.py` — simple Python server with health and leaderboard endpoints
- `README.md` — project overview and setup instructions
- `SECURITY.md` — vulnerability reporting guidance
- `LICENSE` — MIT license

## Development Notes

- The game uses a local Python endpoint at `/api/leaderboard` and `/api/health` for leaderboard support.
- If the Python server is not running, the game falls back to built-in demo leaderboard data.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

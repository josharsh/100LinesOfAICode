# Twitter/X Bot for 100LinesOfAICode

Automated social media presence to showcase tools and grow the community.

## Features

- **Daily Tool Spotlights** (Mon-Fri): Highlights one of the 17 tools with description and link.
- **Weekend Code Tips**: Shares best practices and tips.
- **Contributor Shoutouts**: Randomly thanks contributors and celebrates milestones.
- **Interactive**: (Coming soon) Reply to mentions with tool suggestions.

## Setup

1. Clone the repository.
2. Copy `.env.example` to `.env` and fill in your Twitter API credentials.
3. Install dependencies:

   ```bash
   pip install tweepy
   ```

4. Run in dry-run mode to test:

   ```bash
   DRY_RUN=true python bot.py
   ```

5. To tweet for real, set `DRY_RUN=false`.

## Scheduling with GitHub Actions

Include the provided workflow file `.github/workflows/tweet.yml` and set the secrets in your repository.

## Content

Edit `content.json` to customize tweets. Structure:
- `tools`: Array of tool objects with name, description, lines.
- `tool_spotlight`: Templates for daily spotlights.
- `code_tip`: Templates for weekend tips.
- `tips`: Array of tip text strings.
- `shoutouts`: Array of pre-written shoutout tweets.

## License

MIT

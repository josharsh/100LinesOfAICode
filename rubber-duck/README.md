# 🦆 Rubber Duck AI

**Rubber duck debugging** - But it talks back!

## Quick Start

```bash
pip install anthropic
export ANTHROPIC_API_KEY=your_key

python duck.py                    # Interactive
python duck.py "my bug question"  # Quick mode
```

## Session Example

```
🦆 Hi! Tell me what's bugging you.

You: My API returns 500 but only sometimes

🦆 Interesting! Let's think through this:
   • Is it truly random, or patterns?
   • Does it happen at specific times?
   • Related to traffic load?
   • What changed recently?

You: Only when there are lots of requests!

🦆 *excited quacking* 🎉
   Sounds like concurrency or resource exhaustion!
   - Using connection pooling?
   - Running out of memory?
   - Check the logs for timeouts?

You: The cache is filling up!

🦆 BINGO! 🎯 Classic cache overflow.
   Quick fixes:
   1. Add cache size limits
   2. Implement LRU eviction
   3. Add monitoring
```

**Commands:** `quit` to exit, `clear` to start over

**80 lines. Your debugging buddy.**

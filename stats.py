import glob
import requests

# Change ici si tes outils sont dans un autre dossier ou extension
files = glob.glob("**/*.py", recursive=True)

agent_files = glob.glob("ai-agent/agent*py")

ai_tools = []
for file in agent_files:
    with open(file, encoding="utf-8") as f:
        lines = f.readlines()
    if len(lines) < 100:
        ai_tools.append((file, len(lines)))

total_lines = sum(len(open(f, encoding="utf-8").readlines()) for f in files)

print(f"Nombre d'AI Tools (<100 lignes) : {len(ai_tools)}")
print(f"Total lignes de code : {total_lines}")
print("Fichiers trouvés :")
for f, n in ai_tools:
    print(f" - {f}: {n} lignes")


def make_badge(label, value, color="blue"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="150" height="20">
  <rect width="70" height="20" fill="#555"/>
  <rect x="70" width="80" height="20" fill="{color}"/>
  <text x="35" y="14" fill="#fff" font-family="Verdana" font-size="11" text-anchor="middle">{label}</text>
  <text x="110" y="14" fill="#fff" font-family="Verdana" font-size="11" text-anchor="middle">{value}</text>
</svg>'''


badge_url_AI_tools = f"https://img.shields.io/badge/Agents-{len(ai_tools)}-blue"
badge_url_lines = f"https://img.shields.io/badge/Lines-{total_lines}-blue"
badge_svg_AI_tools = requests.get(badge_url_AI_tools).text
badge_svg_lines = requests.get(badge_url_lines).text

with open("badge_agents.svg", "w", encoding="utf-8") as f:
    f.write(badge_svg_AI_tools)

with open("badge_lines.svg", "w", encoding="utf-8") as f:
    f.write(badge_svg_lines)

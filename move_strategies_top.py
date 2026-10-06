with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract Strategies section
strategies_marker_start = '<!-- Strategies Section -->'
strategies_marker_end = '</section>\n'

start_idx = content.find(strategies_marker_start)
end_idx = content.find(strategies_marker_end, start_idx) + len(strategies_marker_end)

strategies_block = content[start_idx:end_idx]

# Remove strategies_block from current position
content_without_strategies = content[:start_idx] + content[end_idx:]

# Find Hero section end
hero_end_marker = '</section>\n'
hero_start_idx = content_without_strategies.find('<section class="about-hero">')
hero_end_idx = content_without_strategies.find(hero_end_marker, hero_start_idx) + len(hero_end_marker)

# Insert strategies_block right after hero_end_idx
new_content = content_without_strategies[:hero_end_idx] + '\n\n        ' + strategies_block.strip() + '\n' + content_without_strategies[hero_end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Moved Strategies section directly under Hero section!")

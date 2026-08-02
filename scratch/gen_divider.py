divider_svg = '''<svg fill="none" viewBox="0 0 1200 8" width="100%" height="8" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="div-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0"/>
      <stop offset="20%" stop-color="#22D3EE" stop-opacity="0.8"/>
      <stop offset="40%" stop-color="#8B5CF6"/>
      <stop offset="60%" stop-color="#EC4899"/>
      <stop offset="80%" stop-color="#22D3EE" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#22D3EE" stop-opacity="0"/>
    </linearGradient>

    <filter id="div-glow" x="-10%" y="-100%" width="120%" height="300%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Glowing Backdrop Track -->
  <rect width="1200" height="4" y="2" rx="2" fill="url(#div-grad)" filter="url(#div-glow)" opacity="0.6"/>
  <!-- Crisp Central Core Bar -->
  <rect width="1200" height="2" y="3" rx="1" fill="url(#div-grad)"/>
  <!-- Central Diamond Accent Node -->
  <polygon points="600,1 604,4 600,7 596,4" fill="#22D3EE" filter="url(#div-glow)"/>
</svg>
'''

with open('assets/divider.svg', 'w', encoding='utf-8') as f:
    f.write(divider_svg)

print("divider.svg updated successfully")

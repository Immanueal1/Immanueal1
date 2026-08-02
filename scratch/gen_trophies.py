trophies_svg = '''<svg fill="none" viewBox="0 0 1200 230" width="1200" height="230" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1200" y2="230" gradientUnits="userSpaceOnUse">
      <stop stop-color="#090A12"/>
      <stop offset="0.5" stop-color="#121426"/>
      <stop offset="1" stop-color="#090A12"/>
    </linearGradient>

    <radialGradient id="glow-purple" cx="50%" cy="50%" r="50%">
      <stop stop-color="#6D28D9" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#090A12" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="accent" x1="0" y1="0" x2="1200" y2="0" gradientUnits="userSpaceOnUse">
      <stop stop-color="#8B5CF6"/>
      <stop offset="0.5" stop-color="#22D3EE"/>
      <stop offset="1" stop-color="#EC4899"/>
    </linearGradient>

    <linearGradient id="cup-gradient" x1="0" y1="0" x2="0" y2="100%">
      <stop stop-color="#22D3EE"/>
      <stop offset="0.5" stop-color="#8B5CF6"/>
      <stop offset="1" stop-color="#EC4899"/>
    </linearGradient>

    <linearGradient id="card-bg" x1="0" y1="0" x2="0" y2="100%">
      <stop stop-color="#171A30" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#121426" stop-opacity="0.95"/>
    </linearGradient>

    <filter id="glow-soft" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M 30 0 L 0 0 0 30" fill="none" stroke="#8B5CF6" stroke-opacity="0.06" stroke-width="1"/>
    </pattern>

    <style>
      .card { fill: url(#card-bg); stroke: #8B5CF6; stroke-opacity: 0.35; stroke-width: 1.5; }
      .title { font: 800 16px "Inter", -apple-system, sans-serif; fill: #F8FAFC; }
      .label { font: 700 12px "Fira Code", monospace; fill: #22D3EE; letter-spacing: 2px; }
      .cup { stroke: url(#cup-gradient); stroke-width: 2.8; stroke-linecap: round; stroke-linejoin: round; fill: none; }
      .trophy-glow { filter: url(#glow-soft); }
    </style>
  </defs>

  <rect width="1200" height="230" rx="18" fill="url(#bg)"/>
  <rect width="1200" height="230" rx="18" fill="url(#glow-purple)"/>
  <rect width="1200" height="230" rx="18" fill="url(#grid)"/>

  <!-- Outer Glassmorphic Border -->
  <rect x="2" y="2" width="1196" height="226" rx="16" stroke="url(#accent)" stroke-opacity="0.65" stroke-width="2.5" fill="none"/>

  <g transform="translate(50 42)">
    <!-- TROPHY 1: Product Builder -->
    <g>
      <rect class="card" width="165" height="132" rx="16"/>
      <g transform="translate(41 16)" class="trophy-glow">
        <path class="cup" d="M 22 10 H 62 V 34 C 62 56 52 68 42 68 C 32 68 22 56 22 34 V 10 Z M 22 20 H 6 C 6 40 15 50 31 51 M 62 20 H 78 C 78 40 69 50 53 51 M 42 68 V 82 H 58 M 30 82 H 54"/>
        <polygon points="42,22 45,28 52,29 47,34 48,41 42,37 36,41 37,34 32,29 39,28" fill="#22D3EE"/>
      </g>
      <text x="82" y="118" text-anchor="middle" class="title">Product Builder</text>
    </g>

    <!-- TROPHY 2: Firmware -->
    <g transform="translate(185)">
      <rect class="card" width="165" height="132" rx="16"/>
      <g transform="translate(41 16)" class="trophy-glow">
        <path class="cup" d="M 22 10 H 62 V 34 C 62 56 52 68 42 68 C 32 68 22 56 22 34 V 10 Z M 22 20 H 6 C 6 40 15 50 31 51 M 62 20 H 78 C 78 40 69 50 53 51 M 42 68 V 82 H 58 M 30 82 H 54"/>
        <!-- Chip Accent Inside Cup -->
        <rect x="34" y="24" width="16" height="16" rx="3" fill="#8B5CF6" stroke="#22D3EE" stroke-width="1.5"/>
      </g>
      <text x="82" y="118" text-anchor="middle" class="title">Firmware</text>
    </g>

    <!-- TROPHY 3: Edge AI -->
    <g transform="translate(370)">
      <rect class="card" width="165" height="132" rx="16"/>
      <g transform="translate(41 16)" class="trophy-glow">
        <path class="cup" d="M 22 10 H 62 V 34 C 62 56 52 68 42 68 C 32 68 22 56 22 34 V 10 Z M 22 20 H 6 C 6 40 15 50 31 51 M 62 20 H 78 C 78 40 69 50 53 51 M 42 68 V 82 H 58 M 30 82 H 54"/>
        <!-- Neural Nodes Accent -->
        <circle cx="34" cy="30" r="3" fill="#EC4899"/>
        <circle cx="50" cy="30" r="3" fill="#EC4899"/>
        <circle cx="42" cy="40" r="3.5" fill="#22D3EE"/>
        <line x1="34" y1="30" x2="42" y2="40" stroke="#8B5CF6" stroke-width="1.5"/>
        <line x1="50" y1="30" x2="42" y2="40" stroke="#8B5CF6" stroke-width="1.5"/>
      </g>
      <text x="82" y="118" text-anchor="middle" class="title">Edge AI</text>
    </g>

    <!-- TROPHY 4: PCB Design -->
    <g transform="translate(555)">
      <rect class="card" width="165" height="132" rx="16"/>
      <g transform="translate(41 16)" class="trophy-glow">
        <path class="cup" d="M 22 10 H 62 V 34 C 62 56 52 68 42 68 C 32 68 22 56 22 34 V 10 Z M 22 20 H 6 C 6 40 15 50 31 51 M 62 20 H 78 C 78 40 69 50 53 51 M 42 68 V 82 H 58 M 30 82 H 54"/>
        <!-- Trace Trace Accent -->
        <path d="M 32 30 H 42 L 52 40" stroke="#22D3EE" stroke-width="2" stroke-linecap="round" fill="none"/>
        <circle cx="32" cy="30" r="2.5" fill="#22D3EE"/>
        <circle cx="52" cy="40" r="2.5" fill="#22D3EE"/>
      </g>
      <text x="82" y="118" text-anchor="middle" class="title">PCB Design</text>
    </g>

    <!-- TROPHY 5: Open Source -->
    <g transform="translate(740)">
      <rect class="card" width="165" height="132" rx="16"/>
      <g transform="translate(41 16)" class="trophy-glow">
        <path class="cup" d="M 22 10 H 62 V 34 C 62 56 52 68 42 68 C 32 68 22 56 22 34 V 10 Z M 22 20 H 6 C 6 40 15 50 31 51 M 62 20 H 78 C 78 40 69 50 53 51 M 42 68 V 82 H 58 M 30 82 H 54"/>
        <!-- Branching Node Accent -->
        <circle cx="42" cy="24" r="3" fill="#22D3EE"/>
        <circle cx="34" cy="40" r="3" fill="#EC4899"/>
        <circle cx="50" cy="40" r="3" fill="#8B5CF6"/>
        <path d="M 42 27 L 34 37 M 42 27 L 50 37" stroke="#F8FAFC" stroke-width="1.5"/>
      </g>
      <text x="82" y="118" text-anchor="middle" class="title">Open Source</text>
    </g>

    <!-- TROPHY 6: Clean Energy -->
    <g transform="translate(925)">
      <rect class="card" width="165" height="132" rx="16"/>
      <g transform="translate(41 16)" class="trophy-glow">
        <path class="cup" d="M 22 10 H 62 V 34 C 62 56 52 68 42 68 C 32 68 22 56 22 34 V 10 Z M 22 20 H 6 C 6 40 15 50 31 51 M 62 20 H 78 C 78 40 69 50 53 51 M 42 68 V 82 H 58 M 30 82 H 54"/>
        <!-- Bolt Accent -->
        <polygon points="44,22 36,34 43,34 40,46 48,32 41,32" fill="#22D3EE"/>
      </g>
      <text x="82" y="118" text-anchor="middle" class="title">Clean Energy</text>
    </g>
  </g>

  <!-- Bottom Monospace Label -->
  <text x="600" y="202" text-anchor="middle" class="label">LOCAL TROPHY PANEL • STABLE GITHUB MARKDOWN SVG</text>
</svg>
'''

with open('assets/github-trophies.svg', 'w', encoding='utf-8') as f:
    f.write(trophies_svg)

print("github-trophies.svg updated successfully")

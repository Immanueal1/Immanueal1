import os

header_banner_svg = '''<svg fill="none" viewBox="0 0 1200 300" width="1200" height="300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Dark Neon Dashboard Gradients -->
    <linearGradient id="bg" x1="0" y1="0" x2="1200" y2="300" gradientUnits="userSpaceOnUse">
      <stop stop-color="#090A12"/>
      <stop offset="0.5" stop-color="#121426"/>
      <stop offset="1" stop-color="#090A12"/>
    </linearGradient>

    <radialGradient id="ambient-glow1" cx="20%" cy="30%" r="60%">
      <stop stop-color="#6D28D9" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#090A12" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="ambient-glow2" cx="80%" cy="70%" r="60%">
      <stop stop-color="#22D3EE" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#090A12" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="neon-trace" x1="0" y1="0" x2="1200" y2="300" gradientUnits="userSpaceOnUse">
      <stop stop-color="#22D3EE"/>
      <stop offset="0.4" stop-color="#8B5CF6"/>
      <stop offset="0.8" stop-color="#EC4899"/>
      <stop offset="1" stop-color="#38BDF8"/>
    </linearGradient>

    <linearGradient id="card-border" x1="0" y1="0" x2="1200" y2="300" gradientUnits="userSpaceOnUse">
      <stop stop-color="#8B5CF6" stop-opacity="0.6"/>
      <stop offset="0.5" stop-color="#22D3EE" stop-opacity="0.8"/>
      <stop offset="1" stop-color="#EC4899" stop-opacity="0.5"/>
    </linearGradient>

    <linearGradient id="chip-bg" x1="0" y1="0" x2="0" y2="100%">
      <stop stop-color="#171A30" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#121426" stop-opacity="0.9"/>
    </linearGradient>

    <!-- Glow Filters -->
    <filter id="glow-heavy" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="glow-soft" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Technical Grid Pattern -->
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#8B5CF6" stroke-opacity="0.08" stroke-width="1"/>
      <circle cx="40" cy="40" r="1" fill="#22D3EE" fill-opacity="0.15"/>
    </pattern>

    <style>
      .label-mono { font: 700 13px "Fira Code", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; fill: #22D3EE; letter-spacing: 3px; }
      .hero-title { font: 800 54px "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; fill: #F8FAFC; letter-spacing: -0.5px; }
      .hero-sub { font: 500 18px "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; fill: #A1A8C5; }
      .chip-text { font: 700 13px "Fira Code", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; fill: #F8FAFC; letter-spacing: 1px; }

      .trace-line { stroke: url(#neon-trace); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; fill: none; stroke-dasharray: 12 16; animation: flowTrace 12s linear infinite; }
      .trace-bus { stroke: #8B5CF6; stroke-opacity: 0.25; stroke-width: 1; fill: none; }

      .pulse-node { animation: nodePulse 3.5s ease-in-out infinite; }
      .glow-border { animation: borderGlow 6s ease-in-out infinite alternate; }

      @keyframes flowTrace { to { stroke-dashoffset: -280; } }
      @keyframes nodePulse { 0%, 100% { opacity: 0.4; transform: scale(1); } 50% { opacity: 1; transform: scale(1.3); } }
      @keyframes borderGlow { 0% { stroke-opacity: 0.4; } 100% { stroke-opacity: 0.85; } }
    </style>
  </defs>

  <!-- Base Canvas & Ambient Glows -->
  <rect width="1200" height="300" rx="18" fill="url(#bg)"/>
  <rect width="1200" height="300" rx="18" fill="url(#ambient-glow1)"/>
  <rect width="1200" height="300" rx="18" fill="url(#ambient-glow2)"/>

  <!-- Technical Grid -->
  <rect width="1200" height="300" rx="18" fill="url(#grid)"/>

  <!-- Glassmorphic Outer Border -->
  <rect x="2" y="2" width="1196" height="296" rx="16" stroke="url(#card-border)" stroke-width="2" fill="none" class="glow-border"/>

  <!-- Corner Tech Accent Details -->
  <path d="M 25 15 L 15 15 L 15 25" stroke="#22D3EE" stroke-width="2.5" stroke-linecap="round" fill="none"/>
  <path d="M 1175 15 L 1185 15 L 1185 25" stroke="#22D3EE" stroke-width="2.5" stroke-linecap="round" fill="none"/>
  <path d="M 25 285 L 15 285 L 15 275" stroke="#EC4899" stroke-width="2.5" stroke-linecap="round" fill="none"/>
  <path d="M 1175 285 L 1185 285 L 1185 275" stroke="#EC4899" stroke-width="2.5" stroke-linecap="round" fill="none"/>

  <!-- Circuit Trace Lines & Bus Geometry -->
  <path class="trace-bus" d="M 60 70 H 280 L 330 120 H 500 M 700 120 H 870 L 920 70 H 1140"/>
  <path class="trace-bus" d="M 60 230 H 260 L 310 180 H 480 M 720 180 H 890 L 940 230 H 1140"/>

  <path class="trace-line" d="M 60 70 H 280 L 330 120 H 480 M 720 120 H 870 L 920 70 H 1140"/>
  <path class="trace-line" d="M 60 230 H 260 L 310 180 H 500 M 700 180 H 890 L 940 230 H 1140" opacity="0.8"/>

  <!-- Glowing Nodes -->
  <g filter="url(#glow-heavy)">
    <circle cx="60" cy="70" r="4.5" fill="#22D3EE" class="pulse-node"/>
    <circle cx="330" cy="120" r="4.5" fill="#8B5CF6" class="pulse-node"/>
    <circle cx="870" cy="120" r="4.5" fill="#EC4899" class="pulse-node"/>
    <circle cx="1140" cy="70" r="4.5" fill="#22D3EE" class="pulse-node"/>
    <circle cx="60" cy="230" r="4.5" fill="#EC4899" class="pulse-node"/>
    <circle cx="1140" cy="230" r="4.5" fill="#38BDF8" class="pulse-node"/>
  </g>

  <!-- Central Header Text Stack -->
  <g text-anchor="middle">
    <!-- Category Monospace Signal Tag -->
    <text x="600" y="82" class="label-mono">EMBEDDED SYSTEMS  /  FIRMWARE  /  PCB DESIGN  /  EDGE AI  /  IOT</text>
    
    <!-- Main Name Title -->
    <text x="600" y="146" class="hero-title">Krishna Kant Garhe</text>

    <!-- Subtitle -->
    <text x="600" y="186" class="hero-sub">Building intelligent hardware from circuit schematics to deployable firmware and ML pipelines</text>
  </g>

  <!-- Bottom Interactive Skill Chips Stack -->
  <g transform="translate(600 244)" text-anchor="middle">
    <!-- ESP32 -->
    <g transform="translate(-350)">
      <rect x="-62" y="-19" width="124" height="38" rx="12" fill="url(#chip-bg)" stroke="#22D3EE" stroke-opacity="0.6" stroke-width="1.5" filter="url(#glow-soft)"/>
      <text y="5" class="chip-text">ESP32</text>
    </g>

    <!-- RP2040 -->
    <g transform="translate(-210)">
      <rect x="-62" y="-19" width="124" height="38" rx="12" fill="url(#chip-bg)" stroke="#8B5CF6" stroke-opacity="0.6" stroke-width="1.5" filter="url(#glow-soft)"/>
      <text y="5" class="chip-text">RP2040</text>
    </g>

    <!-- STM32 -->
    <g transform="translate(-70)">
      <rect x="-62" y="-19" width="124" height="38" rx="12" fill="url(#chip-bg)" stroke="#8B5CF6" stroke-opacity="0.6" stroke-width="1.5" filter="url(#glow-soft)"/>
      <text y="5" class="chip-text">STM32</text>
    </g>

    <!-- KiCad -->
    <g transform="translate(70)">
      <rect x="-62" y="-19" width="124" height="38" rx="12" fill="url(#chip-bg)" stroke="#22D3EE" stroke-opacity="0.6" stroke-width="1.5" filter="url(#glow-soft)"/>
      <text y="5" class="chip-text">KiCad</text>
    </g>

    <!-- TinyML -->
    <g transform="translate(210)">
      <rect x="-62" y="-19" width="124" height="38" rx="12" fill="url(#chip-bg)" stroke="#EC4899" stroke-opacity="0.6" stroke-width="1.5" filter="url(#glow-soft)"/>
      <text y="5" class="chip-text">TinyML</text>
    </g>

    <!-- BMS -->
    <g transform="translate(350)">
      <rect x="-62" y="-19" width="124" height="38" rx="12" fill="url(#chip-bg)" stroke="#8B5CF6" stroke-opacity="0.6" stroke-width="1.5" filter="url(#glow-soft)"/>
      <text y="5" class="chip-text">BMS</text>
    </g>
  </g>
</svg>
'''

with open('assets/header-banner.svg', 'w', encoding='utf-8') as f:
    f.write(header_banner_svg)

print("header-banner.svg updated successfully")

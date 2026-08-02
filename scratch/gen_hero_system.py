hero_system_svg = '''<svg fill="none" viewBox="0 0 1100 250" width="1100" height="250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Dark Neon Dashboard Gradients -->
    <linearGradient id="bg" x1="0" y1="0" x2="1100" y2="250" gradientUnits="userSpaceOnUse">
      <stop stop-color="#090A12"/>
      <stop offset="0.5" stop-color="#121426"/>
      <stop offset="1" stop-color="#090A12"/>
    </linearGradient>

    <radialGradient id="glow-center" cx="50%" cy="50%" r="50%">
      <stop stop-color="#6D28D9" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#090A12" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="bus-glow" x1="0" y1="0" x2="1100" y2="0" gradientUnits="userSpaceOnUse">
      <stop stop-color="#22D3EE"/>
      <stop offset="0.33" stop-color="#8B5CF6"/>
      <stop offset="0.66" stop-color="#EC4899"/>
      <stop offset="1" stop-color="#38BDF8"/>
    </linearGradient>

    <linearGradient id="card-border" x1="0" y1="0" x2="0" y2="100%">
      <stop stop-color="#8B5CF6" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#22D3EE" stop-opacity="0.3"/>
    </linearGradient>

    <linearGradient id="mcu-border" x1="0" y1="0" x2="100%" y2="100%">
      <stop stop-color="#22D3EE"/>
      <stop offset="0.5" stop-color="#8B5CF6"/>
      <stop offset="1" stop-color="#EC4899"/>
    </linearGradient>

    <linearGradient id="card-bg" x1="0" y1="0" x2="0" y2="100%">
      <stop stop-color="#171A30" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#121426" stop-opacity="0.95"/>
    </linearGradient>

    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <pattern id="grid-pattern" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M 30 0 L 0 0 0 30" fill="none" stroke="#8B5CF6" stroke-opacity="0.07" stroke-width="1"/>
    </pattern>

    <style>
      .wire-base { stroke: #8B5CF6; stroke-opacity: 0.2; stroke-width: 2.5; fill: none; }
      .wire-active { stroke: url(#bus-glow); stroke-width: 2.5; stroke-linecap: round; fill: none; stroke-dasharray: 10 14; animation: busFlow 8s linear infinite; }

      .card-title { font: 800 16px "Inter", -apple-system, sans-serif; fill: #F8FAFC; letter-spacing: 0.5px; }
      .card-sub { font: 700 12px "Fira Code", monospace; fill: #A1A8C5; letter-spacing: 0.8px; }

      .status-dot { animation: dotBlink 2.2s ease-in-out infinite; }
      .mcu-pulse { animation: mcuGlow 4s ease-in-out infinite alternate; }

      @keyframes busFlow { to { stroke-dashoffset: -240; } }
      @keyframes dotBlink { 0%, 100% { opacity: 0.35; transform: scale(0.9); } 50% { opacity: 1; transform: scale(1.15); } }
      @keyframes mcuGlow { 0% { stroke-opacity: 0.5; } 100% { stroke-opacity: 1; } }
    </style>
  </defs>

  <!-- Background & Radial Glow -->
  <rect width="1100" height="250" rx="18" fill="url(#bg)"/>
  <rect width="1100" height="250" rx="18" fill="url(#glow-center)"/>
  <rect width="1100" height="250" rx="18" fill="url(#grid-pattern)"/>

  <!-- Outer Glassmorphic Border -->
  <rect x="2" y="2" width="1096" height="246" rx="16" stroke="url(#card-border)" stroke-width="2" fill="none"/>

  <!-- Neon Circuit Bus Traces (Connecting Modules) -->
  <path class="wire-base" d="M 151 125 H 332 M 494 125 H 642 M 792 125 H 934"/>
  <path class="wire-active" d="M 151 125 H 332 M 494 125 H 642 M 792 125 H 934"/>

  <!-- Parallel Bus Lines (Subtle Top Trace) -->
  <path class="wire-base" d="M 230 78 H 360 L 410 165 H 580 L 630 78 H 860" opacity="0.4"/>
  <path class="wire-active" d="M 230 78 H 360 L 410 165 H 580 L 630 78 H 860" opacity="0.6"/>

  <!-- MODULE 1: SENSORS -->
  <g transform="translate(66 52)">
    <rect width="170" height="146" rx="16" fill="url(#card-bg)" stroke="url(#card-border)" stroke-width="1.5"/>
    <!-- Sensor Icon / Spec Graphic -->
    <g transform="translate(85 42)">
      <circle cx="0" cy="0" r="22" fill="#121426" stroke="#22D3EE" stroke-width="1.5"/>
      <circle cx="0" cy="0" r="14" fill="#6D28D9" fill-opacity="0.4" stroke="#8B5CF6"/>
      <circle cx="0" cy="0" r="6" fill="#22D3EE" filter="url(#glow)"/>
    </g>
    <text x="85" y="86" text-anchor="middle" class="card-title">Sensors</text>
    <text x="85" y="108" text-anchor="middle" class="card-sub">NIR • AFE • ADC</text>
    <!-- Channel Indicators -->
    <g transform="translate(50 122)">
      <circle cx="0" cy="0" r="4" fill="#22D3EE" class="status-dot" filter="url(#glow)"/>
      <circle cx="35" cy="0" r="4" fill="#8B5CF6" class="status-dot" filter="url(#glow)" style="animation-delay: 0.5s"/>
      <circle cx="70" cy="0" r="4" fill="#EC4899" class="status-dot" filter="url(#glow)" style="animation-delay: 1s"/>
    </g>
  </g>

  <!-- MODULE 2: MCU (CORE) -->
  <g transform="translate(322 36)">
    <rect width="180" height="178" rx="20" fill="url(#card-bg)" stroke="url(#mcu-border)" stroke-width="2.5" class="mcu-pulse" filter="url(#glow)"/>
    
    <!-- Microcontroller Package Frame -->
    <rect x="36" y="32" width="108" height="108" rx="14" fill="#090A12" stroke="#8B5CF6" stroke-width="1.5"/>
    <rect x="48" y="44" width="84" height="84" rx="8" fill="#171A30" stroke="#22D3EE" stroke-dasharray="6 4" stroke-opacity="0.6"/>
    
    <!-- IC Text -->
    <text x="90" y="80" text-anchor="middle" class="card-title" fill="#22D3EE">MCU</text>
    <text x="90" y="102" text-anchor="middle" class="card-sub" font-size="10">ESP32 / RP2040</text>
    
    <!-- Microchip IC Pins -->
    <!-- Left Pins -->
    <line x1="20" y1="52" x2="36" y2="52" stroke="#22D3EE" stroke-width="2"/>
    <line x1="20" y1="72" x2="36" y2="72" stroke="#22D3EE" stroke-width="2"/>
    <line x1="20" y1="92" x2="36" y2="92" stroke="#22D3EE" stroke-width="2"/>
    <line x1="20" y1="112" x2="36" y2="112" stroke="#22D3EE" stroke-width="2"/>
    
    <!-- Right Pins -->
    <line x1="144" y1="52" x2="160" y2="52" stroke="#EC4899" stroke-width="2"/>
    <line x1="144" y1="72" x2="160" y2="72" stroke="#EC4899" stroke-width="2"/>
    <line x1="144" y1="92" x2="160" y2="92" stroke="#EC4899" stroke-width="2"/>
    <line x1="144" y1="112" x2="160" y2="112" stroke="#EC4899" stroke-width="2"/>

    <!-- Bottom Status Text -->
    <text x="90" y="160" text-anchor="middle" class="card-sub" fill="#22D3EE">32-BIT CORE</text>
  </g>

  <!-- MODULE 3: EDGE AI -->
  <g transform="translate(632 52)">
    <rect width="170" height="146" rx="16" fill="url(#card-bg)" stroke="url(#card-border)" stroke-width="1.5"/>
    <!-- Neural Node Diagram -->
    <g transform="translate(85 40)">
      <path d="M -30 -10 L 0 0 L 30 -10 M -30 10 L 0 0 L 30 10 M 0 -15 L 0 15" stroke="#8B5CF6" stroke-width="1.5" opacity="0.6"/>
      <circle cx="-30" cy="-10" r="5" fill="#22D3EE" filter="url(#glow)"/>
      <circle cx="-30" cy="10" r="5" fill="#22D3EE" filter="url(#glow)"/>
      <circle cx="0" cy="0" r="6" fill="#8B5CF6" filter="url(#glow)"/>
      <circle cx="30" cy="-10" r="5" fill="#EC4899" filter="url(#glow)"/>
      <circle cx="30" cy="10" r="5" fill="#EC4899" filter="url(#glow)"/>
    </g>
    <text x="85" y="86" text-anchor="middle" class="card-title">Edge AI</text>
    <text x="85" y="108" text-anchor="middle" class="card-sub">SVM • CNN • TinyML</text>
    <!-- Waveform Sine Path -->
    <path d="M 45 125 Q 65 115, 85 125 T 125 125" stroke="#22D3EE" stroke-width="2" fill="none" stroke-linecap="round"/>
  </g>

  <!-- MODULE 4: PRODUCT -->
  <g transform="translate(864 52)">
    <rect width="170" height="146" rx="16" fill="url(#card-bg)" stroke="url(#card-border)" stroke-width="1.5"/>
    <!-- Product Hardware Icon -->
    <g transform="translate(85 42)">
      <rect x="-24" y="-16" width="48" height="32" rx="6" fill="#121426" stroke="#8B5CF6" stroke-width="1.5"/>
      <rect x="-16" y="-8" width="14" height="16" rx="3" fill="#22D3EE" fill-opacity="0.8"/>
      <rect x="2" y="-8" width="14" height="16" rx="3" fill="#EC4899" fill-opacity="0.8"/>
    </g>
    <text x="85" y="86" text-anchor="middle" class="card-title">Product</text>
    <text x="85" y="108" text-anchor="middle" class="card-sub">PCB • IoT • BMS</text>
    <!-- Status LED Bar -->
    <rect x="55" y="120" width="60" height="6" rx="3" fill="#121426"/>
    <rect x="55" y="120" width="45" height="6" rx="3" fill="url(#bus-glow)"/>
  </g>
</svg>
'''

with open('assets/hero-system.svg', 'w', encoding='utf-8') as f:
    f.write(hero_system_svg)

print("hero-system.svg updated successfully")

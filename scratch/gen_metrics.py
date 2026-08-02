metrics_svg = '''<svg fill="none" viewBox="0 0 1200 310" width="1200" height="310" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1200" y2="310" gradientUnits="userSpaceOnUse">
      <stop stop-color="#090A12"/>
      <stop offset="0.5" stop-color="#121426"/>
      <stop offset="1" stop-color="#090A12"/>
    </linearGradient>

    <radialGradient id="glow-purple" cx="30%" cy="40%" r="60%">
      <stop stop-color="#6D28D9" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#090A12" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="accent" x1="0" y1="0" x2="1200" y2="0" gradientUnits="userSpaceOnUse">
      <stop stop-color="#22D3EE"/>
      <stop offset="0.5" stop-color="#8B5CF6"/>
      <stop offset="1" stop-color="#EC4899"/>
    </linearGradient>

    <linearGradient id="card-bg" x1="0" y1="0" x2="0" y2="100%">
      <stop stop-color="#171A30" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#121426" stop-opacity="0.95"/>
    </linearGradient>

    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#8B5CF6" stroke-opacity="0.06" stroke-width="1"/>
    </pattern>

    <style>
      .title { font: 800 28px "Inter", -apple-system, sans-serif; fill: #F8FAFC; letter-spacing: -0.5px; }
      .sub { font: 500 15px "Inter", -apple-system, sans-serif; fill: #A1A8C5; }
      .label { font: 800 14px "Fira Code", monospace; fill: #22D3EE; letter-spacing: 1.5px; }
      .body { font: 700 18px "Inter", -apple-system, sans-serif; fill: #F8FAFC; }
      .muted { font: 500 13px "Inter", -apple-system, sans-serif; fill: #A1A8C5; }

      .card { fill: url(#card-bg); stroke: #8B5CF6; stroke-opacity: 0.35; stroke-width: 1.5; }
      .bottom-trace { stroke: url(#accent); stroke-width: 3; stroke-linecap: round; stroke-dasharray: 12 16; animation: dashPulse 8s linear infinite; }

      @keyframes dashPulse { to { stroke-dashoffset: -280; } }
    </style>
  </defs>

  <rect width="1200" height="310" rx="18" fill="url(#bg)"/>
  <rect width="1200" height="310" rx="18" fill="url(#glow-purple)"/>
  <rect width="1200" height="310" rx="18" fill="url(#grid)"/>

  <!-- Outer Border -->
  <rect x="2" y="2" width="1196" height="306" rx="16" stroke="url(#accent)" stroke-opacity="0.75" stroke-width="2.5" fill="none"/>

  <text x="52" y="58" class="title">Developer Metrics</text>
  <text x="52" y="86" class="sub">Stable repo-hosted summary designed to avoid broken third-party stat widgets while preserving the contribution snake automation.</text>

  <!-- CARD 1 -->
  <g transform="translate(52 118)">
    <rect width="250" height="134" rx="16" class="card"/>
    <text x="24" y="36" class="label">PRIMARY STACK</text>
    <text x="24" y="72" class="body">Embedded C/C++</text>
    <text x="24" y="102" class="muted">ESP32 • RP2040 • STM32 • FreeRTOS</text>
  </g>

  <!-- CARD 2 -->
  <g transform="translate(330 118)">
    <rect width="250" height="134" rx="16" class="card"/>
    <text x="24" y="36" class="label">PRODUCT DEPTH</text>
    <text x="24" y="72" class="body">Hardware to Firmware</text>
    <text x="24" y="102" class="muted">PCB • AFE • BMS • IoT • Test</text>
  </g>

  <!-- CARD 3 -->
  <g transform="translate(608 118)">
    <rect width="250" height="134" rx="16" class="card"/>
    <text x="24" y="36" class="label">AI SIGNAL</text>
    <text x="24" y="72" class="body">Edge ML Pipelines</text>
    <text x="24" y="102" class="muted">Scikit-Learn • PyTorch • CV • TinyML</text>
  </g>

  <!-- CARD 4 -->
  <g transform="translate(886 118)">
    <rect width="250" height="134" rx="16" class="card"/>
    <text x="24" y="36" class="label">OPEN SOURCE</text>
    <text x="24" y="72" class="body">GitHub Actions Ready</text>
    <text x="24" y="102" class="muted">Snake graph • profile assets • docs</text>
  </g>

  <!-- Bottom Animated Circuit Pulse Trace -->
  <path class="bottom-trace" d="M 52 278 H 1148"/>
</svg>
'''

with open('assets/github-metrics.svg', 'w', encoding='utf-8') as f:
    f.write(metrics_svg)

print("github-metrics.svg updated successfully")

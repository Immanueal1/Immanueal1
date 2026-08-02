timeline_svg = '''<svg fill="none" viewBox="0 0 1200 980" width="1200" height="980" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1200" y2="980" gradientUnits="userSpaceOnUse">
      <stop stop-color="#090A12"/>
      <stop offset="0.5" stop-color="#121426"/>
      <stop offset="1" stop-color="#090A12"/>
    </linearGradient>

    <radialGradient id="ambient-purple" cx="20%" cy="30%" r="60%">
      <stop stop-color="#6D28D9" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#090A12" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="accent" x1="0" y1="0" x2="0" y2="980" gradientUnits="userSpaceOnUse">
      <stop stop-color="#8B5CF6"/>
      <stop offset="0.5" stop-color="#22D3EE"/>
      <stop offset="1" stop-color="#EC4899"/>
    </linearGradient>

    <linearGradient id="card-bg" x1="0" y1="0" x2="0" y2="100%">
      <stop stop-color="#171A30" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#121426" stop-opacity="0.95"/>
    </linearGradient>

    <filter id="glow-heavy" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#8B5CF6" stroke-opacity="0.06" stroke-width="1"/>
    </pattern>

    <style>
      .title { font: 800 30px "Inter", -apple-system, sans-serif; fill: #F8FAFC; letter-spacing: -0.5px; }
      .subtitle { font: 500 15px "Inter", -apple-system, sans-serif; fill: #A1A8C5; }
      .role { font: 800 21px "Inter", -apple-system, sans-serif; fill: #F8FAFC; }
      .meta { font: 700 13px "Fira Code", monospace; fill: #22D3EE; letter-spacing: 0.8px; }
      .bullet { font: 600 15px "Inter", -apple-system, sans-serif; fill: #A1A8C5; }

      .card { fill: url(#card-bg); stroke: #8B5CF6; stroke-opacity: 0.35; stroke-width: 1.5; }
      .icon-box { fill: #121426; stroke: #22D3EE; stroke-opacity: 0.4; stroke-width: 1.5; }
      .dot { fill: #EC4899; filter: url(#glow-heavy); animation: dotPulse 3s ease-in-out infinite; }
      .center-line { stroke: url(#accent); stroke-width: 3.5; stroke-linecap: round; stroke-dasharray: 10 14; animation: lineDash 10s linear infinite; }

      @keyframes lineDash { to { stroke-dashoffset: -240; } }
      @keyframes dotPulse { 0%, 100% { opacity: 0.5; transform: scale(1); } 50% { opacity: 1; transform: scale(1.3); } }
    </style>
  </defs>

  <rect width="1200" height="980" rx="20" fill="url(#bg)"/>
  <rect width="1200" height="980" rx="20" fill="url(#ambient-purple)"/>
  <rect width="1200" height="980" rx="20" fill="url(#grid)"/>

  <!-- Outer Glassmorphic Border -->
  <rect x="2" y="2" width="1196" height="976" rx="18" stroke="url(#accent)" stroke-opacity="0.6" stroke-width="2.5" fill="none"/>

  <text x="60" y="62" class="title">Professional Timeline</text>
  <text x="60" y="92" class="subtitle">Teaching, embedded systems, aerospace, power systems, and documentation experience in one scan-friendly view.</text>

  <!-- Central Neon Trace Line -->
  <path class="center-line" d="M 600 132 V 900"/>

  <!-- ENTRY 1: Mentee to Mentor Academy (Left) -->
  <g transform="translate(70 132)">
    <rect class="card" width="470" height="124" rx="16"/>
    <!-- Node on central line -->
    <circle class="dot" cx="530" cy="62" r="8"/>
    <g transform="translate(24 24)">
      <rect class="icon-box" width="60" height="76" rx="12"/>
      <path d="M 18 24 H 42 V 52 H 18 Z M 18 24 L 30 14 L 42 24 M 30 52 V 60" stroke="#22D3EE" stroke-width="2.5" stroke-linecap="round" fill="none"/>
    </g>
    <text x="104" y="38" class="meta">Jul 2025 - Present • Bhilai</text>
    <text x="104" y="67" class="role">Class 11/12 PCM, JEE &amp; NEET Teacher</text>
    <text x="104" y="96" class="bullet">Mentee to Mentor Academy • Study material • Mentoring</text>
  </g>

  <!-- ENTRY 2: BrainStormers' Academy (Right) -->
  <g transform="translate(660 260)">
    <rect class="card" width="470" height="124" rx="16"/>
    <!-- Node on central line -->
    <circle class="dot" cx="-60" cy="62" r="8"/>
    <g transform="translate(24 24)">
      <rect class="icon-box" width="60" height="76" rx="12"/>
      <path d="M 18 22 H 42 M 18 38 H 42 M 18 54 H 32 M 42 24 V 52" stroke="#8B5CF6" stroke-width="2.5" stroke-linecap="round" fill="none"/>
    </g>
    <text x="104" y="38" class="meta">2022 - Present</text>
    <text x="104" y="67" class="role">Teacher</text>
    <text x="104" y="96" class="bullet">BrainStormers' Academy • 9/10 to JEE/NEET • Planning</text>
  </g>

  <!-- ENTRY 3: Vaishnavas Energy (Left) -->
  <g transform="translate(70 388)">
    <rect class="card" width="470" height="124" rx="16"/>
    <!-- Node on central line -->
    <circle class="dot" cx="530" cy="62" r="8"/>
    <g transform="translate(24 24)">
      <rect class="icon-box" width="60" height="76" rx="12"/>
      <path d="M 16 52 H 44 M 20 28 H 40 L 44 52 H 16 Z M 24 28 V 20 H 36 V 28" stroke="#22D3EE" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    </g>
    <text x="104" y="38" class="meta">Mar 2026 - May 2026</text>
    <text x="104" y="67" class="role">Onsite Engineer (Trainee)</text>
    <text x="104" y="96" class="bullet">Vaishnavas Energy • Battery packs • BMS • EV &amp; BESS</text>
  </g>

  <!-- ENTRY 4: India Space Lab (Right) -->
  <g transform="translate(660 516)">
    <rect class="card" width="470" height="124" rx="16"/>
    <!-- Node on central line -->
    <circle class="dot" cx="-60" cy="62" r="8"/>
    <g transform="translate(24 24)">
      <rect class="icon-box" width="60" height="76" rx="12"/>
      <path d="M 30 16 L 46 54 L 30 42 L 14 54 L 30 16 Z M 22 52 L 30 38 L 38 52" stroke="#EC4899" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    </g>
    <text x="104" y="38" class="meta">Feb 2026 - Mar 2026</text>
    <text x="104" y="67" class="role">Aerospace &amp; Drone Systems Trainee</text>
    <text x="104" y="96" class="bullet">India Space Lab • Drone systems • CanSat/CubeSat • GIS</text>
  </g>

  <!-- ENTRY 5: CSPGCL (Left) -->
  <g transform="translate(70 644)">
    <rect class="card" width="470" height="124" rx="16"/>
    <!-- Node on central line -->
    <circle class="dot" cx="530" cy="62" r="8"/>
    <g transform="translate(24 24)">
      <rect class="icon-box" width="60" height="76" rx="12"/>
      <path d="M 16 54 H 44 M 22 54 V 22 H 38 V 54 M 28 30 H 32 M 28 40 H 32" stroke="#22D3EE" stroke-width="2.2" stroke-linecap="round" fill="none"/>
    </g>
    <text x="104" y="38" class="meta">Jun 2025 - Jul 2025</text>
    <text x="104" y="67" class="role">Summer Engineering Intern</text>
    <text x="104" y="96" class="bullet">CSPGCL • SCADA systems • Automation • Power generation</text>
  </g>

  <!-- ENTRY 6: CREDA (Right) -->
  <g transform="translate(660 772)">
    <rect class="card" width="470" height="124" rx="16"/>
    <!-- Node on central line -->
    <circle class="dot" cx="-60" cy="62" r="8"/>
    <g transform="translate(24 24)">
      <rect class="icon-box" width="60" height="76" rx="12"/>
      <path d="M 18 18 H 36 L 42 24 V 58 H 18 Z M 36 18 V 24 H 42 M 24 36 H 36 M 24 46 H 32" stroke="#38BDF8" stroke-width="2.2" stroke-linecap="round" fill="none"/>
    </g>
    <text x="104" y="38" class="meta">Mar 2022 - Apr 2022</text>
    <text x="104" y="67" class="role">Documentation Intern</text>
    <text x="104" y="96" class="bullet">Solar Subsidy Processing • CREDA • Docs • Coordination</text>
  </g>
</svg>
'''

with open('assets/experience-timeline.svg', 'w', encoding='utf-8') as f:
    f.write(timeline_svg)

print("experience-timeline.svg updated successfully")

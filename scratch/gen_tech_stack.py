import os

tech_stack_svg = '''<svg fill="none" viewBox="0 0 1200 1040" width="1200" height="1040" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradients -->
    <linearGradient id="bg" x1="0" y1="0" x2="1200" y2="1040" gradientUnits="userSpaceOnUse">
      <stop stop-color="#090A12"/>
      <stop offset="0.5" stop-color="#121426"/>
      <stop offset="1" stop-color="#090A12"/>
    </linearGradient>

    <radialGradient id="ambient-purple" cx="20%" cy="20%" r="60%">
      <stop stop-color="#6D28D9" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#090A12" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="ambient-cyan" cx="80%" cy="80%" r="60%">
      <stop stop-color="#22D3EE" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#090A12" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="stroke" x1="0" y1="0" x2="1200" y2="1040" gradientUnits="userSpaceOnUse">
      <stop stop-color="#22D3EE" stop-opacity="0.8"/>
      <stop offset="0.5" stop-color="#8B5CF6" stop-opacity="0.8"/>
      <stop offset="1" stop-color="#EC4899" stop-opacity="0.6"/>
    </linearGradient>

    <linearGradient id="card-bg" x1="0" y1="0" x2="0" y2="100%">
      <stop stop-color="#171A30" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#121426" stop-opacity="0.9"/>
    </linearGradient>

    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#8B5CF6" stroke-opacity="0.06" stroke-width="1"/>
    </pattern>

    <style>
      .head { font: 800 28px "Inter", -apple-system, sans-serif; fill: #F8FAFC; letter-spacing: -0.5px; }
      .subhead { font: 500 15px "Inter", -apple-system, sans-serif; fill: #A1A8C5; }
      .cat { font: 800 16px "Inter", -apple-system, sans-serif; fill: #22D3EE; letter-spacing: 0.5px; }
      .name { font: 700 14px "Fira Code", ui-monospace, monospace; fill: #F8FAFC; }
      
      /* Card with border removed for clean borderless floating aesthetic */
      .card { fill: url(#card-bg); stroke: none; }
    </style>
  </defs>

  <!-- Canvas Background -->
  <rect width="1200" height="1040" rx="20" fill="url(#bg)"/>
  <rect width="1200" height="1040" rx="20" fill="url(#ambient-purple)"/>
  <rect width="1200" height="1040" rx="20" fill="url(#ambient-cyan)"/>
  <rect width="1200" height="1040" rx="20" fill="url(#grid)"/>

  <!-- Outer Glassmorphic Border -->
  <rect x="2" y="2" width="1196" height="1036" rx="18" stroke="url(#stroke)" stroke-width="2.5" fill="none"/>

  <!-- Title & Subtitle -->
  <text x="60" y="58" class="head">Technical Skill Matrix</text>
  <text x="60" y="86" class="subhead">Consistent dark-theme SVG cards for firmware, electronics, AI, product design, and development workflows.</text>

  <!-- ========================================================================= -->
  <!-- CATEGORY 1: PROGRAMMING -->
  <!-- ========================================================================= -->
  <g transform="translate(60 120)">
    <text class="cat">Programming</text>
    <g transform="translate(0 20)">
      <!-- C -->
      <g>
        <rect class="card" width="130" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 16 2 L 3 9.5 V 24.5 L 16 32 L 29 24.5 V 9.5 Z" fill="#283593" opacity="0.85"/>
          <path d="M 16 2 L 29 9.5 V 24.5 L 16 32 Z" fill="#3949AB"/>
          <path d="M 21 12.5 C 19.5 11 17.5 10.5 15.5 10.5 C 11.5 10.5 8.5 13.5 8.5 17.5 C 8.5 21.5 11.5 24.5 15.5 24.5 C 18 24.5 20 23.5 21.5 21.5" stroke="#22D3EE" stroke-width="3" stroke-linecap="round" fill="none"/>
        </g>
        <text x="85" y="41" text-anchor="middle" class="name">C</text>
      </g>

      <!-- Embedded C -->
      <g transform="translate(142)">
        <rect class="card" width="130" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 16 2 L 3 9.5 V 24.5 L 16 32 L 29 24.5 V 9.5 Z" fill="#1A237E"/>
          <path d="M 20 12.5 C 18.5 11 16.5 10.5 14.5 10.5 C 11 10.5 8.5 13 8.5 17 C 8.5 21 11 23.5 14.5 23.5 C 17 23.5 19 22.5 20.5 20.5" stroke="#22D3EE" stroke-width="2.5" stroke-linecap="round" fill="none"/>
          <rect x="19" y="19" width="9" height="9" rx="2" fill="#8B5CF6" stroke="#22D3EE" stroke-width="1.2"/>
        </g>
        <text x="85" y="33" text-anchor="middle" class="name">Embedded</text>
        <text x="85" y="50" text-anchor="middle" class="name">C</text>
      </g>

      <!-- C++ -->
      <g transform="translate(284)">
        <rect class="card" width="130" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 16 2 L 3 9.5 V 24.5 L 16 32 L 29 24.5 V 9.5 Z" fill="#004482"/>
          <path d="M 16 2 L 29 9.5 V 24.5 L 16 32 Z" fill="#00599C"/>
          <path d="M 14 12 C 12.5 11 10.5 10.5 9 10.5 C 6 10.5 4 13 4 17 C 4 21 6 23.5 9 23.5 C 11 23.5 12.5 22.5 14 20.5" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" fill="none"/>
          <path d="M 16 17 H 20 M 18 15 V 19 M 22 17 H 26 M 24 15 V 19" stroke="#22D3EE" stroke-width="1.8" stroke-linecap="round"/>
        </g>
        <text x="85" y="41" text-anchor="middle" class="name">C++</text>
      </g>

      <!-- Python -->
      <g transform="translate(426)">
        <rect class="card" width="130" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 15.8 2 C 8.6 2 9 5.1 9 5.1 L 9.1 8.3 H 16 V 9.3 H 6.3 C 2.5 9.3 2 12.8 2 15.8 C 2 19.3 4.6 19.1 4.6 19.1 H 6.2 V 16 C 6.2 12.2 9.4 12 9.4 12 H 15.7 C 19.1 12 19.3 8.7 19.3 8.7 V 5.3 C 19.3 5.3 19.7 2 15.8 2 Z" fill="#3776AB"/>
          <path d="M 16.2 30 C 23.4 30 23 26.9 23 26.9 L 22.9 23.7 H 16 V 22.7 H 25.7 C 29.5 22.7 30 19.2 30 16.2 C 30 12.7 27.4 12.9 27.4 12.9 H 25.8 V 16 C 25.8 19.8 22.6 20 22.6 20 H 16.3 C 12.9 20 12.7 23.3 12.7 23.3 V 26.7 C 12.7 26.7 12.3 30 16.2 30 Z" fill="#FFD43B"/>
          <circle cx="12" cy="5" r="1.2" fill="#FFFFFF"/>
          <circle cx="20" cy="27" r="1.2" fill="#FFFFFF"/>
        </g>
        <text x="85" y="41" text-anchor="middle" class="name">Python</text>
      </g>

      <!-- MATLAB -->
      <g transform="translate(568)">
        <rect class="card" width="130" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 4 24 Q 10 10, 16 16 T 28 8" stroke="#E16737" stroke-width="2.8" fill="none" stroke-linecap="round"/>
          <path d="M 4 24 Q 12 28, 18 20 T 28 22" stroke="#22D3EE" stroke-width="2.2" fill="none"/>
          <path d="M 16 16 Q 18 20, 28 22" stroke="#E16737" stroke-width="2" fill="none"/>
        </g>
        <text x="85" y="41" text-anchor="middle" class="name">MATLAB</text>
      </g>

      <!-- Git -->
      <g transform="translate(710)">
        <rect class="card" width="130" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 30.2 14.5 L 17.5 1.8 C 16.5 0.8 14.9 0.8 13.9 1.8 L 1.8 13.9 C 0.8 14.9 0.8 16.5 1.8 17.5 L 14.5 30.2 C 15.5 31.2 17.1 31.2 18.1 30.2 L 30.2 18.1 C 31.2 17.1 31.2 15.5 30.2 14.5 Z" fill="#F05032"/>
          <path d="M 19.5 13.7 C 18.6 13.3 17.5 13.6 16.9 14.4 L 14.3 11.8 C 14.7 10.9 14.5 9.7 13.6 9 C 12.5 8.1 10.9 8.3 10 9.4 C 9.1 10.5 9.3 12.1 10.4 13 C 11.2 13.6 12.2 13.7 13 13.3 L 15.6 15.9 C 15.5 16.2 15.5 16.6 15.5 17 C 15.5 18 16.1 18.9 17 19.3 L 17 23.6 C 16.4 23.9 16 24.5 16 25.2 C 16 26.3 16.9 27.2 18 27.2 C 19.1 27.2 20 26.3 20 25.2 C 20 24.5 19.6 23.9 19 23.6 L 19 19.2 C 19.9 18.8 20.5 17.9 20.4 16.8 C 20.4 15.5 19.9 14.3 19.5 13.7 Z" fill="#FFFFFF"/>
        </g>
        <text x="85" y="41" text-anchor="middle" class="name">Git</text>
      </g>

      <!-- GitHub -->
      <g transform="translate(852)">
        <rect class="card" width="130" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M 16 0 C 7.16 0 0 7.16 0 16 C 0 23.08 4.58 29.06 10.94 31.18 C 11.74 31.32 12.04 30.84 12.04 30.42 C 12.04 30.04 12.02 28.78 12.02 27.44 C 7.58 28.4 6.64 25.54 6.64 25.54 C 5.92 23.7 4.88 23.2 4.88 23.2 C 3.42 22.2 4.98 22.22 4.98 22.22 C 6.6 22.34 7.46 23.88 7.46 23.88 C 8.88 26.32 11.2 25.62 12.1 25.22 C 12.24 24.18 12.66 23.48 13.12 23.08 C 9.58 22.68 5.86 21.32 5.86 15.22 C 5.86 13.48 6.48 12.06 7.5 10.94 C 7.34 10.54 6.78 8.92 7.66 6.72 C 7.66 6.72 9 6.3 12.04 8.36 C 13.32 8 14.68 7.82 16.04 7.82 C 17.4 7.82 18.76 8 20.04 8.36 C 23.08 6.3 24.42 6.72 24.42 6.72 C 25.3 8.92 24.74 10.54 24.58 10.94 C 25.6 12.06 26.22 13.48 26.22 15.22 C 26.22 21.34 22.48 22.68 18.92 23.08 C 19.5 23.58 20.02 24.56 20.02 26.06 C 20.02 28.22 20 29.96 20 30.42 C 20 30.84 20.3 31.34 21.1 31.18 C 27.46 29.06 32 23.08 32 16 C 32 7.16 24.84 0 16 0 Z" fill="#F8FAFC"/>
        </g>
        <text x="85" y="41" text-anchor="middle" class="name">GitHub</text>
      </g>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- CATEGORY 2: EMBEDDED SYSTEMS -->
  <!-- ========================================================================= -->
  <g transform="translate(60 235)">
    <text class="cat">Embedded Systems</text>
    <g transform="translate(0 20)">
      <!-- ESP32 -->
      <g>
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 16 2 L 30 10 V 22 L 16 30 L 2 22 V 10 Z" fill="#E7352C"/>
          <path d="M 16 7 L 25 12 V 20 L 16 25 L 7 20 V 12 Z" fill="#121426"/>
          <circle cx="16" cy="16" r="4.5" fill="#22D3EE"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">ESP32</text>
      </g>

      <!-- Arduino -->
      <g transform="translate(162)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 10 16 C 6 10, 2 12, 2 16 C 2 20, 6 22, 10 16 C 14 10, 18 12, 22 16 C 26 20, 30 18, 30 16 C 30 12, 26 10, 22 16 C 18 22, 14 20, 10 16 Z" stroke="#00979D" stroke-width="3.8" fill="none" stroke-linecap="round"/>
          <path d="M 5 16 H 9 M 21 16 H 27 M 24 13 V 19" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">Arduino</text>
      </g>

      <!-- RP Pico -->
      <g transform="translate(324)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 16 6 Q 12 0, 8 4 Q 4 10, 10 14 Z" fill="#008080"/>
          <path d="M 16 6 Q 20 0, 24 4 Q 28 10, 22 14 Z" fill="#008080"/>
          <circle cx="11" cy="18" r="4.5" fill="#C51A4A"/>
          <circle cx="21" cy="18" r="4.5" fill="#C51A4A"/>
          <circle cx="16" cy="22" r="5" fill="#C51A4A"/>
          <circle cx="11" cy="26" r="4" fill="#C51A4A"/>
          <circle cx="21" cy="26" r="4" fill="#C51A4A"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">RP Pico</text>
      </g>

      <!-- STM32 -->
      <g transform="translate(486)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 4 8 H 28 L 20 16 H 4 Z" fill="#00A3E0"/>
          <path d="M 12 16 H 28 L 20 24 H 4 Z" fill="#03234C" stroke="#00A3E0" stroke-width="1.2"/>
          <circle cx="24" cy="20" r="3.2" fill="#22D3EE"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">STM32</text>
      </g>

      <!-- FreeRTOS -->
      <g transform="translate(648)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <rect x="4" y="5" width="24" height="6" rx="2" fill="#22D3EE"/>
          <rect x="4" y="13" width="24" height="6" rx="2" fill="#8B5CF6"/>
          <rect x="4" y="21" width="24" height="6" rx="2" fill="#EC4899"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">FreeRTOS</text>
      </g>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- CATEGORY 3: PROTOCOLS & HARDWARE BUSSES -->
  <!-- ========================================================================= -->
  <g transform="translate(60 350)">
    <text class="cat">Protocols &amp; Hardware Busses</text>
    <g transform="translate(0 20)">
      <!-- UART -->
      <g>
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 2 10 H 8 V 22 H 16 V 10 H 24 V 22 H 30" stroke="#22D3EE" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
          <path d="M 6 6 L 10 2 L 14 6 M 26 26 L 22 30 L 18 26" stroke="#8B5CF6" stroke-width="2.2" stroke-linecap="round" fill="none"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">UART</text>
      </g>

      <!-- SPI -->
      <g transform="translate(162)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <line x1="2" y1="8" x2="30" y2="8" stroke="#22D3EE" stroke-width="2.2"/>
          <line x1="2" y1="14" x2="30" y2="14" stroke="#8B5CF6" stroke-width="2.2"/>
          <line x1="2" y1="20" x2="30" y2="20" stroke="#EC4899" stroke-width="2.2"/>
          <line x1="2" y1="26" x2="30" y2="26" stroke="#38BDF8" stroke-width="2.2"/>
          <circle cx="10" cy="8" r="2.2" fill="#FFFFFF"/>
          <circle cx="20" cy="14" r="2.2" fill="#FFFFFF"/>
          <circle cx="15" cy="20" r="2.2" fill="#FFFFFF"/>
          <circle cx="25" cy="26" r="2.2" fill="#FFFFFF"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">SPI</text>
      </g>

      <!-- I²C -->
      <g transform="translate(324)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 2 10 H 12 V 22 H 30" stroke="#22D3EE" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
          <path d="M 2 22 H 18 V 10 H 30" stroke="#EC4899" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
          <circle cx="12" cy="10" r="2.8" fill="#22D3EE"/>
          <circle cx="18" cy="10" r="2.8" fill="#EC4899"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">I²C</text>
      </g>

      <!-- CAN Bus -->
      <g transform="translate(486)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 2 12 Q 8 4, 16 16 T 30 12" stroke="#22D3EE" stroke-width="2.5" fill="none"/>
          <path d="M 2 20 Q 8 28, 16 16 T 30 20" stroke="#8B5CF6" stroke-width="2.5" fill="none"/>
          <line x1="16" y1="4" x2="16" y2="28" stroke="#EC4899" stroke-width="1.8" stroke-dasharray="2 2"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">CAN Bus</text>
      </g>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- CATEGORY 4: AI, MACHINE LEARNING & COMPUTER VISION -->
  <!-- ========================================================================= -->
  <g transform="translate(60 465)">
    <text class="cat">AI, Machine Learning &amp; Computer Vision</text>
    <g transform="translate(0 20)">
      <!-- Scikit-Learn -->
      <g>
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <circle cx="12" cy="16" r="10" fill="#3499CD" opacity="0.85"/>
          <circle cx="20" cy="16" r="10" fill="#F7931E" opacity="0.85"/>
          <path d="M 16 8 A 10 10 0 0 1 16 24 A 10 10 0 0 1 16 8 Z" fill="#121426"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">Scikit-Learn</text>
      </g>

      <!-- TensorFlow -->
      <g transform="translate(162)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 16 2 L 28 9 V 23 L 22 26 V 13 L 16 9 L 10 13 V 26 L 4 23 V 9 Z" fill="#FF6F00"/>
          <path d="M 16 9 L 22 13 V 26 L 16 22 L 10 26 V 13 Z" fill="#FFA000"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">TensorFlow</text>
      </g>

      <!-- PyTorch -->
      <g transform="translate(324)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 18 4 C 18 4, 24 10, 24 16 C 24 22, 19 27, 13 27 C 7 27, 4 22, 4 16 C 4 11, 8 7, 12 5" stroke="#EE4C2C" stroke-width="3.2" fill="none" stroke-linecap="round"/>
          <circle cx="21" cy="9" r="2.8" fill="#EE4C2C"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">PyTorch</text>
      </g>

      <!-- OpenCV -->
      <g transform="translate(486)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <circle cx="16" cy="9" r="6" stroke="#FF2A2A" stroke-width="2.8" fill="none"/>
          <circle cx="9" cy="21" r="6" stroke="#00D26A" stroke-width="2.8" fill="none"/>
          <circle cx="23" cy="21" r="6" stroke="#22D3EE" stroke-width="2.8" fill="none"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">OpenCV</text>
      </g>

      <!-- Pandas -->
      <g transform="translate(648)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <rect x="6" y="4" width="4.5" height="24" rx="2" fill="#150458"/>
          <rect x="14" y="10" width="4.5" height="18" rx="2" fill="#E70488"/>
          <rect x="22" y="16" width="4.5" height="12" rx="2" fill="#150458"/>
          <circle cx="8" cy="6" r="1.8" fill="#22D3EE"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">Pandas</text>
      </g>

      <!-- NumPy -->
      <g transform="translate(810)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 4 16 L 16 4 L 28 16 L 16 28 Z" fill="#013243" stroke="#4DABCF" stroke-width="2.2"/>
          <line x1="4" y1="16" x2="28" y2="16" stroke="#4DABCF" stroke-width="1.8"/>
          <line x1="16" y1="4" x2="16" y2="28" stroke="#4DABCF" stroke-width="1.8"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">NumPy</text>
      </g>

      <!-- Matplotlib -->
      <g transform="translate(972)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 4 24 Q 10 6, 16 16 T 28 8" stroke="#11557C" stroke-width="3.2" fill="none"/>
          <path d="M 4 20 Q 12 28, 20 12 T 28 22" stroke="#22D3EE" stroke-width="2.2" fill="none"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">Matplotlib</text>
      </g>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- CATEGORY 5: PCB DESIGN & HARDWARE TEST EQUIPMENT -->
  <!-- ========================================================================= -->
  <g transform="translate(60 580)">
    <text class="cat">PCB Design &amp; Hardware Test Equipment</text>
    <g transform="translate(0 20)">
      <!-- KiCad -->
      <g>
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 6 4 V 28 M 6 16 L 22 4 M 6 16 L 22 28" stroke="#336699" stroke-width="4.2" stroke-linecap="round"/>
          <circle cx="22" cy="16" r="3.8" fill="#FFCC00"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">KiCad</text>
      </g>

      <!-- Proteus -->
      <g transform="translate(162)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <rect x="5" y="5" width="22" height="22" rx="4" fill="#00AEEF" fill-opacity="0.25" stroke="#00AEEF" stroke-width="2.2"/>
          <path d="M 9 16 H 23 M 16 9 V 23" stroke="#22D3EE" stroke-width="2.5" stroke-linecap="round"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">Proteus</text>
      </g>

      <!-- Oscilloscope -->
      <g transform="translate(324)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <rect x="3" y="5" width="26" height="22" rx="5" fill="#121426" stroke="#22D3EE" stroke-width="2"/>
          <path d="M 5 16 Q 10 7, 16 16 T 27 16" stroke="#22D3EE" stroke-width="2.2" fill="none"/>
          <line x1="3" y1="16" x2="29" y2="16" stroke="#8B5CF6" stroke-opacity="0.35" stroke-width="1.2"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">Oscilloscope</text>
      </g>

      <!-- Logic Analyzer -->
      <g transform="translate(486)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 2 8 H 8 V 16 H 16 V 8 H 22 V 16 H 30" stroke="#EC4899" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
          <path d="M 2 24 H 12 V 18 H 20 V 24 H 30" stroke="#22D3EE" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        </g>
        <text x="96" y="33" text-anchor="middle" class="name">Logic</text>
        <text x="96" y="50" text-anchor="middle" class="name">Analyzer</text>
      </g>

      <!-- Power Electronics -->
      <g transform="translate(648)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <polygon points="16,2 30,26 2,26" fill="none" stroke="#8B5CF6" stroke-width="2.2"/>
          <path d="M 16 9 L 12 17 H 20 L 16 25" stroke="#22D3EE" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        </g>
        <text x="96" y="33" text-anchor="middle" class="name">Power</text>
        <text x="96" y="50" text-anchor="middle" class="name">Electronics</text>
      </g>

      <!-- BMS -->
      <g transform="translate(810)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <rect x="5" y="7" width="22" height="20" rx="3" stroke="#22D3EE" stroke-width="2.2" fill="none"/>
          <rect x="11" y="3" width="10" height="4" rx="1" fill="#22D3EE"/>
          <path d="M 11 17 H 21 M 16 12 V 22" stroke="#EC4899" stroke-width="2.2" stroke-linecap="round"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">BMS</text>
      </g>

      <!-- Circuit Design -->
      <g transform="translate(972)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <circle cx="16" cy="16" r="13" stroke="#38BDF8" stroke-width="2.2" fill="none"/>
          <path d="M 7 16 H 25 M 16 7 V 25" stroke="#8B5CF6" stroke-width="2.2"/>
          <circle cx="16" cy="16" r="3.5" fill="#EC4899"/>
        </g>
        <text x="96" y="33" text-anchor="middle" class="name">Circuit</text>
        <text x="96" y="50" text-anchor="middle" class="name">Design</text>
      </g>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- CATEGORY 6: CREATIVE SOFTWARE -->
  <!-- ========================================================================= -->
  <g transform="translate(60 695)">
    <text class="cat">Creative Software</text>
    <g transform="translate(0 20)">
      <!-- Photoshop -->
      <g>
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <rect width="32" height="32" rx="7" fill="#001E36" stroke="#31A8FF" stroke-width="1.8"/>
          <text x="16" y="22" text-anchor="middle" font-family="sans-serif" font-weight="900" font-size="15" fill="#31A8FF">Ps</text>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">Photoshop</text>
      </g>

      <!-- Illustrator -->
      <g transform="translate(162)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <rect width="32" height="32" rx="7" fill="#330000" stroke="#FF9A00" stroke-width="1.8"/>
          <text x="16" y="22" text-anchor="middle" font-family="sans-serif" font-weight="900" font-size="15" fill="#FF9A00">Ai</text>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">Illustrator</text>
      </g>

      <!-- Premiere Pro -->
      <g transform="translate(324)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <rect width="32" height="32" rx="7" fill="#00005B" stroke="#9999FF" stroke-width="1.8"/>
          <text x="16" y="22" text-anchor="middle" font-family="sans-serif" font-weight="900" font-size="15" fill="#9999FF">Pr</text>
        </g>
        <text x="96" y="33" text-anchor="middle" class="name">Premiere</text>
        <text x="96" y="50" text-anchor="middle" class="name">Pro</text>
      </g>

      <!-- Lightroom -->
      <g transform="translate(486)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <rect width="32" height="32" rx="7" fill="#001E36" stroke="#31A8FF" stroke-width="1.8"/>
          <text x="16" y="22" text-anchor="middle" font-family="sans-serif" font-weight="900" font-size="15" fill="#31A8FF">Lr</text>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">Lightroom</text>
      </g>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- CATEGORY 7: DEVELOPMENT & IDE TOOLS -->
  <!-- ========================================================================= -->
  <g transform="translate(60 810)">
    <text class="cat">Development &amp; IDE Tools</text>
    <g transform="translate(0 20)">
      <!-- VS Code -->
      <g>
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 23 2 L 30 6 V 26 L 23 30 L 10 20 L 4 24 L 1 21 L 6 16 L 1 11 L 4 8 L 10 12 Z" fill="#007ACC"/>
          <path d="M 23 2 L 10 12 L 4 8 L 1 11 L 6 16 L 23 30 Z" fill="#0066B8" opacity="0.75"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">VS Code</text>
      </g>

      <!-- Arduino IDE -->
      <g transform="translate(162)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 10 16 C 6 10, 2 12, 2 16 C 2 20, 6 22, 10 16 C 14 10, 18 12, 22 16 C 26 20, 30 18, 30 16 C 30 12, 26 10, 22 16 C 18 22, 14 20, 10 16 Z" stroke="#00979D" stroke-width="3.8" fill="none"/>
          <path d="M 5 16 H 9 M 21 16 H 27 M 24 13 V 19" stroke="#FFFFFF" stroke-width="2"/>
        </g>
        <text x="96" y="33" text-anchor="middle" class="name">Arduino</text>
        <text x="96" y="50" text-anchor="middle" class="name">IDE</text>
      </g>

      <!-- PlatformIO -->
      <g transform="translate(324)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <path d="M 16 2 L 30 12 L 24 30 H 8 L 2 12 Z" fill="#F58220"/>
          <circle cx="16" cy="16" r="5" fill="#121426"/>
        </g>
        <text x="96" y="41" text-anchor="middle" class="name">PlatformIO</text>
      </g>

      <!-- GitHub Actions -->
      <g transform="translate(486)">
        <rect class="card" width="150" height="70" rx="14"/>
        <g transform="translate(10 10) scale(1.55)">
          <circle cx="8" cy="16" r="4.5" fill="#2088FF"/>
          <circle cx="24" cy="8" r="4.5" fill="#2088FF"/>
          <circle cx="24" cy="24" r="4.5" fill="#2088FF"/>
          <path d="M 12 14 L 20 10 M 12 18 L 20 22" stroke="#2088FF" stroke-width="2.2"/>
        </g>
        <text x="96" y="33" text-anchor="middle" class="name">GitHub</text>
        <text x="96" y="50" text-anchor="middle" class="name">Actions</text>
      </g>
    </g>
  </g>
</svg>
'''

with open('assets/tech-stack.svg', 'w', encoding='utf-8') as f:
    f.write(tech_stack_svg)

print("assets/tech-stack.svg generated with large 1.55x icons and no disc/card borders!")

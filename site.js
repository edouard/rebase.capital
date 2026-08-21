// Shared theme and component styles for every page.
// Loaded after the Tailwind Play CDN, which reads `tailwind.config` and picks up
// any `type="text/tailwindcss"` style it finds in the document.

tailwind.config = {
  theme: {
    extend: {
      colors: {
        ink:    '#101B2D',
        paper:  '#FBFAF8',
        slate:  '#5D6B80',
        rule:   '#E4E2DC',
        signal: '#C58A2A',
        'ink-dark':    '#0B1523',
        'paper-dark':  '#ECEAE5',
        'slate-dark':  '#8B99AE',
        'rule-dark':   '#1F2C40',
        'signal-dark': '#DFA742',
      },
      fontFamily: {
        display: ['"Bricolage Grotesque"', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        body:    ['"Source Serif 4"', 'Georgia', 'serif'],
        mono:    ['"JetBrains Mono"', 'ui-monospace', 'SFMono-Regular', 'monospace'],
      },
    }
  }
}

const styles = document.createElement('style')
styles.type = 'text/tailwindcss'
styles.textContent = `
  @layer base {
    html { -webkit-text-size-adjust: 100%; }
    body { text-rendering: optimizeLegibility; }
    ::selection { @apply bg-signal/25; }
    :focus-visible { @apply outline outline-2 outline-offset-4 outline-signal rounded-sm; }
  }

  @layer components {
    /* Display type: slightly condensed, tightly set. */
    .display {
      font-variation-settings: "wdth" 92, "wght" 800, "opsz" 96;
      letter-spacing: -0.035em;
    }
    .display-sm {
      font-variation-settings: "wdth" 96, "wght" 600, "opsz" 24;
      letter-spacing: -0.02em;
    }

    .wordmark {
      @apply font-mono text-[0.8125rem] font-medium tracking-tight transition-colors;
      @apply hover:text-signal dark:hover:text-signal-dark;
    }
    .nav-link {
      @apply font-mono text-[0.8125rem] text-slate transition-colors hover:text-signal;
      @apply dark:text-slate-dark dark:hover:text-signal-dark;
    }
    .nav-link-current { @apply text-ink dark:text-paper-dark; }

    .link {
      @apply text-ink underline decoration-signal decoration-2 underline-offset-[5px];
      @apply transition-colors hover:text-signal dark:text-paper-dark dark:decoration-signal-dark dark:hover:text-signal-dark;
    }
    .eyebrow {
      @apply font-mono text-xs font-medium uppercase tracking-[0.18em] text-slate dark:text-slate-dark;
    }

    /* Home: a line from the first product to the latest, one node each. */
    .entry:not(:last-child)::before {
      content: "";
      position: absolute;
      top: 1.375rem;
      bottom: -0.5rem;
      left: 0.3125rem;
      width: 1px;
      @apply bg-rule dark:bg-rule-dark;
    }
    .node {
      @apply relative z-10 block h-[0.6875rem] w-[0.6875rem] rounded-full bg-ink;
      @apply transition-colors duration-200 dark:bg-paper-dark;
    }
    .entry:hover .node { @apply bg-signal dark:bg-signal-dark; }
    .shot {
      @apply aspect-[5/4] w-full rounded-md border border-rule object-cover object-top;
      @apply transition duration-300 ease-out dark:border-rule-dark;
    }
    .entry:hover .shot { @apply -translate-y-1 border-signal/50 dark:border-signal-dark/50 shadow-lg shadow-ink/5; }

    /* A label and a destination, ruled like a ledger. */
    .row {
      @apply flex flex-wrap items-baseline justify-between gap-x-6 gap-y-1 border-b py-4 font-mono text-sm;
      @apply border-rule transition-colors hover:border-signal dark:border-rule-dark dark:hover:border-signal-dark;
    }
    .row-label { @apply text-xs uppercase tracking-[0.14em] text-slate dark:text-slate-dark; }
    .row-value { @apply transition-colors group-hover:text-signal dark:group-hover:text-signal-dark; }

    /* Blog index: one ruled row per post. */
    .post-row {
      @apply block border-b border-rule py-6 transition-colors dark:border-rule-dark;
      @apply hover:border-signal dark:hover:border-signal-dark;
    }
    .post-row-date { @apply font-mono text-xs uppercase tracking-[0.14em] text-slate dark:text-slate-dark; }
    .post-row-title {
      @apply mt-2 block font-display text-xl leading-snug transition-colors sm:text-2xl;
      @apply group-hover:text-signal dark:group-hover:text-signal-dark;
      font-variation-settings: "wdth" 96, "wght" 600, "opsz" 24;
      letter-spacing: -0.02em;
    }

    /* Long-form article body. */
    .prose { @apply text-[1.0625rem] leading-[1.75] text-ink/90 dark:text-paper-dark/85; }
    .prose > p { @apply mt-6; }
    .prose > p:first-child { @apply mt-0; }
    .prose h2 {
      @apply mt-14 mb-1 font-display text-[1.5rem] text-ink dark:text-paper-dark sm:text-[1.75rem];
      font-variation-settings: "wdth" 96, "wght" 600, "opsz" 24;
      letter-spacing: -0.02em;
    }
    .prose h3 {
      @apply mt-10 mb-1 font-display text-[1.1875rem] text-ink dark:text-paper-dark;
      font-variation-settings: "wdth" 96, "wght" 600, "opsz" 18;
      letter-spacing: -0.015em;
    }
    .prose a {
      @apply text-ink underline decoration-signal decoration-2 underline-offset-[5px];
      @apply transition-colors hover:text-signal dark:text-paper-dark dark:decoration-signal-dark dark:hover:text-signal-dark;
    }
    .prose ul { @apply mt-6 space-y-3 pl-0; }
    .prose li { @apply relative pl-6; }
    .prose li::before {
      content: "";
      @apply absolute left-0 top-[0.6875rem] h-[0.3125rem] w-[0.3125rem] rounded-full bg-signal dark:bg-signal-dark;
    }
    .prose pre {
      @apply mt-6 overflow-x-auto rounded-md border-l-2 border-signal bg-ink/[0.04] py-4 pl-5 pr-4;
      @apply font-mono text-[0.8125rem] leading-relaxed text-ink dark:bg-paper-dark/[0.06] dark:text-paper-dark;
    }
    .prose strong { @apply font-semibold text-ink dark:text-paper-dark; }
  }

  @layer utilities {
    .rise { animation: rise 0.7s cubic-bezier(0.22, 1, 0.36, 1) both; }
    @keyframes rise {
      from { opacity: 0; transform: translateY(0.75rem); }
      to   { opacity: 1; transform: none; }
    }
    @media (prefers-reduced-motion: reduce) {
      .rise { animation: none; }
      * { transition-duration: 0.01ms !important; }
    }
  }
`
document.head.appendChild(styles)

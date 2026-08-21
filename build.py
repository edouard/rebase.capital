#!/usr/bin/env python3
"""Writes the site's pages from one shared shell.

There is no build step in production: this script just keeps the four static
files consistent when the header, footer or <head> changes. Run it, commit the
HTML it writes, and GitHub Pages serves the files as they are.
"""

import io
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

FAVICON = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'"
    "%3E%3Crect width='32' height='32' rx='7' fill='%23101B2D'/%3E%3Ccircle cx='16' cy='16'"
    " r='6' fill='none' stroke='%23C58A2A' stroke-width='3'/%3E%3C/svg%3E"
)

FONTS = (
    "https://fonts.googleapis.com/css2?"
    "family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,400..800"
    "&family=JetBrains+Mono:wght@400;500"
    "&family=Source+Serif+4:opsz,wght@8..60,400..600&display=swap"
)


def head(title, description, url, og_type="website"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://rebase.capital{url}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:url" content="https://rebase.capital{url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <link rel="icon" href="{FAVICON}">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONTS}" rel="stylesheet">

  <script src="https://cdn.tailwindcss.com"></script>
  <script src="/site.js"></script>
</head>

<body class="bg-paper text-ink dark:bg-ink-dark dark:text-paper-dark font-body antialiased">
  <div class="mx-auto w-full max-w-4xl px-6 sm:px-10">
"""


def header(current=None):
    def nav(label, href):
        klass = "nav-link nav-link-current" if current == label else "nav-link"
        return f'<a href="{href}" class="{klass}">{label}</a>'

    return f"""
    <header class="rise flex items-baseline justify-between gap-4 border-b border-rule dark:border-rule-dark py-6">
      <a href="/" class="wordmark">
        <span class="mr-2 inline-block h-2 w-2 -translate-y-px rounded-full bg-signal dark:bg-signal-dark align-middle"></span>Rebase&nbsp;Capital
      </a>
      <nav class="flex items-baseline gap-6">
        {nav("Blog", "/blog/")}
        {nav("About", "/about/")}
      </nav>
    </header>
"""


FOOTER = """
    <footer class="border-t border-rule dark:border-rule-dark py-8 font-mono text-[0.8125rem] leading-relaxed text-slate dark:text-slate-dark">
      <div class="flex flex-col gap-1 sm:flex-row sm:items-baseline sm:justify-between">
        <p>Rebase Capital SL &middot; ESB56536873</p>
        <p>Calle Sauces 2, 29018 M&aacute;laga, Spain</p>
      </div>
    </footer>

  </div>
</body>
</html>
"""


def write(path, title, description, url, main, current=None, og_type="website"):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    io.open(full, "w", encoding="utf-8").write(
        head(title, description, url, og_type) + header(current) + main + FOOTER
    )
    print("wrote", path)


# --------------------------------------------------------------------------
# Home
# --------------------------------------------------------------------------

def product(year, name, href, blurb, meta, image, alt, last=False):
    pad = "" if last else " pb-14 sm:pb-20"
    return f"""
          <li class="entry relative grid grid-cols-[3.5rem_1fr] gap-y-4 sm:grid-cols-[5rem_1fr]{pad}">
            <div class="pt-[0.4375rem]">
              <span class="node"></span>
              <p class="mt-3 font-mono text-[0.8125rem] font-medium">{year}</p>
            </div>
            <div class="grid gap-6 sm:grid-cols-[1fr_17rem] sm:items-start sm:gap-8">
              <div>
                <h3 class="display-sm font-display text-2xl sm:text-[1.75rem]">
                  <a href="{href}" class="transition-colors hover:text-signal dark:hover:text-signal-dark" target="_blank" rel="noopener">{name}</a>
                </h3>
                <p class="mt-3 max-w-[30rem] leading-relaxed text-slate dark:text-slate-dark">
                  {blurb}
                </p>
                <p class="mt-4 font-mono text-xs text-slate dark:text-slate-dark">
                  {meta}
                </p>
              </div>
              <img src="/images/{image}" alt="{alt}" loading="lazy" decoding="async" class="shot">
            </div>
          </li>"""


HOME_MAIN = f"""
    <main>
      <section class="pt-16 pb-14 sm:pt-28 sm:pb-24">
        <h1 class="rise display font-display text-[clamp(2.75rem,11vw,6rem)] leading-[0.92]" style="animation-delay:0.06s">
          We build and run<br>SaaS<span class="text-signal dark:text-signal-dark">.</span>
        </h1>

        <div class="rise mt-10 max-w-[34rem] space-y-5 text-lg leading-relaxed text-slate dark:text-slate-dark sm:mt-14" style="animation-delay:0.14s">
          <p>
            Rebase Capital is the holding company for the B2B software we write. We build the products, run the
            servers and answer the support email. Nothing is flipped, and nothing is left to rot.
          </p>
          <p>Owned and operated by <a href="/about/" class="link">Edouard Bri&egrave;re</a>.</p>
        </div>
      </section>

      <section class="border-t border-rule dark:border-rule-dark pt-10 pb-16 sm:pt-14 sm:pb-24">
        <h2 class="eyebrow">What we run</h2>

        <ol class="relative mt-10 sm:mt-14">{product(
            "2008", "WebTranslateIt", "https://webtranslateit.com",
            "Translation management for software teams. Eighteen years old and still shipping.",
            "First commit 4 Oct 2008 &middot; Ruby on Rails &middot; PostgreSQL",
            "webtranslateit.webp", "The WebTranslateIt translation editor")}
{product(
            "2026", "TrackBerry", "https://trackberry.com",
            "Transport management for fresh produce traders. Every shipment, from grower to buyer.",
            "First commit 9 Jan 2026 &middot; Ruby on Rails &middot; PostgreSQL",
            "trackberry.png", "The TrackBerry shipment dashboard", last=True)}
        </ol>
      </section>
    </main>
"""

# --------------------------------------------------------------------------
# About
# --------------------------------------------------------------------------

ABOUT_MAIN = """
    <main>
      <section class="pt-14 pb-14 sm:pt-20 sm:pb-20">
        <p class="rise eyebrow">Owner and operator</p>
        <h1 class="rise display font-display mt-6 text-[clamp(2.5rem,9vw,4.75rem)] leading-[0.94]" style="animation-delay:0.06s">
          Edouard Bri&egrave;re
        </h1>

        <div class="rise mt-12 grid gap-10 sm:mt-16 sm:grid-cols-[13rem_1fr] sm:gap-12" style="animation-delay:0.12s">
          <img src="/images/edouard.jpg" alt="Edouard Bri&egrave;re" width="720" height="719"
               class="w-40 rounded-lg border border-rule dark:border-rule-dark sm:w-full">

          <div class="max-w-[34rem] space-y-5 text-lg leading-relaxed text-slate dark:text-slate-dark">
            <p>
              Edouard founded Rebase Capital and writes the software it runs. He built
              <a href="https://webtranslateit.com" class="link" target="_blank" rel="noopener">WebTranslateIt</a>
              in 2008, a translation management platform for software teams, and
              <a href="https://trackberry.com" class="link" target="_blank" rel="noopener">TrackBerry</a>
              in 2026, a transport management system for fresh produce traders.
            </p>
            <p>
              Before that he was a web developer at Last.fm, where he built the internationalization
              system behind the site.
            </p>
            <p>
              He works in Ruby on Rails and PostgreSQL, still answers his own support email, and lives
              in M&aacute;laga, Spain.
            </p>
          </div>
        </div>
      </section>

      <section class="border-t border-rule dark:border-rule-dark pt-10 pb-16 sm:pt-14 sm:pb-24">
        <h2 class="eyebrow">Elsewhere</h2>
        <div class="mt-6 sm:mt-8">
          <a class="row group" href="https://www.linkedin.com/in/edouard-bri%C3%A8re-150247150/" target="_blank" rel="noopener">
            <span class="row-label">LinkedIn</span>
            <span class="row-value">linkedin.com/in/edouard-bri&egrave;re</span>
          </a>
          <a class="row group" href="https://webtranslateit.com" target="_blank" rel="noopener">
            <span class="row-label">WebTranslateIt</span>
            <span class="row-value">webtranslateit.com</span>
          </a>
          <a class="row group" href="https://trackberry.com" target="_blank" rel="noopener">
            <span class="row-label">TrackBerry</span>
            <span class="row-value">trackberry.com</span>
          </a>
        </div>
      </section>
    </main>
"""

# --------------------------------------------------------------------------
# Blog
# --------------------------------------------------------------------------

POSTS = [
    {
        "slug": "upgrading-webtranslateit-from-rails-3-2-to-rails-7",
        "title": "Upgrading WebTranslateIt from Rails 3.2 to Rails 7",
        "date": "2022-10-16",
        "date_label": "16 October 2022",
        "summary": "How a team of two took a large Rails app from Rails 3.2 and Ruby 2.7 to Rails 7 and Ruby 3.1 in four months.",
    },
]


def blog_index_main():
    rows = "".join(
        f"""
          <a class="post-row group" href="/blog/{p['slug']}/">
            <time class="post-row-date" datetime="{p['date']}">{p['date_label']}</time>
            <span class="post-row-title">{p['title']}</span>
            <span class="mt-3 block max-w-[34rem] leading-relaxed text-slate dark:text-slate-dark">{p['summary']}</span>
          </a>"""
        for p in POSTS
    )
    return f"""
    <main>
      <section class="pt-14 pb-16 sm:pt-20 sm:pb-24">
        <p class="rise eyebrow">Writing</p>
        <h1 class="rise display font-display mt-6 text-[clamp(2.5rem,9vw,4.75rem)] leading-[0.94]" style="animation-delay:0.06s">
          Notes from the<br>build<span class="text-signal dark:text-signal-dark">.</span>
        </h1>
        <p class="rise mt-10 max-w-[34rem] text-lg leading-relaxed text-slate dark:text-slate-dark" style="animation-delay:0.12s">
          Occasional write-ups of the work behind our products: upgrades, migrations and the
          things that only show up once software has been running for a decade.
        </p>

        <div class="rise mt-14 sm:mt-20" style="animation-delay:0.18s">{rows}
        </div>
      </section>
    </main>
"""


def post_main(post, body):
    return f"""
    <main>
      <article class="pt-14 pb-16 sm:pt-20 sm:pb-24">
        <header>
          <p class="rise eyebrow">
            <time datetime="{post['date']}">{post['date_label']}</time>
          </p>
          <h1 class="rise display font-display mt-6 max-w-[20ch] text-[clamp(2.125rem,6.5vw,3.75rem)] leading-[0.98]" style="animation-delay:0.06s">
            {post['title']}
          </h1>
          <p class="rise mt-8 max-w-[38rem] text-xl leading-relaxed text-slate dark:text-slate-dark" style="animation-delay:0.12s">
            {post['summary']}
          </p>
        </header>

        <div class="rise prose mt-14 max-w-[38rem] border-t border-rule pt-12 dark:border-rule-dark sm:mt-16" style="animation-delay:0.18s">
{body}
        </div>

        <div class="mt-16 border-t border-rule pt-8 dark:border-rule-dark">
          <a href="/blog/" class="nav-link">&larr; All posts</a>
        </div>
      </article>
    </main>
"""


POST_BODY = """
          <p>
            About a year ago, WebTranslateIt ran on Rails 3.2 LTS and Ruby 2.7. It now runs on vanilla
            Rails 7 and Ruby 3.1. The app started life in 2009 as a Rails 2 app. Time flies.
          </p>
          <p>
            <a href="https://webtranslateit.com" target="_blank" rel="noopener">WebTranslateIt</a> is a
            Rails app with a large codebase, serving about 35 requests per second on average.
          </p>
          <p>
            Rails LTS is a maintained fork of Rails sold by Makandra, with continuous security fixes.
            They also ship patched versions of some Rails dependencies, rake among them. It let us stay
            on an old version of Rails indefinitely and safely, but staying was never the plan. We
            wanted the newer features and the performance improvements. We recommend Rails LTS all the
            same.
          </p>
          <p>
            First, why we were running something so old. For years, WebTranslateIt had a development
            team of one: me. I tried on and off for two years to get from Rails 3.2 to Rails 4, and it
            was simply too hard. Running a business meant shipping the features that paid for it, so
            the upgrade kept getting postponed.
          </p>
          <p>
            We are two now. James, a freelance Rails developer, took the project on. He is experienced
            and knows the framework deeply, and that is why we moved as fast as we did. Here is how we
            went from Rails 3.2 to 7.0, and Ruby 2.7 to 3.1, in four months.
          </p>

          <h2>Preparation</h2>
          <p>
            We started by improving test coverage. Upgrading across a gap that size without good
            coverage is asking for trouble. We spent a few months writing unit tests over the important
            parts of the code, plus feature tests with Capybara.
          </p>
          <p>
            We added RuboCop and fixed the offenses. Normalizing the code and catching problems early,
            many of them correctable automatically, helped enormously. We shipped all of it before
            touching Rails.
          </p>
          <p>
            Strong parameters was one of the headline Rails 4 features, so we added the
            strong_parameters gem on Rails 3 and made the app ready ahead of time.
          </p>
          <p>
            Before each upgrade we read the Rails upgrade guide and the upgrade notes on fastruby.io.
            Both were a great help.
          </p>

          <h2>Rails 4</h2>
          <p>
            Rails 4 was the hardest of the upgrades, despite everything we had done in advance. A lot
            changed in the framework. Rather than recount all of it, here are three things worth
            knowing if you are facing the same jump.
          </p>

          <h3>Go from latest to latest</h3>
          <p>
            We started by moving from Rails 3.2 LTS to vanilla 4.0, and hit a wall. Rails 3.2 LTS let
            us run Ruby 2.7; vanilla 4.0 did not, so we had to downgrade every dependency to a version
            old enough to match. Many of those older versions had different public APIs, which meant
            reimplementing our own code against them. Dependency hell.
          </p>
          <p>
            Then, having finished, we could not release it. Vanilla 4.0 carries known security issues,
            so shipping it would have been a step backwards.
          </p>
          <p>
            So we carried on to vanilla 4.1, then 4.2, then 4.2 LTS. Rails 4.2 LTS supports Ruby 2.7,
            so we could finally upgrade all those dependencies again, and undo the API changes we had
            just made.
          </p>
          <p>
            It was a lot of wasted work. In hindsight, and contrary to what the Rails upgrade guide
            advises, we should have gone straight from 3.2 LTS to 4.2 LTS and skipped the detour
            entirely. We learned the lesson and did exactly that for every later version, and it went
            much faster.
          </p>

          <h3>Backport what you can</h3>
          <p>
            We made one commit for every small change needed to run on the next version of Rails.
            Plenty of those changes work fine on the current version too.
          </p>
          <p>
            Whenever that was the case, we cherry-picked the backportable commits into a pull request
            against main, checked everything still worked, and deployed it. Then we rebased main onto
            the Rails 4 branch. The goal was to keep the Rails 4 pull request as small as possible.
          </p>

          <h3>Have a way back</h3>
          <p>
            We also made sure the upgraded app was easy to revert. When a release was ready, we tested
            the water by deploying the branch without merging it:
          </p>
          <pre>cap production deploy BRANCH=rails4</pre>
          <p>and going back to Rails 3 was one command:</p>
          <pre>cap production deploy</pre>
          <p>
            We deployed to staging first, every time. A small changeset plus a one-command rollback is
            what let us deploy with confidence.
          </p>
          <p>
            Rails 4 went out on May 4. Two months from Rails 3.2 to 4.2, with no disruption.
          </p>

          <h2>Rails 5</h2>
          <p>
            James started on Rails 5 the day Rails 4 shipped, this time targeting the LTS release,
            which made it much easier.
          </p>
          <p>Meanwhile I had maintenance to do:</p>
          <ul>
            <li>read the logs for deprecation warnings and fix them</li>
            <li>
              let Dependabot upgrade our dependencies. There was a lot to get through, since many gems
              had dropped Rails 3 support. We rebased them onto main one at a time and released them
              gradually.
            </li>
            <li>point RuboCop at Rails 4 and work through the new offenses, again in small releases.</li>
          </ul>
          <p>
            All of it was rebased onto the Rails 5 branch, which helped that upgrade along. Team work.
          </p>
          <p>
            Rails 5 went out on June 5, almost exactly a month after Rails 4.
          </p>

          <h2>Serialization</h2>
          <p>
            Rails 5 added support for Postgres JSONB columns, so we converted every field that had been
            serialized as YAML since Rails 2. Plural forms on translations were one of them. Migrating
            30 million translations took a week, and we found a way to do it without any disruption.
            That deserves a post of its own.
          </p>

          <h2>Rails 6</h2>
          <p>
            We went straight on to Rails 6. After 3 to 4 and 4 to 5, this was a small gap. Rails 6.1 was
            still supported at the time, so we went to vanilla 6.1. It felt good to be back among
            supported releases.
          </p>
          <p>
            Rails 6 went out on June 13, twelve days after Rails 5. It went that fast because by then we
            were practiced at this, and RuboCop had kept the code in good shape. There was not much to
            change.
          </p>
          <p>
            Rails 6 introduced framework defaults, so we spent the next few days turning them on one at
            a time and releasing each one. As usual, we watched for deprecation warnings and let
            Dependabot do its work.
          </p>

          <h2>Ruby 3.0, then 3.1</h2>
          <p>
            Rails 6 supports Ruby 3.0, so we upgraded and released on June 14, the day after Rails 6.
          </p>
          <p>
            Then we tried Ruby 3.1 on Rails 6.1, and it worked. We upgraded on June 23, with no changes
            at all.
          </p>

          <h2>Rails 7</h2>
          <p>
            I had not even released Rails 6 when James asked on Slack: &ldquo;Guess how many failing
            specs we have on Rails 7?&rdquo; He was about to go on holiday and wanted the upgrade
            finished. We had one failing spec. The Rails 7 release was ready before Rails 6 had shipped.
          </p>
          <p>
            Rails 7 went out on June 28. We spent the following days enabling the new defaults one by
            one, clearing deprecation warnings and fixing RuboCop offenses.
          </p>

          <h2>What we learned</h2>
          <p>
            Rails 3.2 to Rails 7 in about four months, with a team of two. I will not pretend it was
            relaxing. The holiday afterwards was well earned.
          </p>
          <p>
            Rails upgrades have gotten much easier over the years. There are fewer breaking changes, and
            the framework defaults files let you turn new behavior on one piece at a time.
          </p>
          <p>
            Upgrade stories usually leave out the infrastructure work, and that was the larger part for
            us. Changing how we serialized data was a big migration in its own right, because of the
            size of the database. We also adopted a couple of abandoned gems: we now maintain version_fu
            and payday so they work on Ruby 3.1 and Rails 7.
          </p>
          <p>
            The app uses far less memory now, thanks to Ruby 3.1 and to the dependencies we could
            finally upgrade. It is faster and more reliable than it has ever been.
          </p>
"""


# --------------------------------------------------------------------------

if __name__ == "__main__":
    write(
        "index.html",
        "Rebase Capital &mdash; We build and run SaaS",
        "Rebase Capital builds and runs B2B SaaS products. Owned and operated by Edouard Bri&egrave;re.",
        "/",
        HOME_MAIN,
    )
    write(
        "about/index.html",
        "Edouard Bri&egrave;re &mdash; Rebase Capital",
        "Edouard Bri&egrave;re founded Rebase Capital and writes the software it runs: WebTranslateIt and TrackBerry.",
        "/about/",
        ABOUT_MAIN,
        current="About",
        og_type="profile",
    )
    write(
        "blog/index.html",
        "Blog &mdash; Rebase Capital",
        "Write-ups of the work behind our products: Rails upgrades, data migrations and running software for the long haul.",
        "/blog/",
        blog_index_main(),
        current="Blog",
    )
    post = POSTS[0]
    write(
        f"blog/{post['slug']}/index.html",
        f"{post['title']} &mdash; Rebase Capital",
        post["summary"],
        f"/blog/{post['slug']}/",
        post_main(post, POST_BODY),
        current="Blog",
        og_type="article",
    )

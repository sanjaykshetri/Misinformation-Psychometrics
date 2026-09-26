# Literature synthesis: existing research on misinformation vulnerability measurement

Date: 2026-09-26

## How to read this document

This synthesis was written without a live web-search or citation-verification
tool available in this environment. It draws on general domain knowledge of
well-known research programs in this area, organized to be useful for
Study 1 item development, but it is **not a substitute for a verified
literature search**. Every specific attribution (author, year, exact finding)
is marked `[VERIFY]` and should be checked against a real database (Google
Scholar, PsycINFO, Web of Science) or a reference manager before being cited
in any external-facing document, preregistration, or manuscript. Treat the
named concepts and research programs as reliable pointers for where to look,
not as a finished bibliography.

## 1. Why this matters for this project

[docs/project_status.md](project_status.md) identifies two open problems that existing literature can help
resolve before Study 1 item writing:

1. Study 0C found evidence-evaluation is not cleanly separable from updating
   with the current item design — the literature on belief updating and
   correction may suggest better item structures.
2. Study 2 is meant to test convergent/discriminant validity against existing
   instruments — those instruments need to be identified now so Study 1 items
   can be designed to overlap and differ from them in known, defensible ways.

## 2. Existing instruments and paradigms, mapped to this project's dimensions

| This project's dimension | Related existing research programs (names to verify) | Notes |
|---|---|---|
| Discernment (true/false accuracy) | Fake-news discernment tasks used across the Pennycook & Rand research program `[VERIFY]`; signal-detection reframing of "fake news detection" as accuracy + bias, associated with work sometimes cited as Batailler, Brannon, Teas & Gawronski `[VERIFY]` | This project already adopts the signal-detection (d-prime/criterion) framing found in that reframing literature — worth citing directly as prior justification for the Study 0 design choice. |
| Response bias / credulity | Same signal-detection reframing as above; general "truth bias" literature in deception-detection research (people are more often biased toward judging statements true than false) `[VERIFY]` | Deception-detection truth-bias literature is a distinct but related tradition worth a brief look. |
| Confidence calibration | Overconfidence/calibration literature in judgment and decision-making more broadly (not misinformation-specific); illusory truth effect research on repetition increasing perceived truth independent of accuracy, associated with Fazio and colleagues `[VERIFY]` | The illusory-truth-effect literature is directly relevant to why `prior_exposure` is in the item bank and could motivate an explicit repetition manipulation in Study 1. |
| Evidence evaluation | Not a single well-named instrument; closest analogues are argument-quality/evidence-strength manipulation studies in persuasion research and "epistemic cognition" measures of source evaluation | This is likely the least-covered dimension in existing psychometric instruments, which may partly explain why Study 0C found it hardest to recover — there may not be a mature template to adapt from. |
| Belief updating | The "continued influence effect" literature (misinformation persisting in memory/judgment after correction), associated with Johnson & Seifert and later synthesized by Lewandowsky, Ecker, Cook and colleagues (often cited via a widely used review sometimes referred to informally as the "Debunking Handbook") `[VERIFY]`; the "backfire effect" claim and its more recent non-replication, associated with Wood & Porter `[VERIFY]` | Directly relevant: this literature debates whether corrections reliably move beliefs at all, and under what conditions they backfire — important context for interpreting why Study 0's updating dimension is only moderately recoverable, and for designing more diagnostic updating items. |
| Verification competence | "Lateral reading" research from the Stanford History Education Group, associated with Wineburg & McGrew `[VERIFY]`, on how experts vs. novices verify online claims by leaving the source rather than reading in-depth | Directly actionable: lateral-reading behavior is a well-developed, empirically grounded template for real (not abstract) verification items in Study 1. |
| Sharing restraint | "Lazy, not biased" / accuracy-nudge research associated with Pennycook & Rand, arguing inattention rather than motivated reasoning explains low-quality sharing `[VERIFY]` | Relevant to Study 1 item design: their accuracy-prompt manipulation is a candidate experimental item type for a sharing-restraint task. |
| Composite/omnibus instruments | The "Misinformation Susceptibility Test" (MIST), a validated multi-item scale reportedly associated with Maertens, Roozenbeek, van der Linden and colleagues `[VERIFY]` | This is the single most important instrument to verify and obtain, since it is the closest existing composite measure and the natural convergent-validity anchor for Study 2. |
| General analytic-thinking correlate | Cognitive Reflection Test (Frederick, 2005) and its association with fake-news discernment in the Pennycook & Rand program `[VERIFY]` | Useful as a discriminant-validity check: this project's `general_knowledge` and `discernment` dimensions should relate to, but not collapse into, CRT-style analytic thinking. |
| Bullshit receptivity / epistemically suspect beliefs | "Bullshit receptivity" scale associated with Pennycook, Cheyne, Barr, Fugelsang & Koehler `[VERIFY]` | A candidate discriminant-validity comparison for `credulity_bias`. |

## 3. Implications for the next steps

1. **Obtain and verify the MIST** as the primary convergent-validity anchor
   before finalizing Study 1 item content — if it already covers several of
   this project's dimensions well, item design should explicitly differentiate
   rather than duplicate it.
2. **Use lateral-reading research as the template for verification items**,
   replacing the current abstract "verification item" parameters
   (`difficulty`, `discrimination`, `topic` only, no described task) with
   concrete source-checking tasks grounded in that literature.
3. **[Done, 2026-09-26] Revisit the updating item design using the continued-influence-effect and
   backfire-effect literatures.** Study 0C's finding that evidence-evaluation
   was not recoverable was traced to the simulated item structure exposing no
   directly observable comprehension signal (only a hidden latent folded into
   the movement calculation). The updating task was redesigned (V1.1) to emit
   an observable comprehension-check response, and a matching item-level model
   raised evidence-evaluation recovery from r &asymp; 0.13 (frequently sign-reversed)
   to r &asymp; 0.68-0.75 across the full Monte Carlo sweep. See
   [study_00_results.md](../studies/study_00_simulation/study_00_results.md) and
   [project_status.md](project_status.md) for details. Still open: whether a
   richer multi-round evidence structure would further improve the still-modest
   updating recovery (r &asymp; 0.26-0.55).
4. **Treat evidence evaluation as the least mature dimension by design, not
   just by simulation accident** — there may not be an established instrument
   to adapt, which means this project may need to originate item types here
   rather than adapt existing ones.
5. **Use the illusory-truth-effect literature to justify (or redesign)** the
   `prior_exposure_rate` mechanism already in the simulated item bank, ideally
   with an explicit repeated-exposure manipulation in Study 1 rather than a
   single hidden exposure probability.

## 4. What still needs to happen before this is a real literature review

- Run an actual search (Google Scholar / PsycINFO / Web of Science) for each
  `[VERIFY]`-tagged item above, confirm the citation, and record full
  bibliographic details.
- Search specifically for any existing multidimensional misinformation
  vulnerability instruments beyond MIST that this synthesis may have missed.
- Check for recent (post-2023) replications or critiques of the backfire
  effect and illusory truth effect, since those literatures are actively
  contested.
- Once verified, convert this into a properly cited related-work section
  suitable for a preregistration or manuscript.

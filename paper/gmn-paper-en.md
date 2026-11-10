# Blind Men Touching Characters: Probing Symbolic Algebra vs. 2D Spatial Perception in LLMs via Chinese Character Riddles

## — Probing 1D symbolic algebra and 2D spatial blindness in large language models through Chinese character riddles

**Authors**: Computational Linguistics and LLM Cognitive Diagnostics Research Group (计算语言学与大模型认知诊断课题组)　　**Date of Chinese original**: 2026-11-06　　**English translation**: 2026-11-10　　**Chinese title**: 盲人摸字：通过汉字字谜探查大模型的一维符号代数与二维空间失明

> **Translator's note on conventions.** (1) The English title above is the one printed by the author on the title page of the Chinese original; the Chinese title is given here for identification. (2) All Chinese clue texts, component names and example characters are preserved verbatim, because a riddle built on glyph decomposition, meaning or tone cannot be translated without destroying its subject matter; each is accompanied by a literal English gloss or a structural annotation. (3) All numbers, percentages, *p*-values, sample sizes, GIDs and model identifiers are copied verbatim from the Chinese original; no recomputation, rounding or correction was introduced in translation. (4) Terminology follows the author's own English usage: 拆形 *Chaixing* (graphemic decomposition), 会意 *Huiyi* (semantic reinterpretation), 谐音 *Xieyin* (homophonic pun), 独体字 *indecomposable character*, 合体字 *decomposable / compound character*, 一维符号代数 *1D symbolic algebra*, 二维空间失明 *2D spatial blindness*, 交叉盲测 *cross-blind evaluation*, 全新单轮同题自测 *fresh-session same-item self-test*, 制谜方 *maker*, 猜题方 *solver*, 同错收敛 *convergent misdirection*, 早熟命中后自我推翻 *early-hit self-sabotage*, 字理卡 *character-structure card*; "pp" = percentage points; K = kimi-k3.1-pro and U = u2-flash. (5) The Chinese original carries an author-provided English abstract; it is reproduced verbatim after the translated abstract so that no authorial wording is lost. (6) Inline bar charts embedded in Tables 3 and 4 of the Chinese edition are represented here by the numerical columns from which they were drawn. (7) The 17 reference entries are reproduced as printed, without verification or correction: several use generic group attributions or arXiv identifiers dated 2026 that readers should check against the original sources before citing. (8) Editorial notes about dataset scope and authorship are collected at the end of this translation; they are not part of the original paper.

---

## Abstract

Mainstream large language models (LLMs) process natural language through discrete token IDs, whose input layer strips away the two-dimensional raster-pixel information of logographic script. Yet frontier LLMs display reasoning performance far above early baselines when solving and composing Chinese character riddles. This apparent achievement raises a basic question in cognitive science: do LLMs "see" the two-dimensional geometry of Chinese characters as humans do, or are they merely performing a "blind men touching characters" style of one-dimensional symbolic operation detached from visual topology? Moreover, does the multi-step process of solving a riddle constitute a valid sub-character chain of thought (CoT) that could serve future model training?

Rather than continuing to chase scores on traditional static riddle datasets such as CC-Riddle, this paper systematically recasts Chinese character riddles as a **sub-character cognitive probe** and as a **reasoning training ground with verifiable rewards (RLVR testbed)**. We audit 1,050 reference riddles built over the 100 most frequent characters in modern Chinese, together with 597 high-quality riddles originally authored by two frontier models (kimi-k3.1-pro and u2-flash) under a fourfold anti-contamination quality-control pipeline, spanning three orthogonal techniques (Chaixing, Huiyi, Xieyin). On this basis we run a strictly controlled paired experiment: **cross-blind evaluation** (A makes → B guesses) versus **fresh single-session same-item self-testing** (A makes → A guesses), for a total of 1,194 independent reasoning trajectories.

The empirical analysis reveals four core laws. **(1) A dichotomy between 1D symbolic algebra and 2D spatial blindness.** Models excel on compound characters that can be discretised into Unicode Ideographic Description Sequences (IDS): Chaixing cross-blind accuracy reaches 56.0% and same-item self-test accuracy 64.0%. They collapse on indecomposable characters that depend on 2D stroke geometry and relative spatial position (overall cross accuracy only 22.4%; Fisher's exact test *p* = 2.0 × 10⁻⁶), and show a counter-intuitive stroke-complexity gradient completely opposite to human cognition (Chaixing blind-test accuracy 39.3% on characters of 1–4 strokes vs. 64.6% on characters of ≥ 9 strokes). **(2) Encoder–decoder isomorphism of model-private character-decomposition priors.** A 2 × 2 full-factorial additive decomposition, after partialling out the solver-ability main effect (*β* = +16.3 pp) and the item-source clarity main effect (*α* = +11.4 pp), leaves a significant net self-familiarity advantage (*γ* = +5.2 pp, paired exact McNemar test *p* = 0.0144). This advantage is almost entirely concentrated in formalizable Chaixing (*γ*<sub>Chaixing</sub> = +10.8 pp, *p* = 0.0139; kimi's self-solved Chaixing rises from 49.0% to 84.7%), and is wholly non-significant for Huiyi (+2.0 pp, *p* = 0.6655) and Xieyin (+3.0 pp, *p* = 0.4050). **(3) Coordinate-free "bag-of-components" blindness and component hallucination.** A micro-analysis of 44 cross-model convergent-error pairs shows that models retain only a *set* of components and lose their 2D positions (the clue 「有力添两点」 for 为 is consistently mis-solved as 办; 「门口站个人」 for 们 as 闪), and that they frequently fabricate illegal glyph structures (asserting 「寺+中=诗」 or 「禾+么=秘」). **(4) The "overthinking paradox" of riddle-solving CoT and early-hit self-sabotage.** Incorrect traces are on average 2.3–3.3 times longer than correct ones; among 364 cross-blind errors, as many as 23.6% (86 cases) had already derived the correct single character in the first half of the chain of thought, only to overturn it because of a "compound-character complexity bias".

On the basis of these findings we propose a **Decomposed Orthographic CoT** coupled with a symbolic IDS verifier, and a self-play reinforcement-learning framework called **RiddlePlay**.

**Keywords**: large language models; Chinese character riddles; sub-character cognitive probe; Ideographic Description Sequence (IDS); spatial-topology blindness; chain-of-thought degeneration; reinforcement learning with verifiable rewards (RLVR)

### Author-provided English abstract (reproduced verbatim from the Chinese edition)

Mainstream Large Language Models (LLMs) process logographic scripts such as Chinese via discrete token embeddings that strip away 2D visual glyph geometry. Yet frontier LLMs achieve surprisingly strong performance in solving and generating Chinese character riddles. Does this imply that LLMs perceive character shapes like human readers, or are they acting as "blind men touching characters" by executing 1D symbolic algebra learned from textual meta-descriptions? Rather than treating riddle solving merely as another QA benchmark like CC-Riddle, this study repurposes Chinese character riddles as both a diagnostic cognitive probe of sub-character representation and a verifiable reasoning training testbed. Using a strictly audited corpus across the 100 most frequent Chinese characters (1,050 reference riddles and 597 contamination-free LLM generated riddles spanning component decomposition Chaixing, semantic association Huiyi, and homophonic pun Xieyin), we conduct a paired 2×2 evaluation comparing Cross-Blind solving against Fresh-Session Self-Testing across 1,194 reasoning trajectories. We establish four empirical findings: (1) a stark dichotomy between strong 1D Symbolic IDS Algebra on decomposable characters (56.0% cross / 64.0% self on Chaixing) and severe 2D Spatial Blindness on indecomposable characters (22.4% cross, Fisher's *p* = 2.0 × 10⁻⁶), accompanied by an inverse stroke-complexity gradient (39.3% on 1–4 strokes vs. 64.6% on ≥ 9 strokes); (2) an additive 2 × 2 decomposition isolating a significant net Self-Familiarity advantage (*γ* = +5.2 pp, McNemar *p* = 0.0144) that concentrates exclusively in formalizable component decomposition (*γ*<sub>Chaixing</sub> = +10.8 pp, *p* = 0.0139, with kimi surging from 49.0% to 84.7%) while vanishing in semantic and phonetic riddles; (3) systematic "Bag-of-Components" coordinate blindness and illegal glyph synthesis (寺+中=诗, 禾+么=秘) across 44 convergent error pairs; and (4) an Overthinking Paradox in riddle Chain-of-Thought (CoT), where incorrect traces are 2.3×–3.3× longer than correct ones and exhibit a 23.6% Early-Hit Self-Sabotage rate driven by over-composition bias. Finally, we formalize a neuro-symbolic IDS-verified CoT and self-play Reinforcement Learning with Verifiable Rewards (RLVR) paradigm.

---

## 1 Introduction: the paradox of character vision under discrete token representations

As the principal logographic writing system still in use, Chinese characters (logographic script) differ fundamentally from alphabetic scripts in cognitive processing: each character corresponds not only to a pronunciation (*yin*) and a lexical meaning (*yi*), but is also a visual figure (*xing*) assembled inside a two-dimensional square from basic strokes (horizontal, vertical, left-falling, right-falling, turning, etc.) and sub-character components (radicals) according to specific spatial-topological relations [3, 5]. Human readers naturally recruit the primary visual cortex and the visual word form area (VWFA) for continuous geometric perception of stroke junctions, the relative positions of components, and 2D symmetry. Modern LLMs built on the Transformer, however, generally adopt discrete tokenization based on byte-pair encoding (BPE) or vocabulary indices [6, 7]. Under this mechanism, 「一」, 「不」, 「国」 and 「赢」 are all mapped to isolated positive integers and high-dimensional dense vectors at the embedding layer, whether they contain 1 stroke or 17, and whether they are indecomposable or enclosed structures; their physical glyph pixels are completely erased.

This innate absence at the input modality produces a fascinating cognitive paradox. On the one hand, recent work on robustness to glyph confusion (e.g. SinoGlyphBench [9] and full-glyph image modelling [7, 8]) repeatedly shows that text-only LLMs are extremely fragile in the face of radical-decomposition confusion or visually similar character substitution. On the other hand, when we test the latest reasoning models with Chinese character riddles [1, 2], which depend heavily on the ability to decompose and recombine glyphs, the models not only create legal riddles autonomously under a prescribed technique (Chaixing, Huiyi, Xieyin), but also reach 39.0% overall accuracy in fully open single-character blind answering (and as high as 60.4%–84.7% in Chaixing same-item self-testing) — a jump of two orders of magnitude over the early GPT-3.5 baseline (0.39%).

Why can a discrete symbolic model that "cannot see glyph pixels" decompose characters, make riddles and solve them? More importantly, where is the boundary of its success and failure? Existing riddle research (CC-Riddle [2], Tan et al. (2016) [1], and multilingual puzzle benchmarks [12, 13]) mostly treats riddles as static question answering or text generation, evaluating overall model scores around dataset scale or prompt engineering. Yet as the Turing-test and formal-probing literature [14, 15] emphasises, static scores often conceal shortcut learning in the underlying representation and data contamination (riddles on the internet are highly homogeneous reposts). If we change perspective — no longer asking "is some riddle dataset good", but treating Chinese character riddles as a **cognitive probe** of sub-character representation inside LLMs and as a **CoT training testbed** for constrained symbolic reasoning — we touch the core issue of representation theory directly:

1. **Probing orthographic perception.** When processing character structure, do LLMs build a 2D spatial perception comparable to that of humans? Or have they merely acquired, from pretraining text (dictionary definitions, folk character-splitting sayings, input-method encoding descriptions), a set of 1D discrete "component algebra rules" (1D symbolic algebra) that goes completely blind as soon as it leaves standard radical composition and enters a domain requiring 2D geometric positions and indecomposable stroke decomposition?
2. **Diagnosing and training riddle CoT.** Riddle solving consists of "clue segmentation → cue mapping → component / phonological synthesis → dual verification of orthography and semantics", and is naturally isomorphic to a multi-step chain of thought. What systematic degeneration exists in the riddle CoT of current LLMs? How can we exploit the natural generation–solving duality of riddles and the verifiability of a unique single-character answer to build a contamination-free self-play reinforcement learning (RLVR) training loop?

Addressing these two questions, we construct a full-chain experimental system over the 100 most frequent core characters of modern Chinese: a reference-set audit (1,050 items), controlled original riddle generation (600 generated, 597 passing fourfold QC), cross-model blind testing (597 trials) and fresh-session same-item self-testing (597 trials). The core contributions are as follows:

- **Revealing a representational fault line: strong 1D symbolic algebra, blind 2D geometry.** With character frequency strictly controlled, we show for the first time that the blind-test solve rate of LLMs on decomposable compound characters (44.3%) is nearly twice that on indecomposable characters (22.4%) (Fisher's exact test *p* = 2.0 × 10⁻⁶), with a monotone collapse along the spatial-topology dimension (1D left–right / top–bottom juxtaposition ≈ 59.3% → 2D enclosure / inlay 43.8% → continuous-stroke indecomposable characters 29.8%) and a stroke-count reversal gradient contrary to human intuition (Chaixing accuracy 64.6% on ≥ 9 strokes, far above 39.3% on 1–4 strokes).

- **Establishing a 2 × 2 orthogonal generation–solving additive decomposition and localising model-private decomposition priors.** By pairing cross-blind testing with fresh-session same-item self-testing, we resolve apparently opposite maker-stratified differences (kimi self-test +21.5 pp vs. u2 self-test −11.0 pp) exactly into a solver-ability gap (*β* = +16.3 pp), an item-source clarity gap (*α* = +11.4 pp) and a genuine net self-familiarity advantage (*γ* = +5.2 pp, *p* = 0.0144). More importantly, stratified tests show that the self-advantage is highly significant only for Chaixing (*γ*<sub>Chaixing</sub> = +10.8 pp, *p* = 0.0139) and close to zero for Huiyi and Xieyin, directly confirming that each model maintains a private, reversible, textual character-decomposition rule table.

- **Building a fine-grained taxonomy of sub-character spatial blindness and riddle-CoT degeneration.** Through item-by-item analysis of 44 cross-model convergent-error cases and 1,194 reasoning traces, we identify coordinate-free bag-of-components blindness (「为/办」 confusion, 「们/闪」 confusion), visual component hallucination and illegal glyph fabrication (asserting 「寺+中=诗」), and a severe "overthinking paradox" in riddle CoT (incorrect answers consume 2.3–3.3 times as many tokens as correct ones) together with early-hit self-sabotage (in up to 23.6% of blind-test errors the correct answer was derived first and then overturned because of a compound-character complexity bias).

- **Proposing Decomposed Orthographic CoT and the RiddlePlay training paradigm.** Against the 58.9% low-confidence post-hoc rationalisation found in explanations, we argue that static riddle collections cannot be distilled into CoT directly. Instead, the fourfold automatic verifier validated here (answer-leak gate, 3-gram originality gate, IDS-tree consistency check, bidirectional mutual-guessing verification) should be used to build a reinforcement-learning loop with verifiable rewards.

---

## 2 Related work: from riddle benchmarks to sub-character cognitive probes

### 2.1 Computational modelling of Chinese character riddles and language-puzzle benchmarks

Early computational work on Chinese character riddles goes back to Tan et al. (2016) [1], which first formalised riddles as a translation-and-ranking problem based on statistical phrase-to-radical alignment and rule-based combination / decomposition, pointing out that what distinguishes riddles from ordinary commonsense puzzles is the addition and subtraction of glyph components and metaphorical alignment. Xu et al. (2022) then released CC-Riddle [2], a large-scale Chinese character riddle QA dataset of more than 20,000 items combining web crawling with template / model generation, and introduced radical decompositions from IDS dictionaries and HanziCraft.

In the last two years, puzzles and word games have become important probes of non-literal reasoning and cultural common sense in LLMs [10]. Saxena et al. (2025) [12] built a multi-task Bengali traditional-puzzle benchmark and exposed model weaknesses in metaphor triggers and semantic-ambiguity resolution. Adaptive Originality Filtering (AOF, 2025) [11] observed that conventional CoT and few-shot prompting easily replicate ready-made internet material when generating puzzles, and proposed an adaptive originality filter. In Chinese, X-Riddles (2026) [13] examines the understanding and generation of homophonic and semantic two-part allegorical sayings (*xiehouyu*). However, as our experiments confirm, riddle websites and CC-Riddle overlap through reposting chains at a rate as high as 84%; evaluating LLMs directly on existing static datasets therefore cannot distinguish real-time sub-character reasoning from recitation of high-frequency clue texts in pretraining corpora.

### 2.2 Sub-character representation, tokenization blindness and visual glyph modelling

In computational linguistics, the masking effect of discrete tokenization on intra-character morphology and orthography has attracted wide attention. A 2025 study in *Computational Linguistics* (MIT Press) states explicitly that, because LLMs perceive byte sequences or atomic tokens rather than the surface visual form of characters, the internal association between phonetic and semantic radicals is severed at the input layer [6]. Work in the pretraining era tried to inject sub-character features explicitly: ChineseBERT (Sun et al., 2021) [3] fused multi-font glyph-rendering embeddings and pinyin embeddings into the input representation; Li et al. (2022) [4] designed glyph–phonetic probes for Chinese spell checking (CSC); Si et al. (2023/2026) [5] proposed sub-character tokenization based on strokes, Wubi, Zhengma and Cangjie encodings.

More radical approaches replace discrete token IDs with 2D visual input altogether. *Full Glyph Images Beat Token Embeddings* (2026) [7] showed in a strictly controlled two-branch experiment that rendering a character sequence as 2D greyscale images and processing it with a ViT carrying 2D positional encoding improves next-token prediction accuracy by 21% relative to a standard token-embedding baseline while doubling convergence speed. MIXAR (2026) [8] further showed that pixel-level autoregressive language models must enlarge image patches from 8 × 8 to 32 × 32 to capture the fine stroke topology of CJK scripts. Meanwhile, the safety-moderation benchmark SinoGlyphBench (EMNLP Findings 2026) [9] found in 176,916 paired evaluations that when clearly legible Chinese characters are subjected to component splitting (a single character written as its left and right components) or cross-script visually similar substitution, 12 mainstream LLMs and multimodal models lose 24.3% of their original accuracy. The present study complements this line of work rigorously: instead of relying on external adversarial noise, we use the constructive task of Chinese character riddles, which intrinsically requires manipulating strokes and components, to map the geometric boundary of glyph representation inside text-only LLMs directly.

### 2.3 Structured reasoning probes and chain-of-thought pathology in LLMs

How to probe the reasoning ability of a black-box LLM scientifically rather than its surface fitting is a frontier topic in interpretability. X-RAY (2026) [14] proposed a formal calibrated-probe framework for reasoning maps and revealed a systematic asymmetry: models are fairly robust at tightening constraints within a fixed solution space (constraint refinement) but degrade sharply when the manifold of the solution space must be restructured (solution-space restructuring). On spatial perception, *Stuck in the Matrix* (2025) [15] confirmed structural bottlenecks in text-only LLMs when handling 2D grid topology and rotation of relative positions. Work on proof-tree construction and alignment reasoning [16, 17] shows that autoregressive CoT without structure-aware pruning easily falls into fruitless branch search. This paper brings these formal probing ideas down to the sub-character scale and quantifies, for the first time, early-hit self-sabotage and post-hoc rationalisation hallucination in riddle CoT.

---

## 3 Formal theoretical framework and orthogonal double-blind experimental design

### 3.1 A dual representation model of Chinese characters: 1D symbolic tree vs. 2D continuous stroke manifold

To define rigorously whether "LLMs see Chinese characters the way humans do", we first distinguish two orthogonal representational forms mathematically.

**Definition 1 (1D Ideographic Description Sequence tree, T<sub>IDS</sub>).** At the symbolic encoding level, any modern Chinese character *c* ∈ Σ can be defined as a finite rooted ordered tree T<sub>IDS</sub>(*c*) via Unicode Ideographic Description Characters (IDCs). Let the set of structural operators be:

```
(1)  Ω = { ⿰ LR, ⿱ TB, ⿲ left-middle-right, ⿳ top-middle-bottom }        [Ω1D: 1D linear juxtaposition]
       ∪ { full enclosure, upper-three enclosure, lower-three enclosure,
           upper-left enclosure, lower-left enclosure, inlaid }           [Ω2D: 2D enclosure and inlaid operators]
```

If *c* is a decomposable compound character (`decomposable = True`), then T<sub>IDS</sub>(*c*) = ⟨ω, c₁, …, c<sub>k</sub>⟩, where ω ∈ Ω, k ∈ {2, 3} and c<sub>i</sub> are sub-components. If *c* is an indecomposable character (`decomposable = False`), T<sub>IDS</sub>(*c*) = ⟨∅, c⟩ degenerates to a single-node atomic symbol.

**Definition 2 (2D continuous geometric stroke manifold, G<sub>2D</sub>).** At the level of human visual perception, a character *c* is a set of directed continuous stroke trajectories defined on a normalised 2D canvas [0, 1]²:

```
(2)  G2D(c) = { (τm, γm(t))  |  m = 1, …, S(c), t ∈ [0, 1],
                 γm(t) = (xm(t), ym(t)) ∈ [0, 1]² }
```

where S(*c*) is the total number of strokes, τ<sub>m</sub> ∈ {horizontal, vertical, left-falling, right-falling, dot, rising, turning, hook} is the stroke category, and any two strokes have well-defined Euclidean distance, topological intersection γ<sub>m</sub>(t₁) = γ<sub>n</sub>(t₂) and relative direction angle θ<sub>mn</sub> ∈ [−π, π].

Humans solving riddles switch freely between T<sub>IDS</sub>(*c*) (adding or subtracting radicals, e.g. 「日+月=明」) and G<sub>2D</sub>(*c*) (fine geometric stroke adjustment, e.g. 「大字去人剩一横」, 「木字少横下加点」). For a text-only LLM M<sub>θ</sub> receiving only a discrete token embedding e(*c*) ∈ ℝ<sup>d</sup>, however, the input satisfies G<sub>2D</sub>(*c*) ≡ ∅. We therefore state the core theoretical hypothesis:

**Core Hypothesis 1 (Blind men touching characters: the 1D symbolic component algebra hypothesis).** A text-only LLM M<sub>θ</sub> does not possess a 2D metric-space representation isomorphic to G<sub>2D</sub>(*c*). Instead, from co-occurring character-decomposition descriptions in pretraining text it implicitly fits a noisy 1D symbolic relation map D̂<sub>θ</sub> : Σ → 2<sup>Ω×Σ*</sup>. This mechanism entails three testable empirical consequences:

1. **Law of topological-complexity degradation.** Riddle-solving accuracy decreases monotonically as the required degrees of spatial-geometric freedom increase: 1D linear compound characters (Ω1D) > 2D enclosure / inlaid compound characters (Ω2D) > indecomposable characters depending on G<sub>2D</sub> stroke geometry (`decomposable = False`).
2. **Law of reversed stroke complexity.** Because high-stroke characters are mostly compound characters with multiple radical constraints (the intersection of candidate sets ∩<sub>i</sub> {c | c<sub>i</sub> ∈ D̂<sub>θ</sub>(c)} leaves a very small solution space), whereas low-stroke characters are mostly indecomposable characters relying on continuous G<sub>2D</sub> deformation, accuracy rises significantly with the stroke count S(*c*).
3. **Law of model-private decomposition isomorphism.** The implicit maps D̂<sub>θA</sub> and D̂<sub>θB</sub> learned by different models carry individual bias. When the same model solves its own riddle in a fresh session, forward encoding D̂<sub>θA</sub>(c) → q and inverse decoding q → D̂⁻¹<sub>θA</sub>(q) share the same parameter prior, producing a significant net self-familiarity dividend on — and only on — Chaixing tasks that depend on formal decomposition.

### 3.2 Full-coverage 100-character benchmark and the fourfold anti-contamination QC pipeline

To avoid interference from rare-character frequency and to eliminate pretraining-corpus leakage entirely, we select the 100 most frequent core characters of modern Chinese (from 「一、丁、上、下、不」 to 「那、都、里、面」) as controlled experimental anchors. Table 1 summarises the complete experimental data assets and QC results.

During riddle generation (prompt version `riddle-gen-skill-v0.2-full100`), we build a structured character card for each target character (pinyin, radical, Unicode code point, stroke count, IDS decomposition, decomposable flag) and require the model to create a clue plus its creative reasoning (`reasoning`) without revealing the answer character. To prevent recitation of the reference set, we isolate the reference clues of the same character and deploy a strict fourfold automatic QC pipeline: (1) **legality gate** — enforce a single-character answer, forbid the answer character or meta-linguistic cue words in the clue, and control clue length; (2) **N-gram originality gate** — compute character-level 3-gram Jaccard similarity and longest-common-subsequence ratio between the generated clue and all reference clues of the same character plus previously generated clues (on 60 items from the 10-character pilot, p90 = 0.0 and max = 0.167, so the plagiarism-rejection threshold was tightened to Jaccard<sub>3-gram</sub> ≥ 0.35, successfully intercepting 3 latent paraphrases); (3) **coarse glyph-consistency check** — automatically verify that components claimed in the `reasoning` of compound characters really appear in the IDS sequence of that character; (4) **full-chain hash attestation** — record model version, timestamp and SHA-256 of the input snapshot item by item, excluding any fabricated provenance.

**Table 1　Overview of the 100-character full-coverage experimental system (reference audit set and controlled model-generated set)**

| Data module / QC dimension | Value | Experimental design and computational audit note |
|---|---|---|
| Target characters | 100 | Top-100 high-frequency characters of modern Chinese; 76 decomposable compound characters (76.0%) and 24 indecomposable characters (24.0%); stroke span 1–13 |
| Reference clue pool | 1,050 | 1,019 items from the human-authored CC-Riddle subset + 31 targeted web top-ups after deduplication (of 43 raw scraped items, 12 duplicated CC-Riddle, confirming an 84% same-source reposting chain among riddle sites) |
| Reference explanations | 1,050 | 27 site-native hints; 1,023 model post-hoc explanations, of which 602 (58.9%) were self-rated `confidence = low`, with technique classification heavily skewed towards Huiyi (594 items) |
| Controlled model-authored riddles | 600 | kimi-k3.1-pro and u2-flash each generated 1 riddle per character for each of the three techniques (2 × 100 × 3 = 600), using cross-character few-shot isolation (「的、是」 used only as format examples) |
| Automatic retries at generation | 31 | 31 violating drafts intercepted and regenerated (u2: 29 clue-contains-answer, 2 over-length; kimi: 2 clue-contains-answer); answer-leakage rate of the final accepted set strictly 0.0% |
| Accepted after fourfold gating | 597 | 3 rejected (kimi 2, u2 1) because 3-gram Jaccard similarity exceeded the threshold (> 0.35), indicating paraphrase of a reference clue or exact duplication; accepted set 3-gram Jaccard median p50 = 0.0, p90 = 0.0 |
| Paired double-blind trajectories | 1,194 | For all 597 accepted items, a cross-blind test on 11-05 (A makes → B guesses, 597) and a same-item self-test on 11-06 (A makes → A guesses in a fresh single-turn conversation, 597); interface and format anomalies both 0 |

**Table 1 (continued)　The two evaluation conditions**

- **Cross-blind evaluation**: the 298 riddles made by kimi were answered by u2; the 299 made by u2 were answered by kimi.
- **Fresh-session same-item self-test**: one day later, in an independent process with context history completely cleared and carrying no generation-stage reasoning or memory, the same 597 riddles were returned to their own maker (kimi answers kimi, u2 answers u2). Both tests sent only the same single-turn `[system, user]` instruction (`SYSTEM_PROMPT-v2-json-no-thinking`), requiring a Chinese reasoning process of no more than 200 characters and a unique single-character answer in JSON.

### 3.3 The 2 × 2 orthogonal cross-blind / fresh-session self-test statistical model

Why must cross-blind testing and same-item self-testing be run together? Because a direct maker-stratified comparison of "self-test accuracy" versus "cross accuracy" changes the guessing model at the same time as it changes the experimental condition (for kimi-made items the self-test solver is kimi, while the cross solver is u2), badly confounding "self-familiarity" with "the two models' own solving-ability gap". We therefore establish a **2 × 2 full-factorial linear additive decomposition model**. Let P<sub>i→j</sub> be the expected solve rate for items made by maker *i* ∈ {K, U} and answered by solver *j* ∈ {K, U}:

```
(3)  Pi→j = µ + αi + βj + γ · I[i = j]
```

Here µ is the baseline; α<sub>K</sub> − α<sub>U</sub> = Δ<sub>maker</sub> is the item-source clarity main effect (positive means K-made items are easier for every solver); β<sub>K</sub> − β<sub>U</sub> = Δ<sub>solver</sub> is the solver-ability main effect (positive means K is better at solving than U); and γ is the pure **net self-familiarity effect**. From the four observed cell rates {P<sub>K→K</sub>, P<sub>K→U</sub>, P<sub>U→K</sub>, P<sub>U→U</sub>}, three orthogonal contrasts give unbiased estimators:

```
(4)  Δ̂solver = ½ [ (PK→K − PK→U) + (PU→K − PU→U) ]
(5)  Δ̂maker  = ½ [ (PK→K − PU→K) + (PK→U − PU→U) ]
(6)  γ̂       = ½ [ (PK→K + PU→U) − (PK→U + PU→K) ]
```

It follows immediately that the apparent self-test gains observed by maker are P<sub>K→K</sub> − P<sub>K→U</sub> = +Δ̂<sub>solver</sub> + γ̂ and P<sub>U→U</sub> − P<sub>U→K</sub> = −Δ̂<sub>solver</sub> + γ̂. When |Δ̂<sub>solver</sub>| > |γ̂|, the apparent self-test differences of the two makers must have opposite signs, while their arithmetic mean cancels ±Δ̂<sub>solver</sub> exactly and recovers the pure net self-familiarity effect γ̂. For the paired binary outcomes (Y<sub>g,cross</sub>, Y<sub>g,self</sub>) ∈ {0, 1}² of the same riddle *g* under the two conditions, we assess significance with a two-sided exact binomial McNemar test based on the discordant cells (*b* = cross-only correct, *c* = self-only correct):

```
(7)  pMcNemar = min( 1, 2 · Σ(k = 0 … min(b,c)) C(b+c, k) · 2^−(b+c) )
```

---

## 4 Empirical probe findings: 1D symbolic algebra and 2D spatial blindness

### 4.1 The structural fault line between compound and indecomposable characters, and the spatial-topology degradation gradient

We first test consequence 1 of Core Hypothesis 1 (the law of topological-complexity degradation). Among the 100 high-frequency characters, the 76 compound characters yielded 454 valid riddles and the 24 indecomposable characters (「一、丁、上、下、不、中、为、么、之、了、事、于、人、出、小、己、年、开、心、手、无、日、生、用」 etc.) yielded 143 valid riddles. Table 2 compares the blind-test and self-test performance of the two character classes under the three techniques.

**Table 2　Solve-rate fault line between decomposable compound characters (`decomposable=True`) and indecomposable characters (`decomposable=False`)**

| Specified technique | n (compound) | Cross-blind | Same-item self | n (indecomp.) | Cross-blind | Same-item self | Cross gap Δ | Fisher exact *p* (cross / self) |
|---|---|---|---|---|---|---|---|---|
| Chaixing | 150 | 56.0% (84) | 64.0% (96) | 47 | 29.8% (14) | 48.9% (23) | +26.2 pp | *p* = 0.0024** / 0.0869 |
| Huiyi | 152 | 39.5% (60) | 40.8% (62) | 48 | 20.8% (10) | 25.0% (12) | +18.7 pp | *p* = 0.0235* / 0.0592 |
| Xieyin | 152 | 37.5% (57) | 40.1% (61) | 48 | 16.7% (8) | 20.8% (10) | +20.8 pp | *p* = 0.0078** / 0.0157* |
| **All** | **454** | **44.3% (201)** | **48.2% (219)** | **143** | **22.4% (32)** | **31.5% (45)** | **+21.9 pp** | ***p* = 2.0 × 10⁻⁶∗∗∗ / 0.0005∗∗∗** |

The data show an extremely sharp structural fault line: overall cross-blind accuracy on compound characters (44.3%) is almost exactly twice that on indecomposable characters (22.4%), a gap of +21.9 pp, with a two-sided Fisher exact test reaching the highly significant level *p* = 2.0 × 10⁻⁶. On Chaixing, the technique that most directly tests glyph perception, compound characters reach 56.0% cross-blind (64.0% self-test), while indecomposable characters plunge to 29.8% cross-blind (a drop of 26.2 pp, *p* = 0.0024). Among all 100 characters, 13 were answered 0/6 correctly in the cross-blind test, the great majority being high-frequency indecomposable or semi-enclosed characters (「不、为、么、以、同、后、手、无、来、用」).

To test sensitivity to 2D topological relations further, we subdivide the 100 characters into four spatial-topology levels by the top-level Unicode IDS operator ω (Table 3): (1) 1D left–right juxtaposition (LR); (2) 1D top–bottom stacking (TB); (3) 2D enclosure and inlaid structures (Surround / Inlaid, e.g. 「国、同、过、这、道、在、看、出、事」); (4) continuous-stroke indecomposable characters.

**Table 3　Monotone accuracy-degradation gradient along spatial-topology complexity (the Chinese edition embeds proportional bars for Chaixing cross / Chaixing self)**

| IDS spatial-topology level | Total items | All cross | All self | Chaixing n | Chaixing cross | Chaixing self |
|---|---|---|---|---|---|---|
| 1. Left–right juxtaposition (LR) | 173 | 48.6% | 52.6% | 57 | 59.6% | 64.9% |
| 2. Top–bottom stacking (TB) | 185 | 47.6% | 46.5% | 61 | 59.0% | 67.2% |
| 3. 2D enclosure / inlaid (Ω2D) | 96 | 30.2% | 43.8% | 32 | 43.8% | 56.2% |
| 4. Continuous-stroke indecomposable (∅) | 143 | 22.4% | 31.5% | 47 | 29.8% | 48.9% |

Table 3 confirms consequence 1 clearly: when a 2D planar structure can degenerate into a 1D ordered pair ("A left of B" or "A above B"), Chaixing cross accuracy stays stable at 59.0%–59.6% (self 64.9%–67.2%); as soon as the 2D topological operator Ω2D requiring understanding of containment and semi-enclosure is involved (「同」, 「在/看」, 「过/道」), overall cross accuracy drops immediately from ≈ 48% to 30.2% (Chaixing to 43.8%); and when discrete component anchors disappear entirely and strokes must be added, removed and spatially related *inside* an indecomposable character, Chaixing cross accuracy collapses further to 29.8% (overall only 22.4%).

### 4.2 The inverse stroke-complexity gradient

In the cognitive psychology of human visual recognition, the difficulty of recognising and writing a Chinese character normally rises with its stroke count S(*c*). Yet when we divide the 100 characters into low-stroke (1–4 strokes, 28 characters), mid-stroke (5–8 strokes, 48) and high-stroke (≥ 9 strokes, 24) bands, LLMs show a startling positive monotone increasing gradient (Table 4).

**Table 4　The counter-intuitive stroke-complexity gradient: more strokes, higher riddle-solving accuracy**

| Stroke band | Characters | Total items | All cross | All self | Chaixing cross | Chaixing self | Huiyi cross | Xieyin cross |
|---|---|---|---|---|---|---|---|---|
| 1–4 (low) | 28 | 168 | 28.6% | 39.3% | 39.3% | 58.9% | 26.8% | 19.6% |
| 5–8 (mid) | 48 | 285 | 38.6% | 43.2% | 48.4% | 57.0% | 37.5% | 30.2% |
| ≥ 9 (high) | 24 | 144 | 52.1% | 52.1% | 64.6% | 68.8% | 39.6% | 52.1% |
| High − low range | — | — | +23.5 pp | +12.8 pp | +25.3 pp | +9.9 pp | +12.8 pp | +32.5 pp |

Fisher's exact test over all bands: *p*<sub>all</sub> = 2.6 × 10⁻⁵∗∗∗. The Chinese edition embeds a bar chart for "all cross / Chaixing cross"; the numerical columns above are the values from which it was drawn.

As Table 4 shows, from 1–4 strokes to ≥ 9 strokes the overall cross-blind solve rate jumps from 28.6% to 52.1% (a net gain of +23.5 pp, Fisher's exact *p* = 2.6 × 10⁻⁵); Chaixing cross accuracy climbs from 39.3% to 64.6% (self 68.8%), and Xieyin cross accuracy from 19.6% to 52.1%. On typical high-stroke compound characters — 「想」 (top–bottom: 相 + 心), 「意」 (top–bottom: 音 + 心), 「样」 (left–right: 木 + 羊), 「看」 (semi-enclosure: 手 + 目), 「第」 (top–bottom: 竹 + 弟), 「美」 (top–bottom: 羊 + 大), 「家」 (top–bottom: 宀 + 豕), 「情」 (left–right: 忄 + 青) — the models almost all reach 5/6 or even a perfect 6/6.

**Core finding 1 (symbolic-intersection convergence vs. geometric-transformation divergence).** Why are 11-stroke characters such as 「想、看、第」 extremely easy for LLMs, while 1–4-stroke characters such as 「一、不、为、之、手、无」 are extremely hard? Because LLM riddle solving is essentially a set-intersection operation in the symbolic relation library D̂<sub>θ</sub>: when a clue offers 「木、目、心」 (for 想) or 「竹、弟」 (for 第), the character satisfying the multi-component algebraic intersection S = {c | 木 ∈ c ∧ 目 ∈ c ∧ 心 ∈ c} is unique in the vocabulary. By contrast, low-stroke characters can only be described through 2D continuous geometric transformations such as "drop a dot, add a left-falling stroke, remove a horizontal"; with no visual canvas on which to execute stroke rendering, the search space diverges completely at the symbolic level.

### 4.3 The 2 × 2 × 3 generation–solving asymmetry matrix and model-private decomposition priors

We now test consequence 3 of Core Hypothesis 1 (the law of model-private decomposition isomorphism): if models process characters through a textual decomposition prior D̂<sub>θ</sub>, then when maker and solver are the same model (sharing θ), should a higher fit than cross-model blind testing appear even in a fresh session with memory completely cleared? How is that fit distributed across techniques? Table 5 gives the complete 2 × 2 × 3 stratified results with paired McNemar tests.

**Table 5　Maker × solver × technique 2 × 2 × 3 full-factorial accuracy, paired discordant cells (b, c) and additive effect decomposition**

| Stratum | Maker | n | Cross-blind | Same-item self | Apparent Δ | Cross-only b / self-only c | McNemar *p* |
|---|---|---|---|---|---|---|---|
| All | kimi | 298 | 36.6% (109) | 58.1% (173) | +21.5 pp | b = 7, c = 71 | < 0.0001∗∗∗ |
| All | u2 | 299 | 41.5% (124) | 30.4% (91) | −11.0 pp | b = 53, c = 20 | 0.0001∗∗∗ |
| **All · pooled** | **597** | **39.0% (233)** | **44.2% (264)** | **+5.2 pp** | **b = 60, c = 91** | **0.0144∗** |
| Chaixing | kimi | 98 | 49.0% (48) | 84.7% (83) | +35.7 pp | b = 2, c = 37 | < 0.0001∗∗∗ |
| Chaixing | u2 | 99 | 50.5% (50) | 36.4% (36) | −14.1 pp | b = 21, c = 7 | 0.0125∗ |
| **Chaixing · pooled** | **197** | **49.8% (98)** | **60.4% (119)** | **+10.7 pp** | **b = 23, c = 44** | **0.0139∗** |
| Huiyi | kimi | 100 | 26.0% (26) | 44.0% (44) | +18.0 pp | b = 3, c = 21 | 0.0003∗∗∗ |
| Huiyi | u2 | 100 | 44.0% (44) | 30.0% (30) | −14.0 pp | b = 19, c = 5 | 0.0066∗∗ |
| **Huiyi · pooled** | **200** | **35.0% (70)** | **37.0% (74)** | **+2.0 pp** | **b = 22, c = 26** | **0.6655 (ns)** |
| Xieyin | kimi | 100 | 35.0% (35) | 46.0% (46) | +11.0 pp | b = 2, c = 13 | 0.0074∗∗ |
| Xieyin | u2 | 100 | 30.0% (30) | 25.0% (25) | −5.0 pp | b = 13, c = 8 | 0.3833 (ns) |
| **Xieyin · pooled** | **200** | **32.5% (65)** | **35.5% (71)** | **+3.0 pp** | **b = 15, c = 21** | **0.4050 (ns)** |

**Table 5a　2 × 2 orthogonal additive estimates reported in the right-hand column of the Chinese edition**

| Stratum | Δ̂<sub>solver</sub> (solver-ability main effect) | Δ̂<sub>maker</sub> (item-source main effect) | γ̂ (net self-familiarity effect) |
|---|---|---|---|
| All (N = 597) | +16.3 pp | +11.4 pp | **+5.2 pp∗** |
| Chaixing | +24.9 pp | +23.4 pp | **+10.8 pp∗** (γ̂<sub>Chaixing</sub>) |
| Huiyi | +16.0 pp | −2.0 pp | +2.0 pp (ns) (γ̂<sub>Huiyi</sub>) |
| Xieyin | +8.0 pp | +13.0 pp | +3.0 pp (ns) (γ̂<sub>Xieyin</sub>) |

Table 5 is highly instructive and demonstrates the power of the orthogonal design:

1. Why do kimi (+21.5 pp) and u2 (−11.0 pp) show apparently opposite directions when stratified by maker? As derived in Equations (3)–(6), this is because the overall solving ability of kimi-k3.1-pro exceeds that of u2-flash by Δ̂<sub>solver</sub> = +16.3 pp. When evaluating kimi-made items, switching from cross-blind (solved by the weaker u2, 36.6%) to same-item self-test (solved by the stronger kimi, 58.1%) gives an apparent difference of +Δ̂<sub>solver</sub> + γ̂ = +16.3 + 5.2 = +21.5 pp. Conversely, for u2-made items, switching from cross-blind (strong solver kimi, 41.5%) to self-test (weak solver u2, 30.4%) gives −Δ̂<sub>solver</sub> + γ̂ = −16.3 + 5.2 = −11.1 pp. Both models in fact share the same positive net self-familiarity effect γ̂ = +5.2 pp (discordant cells 60 vs. 91, exact McNemar *p* = 0.0144).
2. The net self-familiarity effect is highly concentrated in Chaixing (γ̂<sub>Chaixing</sub> = +10.8 pp, *p* = 0.0139). Solving γ̂ separately for each technique reveals a decisive divergence: on Huiyi, which relies on open semantic association, γ̂<sub>Huiyi</sub> = +2.0 pp (*p* = 0.6655, wholly non-significant); on Xieyin, based on phonetic puns, γ̂<sub>Xieyin</sub> = +3.0 pp (*p* = 0.4050, wholly non-significant); only on Chaixing, based on glyph-component decomposition, is the net self-advantage as large as γ̂<sub>Chaixing</sub> = +10.8 pp (*p* = 0.0139), with kimi's accuracy on its own Chaixing riddles surging from 49.0% cross to a striking 84.7% (83 of 98 items correct; only 2 cross-only correct vs. 37 self-only correct, *p* < 10⁻⁸).

Why does Chaixing alone exhibit such strong model self-isomorphism? This directly confirms our theoretical hypothesis: Huiyi and Xieyin are many-to-many divergent semantic / homophonic mappings (the syllable *yī*, for instance, has dozens of homophones, so even one's own riddle faces enormous homophone ambiguity during inverse decoding), whereas Chaixing is an algebraic operation over the model's internal discrete decomposition-rule library D̂<sub>θ</sub>. Each model develops, during pretraining, its own preferred component segmentation and metaphorical references (for example, habitually decomposing 「丁」 as "a horizontal plus a vertical hook", or habitually referring to a radical with a particular phrase). When the same parameter set θ performs inverse solving in a new session, forward encoding and inverse decoding achieve exact symbolic alignment.

### 4.4 A micro-taxonomy of sub-character spatial blindness and component hallucination (44 convergent-error cases and typical traces)

Across the two independent answer sessions on the 597 riddles, the two models' conclusions agreed (both correct or both wrong) on 74.7% (446/597) of items, and gave exactly the same single-character answer on 36.3% (217/597). Most remarkably, among the 273 items answered incorrectly in both sessions, 44 (16.1%) were cases where two different models, in independent blind testing and self-testing, produced *exactly the same wrong character* (**convergent misdirection**). Comparing these 44 convergent-error samples and typical failure traces item by item, we reduce the "character-vision blindness" of LLMs to the five cognitive pathologies listed in Table 6 (seven illustrative cases are tabulated in the Chinese original).

**Table 6　Five micro-pathologies of sub-character spatial blindness and symbolic hallucination, with experimental evidence (from real traces in `data.json`)**

| Blindness / hallucination type | Sample GID / answer | Maker / technique | Wrong answers (cross / self) | Clue, maker glyph reasoning and dual-model pathology |
|---|---|---|---|---|
| 1. Coordinate-free bag-of-components (Bag-of-Components) | `19c088e21c2c` / 为 | kimi / Chaixing | u2: 办; kimi: 办 | Clue: 「有力添两点」 ("add two dots to 力"). The maker knows 为 contains 力 and two dots (upper-left, lower-right) but ignores 2D coordinates; when solving, both models decode the high-frequency left–right symmetric layout as 办. |
| 2. Spatial-topology boundary confusion (LR vs. Surround) | `795c30b6ac7f` / 们 | u2 / Chaixing | u2: 闪; kimi: 闪 | Clue: 「门口站个人」 ("a person stands at the gate"). The maker intends a left–right structure (亻 + 门 = 们), but the natural phrase 「门口」 activates an enclosing operator (a person *inside* the gate), so both models answer 闪. |
| 3. Indecomposable stroke-geometry blindness (2D Stroke Blindness) | `d5c4f5dc2311` / 不 | kimi / Chaixing | u2: 仃; kimi: 才 | Clue: 「下字丢了点，左边添一撇」 ("下 loses its dot, a left-falling stroke is added on the left"). The models cannot perceive, on a 2D canvas, the geometric relation between 下-minus-dot-plus-left-falling and 不, and algebraically assemble 仃 and 才 instead. |
| 4. Maker-side component hallucination (Maker Glyph Halluc.) | `8010577fb10f` / 事 | u2 / Chaixing | kimi: 搰; u2: 挖 | Clue: 「一口古井横山前，手旁垂钓待月圆」. While making the riddle, u2 hallucinates the lower 彐+亅 of 事 as the hand radical 扌, inducing the solver to synthesise 搰 / 挖. |
| 5. Maker-side fabricated radical (Fabricated Radical) | `f31e5f76aaf1` / 以 | u2 / Chaixing | kimi: 佃; u2: 佃 | Clue: 「人前自有一口田」. While making the riddle, u2 falsely claims that the right part 厶 of 以 resembles a cornerless 田 with 口 at the right centre; both models then apply standard left–right algebra (亻 + 田) and answer 佃. |
| 6. Solver-side illegal character synthesis (Illegal IDS Synthesis) | `f844df905356` / 中 | u2 / Xieyin | u2: 诗; kimi: 中 (correct) | Clue: 「古寺钟声传耳边」. In its self-test u2 derives 寺 and the phonetic 中 from 钟, then openly fabricates a glyph: "'寺' plus '中' makes '诗', and '诗' indeed has the structure 寺 + 中". |
| 7. Over-composition hallucination (Over-Composition) | `a488db54ac70` / 么 | u2 / Chaixing | u2: 秘; kimi: 么 (correct) | Clue: 「私右添一撇」. u2 correctly works out that the right side of 私 is 厶 and that adding a left-falling stroke yields 么, but refuses to stop at an indecomposable character, reattaches the left 禾 and falsely claims "禾 + 么 makes 秘". |

The empirical cases in Table 6 provide irrefutable micro-level evidence for "blind men touching characters":

- **Bag-of-components without coordinates.** For `gid=19c088e21c2c` (answer 为) and `gid=812d2b4f0baf` (answer 为, clue 「一点落力巧相助」), both kimi and u2 reflexively map the component set {力, dot} to the high-frequency compound character 办 as soon as they see it, entirely unable to distinguish the 2D geometric difference between dots at upper-left / lower-right (为) and dots on the left and right sides (办).
- **Bidirectional component hallucination in making and solving.** For characters such as 事 (`8010577fb10f`) or 以 (`f31e5f76aaf1`) that do not fit standard left–right / top–bottom radical templates, models fabricate non-existent radicals already at the making end (claiming 事 has the hand radical 扌, or 以 has 口 and 田). At the solving end, when a derived component combination ({寺, 中} or {禾, 么}) cannot be assembled into a real character, the absence of a visual buffer for glyph checking leads them to call a deer a horse, asserting 「寺+中=诗」 (forcing the speech radical 讠 to equal 中) or 「禾+么=秘」 (forcing 必 to equal 么).

---

## 5 Diagnosing riddle-solving CoT degeneration and a verifiable-reward training framework

Beyond serving as a cognitive probe, the second central concern of this experiment is whether the reasoning process of riddle solving resembles a chain of thought, and what its success and failure modes imply for reasoning training in LLMs. We quantitatively analyse 1,194 solving traces and 1,023 post-hoc explanations of the reference set.

### 5.1 The "overthinking paradox" and early-hit self-sabotage

In mathematical and code reasoning, increasing test-time compute (a longer CoT) usually raises accuracy. On the Chinese character riddle task we observe a strong **overthinking paradox**: as Table 7 shows, in both cross-blind and same-item self-testing, and for both kimi-k3.1-pro and u2-flash, the mean output token count on wrong answers is 2.3–3.3 times that on correct ones.

**Table 7　The inverse CoT-length law and stratified statistics of early-hit self-sabotage**

| Evaluation mode | Solver | Correct n | Mean tokens | Median | Wrong n | Mean tokens | Median | Traces that had reached the correct answer and then overturned it (share) |
|---|---|---|---|---|---|---|---|---|
| Cross-blind (11-05 Cross) | kimi-k3.1-pro | 124 | 306.8 | 163.5 | 175 | 734.1 (2.4×) | 486.0 | 45 / 175 (25.7%; Chaixing 38.8%) |
| Cross-blind (11-05 Cross) | u2-flash | 109 | 142.2 | 81.0 | 189 | 372.2 (2.6×) | 213.0 | 41 / 189 (21.7%) |
| Same-item self-test (11-06 Self) | kimi-k3.1-pro | 173 | 183.5 | 137.0 | 125 | 489.7 (2.7×) | 358.0 | 21 / 125 (16.8%) |
| Same-item self-test (11-06 Self) | u2-flash | 91 | 206.6 | 112.0 | 208 | 684.0 (3.3×) | 306.5 | 44 / 208 (21.2%) |

Why are longer chains more likely to be wrong? Automatic matching and manual review of the CoT text of every wrong answer uncovered a crucial phenomenon — **early-hit self-sabotage**:

- Among the 364 cross-blind errors, 86 (as many as 23.6%) had already derived the standard answer character explicitly, in quotation marks, within the chain of thought (in 46 of them the answer was hit within the first 120 characters!); among the 49 Chaixing items kimi got wrong, this self-overturn rate reaches 38.8% (19/49).
- **Typical degeneration traces.**
  - **Case A** (`gid=aebd4ed8d989`, answer 一, clue 「大字少人独自横」): in its very first reasoning sentence u2 writes, "'大' minus '人' (i.e. remove the left- and right-falling strokes) leaves '一', and '独自横' emphasises the horizontal stroke." Immediately afterwards the model triggers a **compound-character complexity prior bias**: "But '一' is already a character … riddle answers are mostly compound … but '一' is too simple … more reasonable: '大' minus '人' leaves '一' and '一'? But the usual answer is '个'? Or perhaps '天'?" After 478 tokens of repeated vacillation, the raw JSON is truncated by the generation window (24 such dead-loop truncations occurred across the full blind test and self-test).
  - **Case B** (`gid=2c5944b955ef`, answer 个, clue 「哥哥立于人前，中间隔根棍」): kimi has already computed in its native thinking chain that "哥哥 is reinterpreted as 个个, and a vertical stroke before 人 forms 个", but then over-elaborates: "two 个 side by side combine into 竹", finally outputting the wrong answer 竹.
  - **Case C** (`gid=e04c3af35faf`, answer 只, clue 「与知同音，归在口部」): both models recognise the reading *zhī* and the radical 口, but because they tend to treat "some radical + some pronunciation" as the formula for a phono-semantic compound, both ignore the basic character 只 and converge on 吱 (convergent misdirection).

**Core finding 2 (sub-character CoT lacks a stopping criterion and a visual verifier).** In mathematical or code CoT, intermediate steps are hard-constrained by formal logic or grammar. In text-only riddle CoT, however, the model has neither a "2D glyph renderer" to check whether the assembled character really exists nor freedom from a strong prior that "a riddle must contain a second compositional trick". With no external symbolic stopping criterion, extending the CoT merely induces over-composition (changing 一 into 天, combining 个 into 竹, or 中 into 串).

### 5.2 Post-hoc rationalisation hallucination: why ready-made riddle collections cannot be distilled into CoT directly

If simply extending free CoT degenerates, could we follow multilingual puzzle research [12] and let an LLM auto-complete a CoT explanation given a (clue *q*, answer *c*) pair, then fine-tune a smaller model on those explanations? Our explanation-generation experiment on the 1,050 reference clues gives a clear negative warning:

1. **Post-hoc forced rationalisation as high as 58.9%.** After excluding the 27 site-native explanations, of the 1,023 explanations generated by models given the answer, 58.9% (602/1,023) were self-rated `low` confidence (only 421 were `high`). For example, for the reference clue 「矢下之广，大有人在」 (answer 一; the original intent is subtractive character splitting — 「大有人在」 means 大 contains 人, 「矢下之广」 refers to the illness radical minus 矢, and other complex separations), a model unaware of the splitting logic fabricates a Huiyi explanation: "The region below the arrow is broad and there are many people; a crowd gathering can be extended to mean unity, returning to one, which fits 一."
2. **Severe technique-classification drift.** Among the model's classifications of the 1,023 reference clues, 594 (58.1%) were labelled Huiyi, 427 (41.7%) Chaixing, and only 2 (0.2%) Xieyin. This shows that when a model cannot understand the underlying glyph arithmetic or dialect homophones, it defaults to Huiyi, the category most easily smoothed over in natural language. Training a model on pseudo-CoT full of post-hoc rationalisation would not improve glyph perception; it would aggravate confabulation.

### 5.3 From probe to training: Decomposed Orthographic CoT and the RiddlePlay self-play RLVR framework

On the basis of these diagnoses we answer our second central question: **how can riddles genuinely improve sub-character perception and constrained reasoning in LLMs?** We propose **RiddlePlay**, a neuro-symbolic co-training architecture requiring no human annotation (Table 8).

**Table 8　RiddlePlay: a riddle self-play training architecture anchored in verifiable orthographic rewards (RLVR) and symbolic IDS trees**

| Stage | Formal input / output and operators | Repair mechanism for the pathologies diagnosed here |
|---|---|---|
| Stage 1: Symbolically anchored riddle maker | Input: character card C(c) = ⟨IDS(c), S(c), Pinyin(c), Pos2D(c)⟩ and technique t ∈ {Chaixing, Huiyi, Xieyin}; output (q, τ<sub>make</sub>) | Inject explicit 2D position descriptors Pos2D(c) (distinguishing upper-left / lower-right dots from left / right dots), eliminating coordinate-free making ambiguity such as 为/办 and 们/闪 at the source |
| Stage 2: Fourfold symbolic gatekeeper | V<sub>gate</sub> = I<sub>legal</sub> · I<sub>Jaccard<0.35</sub> · I<sub>IDS</sub>(τ<sub>make</sub>, c) | Reuse the validated 0% answer-leak interception, 3-gram originality filter (< 0.35) and hard IDS subtree-inclusion check to remove 100% of making hallucinations such as "事 contains 扌" or "以 contains 田" |
| Stage 3: Decomposed Orthographic CoT | Force the solving trace into four steps: τ<sub>solve</sub> = ⟨clue segmentation, technique identification, IDS algebraic equation, vocabulary-legality early stop⟩ | Introduce an explicit IDS lookup operator T⁻¹<sub>IDS</sub>(ω, c₁, c₂) at step 3: once a unique legal character is hit (e.g. 大 − 人 = 一), trigger early stopping, eliminating the 23.6% early-hit overturn and illegal character synthesis (e.g. 寺 + 中 = 诗) |
| Stage 4: Double-blind verifiable reward | R = w₁ I[ĉ<sub>self</sub> = c] + w₂ I[ĉ<sub>cross</sub> = c] − λ max(0, ‖τ<sub>solve</sub>‖ − L₀) | Combine exact matching in same-item self-test and cross-model blind test as an objective binary reward (RLVR), and apply an over-long-CoT penalty −λΔL to suppress unanchored divergent overthinking |

In the **RiddlePlay** framework we no longer use post-hoc pseudo-explanations, but exploit the **generation–solving bidirectional symmetry** validated in this experiment: the reasoning chain τ<sub>make</sub> generated forward by the maker under the constraint of a real IDS tree T<sub>IDS</sub>(c), once filtered by the fourfold gatekeeper and solved correctly in blind testing, yields by inverse rewriting a **hallucination-free, symbolically verified golden solving CoT (Verified Orthographic CoT)**. Extending this pipeline to the 3,500 common characters of the *Table of General Standard Chinese Characters* would synthesise tens of thousands of contamination-free RL trajectories at zero human-labelling cost, directly benefiting Chinese spell checking (CSC) [4], robustness against glyph-decomposition attacks (e.g. SinoGlyphBench [9]) and multi-constraint symbolic reasoning tasks.

---

## 6 Discussion, limitations and future extensions

To ensure scientific rigour we disclose the boundary conditions of the experimental design and plan extensions accordingly:

1. **Sampling variance and non-contextual weight familiarity.** Although the cross-blind test of 11-05 and the same-item self-test of 11-06 strictly guarantee single-turn, history-free conversations with identical prompts and scoring, both are single samples (Pass@1), and some server-side APIs (e.g. K3) do not support explicitly locking temperature / top_p. Future work will introduce repeated sampling (Pass@k and Majority Voting @ 8) and extend the 2 × 2 matrix into an N × N cross-model-family matrix covering Qwen, DeepSeek, GPT-4o and Claude.
2. **The blank meaning field constrains Huiyi.** In this `v0.2-full100` experiment the character card does not yet contain authoritative dictionary senses (`meaning = null`), which limits the richness of Huiyi to some degree. Once senses from the *Modern Chinese Dictionary* and 2D component coordinates (bounding boxes in [0, 1]²) are added in a later version, we can quantify how much explicit spatial-coordinate injection improves accuracy on indecomposable characters.
3. **A direct contest between text-only LLMs and multimodal MLLMs.** If text-only LLMs become "blind men touching characters" for lack of G<sub>2D</sub>(c), can rendering candidate characters or whole sentences as images and feeding them to multimodal LLMs (MLLMs) or pixel language models [7, 8] eliminate the counter-intuitive stroke gradient and the indecomposable-character fault line? This constitutes a highly valuable cross-modal cognitive control experiment.

---

## 7 Conclusion

Moving beyond the traditional framing of Chinese character riddles as static QA scoring, this paper is the first to argue systematically for the dual scientific value of riddles as a sub-character cognitive probe and as a verifiable reasoning training ground, on the basis of full-coverage controlled generation over 100 modern Chinese characters (597 items) and paired double-blind evaluation (1,194 reasoning traces). We show that contemporary text-only LLMs do not "see" characters in a 2D geometric space as humans do; they are "blind men touching characters" relying on 1D symbolic component algebra acquired from pretraining corpora. They perform effortlessly on left–right / top–bottom compound characters and high-stroke multi-component characters (Chaixing accuracy 59%–85%), and display highly significant isomorphism of private decomposition priors in same-model self-testing (γ̂<sub>Chaixing</sub> = +10.8 pp, *p* = 0.0139). Yet as soon as they face indecomposable characters (accuracy halved to 22.4%, *p* = 2.0 × 10⁻⁶) or 2D position distinctions (为/办, 们/闪), their 2D spatial blindness and component hallucination are laid bare. At the same time, the 23.6% early-hit self-sabotage rate in riddle CoT and the 2.3–3.3× token inflation on wrong answers show that free CoT without a symbolic verifier readily degenerates into an over-composition dead loop. By introducing the IDS symbolic-tree verification and the **RiddlePlay** self-play RLVR paradigm proposed here, Chinese character riddles promise to become an ideal bridge between low-level sub-character perception and high-level symbolic logical reasoning.

---

## References

[1] Chuanqi Tan, Furu Wei, Li Dong, Weifeng Lv, and Ming Zhou. 2016. Solving and Generating Chinese Character Riddles. In Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 846–855.

[2] ZGP / Jingjing Xu et al. 2022. CC-Riddle: A Question Answering Dataset of Chinese Character Riddles. arXiv preprint arXiv:2206.13778 (GitHub Repository).

[3] Zijun Sun, Xiaoya Li, Xiaofei Sun, Yuxian Meng, Xiang Ao, Qing He, Fei Wu, and Jiwei Li. 2021. ChineseBERT: Chinese Pretraining Enhanced by Glyph and Pinyin Information. In Proceedings of ACL 2021 (arXiv:2106.16038).

[4] Yinghui Li et al. 2022. Investigating Glyph-Phonetic Information for Chinese Spell Checking: What Works and What's Next?. arXiv preprint arXiv:2212.04068.

[5] Chenglei Si, Zhengyan Zhang, Yingfa Chen, Fanchao Qi, Xiaozhi Wang, Zhiyuan Liu, Yasheng Wang, Qun Liu, and Maosong Sun. 2023. Sub-Character Tokenization for Chinese Pretrained Language Models. Transactions of the Association for Computational Linguistics (TACL), 11:469–487.

[6] N. Author et al. 2025. Tokenization Changes Meaning in Large Language Models: Evidence from Chinese. Computational Linguistics, 51(3):785–812, MIT Press.

[7] Controlled Modality Study Group. 2026. Full Glyph Images Beat Token Embeddings: A Controlled Study for Chinese Language Modeling. arXiv preprint arXiv:2607.03994.

[8] PixelLM Research Team. 2026. MIXAR: Scaling Autoregressive Pixel-based Language Models to Multilingual and CJK Scripts. arXiv preprint arXiv:2604.11575v2.

[9] Shun Feng et al. 2026. SinoGlyphBench: A Diagnostic Benchmark for Chinese Glyph-Level Obfuscation in LLM and MLLM Moderation. In Findings of the Association for Computational Linguistics: EMNLP 2026 (arXiv:2609.05843).

[10] Panagiotis Giadikiaroglou et al. 2024. Puzzle Solving using Reasoning of Large Language Models: A Survey. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 11574–11591.

[11] Multilingual Riddle Generation Group. 2025. Adaptive Prompting for Multilingual Riddle Generation in LLMs. arXiv preprint arXiv:2508.18709v2.

[12] S. Saxena et al. 2025. Can LLMs Solve My Grandma's Riddle? Evaluating Multilingual and Culturally Grounded Riddle Reasoning. arXiv preprint arXiv:2512.20324.

[13] X-Riddles Authors. 2026. Can LLMs Understand and Generate Chinese Xiehouyu Riddles?. arXiv preprint arXiv:2607.23440.

[14] Formal Reasoning Probe Team. 2026. X-RAY: Mapping LLM Reasoning Capability via Formalized and Calibrated Probes. arXiv preprint arXiv:2603.05290.

[15] Spatial Probing Group. 2025. Stuck in the Matrix: Probing Spatial Reasoning in Large Language Models. arXiv preprint arXiv:2510.20198.

[16] Structure-Aware Reasoning Group. 2025. Exploring the Role of Reasoning Structures for Constructing Proofs with Large Language Models. arXiv preprint arXiv:2410.08436v2.

[17] Reasoning Alignment Group. 2026. Probing the Misaligned Thinking Process of Language Models. arXiv preprint arXiv:2606.24251v1.

---

## Editorial notes (not part of the original paper)

1. **Authorship.** The Chinese original is signed by the Computational Linguistics and LLM Cognitive Diagnostics Research Group (计算语言学与大模型认知诊断课题组). This differs from the corporate author of the companion dataset, Spring Buds Data Source Inc. (春芽数源). The translation does not alter, reassign or extend the authorship of the original. The Chinese original states a dataset licence (CC BY-NC-SA 4.0) but does not state a licence for the paper text itself; accordingly the repository-wide `paper/` CC BY 4.0 notice applies only to the dataset's own first paper, and this edition is provided for reference alongside the dataset. Reuse beyond reading requires the original author's permission.
2. **Counting conventions.** The values 1,050 reference clues, 1,050 explanations and 1,023 model-generated explanations are *build-time* counts from the local research tree, reproduced verbatim as the author reports them. The public CCRP DataSet v0.1 release withholds 31 web-UGC clues and their bound explanations under scheme C, so the published counts are 1,019 / 1,019. No number in the translated paper has been changed; see `paper/riddle-paper.md` §3.4 and `data/WITHHELD.md` in the repository.
3. **Relationship between the two papers.** This is the second paper associated with CCRP DataSet v0.1. The first, *Can Chinese Character Riddles Serve as Structural Probes for Large Language Models?* (`riddle-paper{,-en}.md`), adjudicates the validity of riddles as a structural probe; the present paper uses the same 597-item closed loop to characterise 1D symbolic algebra, 2D spatial blindness and CoT degeneration. They are independent works with different authors and different conclusions; neither supersedes the other.
4. **Bibliographic caution.** The 17 references are reproduced exactly as printed in the Chinese edition. Several carry generic group attributions (e.g. "N. Author et al.") or arXiv identifiers dated 2026 that could not be verified during translation. They are retained verbatim rather than corrected or supplemented, in keeping with the project's rule never to fabricate URLs or DOIs. Readers should verify them against primary sources before citing.
5. **Chinese original.** The Chinese PDF is archived in this repository as `gmn-paper-zh.pdf` for side-by-side verification. Both editions were checked against the 31 withheld web-UGC clue texts: neither contains any of them, nor any web URL or local absolute path.

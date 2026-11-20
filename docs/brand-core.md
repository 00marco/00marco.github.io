# LivingNotes Brand Core

**Status:** Leading branding reference  
**Recorded:** November 18, 2026  
**Last revised:** November 19, 2026

This document defines the current brand direction for LivingNotes. It guides positioning, marketing, voice, product communication, and future App Store and website work. It does not replace the product principles, which continue to guide product decisions.

## Brand foundation

### Purpose

Help one person develop a long-term understanding of subjects too large—and too numerous—to understand all at once.

### Brand promise

> **Some thoughts need time.**

### Core belief

> Large subjects are understood through repeated encounters, reflection, and revision—not necessarily in one sitting.

Understanding does not come from passive waiting alone. It develops when someone returns to their own observations, notices what has changed, revises what no longer fits, and gradually makes the larger subject familiar.

The difficulty is not only that one worthwhile subject can exceed a single sitting. A person may also care about more substantial subjects than they can actively hold in attention at the same time. A useful system must therefore preserve continuity while attention moves elsewhere.

### Positioning

LivingNotes is a place for personal thoughts about subjects too large to understand all at once, especially when several of those subjects compete for limited time and attention.

It is designed for long-horizon, self-directed sensemaking. A user can capture a small piece of thought, set it aside while attention moves elsewhere, and return across days, months, or longer without starting over.

LivingNotes does not attempt to become the surface on which all thinking happens. It preserves continuity between deeper encounters with a subject.

### Product role

LivingNotes supports a person's own thinking rather than producing conclusions, summaries, or answers for them. Its role is to hold unfinished observations, questions, interpretations, and working conclusions until the person is ready to encounter them again.

This is a product principle first and a selective public message second. LivingNotes should support independent thought without defining itself broadly as anti-AI.

### Low-tech usefulness

LivingNotes should be as technically modest as possible while remaining meaningfully more useful than pen and paper.

The product should prefer simple, deterministic, device-side behavior over semantic analysis, content classification, generated recommendations, or continuous remote computation. This reduces operational cost, limits unnecessary infrastructure and energy use, preserves privacy, and keeps the product understandable.

The aspiration is to provide a substantial upgrade to a personal paper-note system without turning every note into input for a data-center service.

This is an engineering and product constraint, not a quantified environmental claim. LivingNotes should not advertise a measured carbon advantage unless that advantage is independently assessed.

LivingNotes does not need to understand what a note means. A note may be a refined insight, an unresolved fragment, gibberish, a grocery list, or something meaningful only to its author. The app should remain useful without inspecting or judging the content.

### Audience

LivingNotes is for people trying to understand something substantial by themselves over time. They may be reading, researching, building, reflecting, or exploring without a class, team, or prescribed sequence telling them what to think next.

They prefer to form their own understanding from repeated contact with the material rather than outsource interpretation or force the whole subject into one intensive session.

They may also have several unfinished subjects competing for attention. LivingNotes should help them preserve the thread of each subject without implying that every subject must remain active, current, or equally important.

## Core use cases

LivingNotes is suited to long-running personal efforts such as:

- Reading and making sense of a large or dense book
- Becoming familiar with an unfamiliar codebase
- Developing an understanding of a broad field, system, or topic
- Reflecting on a difficult question, experience, or period of life
- Thinking through the meaning and context of a large project without managing the project itself
- Preserving unresolved observations that need more time or experience before they can be integrated

The user does not need to finish understanding the subject today. LivingNotes gives small pieces of thought somewhere to wait without losing their connection to the larger effort.

## The problem

### Large subjects exceed a single sitting

Some subjects cannot be understood linearly or held in working memory all at once. They require time away, repeated encounters, changing perspectives, and opportunities to reconsider earlier conclusions.

Traditional note archives preserve information, but preservation alone does not maintain a person's relationship with it. A saved item can remain technically available while its context, urgency, and felt relevance fade.

### There are more worthwhile subjects than available attention

Even when each subject is divided into manageable pieces, a person may still care about more subjects than they can actively revisit. Time spent with one necessarily means setting others aside.

This creates a second problem beyond complexity: continuity has to survive competition. A subject should be able to leave the foreground without becoming an anonymous pile of saved material when the person returns.

LivingNotes should not promise to keep everything equally fresh or encourage endless accumulation. It should make it practical to pause, resume, reconsider, and sometimes let go. Its structure and return mechanisms exist to preserve enough context that attention can move without every return becoming a restart.

The durable principle is:

> Preserve the thread while attention moves elsewhere.

### Saved but not meaningfully revisited

Research in personal information management supports the broader revisitation problem: people save web pages and bookmarks for later, yet bookmarks are often not the method through which those pages are eventually recovered. Research also treats the reconstruction of past sensemaking context as a distinct design problem.

The evidence does **not** establish that lost interest is always the cause. LivingNotes therefore treats the following as a product hypothesis rather than a settled fact:

> Small amounts of change and novelty may help revive the context, curiosity, and unfinished feeling attached to something a person previously cared about.

LivingNotes should continue testing this hypothesis. The current mechanics are attempts, not final answers.

### Attention compression, not notification accumulation

A large personal collection can contain hundreds of items that could individually ask for attention. Turning each one into a reminder, badge, or push notification would reproduce the same overload LivingNotes is meant to reduce.

LivingNotes should instead compress many note-level changes into a small number of persistent visual signals. Plant yellowing, section state, and other garden-level cues let a user notice that something has changed without receiving a separate interruption for every affected note.

The garden is therefore functional information design, not merely decoration. It should help a person scan the condition of a large collection, choose where to look, and ignore the rest until they have capacity.

The durable principle is:

> Summarize demands on attention; do not multiply them.

Push notifications should not be the default return mechanism. When notifications are used at all, they should remain sparse, optional, and subordinate to the calmer visual state inside the app.

Decay and the plant overview must be explained together. Decay creates small reasons to return, while plant yellowing combines those reasons into a readable visual summary. One mechanism introduces attention; the other prevents that attention from becoming another inbox.

The intended sequence is:

1. A note accumulates visible decay.
2. Its plant gradually reflects that condition.
3. The user decides whether and when to inspect it.

The plant is not a warning that every affected note must be repaired. It is a compact representation of accumulated change that leaves prioritization with the user.

### Research references

- [Out of sight and out of mind: Bookmarks are created but not used](https://doi.org/10.1177/0961000620949652) — a study of bookmark retrieval behavior in which only a minority of bookmarked targets were retrieved through the bookmark facility.
- [From Tabs to Structures: Understanding and Supporting Web Page Management](https://doi.org/10.1145/3772318.3791979) — CHI 2026 research on evolving personal web-information structures, uncertainty, maintenance, and revisitation.
- [IRCHIVER: An Information-Centric Personal Web Archive for Revisiting Past Online Sensemaking Tasks](https://doi.org/10.1145/3698204.3716459) — research focused on revisiting consumed information and reconstructing earlier mental models and sensemaking contexts.

## Product form and device continuity

### Mobile-friendly by design

LivingNotes is designed for quick capture and short encounters on a phone. A small note can be written or revisited without reopening an entire research environment or recreating a previous thinking session.

The phone is not presented as the ideal place for every kind of deep work. Its role is to keep continuity with the subject during the ordinary moments between deeper sessions.

### Return on a larger screen

iCloud synchronization lets the same garden continue across iPhone, iPad, and Mac. A thought captured or briefly revisited on mobile can later be read, revised, and considered on a larger screen.

Device continuity supports the long time horizon: the user can encounter the same subject in different contexts without rebuilding the collection or transferring notes manually.

### What LivingNotes is not

LivingNotes is not:

- A collaborative whiteboard
- A freeform diagramming or real-time thinking surface
- A project-management system
- A complete source repository or permanent research archive
- A flashcard system or guarantee of memorization
- A substitute for reading, research, experimentation, or deeper thinking sessions
- A system that generates the user's understanding for them
- A semantic engine that profiles note contents or recommends what the user should think about next
- A data-center-dependent terminal that requires remote intelligence to make ordinary notes useful

Its role is smaller and more specific: help a person preserve and renew their relationship with something they are still understanding.

## Experimental return mechanisms

Decay, repair, structural pressure, connections, and conditions are current experiments for making a return feel slightly different from the last encounter.

Their purpose is to:

- Interrupt the stagnant feeling of reopening an unchanged archive
- Give the user a small reason to inspect an older note again
- Make revision and curation feel more tactile and playful
- Create gentle variation without requiring a competitive or daily practice
- Surface accumulated change through a few visual cues instead of repeated notifications

These mechanics are not the permanent brand essence. Their rules, presentation, balance, and even their continued existence may change as LivingNotes learns what actually helps people return to difficult subjects.

The invariant beneath the experiments is:

> LivingNotes should give people reasons to renew their relationship with subjects they are still understanding.

Mechanics must not imply that novelty alone creates understanding. The user still has to read, reflect, revise, connect, and decide what the subject means.

### Low-friction repair

Responding to decay should remain deliberately lightweight. Repair is not a quiz, comprehension test, overdue task, or required review session. The user presses and holds a changed character and waits briefly for it to clear.

This interaction creates a small pause in which the surrounding note becomes visible again. A user may repair several characters over coffee, between other activities, or as an alternative to opening an endless feed. The product should allow this to feel focused or meditative without promising meditation, learning, or insight as an automatic result.

The durable interaction principle is:

> Make returning easy enough to begin, then let the writing earn further attention.

Repair should never require the user to prove recall, answer a question, or complete every available item. Its role is to lower the activation energy of revisitation while leaving deeper reading and revision optional.

### User-authored connections

User-authored connections let a person relate two plants without asking the app to infer meaning or inspect either plant's notes. The user decides whether a relationship exists and describes what it means.

Connections should help a large structure remain legible without becoming a dense graph or another source of visual noise. Their purpose is organization and synthesis, not reward farming.

The durable principle is more important than the reward design:

> Prompt the user to create meaning; do not generate the meaning for them.

## Emotional direction

### Primary outcome: long-term personal understanding

The main goal is gradual familiarity with large subjects through repeated, self-directed encounters. LivingNotes should help the user recognize where they have been, notice what has changed, and build a personal understanding that remains their own—even when other subjects occupy their attention between visits.

### Secondary feeling: relief

Relief comes from knowing the subject does not have to be resolved now. A user can put down an unfinished thought without losing the thread and return when they have the attention, experience, or emotional capacity to continue.

It also comes from accepting that not every worthwhile subject can remain active at once. LivingNotes should make setting something aside feel recoverable without turning the collection into a queue of obligations.

LivingNotes should never turn this reassurance into a maintenance obligation.

### Supporting feeling: curiosity

Playful changes can make an old note feel slightly new. Curiosity should encourage another look without creating anxiety, urgency, or fear of falling behind.

### Interaction quality: an unhurried pause

Clearing decay should feel tactile, patient, and low pressure. The press-and-hold interaction gives the user something small to do while encountering older writing again. It can occupy a spare moment without turning that moment into a test or productivity session.

### Personality: Quiet Discovery

LivingNotes is quiet, thoughtful, unusual, patient, and lightly playful. It respects the seriousness of the subject while acknowledging that returning can benefit from surprise and texture.

## Visual and verbal identity

### Visual identity

The garden represents a subject that remains alive across time. Plants, growth stages, changing colors, connections, and condition icons provide continuity and visible change without pretending to map every conceptual relationship.

The garden is a recognizable personal landscape, not a whiteboard or literal diagram of the user's knowledge.

LivingNotes deliberately bends the design of the entire app around this familiar metaphor. Sections organize plants, plants hold related notes, growth reflects continued investment, and changing leaves summarize accumulated decay. These relationships create one visual language that can carry unfamiliar mechanics across the product.

The metaphor is functional onboarding. People already understand that plants grow, change, and sometimes need attention, so a novel return mechanic can feel legible before every rule is explained. LivingNotes should use that familiarity to reduce the need for dashboards, terminology, alerts, and lengthy tutorials.

The durable principle is:

> Use a familiar metaphor to make unfamiliar behavior understandable.

The metaphor must remain internally consistent and must not misrepresent what happens to the user's data. A changing plant may invite attention, but it must never imply that the underlying writing has been deleted, corrupted, or placed in danger.

It also acts as an attention-compression layer. A plant can summarize the condition of many notes, allowing hundreds of possible note-level alerts to become a readable overview. Yellowing should communicate that something may deserve another look without implying an emergency or demanding immediate action.

### Verbal style

Copy should be direct, calm, patient, and concise. Use garden language selectively. Avoid claims of mastery, guaranteed memorization, effortless understanding, or automatic intellectual progress.

### Game language

Show decay, repair, trophies, upgrades, and conditions without positioning LivingNotes as a deck builder, strategy game, productivity scoreboard, or generic gamified notes app.

Describe the purpose of the mechanics: they provide small reasons to return and reconsider.

Use **conditions**, **effects**, and **discoveries** in public copy rather than the more technical term **status effects**.

### Decay vocabulary

Use softer language such as *change*, *rest*, *return*, and *revisit* in broad marketing. Use the explicit word *decay* when explaining the actual mechanic, paired with the facts that it is repairable and stored writing remains safe.

Decay must be described accurately as a display effect: it changes how certain characters appear but does not delete or corrupt the underlying writing.

## Trust contract

- Stored writing is never silently deleted.
- A user may set a subject aside without being told they failed.
- Decay and conditions invite attention rather than demand it.
- The app summarizes changes visually instead of producing a notification for every item that could use attention.
- There are no streaks, overdue thoughts, or competitive rankings.
- Returning is valuable because the user reflects and revises, not because the app claims that repetition automatically creates understanding.
- Experimental mechanics may change, but the user's writing and the core purpose remain stable.
- The app supports independent thought rather than replacing it with generated interpretation.
- A phone encounter may preserve continuity, but it does not replace deeper work when deeper work is needed.
- Notes do not need to be semantically analyzed, categorized, or understood by LivingNotes to remain useful.
- Ordinary writing and return mechanics should not depend on remote inference services.

## Messaging framework

### Primary message

> Some thoughts need time.

### Supporting explanation

> LivingNotes is a mobile-friendly place for things you are still understanding. Set aside small pieces of thought while attention moves elsewhere, then return without starting over.

### Problem message

> Big subjects take more than one sitting, and there are often too many of them competing for attention. Saving pieces is easy; preserving enough context to return is harder.

### Product-role message

> LivingNotes holds your unfinished observations and brings you back to them. It gives your thinking continuity without trying to do the thinking for you.

### Mechanism message

> Saved notes are easy to stop noticing. Decay is an evolving attempt to bring some of them back into view, while the garden summarizes many changes without overwhelming the user with notifications.

### Repair message

> Returning does not require a test or a review session. Press and hold a changed character to clear it, then decide whether the note deserves a closer look.

### Relief message

> You do not have to understand it all today. Set it down without losing the thread, and come back when you are ready.

### Safety message

> Your writing remains yours, stays readable, and is never silently deleted.

## Marketing and product guardrails

- Lead with long-term personal understanding, not archive cleanup or productivity.
- Present limited attention as part of the problem: substantial subjects take time, and several may compete for that time.
- Do not imply that users should maintain every subject indefinitely or give every saved note equal attention.
- Describe gradual familiarity rather than guaranteed mastery or memorization.
- Do not claim that passive waiting produces insight.
- Do not market LivingNotes as a whiteboard, knowledge graph, project manager, source archive, or replacement for deeper work.
- Do not imply that the app summarizes, interprets, or reaches conclusions for the user.
- Do not require context-aware recommendations or semantic inspection to make the core experience work.
- Prefer content-blind prompts that ask the user to notice, recall, revise, or connect ideas themselves.
- Prefer simple local rules and deterministic mechanics before adding infrastructure-heavy intelligence.
- Do not claim a specific carbon reduction without measuring and substantiating it.
- Do not define the brand primarily by what it lacks; explain what independent, long-horizon thinking makes possible.
- Do not use urgency, guilt, obligation, streak loss, or failure language.
- Do not turn note-level changes into a stream of alerts, badges, or repeated push notifications.
- Present yellowing as compressed information and an invitation to inspect, not as an alarm.
- Treat the garden as a consistent interface language rather than decorative theming.
- Prefer mechanics that can be explained through the existing garden metaphor before introducing unrelated visual systems or specialist terminology.
- Do not force the metaphor where it obscures behavior, compromises accessibility, or makes writing appear unsafe.
- Do not present experimental mechanics as permanent or scientifically proven solutions.
- Do not imply that users must repair every note or clear every condition.
- Do not frame repair as a quiz, recall test, obligation, or proof of understanding.
- Keep repair low effort; deeper reading and revision should emerge from renewed interest rather than coercion.
- Do not let playful visuals trivialize serious subjects.
- Keep relief as reassurance, not the central outcome.
- Evaluate future features and communication by asking:

  > Does this help someone renew and deepen their own relationship with a subject over time without pretending to understand it for them?

## App Store direction: revision required

The previous **Quiet Discovery** App Store direction was based on an earlier brand hierarchy and is now superseded.

No replacement App Store name treatment, subtitle, promotional text, description, keyword strategy, screenshot story, or artwork direction is currently approved. Future App Store work must begin from the long-term-understanding core defined in this document.

App Store listing and screenshot revisions remain deferred and should be handled as a separate project.

## Deferred work

The following work is intentionally **not implemented as part of this branding revision**:

- App Store metadata or listing changes
- App Store screenshot concepts or artwork changes
- Landing-page copy, layout, or style changes
- Frontend implementation based on this brand direction
- Changes to existing product-principles or README documents

## Ideas for later consideration

The following copy directions are exploratory rather than approved positioning. Preserve them for future campaigns, App Store experiments, landing-page concepts, or product-language discussions:

- Make revision fun again
- Make curation fun again
- Train conciseness
- Living sticky note
- Better than a sticky note
- Knowledge management without the project management

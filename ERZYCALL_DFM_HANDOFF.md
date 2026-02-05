# ErzyCall Daily Fire Mission (DFM) — Agent Builder Handoff

> **Status:** DRAFT — Living architecture document. Not final. Iterate until the success metric is consistently met.
>
> **Success Metric:** Deni's calendar has **4 qualified meetings per day** with warm leads who have already spoken to AI and want to discuss ErzyCall further. If the system cannot sustain this rate, it is incomplete and needs more work.
>
> **Owner:** Deni (CEO, ErzyCall)
> **Context:** This document lives in the same repo as the FPF ontology docs. Reference them directly — don't duplicate.

---

## 1. What This System Does

The DFM is a **sales machine** that:

1. **Fires outbound "shots"** across every viable channel — digital, voice, physical, partnerships, VIP enterprise — every single day
2. **Qualifies inbound responses** through AI voice conversations (Vapi) so that by the time a lead reaches Deni's calendar, they've already talked to AI about their needs
3. **Measures everything** to converge on what works — best channels, ICPs, messages, timing, offers
4. **Fills a calendar** — not a CRM dashboard, not a report, a calendar with real meetings

The system's job is NOT to close deals. It is to **fill the calendar with people who are warm and ready to talk**. Deni (and later, a salesperson) handles the close.

### What "Warm Lead" Means Here

A warm lead has passed through ALL of these gates:

```
[SOURCED] → [CONTACTED] → [AI CONVERSATION COMPLETED] → [EXPRESSED INTEREST] → [BOOKED ON CALENDAR]
     ↑            ↑                    ↑                         ↑                       ↑
  Lead exists   Shot fired      Vapi spoke to them        They said "yes,          Calendly/Cal.com
  in Attio      & delivered     & they engaged            tell me more"            slot confirmed
```

A meeting that appears on calendar without passing through the AI conversation gate does NOT count toward the 4/day metric (except for inbound that self-books — which is a bonus, not the system's core function).

---

## 2. FPF Foundation (Read These First)

This system is built on the First Principles Framework. Before building anything, read:

- **[`FPF_ONTOLOGY_ANALYSIS.md`](./FPF_ONTOLOGY_ANALYSIS.md)** — Full ontology extraction. Key sections:
  - §"Holonic Foundation" — the System/Episteme split (actors vs. artifacts). Every component below is classified as one or the other.
  - §"Transformer Quartet" — the WHO/HOW/WHAT-CAPABILITY/WHAT-HAPPENED pattern. Every automation in DFM follows this pattern.
  - §"Trust & Assurance Calculus" — the F-G-R scoring system. This is how we measure whether automations are working and whether leads are actually warm.
  - §"Automation Discovery Framework" → §"Assess Automation Candidates" — the decision matrix for what to automate vs. keep manual.

- **[`FPF_SKILL.md`](./FPF_SKILL.md)** — Condensed skill prompt. Key sections:
  - §"The System/Episteme Split" — enforce this everywhere. Documents don't act. Agents act on documents.
  - §"Transformer Quartet" — use this as the template for every automation definition.
  - §"Trust Calculus" — use F-G-R for lead scoring and channel scoring.

### FPF Concepts You'll Use Constantly

| FPF Concept | DFM Usage | Reference |
|---|---|---|
| `U.System` | Vapi agent, Make.com scenarios, Deni, future salesperson | `FPF_ONTOLOGY_ANALYSIS.md` §"Holonic Foundation" |
| `U.Episteme` | Lead records, call transcripts, email templates, scripts, metrics | Same |
| `Transformer Quartet` | Every automation = Acting Side + MethodDescription + Method + Work | `FPF_ONTOLOGY_ANALYSIS.md` §"Transformer Quartet" |
| `⟨F, G, R⟩` tuple | Lead warmth scoring, channel effectiveness scoring, script quality scoring | `FPF_ONTOLOGY_ANALYSIS.md` §"Trust & Assurance Calculus" |
| `U.BoundedContext` | Different messaging per ICP segment — real estate vs. dental vs. F&B | `FPF_SKILL.md` §"Bounded Context" |
| `Congruence Level (CL)` | When adapting a script from one ICP to another, track translation quality | `FPF_ONTOLOGY_ANALYSIS.md` §"Bounded Context" |
| Automation Decision Matrix | F≥2 + R≥0.8 = automate; F<1 = document first; R<0.6 = keep manual | `FPF_ONTOLOGY_ANALYSIS.md` §"Assess Automation Candidates" |

---

## 3. System Architecture (Current Target — Will Evolve)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         LEAD SOURCING LAYER                             │
│  Scraping · Facebook Lead Ads · LinkedIn · Google Ads · Events · Lists │
│  Physical: Taxi QR · Erzy Riddler cards · Flyers · Marketplace listings│
└────────────────────────────┬────────────────────────────────────────────┘
                             │ raw leads
                             ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        ATTIO CRM (Central Hub)                          │
│  Every lead gets:                                                       │
│    - channel_source (which weapon fired this shot)                     │
│    - icp_tags [industry, size, location]                               │
│    - message_variant (which copy/angle was used)                       │
│    - fpf_F (formality of engagement: 0-3)                              │
│    - fpf_R (reliability/warmth: 0.0-1.0)                              │
│    - fpf_G (scope: subscription | agency_deal | reseller | enterprise) │
│    - shot_count (how many touches)                                     │
│    - stage: sourced → contacted → ai_spoken → interested → booked     │
└────────────────────────────┬────────────────────────────────────────────┘
                             │ trigger: new lead OR lead replied
                             ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    MAKE.COM ORCHESTRATION LAYER                          │
│                                                                         │
│  Scenario A: Lead Ingestion                                             │
│    Source → normalize → deduplicate → create in Attio → tag            │
│                                                                         │
│  Scenario B: Outbound Firing                                            │
│    Daily trigger → pull today's targets from Attio →                   │
│    route to channel executors (email, WhatsApp, Vapi, LinkedIn)        │
│                                                                         │
│  Scenario C: Response Processing                                        │
│    Reply detected → update Attio stage → trigger AI conversation       │
│                                                                         │
│  Scenario D: AI Conversation → Calendar                                 │
│    Vapi call completed → transcript to Attio → if interested →         │
│    send booking link → confirm slot → update stage to "booked"         │
│                                                                         │
│  Scenario E: Measurement & Reporting                                    │
│    Daily: shot count, response rates per channel                       │
│    Weekly: full Fire Report with R-score convergence                   │
└────────────────────────────┬────────────────────────────────────────────┘
                             │
                   ┌─────────┼──────────┐
                   ▼         ▼          ▼
            ┌──────────┐ ┌────────┐ ┌──────────┐
            │ VAPI.AI  │ │ EMAIL  │ │ WHATSAPP │  ... (more channel executors)
            │ Voice AI │ │ Engine │ │ API      │
            │          │ │        │ │          │
            │ THIS IS  │ │Instant-│ │ WA Biz   │
            │ THE DEMO │ │ly.ai / │ │ API via  │
            │ ITSELF   │ │Smart-  │ │ Make.com │
            │          │ │lead    │ │          │
            └─────┬────┘ └────────┘ └──────────┘
                  │
                  │ qualified + interested
                  ▼
         ┌─────────────────┐
         │   CALENDLY /    │
         │   CAL.COM       │
         │                 │
         │  THE SCOREBOARD │
         │  ≥4 meetings/   │
         │  day = working  │
         │  <4 = fix it    │
         └─────────────────┘
```

### Critical Design Principle: The Product IS The Sales Tool

ErzyCall sells AI phone answering. The Vapi qualification call IS the product demo. When a prospect picks up and talks to AI, they are simultaneously being qualified AND experiencing what they'd be buying. This is the single most important architectural insight — don't separate "sales process" from "product experience."

---

## 4. The Channel Arsenal

Every channel is a **weapon** in the arsenal. Each gets defined as an FPF Transformer Quartet.

### Quartet Template for Channels

```
CHANNEL: [ID] [Name]
───────────────────────────────────────────────────────
Acting Side:        [U.System performing the shot]
MethodDescription:  [Script/template/SOP — the recipe] (F=[0-3])
Method:             [Tool/capability used to fire]
Work:               [What gets recorded per shot]
───────────────────────────────────────────────────────
Volume:             [shots per day/week]
Cost per shot:      [RM or USD]
Measurement:        [what signals indicate hit/miss]
Current R:          [0.0 — unknown until data exists]
```

### Channel Inventory

**A — Digital Direct (High Volume, Low Cost)**

| ID | Channel | Volume Target | Executor Tool | Key Metric |
|----|---------|---------------|---------------|------------|
| A1 | Cold Email — Malaysian SMEs | 50-100/day | Instantly.ai or Smartlead | Reply rate → demo booked |
| A2 | LinkedIn DM — decision makers | 20-30/day | Expandi or manual | Accept → reply → call booked |
| A3 | Facebook/IG DM to biz pages | 20-30/day | Manual or ManyChat | Reply → demo booked |
| A4 | WhatsApp broadcast | 30-50/day | WA Business API via Make.com | Read → reply → demo booked |
| A5 | Google Ads (search intent) | Always-on | Google Ads | CPC → conversion to demo |
| A6 | Facebook/IG Ads → Lead Form → Vapi | Always-on | Meta Ads + Make.com + Vapi | CPL → qualification rate → booked |
| A7 | Short-form video (TikTok/Reels/Shorts) | 3-5/week | Organic posting, optionally HeyGen | Views → link clicks → demo booked |

**B — Voice & Direct Engagement (High Touch)**

| ID | Channel | Volume Target | Executor Tool | Key Metric |
|----|---------|---------------|---------------|------------|
| B1 | Vapi AI cold calls to business listings | 100-200/day | Make.com → Vapi | Pick-up → qualified → booked |
| B2 | Deni personal warm calls (founder calls) | 5-10/day | Phone + Attio logging | Conversion to demo/close |
| B3 | Voice drops / voicemail broadcasts | 50-100/day | Vapi or Drop Cowboy | Callback rate → booked |

**C — Physical & Guerrilla (High Memorability)**

| ID | Channel | Volume Target | Executor Tool | Key Metric |
|----|---------|---------------|---------------|------------|
| C1 | Taxi cab QR ads | Ongoing | Physical install | Scans → demo completions → signups |
| C2 | Erzy Riddler cards at events | Per event | Print + distribute | Cards out → QR scans → demo booked |
| C3 | Physical snail mail to top prospects | 20/week | Print + Lalamove/Pos Malaysia | Response rate → code redemption → booked |
| C4 | Gift drops to VIP prospects | 5/week | Branded item + note + QR | Response rate → meeting booked |
| C5 | Flyers/stickers in SME areas | Batch | Print + post | QR scans → demo booked |
| C6 | "AI answered this call" demo kits | 10/week | Print + mail + Vapi number | Kit received → callback → booked |

**D — Partnership & Platform (Leverage)**

| ID | Channel | Volume Target | Executor Tool | Key Metric |
|----|---------|---------------|---------------|------------|
| D1 | Telco partnerships (Maxis, TM, etc.) | 2-3 outreach/week | Direct outreach | Meeting → pilot → deal |
| D2 | POS/CRM platform integrations | 2-3 outreach/week | Direct outreach | Meeting → integration |
| D3 | Accounting firm referral partnerships | 3-5 outreach/week | Email + call | Referral agreement signed |
| D4 | Real estate agency bulk deals | 3-5 outreach/week | Email + Vapi demo | Pilot agreement |
| D5 | Chambers of Commerce / SME associations | 1-2/week | Applications + sponsorship | Events booked, leads from event |
| D6 | Marketplace listings (AppSumo, PitchGround) | Setup + optimize | Platform-specific | Sales, reviews, upsell rate |
| D7 | MDEC/MOSTI/MaGIC ecosystem | 1-2/week | Applications + networking | Grants, program acceptance |

**E — VIP Enterprise (Whale Hunting)**

| ID | Channel | Volume Target | Executor Tool | Key Metric |
|----|---------|---------------|---------------|------------|
| E1 | Top 50 enterprise target list (ABM) | 3-5 touches/week/account | Multi-touch sequences | Touch-to-meeting ratio |
| E2 | Personalized AI video pitch (HeyGen) | 2-3/week | HeyGen + email delivery | View rate → response → meeting |
| E3 | Conference/event VIP targeting | Per event | Pre-event → at-event → follow-up | Meetings set at event |
| E4 | Warm intros via investor/advisor network | 2-3/week | Personal ask → intro made | Intro → meeting booked |

---

## 5. Lead Scoring via FPF Trust Calculus

Every lead in Attio carries an `⟨F, G, R⟩` tuple. See `FPF_ONTOLOGY_ANALYSIS.md` §"Trust & Assurance Calculus" for the formal definitions. Here's how they map:

### F — Formality of Engagement

| F Level | Meaning in DFM | Example |
|---------|----------------|---------|
| F0 | Cold — no structured interaction yet | Name scraped from directory |
| F1 | Light touch — informal contact made | Replied to DM, clicked a link |
| F2 | Structured interaction — AI conversation completed | Vapi call happened, needs expressed |
| F3 | Formal commitment — meeting booked or proposal sent | On calendar, reviewing pricing |

### R — Reliability (How Warm)

| R Range | Meaning | Action |
|---------|---------|--------|
| 0.0–0.2 | Cold — no engagement signal | Keep in sequence, don't push |
| 0.2–0.4 | Cool — some signal (opened email, clicked) | Escalate to next channel |
| 0.4–0.6 | Warm — engaged but not committed (replied, chatted) | Trigger Vapi AI conversation |
| 0.6–0.8 | Hot — AI conversation done, expressed interest | Push booking link aggressively |
| 0.8–1.0 | Booked — on calendar or verbal commitment | Prep for meeting, don't over-touch |

### G — Scope (Deal Size)

| G Tag | Meaning | Approx Value |
|-------|---------|-------------|
| `single_sub` | One RM15/month subscription | RM180/year |
| `multi_seat` | Business with 2-10 lines | RM360-1800/year |
| `agency_deal` | Agency deploying for clients | RM5K-20K/year |
| `reseller` | Partner reselling ErzyCall | RM20K+/year |
| `enterprise` | Large deployment, custom pricing | RM50K+/year |

### The Key Rule (from FPF)

```
R_eff = min(R_i) - Φ(CL_min)
```

In practice: **a lead's warmth is only as strong as the weakest signal.** If they replied enthusiastically (R=0.7) but you're not sure they're the decision-maker (authority_R=0.3), the effective R is 0.3. Track R across dimensions:

- `R_interest`: Did they express need?
- `R_authority`: Are they the buyer?
- `R_budget`: Can they pay?
- `R_timeline`: Are they ready now?

`R_eff = min(R_interest, R_authority, R_budget, R_timeline)`

A lead is only "warm enough for calendar" when `R_eff ≥ 0.6` AND `F ≥ 2` (AI conversation completed).

---

## 6. The Vapi AI Conversation (The Core Gate)

This is the most important component. Everything upstream feeds leads TO the Vapi conversation. Everything downstream flows FROM it.

### Vapi Agent Specification

**Role (FPF):** `VapiAgent#Qualifier:ErzyCall:Sales_Feb2026`

**MethodDescription (the script — must be F≥2):**

The Vapi agent must accomplish these things in a single conversation:

1. **Confirm identity** — "Hi, am I speaking with [name] from [business]?"
2. **Establish need** — "I noticed you run [type of business]. Do you ever miss calls when you're busy?"
3. **Demo the product** — "Actually, the fact that I'm calling you right now? I'm an AI. This is exactly what ErzyCall does for businesses like yours."
4. **Qualify** — Probe for:
   - How many calls they miss (need)
   - Who answers currently (pain)
   - What they'd pay to never miss a call (budget signal)
   - Timeline ("When would you want this running?")
5. **Book or hand off** — "Would you like to speak with our founder Deni to set this up? I can book a 15-minute call for you right now."

**Output (Work record → Attio):**

```json
{
  "lead_id": "attio_record_id",
  "call_id": "vapi_call_id",
  "call_date": "2026-02-07T10:32:00+08:00",
  "duration_seconds": 187,
  "outcome": "interested | not_interested | callback_requested | no_answer | voicemail",
  "qualification": {
    "R_interest": 0.8,
    "R_authority": 0.6,
    "R_budget": 0.5,
    "R_timeline": 0.7,
    "R_eff": 0.5
  },
  "icp_tags_detected": ["real_estate", "5_staff", "kl"],
  "pain_points_mentioned": ["missed calls on weekends", "no receptionist budget"],
  "objections": ["worried about AI sounding robotic"],
  "meeting_booked": false,
  "next_action": "send_booking_link",
  "transcript_url": "...",
  "notes": "Interested but wants to hear pricing from human. Send Calendly link via WhatsApp."
}
```

### Gate Logic

```
IF outcome = "interested" AND R_eff ≥ 0.6:
    → Send booking link immediately (WhatsApp + Email)
    → Update Attio: stage = "interested", F = 2
    → If no booking within 24h: Vapi follow-up call

IF outcome = "interested" AND R_eff < 0.6:
    → Flag which R dimension is low
    → Route to appropriate nurture sequence
    → e.g., R_authority low → "Can you connect me with the owner?"

IF outcome = "callback_requested":
    → Schedule Vapi callback at requested time
    → Update Attio: stage = "contacted", add callback note

IF outcome = "not_interested":
    → Update Attio: stage = "dead", R = 0.0
    → Log reason for pattern analysis
    → Do not contact again for 90 days

IF outcome = "no_answer" OR "voicemail":
    → Retry up to 3 times (different days/times)
    → After 3 misses: fall back to WhatsApp/email
```

---

## 7. Daily Operations Spec

### The Daily Fire Mission (DFM) Cycle

```
06:00  MORNING SCAN
       ├── Pull overnight: new leads, replies, bounces, unsubscribes
       ├── Update Attio stages and R scores
       └── Generate Action Brief (top priority actions for Deni)

06:30  LOAD GUNS (automated, Deni reviews/approves)
       ├── Queue cold emails (A1): 50-100 targets
       ├── Queue LinkedIn DMs (A2): 20-30 targets
       ├── Queue WhatsApp broadcasts (A4): 30-50 targets
       ├── Queue Vapi cold calls (B1): 100-200 targets
       └── Queue voicemail drops (B3): 50-100 targets

07:00  DENI'S FOUNDER FIRE (manual, high-touch)
       ├── 5-10 warm calls to highest-R leads (B2)
       ├── 2-3 VIP LinkedIn voice messages (E1)
       ├── 1-2 partnership outreach with personal touch (D1-D5)
       └── Review/approve any AI-drafted messages

08:00  GUERRILLA PREP (weekly/as-needed)
       ├── Brief runner on physical deliveries (C3, C4)
       ├── Check taxi QR analytics (C1)
       └── Queue HeyGen personalized videos (E2)

08:30+ MACHINE RUNS AUTONOMOUSLY
       ├── Vapi calls going out
       ├── Email sequences dripping
       ├── Ads capturing leads → Make.com → Attio → Vapi
       ├── WhatsApp messages delivering
       └── Responses triggering Scenario C (response processing)

17:00  END-OF-DAY SCORING
       ├── Log results: shots fired, responses, demos booked
       ├── Update R scores for contacts touched today
       ├── Note new ICP insights
       └── Flag tomorrow's priority targets

FRIDAY WEEKLY REVIEW (1 hour)
       ├── Generate Weekly Fire Report
       ├── Rank channels by cost-per-demo
       ├── Rank ICPs by conversion rate
       ├── Rank message variants by response rate
       ├── Decide: which channels to scale, cut, or test
       └── Update MethodDescriptions (scripts, templates) based on data
```

---

## 8. Measurement Schema

### Shot Record (every outbound action)

Every shot fired by the machine is a **Work unit** per FPF (see `FPF_ONTOLOGY_ANALYSIS.md` §"Transformer Quartet"):

```
shot_id:            DFM-{date}-{channel}-{sequence_number}
channel_id:         A1 | A2 | ... | E4
target_lead_id:     Attio record ID
method_desc_id:     Which script/template version was used
fired_at:           ISO timestamp
delivered:          boolean
opened:             boolean (if applicable)
replied:            boolean
ai_conversation:    boolean (did Vapi gate happen?)
interested:         boolean
booked:             boolean
closed:             boolean (tracked later)
```

### Channel Scorecard (aggregated weekly)

| Metric | Formula | Target |
|--------|---------|--------|
| Shot volume | Count of shots fired | Per channel target above |
| Delivery rate | delivered / fired | > 95% |
| Engagement rate | (opened OR replied) / delivered | Varies by channel |
| AI conversation rate | ai_conversation / engaged | > 30% |
| Interest rate | interested / ai_conversation | > 40% |
| Booking rate | booked / interested | > 50% |
| **Cost per booking** | total_spend / booked | **Primary optimization metric** |
| **Calendar fill contribution** | booked_meetings / 4-per-day target | **The scoreboard** |

### Convergence Tracking

The whole point of firing across all channels simultaneously is to **converge on what works**. Track these weekly:

```
Week 1: R_channel is unknown (0.1) for all channels → fire everywhere equally
Week 2: R_channel starts diverging → WhatsApp 0.3, Email 0.15, Vapi 0.25
Week 3: Clear winners emerging → double down on high-R channels
Week 4: Playbook solidifying → document top channels/ICPs/messages at F2
```

This follows the FPF trust convergence pattern: R starts uncertain and increases as evidence accumulates. See `FPF_ONTOLOGY_ANALYSIS.md` §"Trust & Assurance Calculus" for formal treatment.

---

## 9. Bounded Contexts (ICP Segments)

Per FPF (see `FPF_SKILL.md` §"Bounded Context"), each ICP segment is a separate context with its own vocabulary and messaging.

### Initial Segments to Test

| Context ID | ICP | Pain Vocabulary | Key Message Angle |
|------------|-----|-----------------|-------------------|
| `ICP:RealEstate_MY` | Malaysian real estate agents, 5-20 staff | "missed call = missed commission", "weekend showings", "always available" | "Never lose a property inquiry again" |
| `ICP:Dental_MY` | Dental clinics, 3-10 staff | "receptionist busy with patients", "after-hours appointment requests" | "Your receptionist can't answer during procedures" |
| `ICP:FnB_MY` | F&B businesses, restaurants, catering | "reservation calls during rush", "catering inquiries missed" | "Every missed reservation is an empty table" |
| `ICP:Legal_MY` | Small law firms, 2-10 staff | "client calls during court", "intake calls after hours" | "Clients call when they're desperate — be there" |
| `ICP:Trades_MY` | Plumbers, electricians, contractors | "on-site can't answer", "losing jobs to competitor who picked up" | "The plumber who answers first gets the job" |

**Bridge rules (CL tracking):** When adapting a script from one ICP to another, track what changes:

```
Bridge: ICP:RealEstate_MY → ICP:Dental_MY
CL: CL1 (plausible — similar pain, different vocabulary)
Changes needed: "commission" → "patient", "showing" → "appointment", "property" → "treatment"
Loss notes: Urgency framing different — real estate is competitive speed, dental is patient trust
```

### Segment Performance Tracking

Each ICP context gets its own R score. After 2-4 weeks, rank them:

```
ICP:RealEstate_MY   R = 0.45  ← strongest signal, double down
ICP:Trades_MY       R = 0.32  ← promising, test more
ICP:Dental_MY       R = 0.18  ← weak signal, keep testing
ICP:FnB_MY          R = 0.08  ← consider pausing, low intent
ICP:Legal_MY        R = 0.22  ← moderate, needs script work
```

---

## 10. What "Done" Looks Like (And What "Not Done" Means)

### The System is COMPLETE When:

- [ ] **4 qualified meetings/day sustained for 2+ consecutive weeks**
- [ ] Every meeting was preceded by an AI conversation (Vapi gate passed)
- [ ] Cost-per-meeting is known and trending down
- [ ] Top 3 channels identified and documented at F2
- [ ] Top 2 ICP segments identified with validated messaging (CL≥2)
- [ ] The entire system can run with <2 hours/day of Deni's time
- [ ] A new salesperson could read this doc + the MethodDescriptions and operate the machine on Day 1

### The System is NOT COMPLETE When:

- Calendar has <4 meetings/day → **add more channels or increase volume on working channels**
- Meetings are happening but leads aren't warm → **Vapi qualification script needs work (F upgrade)**
- Can't tell which channels work → **measurement pipeline broken, fix Attio tracking first**
- Takes >3 hours/day of Deni's time → **automate more of the manual steps**
- R scores aren't converging after 3 weeks → **not enough shot volume or segments too broad**

### Iteration Protocol

When the system is not hitting 4/day:

1. **Check volume first** — are enough shots being fired? (Need 500+ shots/day across all channels to generate 4 bookings at ~1% end-to-end conversion)
2. **Check the funnel** — where is the biggest drop-off? (Sourcing? Delivery? Engagement? AI conversation? Booking?)
3. **Check by channel** — which channels are pulling weight? Kill the dead ones, scale the live ones.
4. **Check by ICP** — which segments respond? Narrow targeting to winners.
5. **Check the scripts** — is the Vapi agent converting conversations to interest? Review transcripts, improve MethodDescription.
6. **Add a new weapon** — if all existing channels are optimized and still short, add a new channel from the arsenal.

Repeat until 4/day is sustained. **This is the only metric that matters.**

---

## 11. Tech Stack Summary

| Layer | Tool | Purpose |
|-------|------|---------|
| CRM | Attio | Central hub — every lead, every score, every stage |
| Orchestration | Make.com | Connects everything — triggers, routing, data flow |
| Voice AI | Vapi.ai | Cold calls, qualification calls, follow-up calls |
| Email outbound | Instantly.ai or Smartlead | Volume cold email with warmup |
| WhatsApp | WA Business API (via Make.com) | Direct messaging channel |
| LinkedIn | Expandi or manual | Professional outreach |
| Ads | Meta Ads Manager + Google Ads | Paid lead generation |
| Calendar | Calendly or Cal.com | THE SCOREBOARD — booking link |
| Video | HeyGen | Personalized VIP video messages |
| Physical | Local print + Lalamove/Pos Malaysia | Guerrilla marketing delivery |
| Analytics | Attio reports + Google Sheets | Weekly Fire Report generation |
| AI Assistant | Claude (via Co-work or chat) | Morning Scanner, Action Brief, Weekly Report |

---

## 12. For the Agent Builder: Where to Start

You're not building all of this at once. Build in this order, and **don't move to the next layer until the current one is producing measurable output:**

### Phase 1: The Core Loop (Week 1-2)

Get leads into Attio, fire Vapi calls, get bookings on calendar.

```
Facebook Lead Ad → Make.com → Attio (lead created) → Make.com → Vapi call
→ Vapi outcome → Make.com → Attio (stage updated) → if interested → booking link sent
→ Calendly webhook → Make.com → Attio (stage = booked)
```

This alone, if working at volume, can hit the target.

### Phase 2: Multi-Channel Fire (Week 3-4)

Add email, WhatsApp, and LinkedIn as parallel channels. All roads lead to the same Vapi gate.

### Phase 3: Measurement & Optimization (Week 4-6)

Build the shot tracking, channel scorecards, and weekly report automation. Start converging on winners.

### Phase 4: Physical & Partnership Channels (Month 2)

Layer in guerrilla marketing, partnership outreach, and VIP enterprise plays. These have longer cycles but higher deal sizes.

### Phase 5: Full Autonomy (Month 3)

System runs with minimal Deni input. Ready for salesperson handoff. All MethodDescriptions at F2+. Playbook documented.

---

## Appendix: Glossary (FPF → DFM Translation)

| Term in This Doc | FPF Formal Term | Definition |
|------------------|----------------|------------|
| Shot | U.Work | A single outbound action fired by the machine |
| Channel | MethodDescription + Method | The recipe + capability combination for reaching leads |
| Lead | U.Episteme (lead record) | A contact record that gets acted upon by systems |
| Vapi Agent | U.System bearing Qualifier role | The AI that conducts qualification conversations |
| R score | Reliability from ⟨F, G, R⟩ tuple | How warm/reliable a lead or channel is |
| F level | Formality from ⟨F, G, R⟩ tuple | How structured/documented the process is |
| ICP Segment | U.BoundedContext | A vocabulary and messaging boundary per customer type |
| Script | MethodDescription (U.Episteme) | The documented recipe for a channel or conversation |
| Booking | Work output (successful) | A confirmed calendar slot = system success |
| Fire Report | Aggregated Work + R assessment | Weekly analysis of all shots and their outcomes |

> **Full FPF reference:** See [`FPF_ONTOLOGY_ANALYSIS.md`](./FPF_ONTOLOGY_ANALYSIS.md) and [`FPF_SKILL.md`](./FPF_SKILL.md) in this repo.

---

*Document version: 0.1.0-draft*
*Created: 2026-02-06*
*This is a living document. It is not final. Update it every time the system teaches you something new.*

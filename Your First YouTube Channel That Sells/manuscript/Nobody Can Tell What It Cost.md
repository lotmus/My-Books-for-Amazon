*A working guide for creators who want a channel, not a hobby*

# Nobody Can Tell What It Cost

*A tour of the free and near-free tools that generate footage, cut it together, score it, and put a voice on it — and the one habit none of them will build for you: checking what you are actually allowed to use.*

A viewer who watches your video to the end has no idea whether it cost four hundred dollars or four dollars to make. They saw a thumbnail, they saw the first few seconds decide whether to keep watching, and then they saw a finished video — nothing about your budget survived the upload. That is the premise of this chapter: every job a first channel needs done — generating or sourcing footage, cutting it together, adding music, adding a voice, exporting it in the right shape — has a free or near-free tool doing it well enough that the gap between "free" and "paid" shows up in your time, not in what the viewer sees.

The one thing free tools do not do for you is tell you what you are allowed to do with their output. That check is yours, every time, and it is the thread running through every section below.

![The Free Production Pipeline: five stages — Generate Footage (Sora 2, InVideo, Magic Hour), Stock Footage & Photos (Pexels, Pixabay, Mixkit), Music & Sound (YouTube Audio Library, FreePD, Incompetech), Voice (FineVoice, Revoicer, Turboscribe), and Edit & Export (CapCut, 123apps, FFmpeg) — with a banner reading "Free tool ≠ free to use commercially. Read the license page before you publish."](../figures/free-production-pipeline.svg)

*The five jobs this chapter covers, in order, with one example tool from each section below. Section numerals match.*

## I. Generating footage without a camera

Text-to-video generators have crossed from novelty to usable in the last few years: describe a shot, get back several seconds of footage that did not exist an hour ago. Tools worth knowing by name include OpenAI's **Sora 2**, **InVideo**, **Media.io**, and **Magic Hour** — the last of which bundles far more than video generation into one account: face swap, a talking head built from a single photo, lip sync, voice cloning, image generation, and a handful of restyling filters. **Remaker** and **Deepswap** focus specifically on face-swap and AI video generation as their core feature.

Two things to expect going in. First, quality is inconsistent — plan to regenerate a clip two or three times before one is usable, not once. Second, and more important: what you are allowed to do with the output — commercial use, resale, republishing at scale — is set by that specific tool's terms of service, and those terms differ from tool to tool and change as the tools themselves update. Read the commercial-use section before you publish anything a generator made for you, not just the pricing page.

## II. The free stock library, and the license attached to each clip

For footage and photos you did not generate yourself, several libraries offer genuinely free, high-quality clips with no subscription required:

| Library | Attribution required | Note |
|---|---|---|
| [Pexels](https://www.pexels.com/videos/) | No | Free for commercial use, no signup needed to browse. |
| [Pixabay](https://pixabay.com/videos/) | No | Video, photo, and music under one shared license. |
| [Mixkit](https://mixkit.co/free-stock-video/) | No | Smaller, cinematic-quality library; also free music and editing templates. |
| [Coverr](https://coverr.co/) | No | Film-style background clips, personal and commercial use. |
| [Videezy](https://www.videezy.com/) | Varies by clip | Free and paid mixed together — check each clip's own license page. |
| [Vecteezy](https://www.vecteezy.com/) | Varies by asset | Free tier exists; read the specific asset's terms before use. |
| [Envato Elements](https://elements.envato.com/stock-video) / [iStock](https://www.istockphoto.com) | Paid | Subscription libraries — worth it once the free libraries stop covering a niche, not before. |

[Unsplash](https://unsplash.com/) covers photos on similar terms to the no-attribution rows above: free for commercial and non-commercial use under its own license, no permission required.

Treat "no attribution required" as that library's current policy, not a permanent guarantee attached to every clip forever — it can change going forward. The habit worth building is reading the license line on a library before a batch download, not assuming last year's library still works the same way this year.

## III. Free music and sound effects, and the one library built for this platform

Start with **YouTube's own Audio Library**, inside [YouTube Studio](https://studio.youtube.com/channel/UC/audio). It exists specifically so creators can score a video without a copyright claim landing on it afterward, which makes it the safest default — especially before you have learned to read a third-party library's license carefully.

Beyond it: [Pixabay Music](https://pixabay.com/music/) and [FreePD](https://freepd.com/) are free with no attribution required, the latter because its tracks are public domain outright. Sites built around a specific composer's catalog, like Incompetech, or a named creator's free tier, like Bensound, commonly require crediting that person by name in the video description even when the track itself costs nothing — read the attribution wording on the specific track, not just its price. For sound effects and short clips rather than full tracks, [bitmidi.com](http://bitmidi.com) and [sounddino.com](https://sounddino.com/) are worth bookmarking, along with [101soundboards](https://www.101soundboards.com/) for effect and voice-line boards; [mp3cut.net](https://mp3cut.net) handles trimming a track down to length once you have picked one.

## IV. Getting a voice into the video without recording one

Text-to-speech tools like [FineVoice](https://finevoice.ai/) and [Revoicer](https://revoicer.com/) generate a spoken voiceover from a script; free tiers are normally sufficient to test how a script sounds before paying for a final, higher-quality render. **Turboscribe** does the reverse job — turning a recorded voice into text — which is worth knowing about specifically because that transcript can go straight into the caption workflow this book's first chapter covers, rather than requiring a second, separate transcription pass.

Voice cloning deserves a harder line than the rest of this chapter. Cloning your own voice to save recording time is the low-risk version of this feature. Cloning someone else's — a narrator whose style you like, a public figure, a relative — moves into consent and, in a growing number of places, legal territory that a hobbyist tool's terms of service does not resolve on your behalf. If a tool offers voice cloning as a feature, that permission question is yours to answer before you use it, not the tool's.

## V. The free engine editing everything else runs on

For the mechanical editing work — trimming, resizing to the 9:16 vertical frame Shorts needs, merging clips, burning in a caption, converting a file to a format YouTube accepts — general-purpose browser editors cover a first channel's needs at no cost. **123apps**, **EZGIF**, **Clideo**, and **CapCut** each bundle most of that into one free tier; [online-video-cutter.com](https://online-video-cutter.com/) is a narrower option if all you need is a trim. Where a free tier hits a wall — Clideo's watermark, for instance, lifts only on its paid subscription, in roughly the $6–9-per-month range at the time of the author's own research, though confirm current pricing before relying on that figure — it is usually because the export is genuinely a premium feature, not because the tool is holding basic editing hostage.

Underneath nearly all of these, doing the actual video processing, is **FFmpeg** — the same free, open-source engine much commercial editing software is built on. It has no graphical interface of its own and no watermark or subscription either; **Shutter Encoder** wraps it in one for anyone not ready to type commands. Worth learning once uploading is a weekly habit, not before — the browser tools above cover everything a first month of videos actually needs.

## VI. Claims that do not survive checking a license page

- That "free" and "free to use commercially" mean the same thing. They frequently do not — an AI generator's free tier and a stock clip's license can each carry restrictions a price tag alone does not disclose.
- That every clip in a "no attribution required" library carries that status forever, unchanged. It is the library's current policy, not a permanent grant attached to the file you downloaded last year.
- That professional-looking video requires paid software. Every job in this chapter — generation, footage, music, voice, editing — has a free tool doing it competently; money buys convenience and polish, not a capability a free tier lacks entirely.
- That an AI-cloned voice is fine to use as long as the result sounds good. Sounding good and having the right to use that voice are unrelated questions, and only one of them is checkable by ear.
- That auto-transcribed narration is caption-ready the moment it is generated. It still needs the same review pass this book's first chapter describes for automatic captions — a transcription tool mishears the same way a captioning one does.

A last limit. This chapter names specific tools because specific tools are what a first video actually needs, not because any one of them is guaranteed to still exist, still be free, or still carry the same terms by the time you read this. Confirm the current price, license, and terms of service on any tool or library named here before you build a video on top of it — tool lineups change faster than platform policy does.

---

*Sources: Tool names and URLs in this chapter are drawn from the author's own working bookmark list of video, footage, music, and voice tools, current at the time of writing. Pricing, license terms, and feature availability on every platform named here change; none of this chapter is a substitute for reading that platform's own current terms before publishing anything built with it. Not legal advice on licensing, attribution, or AI-generated content rights.*

*Not an official YouTube publication.*

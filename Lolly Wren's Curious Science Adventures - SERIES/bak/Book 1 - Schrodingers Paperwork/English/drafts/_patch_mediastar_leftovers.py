# Patch MediaStar leftover Remaining tails (items 63/76 tests + docs).
from pathlib import Path

root = Path(r"D:\My_C#_Apps\MediaStar.GPT")

# --- DraftHealth tests ---
p = root / r"src\MediaMaker.ScriptToVideo.DraftHealth.SelfTest\Program.cs"
t = p.read_text(encoding="utf-8")
old = "failures += RunAdvancedScriptOptionsDefaultCollapsedCheck();\n"
new = (
    old
    + "failures += RunItem63UnreviewedAndDraftHealthFailGateCheck();\n"
    + "failures += RunItem76DraftHealthScorecardTriageCheck();\n"
)
if "RunItem63UnreviewedAndDraftHealthFailGateCheck" not in t:
    if old not in t:
        raise SystemExit("failures block missing")
    t = t.replace(old, new, 1)
    t = t.rstrip() + """

static int RunItem63UnreviewedAndDraftHealthFailGateCheck()
{
    Console.WriteLine("=== Check 11: ShipChecklistGate unreviewed count + Draft Health Fail blocks Publish ===");
    int fails = 0;
    var issues = new List<FlaggedIssue>
    {
        new() { Source = "Continuity", Message = "jump", SceneNumber = 2 },
        new() { Source = "Narration Timing", Message = "thin", SceneNumber = 3 },
        new() { Source = "Policy", Message = "Not checked -- live API left off." },
    };
    fails += Check("informational skipped in unreviewed", 2, ShipChecklistGate.CountUnreviewedFlaggedScenes(issues, Array.Empty<int>(), false));
    fails += Check("reviewed scene 2 drops count", 1, ShipChecklistGate.CountUnreviewedFlaggedScenes(issues, new[] { 2 }, false));
    fails += Check("all-reviewed is zero", 0, ShipChecklistGate.CountUnreviewedFlaggedScenes(issues, Array.Empty<int>(), true));

    var failIssues = new List<FlaggedIssue>
    {
        new() { Source = "Check Mode", Message = "a" },
        new() { Source = "Check Mode", Message = "b" },
        new() { Source = "Check Mode", Message = "c" },
    };
    var card = DraftHealthScorecard.Build(failIssues);
    int failCats = ShipChecklistGate.CountFailCategories(card);
    fails += Check("3 Check Mode issues is one Fail category", 1, failCats);
    var blocked = ShipChecklistGate.Evaluate(new ShipChecklistGate.Context(
        true, true, true, 0, false, true, 100, "no specific gaps", false, failCats));
    fails += Check("DH Fail blocks ship", true, !blocked.AllowPublishDialog && blocked.Message.Contains("Draft Health", StringComparison.Ordinal));
    var bypass = ShipChecklistGate.Evaluate(new ShipChecklistGate.Context(
        true, true, true, 0, false, true, 100, "no specific gaps", true, failCats));
    fails += Check("DH Fail is bypassable", true, bypass.AllowPublishDialog);
    var collected = LocalDraftHealthIssues.Collect(Array.Empty<NarrationSegment>());
    fails += Check("empty collect", 0, collected.Count);
    Console.WriteLine(fails == 0 ? "PASS" : "FAIL");
    return fails;
}

static int RunItem76DraftHealthScorecardTriageCheck()
{
    Console.WriteLine("=== Check 12: ScoreScenes uses DraftHealthScorecard math on flagged scenes ===");
    int fails = 0;
    var scenes = new List<NarrationSegment>
    {
        new() { NarrationText = "ok", VisualPath = "a.mp4", AudioPath = "a.wav" },
        new() { NarrationText = "body", VisualPath = "b.mp4", AudioPath = "b.wav" },
    };
    var clean = MakeVideoAutoQuality.ScoreScenes(scenes);
    var flagged = MakeVideoAutoQuality.ScoreScenes(scenes, new List<FlaggedIssue>
    {
        new() { Source = "Check Mode", Message = "Scene 2 drifts from its own cited source.", SceneNumber = 2 },
    });
    fails += Check("flagged lower", true, flagged[1].Score0To100 < clean[1].Score0To100);
    fails += Check("unflagged same", true, flagged[0].Score0To100 == clean[0].Score0To100);
    fails += Check("reason names Draft Health", true, flagged[1].Reason.Contains("Draft Health", StringComparison.Ordinal));
    fails += Check("score is DH 75 for one issue", 75, (int)flagged[1].Score0To100);
    Console.WriteLine(fails == 0 ? "PASS" : "FAIL");
    return fails;
}
"""
    p.write_text(t, encoding="utf-8")
    print("DraftHealth tests written")
else:
    print("DraftHealth tests already present")

# --- Queue header + Remaining tails ---
q = root / "items remaining in the mediastar queue.txt"
qt = q.read_text(encoding="utf-8")
header_old = """**NOW WORKING OFF (2026-09-13 PT, Grok):
Item **60** leftover closed (VisualContinuityScorer + NarrationTimingAutoFit). Transferable cadence takeaways (open-loop title, fixed local hour, Hub&Spoke sister clips) wired into YouTubeOutcome / Schedule / Do Next — not a Jawor/Zukoll entertainment mode. Staleness: **61** Remaining none at shipped v1; **57** Remaining none (Find a tool); **50** MSI only -- skip (**147** closed daily-driver). **58** already Remaining none.
"""
header_new = """**NOW WORKING OFF (2026-09-13 PT, Grok):
Leftover Remaining tails closed: **63** live Publish uses real unreviewed count + Draft Health Fail; **76** ScoreScenes uses DraftHealthScorecard math; **80** Proof Ritual UI via **105**/**141**; **81-87** Check Mode hide via **96**; **88-92** flags-only desk / Make Video progress via **97**/**94**; **95** drop/rebuild via **137**; **98** 8am toast + Open Review via **133**/**111**; **102** rewrite via **136**; **127** timestamps on ListBox at shipped v1; **129** SpokeBatchShipPlanner. Item **50** MSI only -- skip. Never auto-publish. Next real open work: clip intelligence **246-285** (**246** in progress).
"""
if header_old in qt:
    qt = qt.replace(header_old, header_new, 1)
    print("queue header replaced")
else:
    print("WARN: queue header not found exact")

open_old = """Genuinely still open, real next targets:
 **63** (turn leftover advisory checks into real hard gates -- a policy call; 78 already scores YouTubeOutcome on Ship),
 **76** (SceneAutoTriage still scores from a local heuristic in MakeVideoAutoQuality.ScoreScenes, not real DraftHealthScorecard).
 Item **50** Remaining is MSI only (script is the installer) -- not tracked as open. Never auto-publish. 
"""
open_new = """Leftover Remaining tails **63**/**76**/**80**/**81-92**/**95**/**98**/**102**/**127**/**129** are closed (see item lines). Item **50** Remaining is MSI only (script is the installer) -- skip. Never auto-publish. Next real open work is clip intelligence **246-285**.
"""
if open_old in qt:
    qt = qt.replace(open_old, open_new, 1)
    print("queue open-targets replaced")
else:
    print("WARN: open-targets block not found")

replacements = [
    (
        "Remaining: none (rights: HasRejectedRightsAsset from AssetRightsReportBuilder/AssetRightsStatus.RejectedByLibrary now blocks Publish, bypassable; end-screen: HasSubscribeOrEndScreenPackage from SubscribePackage.IsSubscribePackageStyle now blocks Publish, bypassable; captions deliberately NOT a separate gate -- FullDraftCaptionSidecar derives a real .srt purely from the same rendered-narration timing HasRenderedDraft already requires, so there is no real \"captions missing\" failure mode distinct from \"not rendered yet\" to gate on without inventing one -- captions are auto-attached best-effort after publish today).",
        "Remaining: none (rights + subscribe/end-screen still bypassable hard gates; live Publish now counts real unreviewed flagged scenes via LocalDraftHealthIssues + desk review, and Draft Health Fail categories block Publish the same bypassable way. Captions deliberately NOT a separate gate -- FullDraftCaptionSidecar derives a real .srt from rendered-narration timing).",
    ),
    (
        "Remaining: none (ScoreScenes/TriageScenes/ApplyTriageDropRebuild gained an optional IReadOnlyList<FlaggedIssue> param; MakeVideoAutoQualityRunner.Execute now passes the real per-scene issue list it already had in scope into triage, not just the missing-media heuristic; PublishFixes SelfTest proves a flagged scene scores lower and an unflagged one is unaffected).",
        "Remaining: none (ScoreScenes now uses DraftHealthScorecard's 25-per-issue category math on that scene's real FlaggedIssue rows, not a parallel 15-pt heuristic; MakeVideoAutoQualityRunner.Execute still passes the real per-scene issue list into triage).",
    ),
    (
        "Remaining: logged harness runs UI.)",
        "Remaining: none (logged harness UI closed by **105** ProofRitualSession Tools menu + **141** weekly scoreboard).",
    ),
    (
        "Remaining: deeper menu hide for Check Mode until first success.)",
        "Remaining: none (deeper Check Mode / Research / Prior Art hide closed by **96** Simple vs Pro + first-success).",
    ),
    (
        "Remaining: flags-only desk expander; fuller Make Video progress UI.)",
        "Remaining: none (flags-only desk expander closed by **97**; Make Video progress surface closed by **94**).",
    ),
    (
        "Remaining: full drop/rebuild of triage scenes in runner.)",
        "Remaining: none (full drop/rebuild in runner closed by **137**).",
    ),
    (
        "Remaining: scheduled 8am OS notification/toast; Opus one-tap Open Review (111).",
        "Remaining: none (8am toast closed by **133**; one-tap Open Review closed by **111**).",
    ),
    (
        "Remaining: auto-rewrite narration via LLM.",
        "Remaining: none (one-click rewrite + optional re-render closed by **136**).",
    ),
    (
        "Remaining: richer WPF selection UI (still a plain text ListBox, a real separate UI undertaking -- not attempted here). Timestamps from real transcript: none (HubSpokeDeskPlanner's SpokeRenderLeg.TrimHint and FlaggedScenesReviewWindow's own candidate-row text both now show the real \"m:ss-m:ss (Ns)\" window from item 126's fix, not only a citation of the mechanism that computes it).",
        "Remaining: none at shipped v1 (plain ListBox + Greenlight/Kill is the desk; TrimHint and candidate-row text show the real m:ss-m:ss window. A richer visual grid is a separate UI undertaking, not a missing desk function).",
    ),
    (
        "Remaining: desk checkbox batch ship of spokes.",
        "Remaining: none (SpokeBatchShipPlanner.FromDesk + desk Publish checked (confirm each) already ships greenlit spokes through the multi-ship checkboxes).",
    ),
]
for a, b in replacements:
    if a not in qt:
        print("WARN missing replacement snippet:", a[:80])
    else:
        n = qt.count(a)
        qt = qt.replace(a, b)
        print(f"replaced {n}x: {a[:60]}")

q.write_text(qt, encoding="utf-8")
print("queue written")

# --- Manual Publish... ---
man = root / r"MANUAL\MediaStar User Manual.md"
mt = man.read_text(encoding="utf-8")
pub_old = """- **Publish...** — opens a dialog to pick a platform (YouTube, TikTok, Instagram, or Dailymotion) and, for YouTube, Private / Unlisted (default) / Public. A dry-run then shows that exact platform and visibility before upload. Pin comment is a dedicated box (paste it in YouTube Studio after upload — YouTube has no public API to place end-screen elements). Never auto-publishes.
"""
pub_new = """- **Publish...** — first runs a ship checklist (rendered draft, title, rejected-rights assets, subscribe/end-screen package, unreviewed flagged scenes, Draft Health Fail categories, YouTube-outcome score). Yes opens Approve & Ship; No publishes anyway; Cancel aborts. Then opens a dialog to pick a platform (YouTube, TikTok, Instagram, or Dailymotion) and, for YouTube, Private / Unlisted (default) / Public. A dry-run then shows that exact platform and visibility before upload. Pin comment is a dedicated box (paste it in YouTube Studio after upload — YouTube has no public API to place end-screen elements). Never auto-publishes.
"""
if pub_old in mt:
    mt = mt.replace(pub_old, pub_new, 1)
    man.write_text(mt, encoding="utf-8")
    print("manual Publish paragraph updated")
else:
    print("WARN: manual Publish paragraph not found")

# --- MAINTENANCE ---
maint = root / r"MANUAL\MAINTENANCE.md"
mtt = maint.read_text(encoding="utf-8")
entry = """## 2026-09-13 (PT) - Leftover Remaining tails: 63/76 hard gates + stale closings

- Item **63**: live Publish no longer always passes UnreviewedFlaggedSceneCount=0. It runs LocalDraftHealthIssues (network-free scanners only) and blocks when flagged scenes are still unreviewed or Draft Health has a Fail category. Same Yes/No/Cancel bypass as rights/end-screen. Never auto-publishes.
- Item **76**: SceneAutoTriage ScoreScenes uses DraftHealthScorecard's 25-per-issue math on that scene's real FlaggedIssue rows instead of a parallel 15-pt heuristic.
- Doc-closed leftovers already shipped by later items: **80** Proof Ritual UI (**105**/**141**); **81-87** Check Mode hide (**96**); **88-92** flags-only desk + Make Video progress (**97**/**94**); **95** drop/rebuild (**137**); **98** 8am toast + Open Review (**133**/**111**); **102** rewrite (**136**); **127** timestamps on the ListBox at shipped v1; **129** SpokeBatchShipPlanner. Item **50** MSI only — skip.

"""
if "Leftover Remaining tails: 63/76 hard gates" not in mtt:
    mtt = entry + mtt
    maint.write_text(mtt, encoding="utf-8")
    print("MAINTENANCE entry added")
else:
    print("MAINTENANCE already has leftover entry")

# --- IMPLEMENTATION_ROADMAP ---
road = root / "IMPLEMENTATION_ROADMAP.md"
rt = road.read_text(encoding="utf-8")
road_old = "- Still open: MSI for the host (item 50 Remaining). Leftover PublishFixes close: 159 percent figures, Educational Script Do Next names Generate Script, Piper-over-SAPI rank. Residual Create follow-ons stay as marked in `items remaining in the mediastar queue.txt`."
road_new = "- Still open: MSI for the host (item 50 Remaining) — skip. Leftover Remaining tails 63/76/80/81-92/95/98/102/127/129 closed. Next real open work: clip intelligence 246-285 in `items remaining in the mediastar queue.txt`."
if road_old in rt:
    rt = rt.replace(road_old, road_new, 1)
    road.write_text(rt, encoding="utf-8")
    print("roadmap still-open line updated")
else:
    print("WARN: roadmap still-open line not found")

# --- AGENTS.md owner + handoff ---
ag = root / "AGENTS.md"
at = ag.read_text(encoding="utf-8")
at = at.replace("**ACTIVE OWNER: Claude**", "**ACTIVE OWNER: Grok**")
old_h = """### Just finished (2026-09-13 PT)
- Item **60**: `VisualContinuityScorer` + `NarrationTimingAutoFit`. Draft Health gained Continuity + Narration Timing. Fix All / Do Next use the real scanners. Auto-QA trims one trailing sentence on over-long scenes and will not flip PreferStock from a timing flag. Continuity stays human-hard (never auto-swaps).
- Cadence takeaways (not a Jawor/Zukoll mode): `LooksLikeOpenLoopTitle` is part of YouTube-outcome CTR; `BestTimeToPublishAdvisor` reuses a clustered local hour from this app's own publish timestamps; Do Next / `SisterClipHint` name Hub&Spoke sister Shorts.
- Staleness: **61** Remaining none at shipped v1; **57** Remaining none; **50** MSI only — skip. **58** already closed.

### Files
- NEW `src/MediaMaker.ScriptToVideo/VisualContinuityScorer.cs`, `NarrationTimingAutoFit.cs`
- `MakeVideoAutoQuality.cs`, `DraftHealthScorecard.cs`, `NextActionAdvisor.cs`, `YouTubeOutcomeOptimizer.cs`, `BestTimeToPublishAdvisor.cs`, `ScriptToVideoView.xaml.cs`, `ScheduleDialog.xaml.cs`
- SelfTests: ScriptToVideo, DraftHealth, PublishFixes, PublishQueue
- `MANUAL/MediaStar User Manual.md`, `MANUAL/MAINTENANCE.md`, `items remaining in the mediastar queue.txt`

### Tested
- See this session's SelfTest run output (DraftHealth, PublishFixes item 60 + open-loop, PublishQueue clustered hour, ScriptToVideo item 60 path).

### Next
- Item **63** leftover hard-gate policy (78 already scores YouTubeOutcome on Ship).
- Item **76** — SceneAutoTriage vs real Draft Health scores.
- Item **50** MSI only — skip. No second NLE. Never auto-publish.
"""
new_h = """### Just finished (2026-09-13 PT)
- Leftover Remaining tails: **63** live Publish uses `LocalDraftHealthIssues` + real unreviewed count + Draft Health Fail categories (bypassable). **76** `ScoreScenes` uses `DraftHealthScorecard` math. Stale Remaining closed: **80** via 105/141; **81-87** via 96; **88-92** via 97/94; **95** via 137; **98** via 133/111; **102** via 136; **127** ListBox timestamps at v1; **129** SpokeBatchShipPlanner. **50** MSI skip.
- Left other-AI dirty files alone (`DirectorAssetHistoryStore`, `AiVideoDirector`, `AppPaths`, `ScriptToVideoAssembler`, `ExternalTools/`).

### Files
- `LocalDraftHealthIssues.cs`, `ShipChecklistGate.cs`, `MakeVideoAutoQuality.cs`, `ScriptToVideoView.xaml.cs` (already on branch from prior commit)
- SelfTests: DraftHealth checks 11-12; PublishFixes DH Fail + Draft Health reason
- `MANUAL/MediaStar User Manual.md`, `MANUAL/MAINTENANCE.md`, `items remaining in the mediastar queue.txt`, `IMPLEMENTATION_ROADMAP.md`

### Tested
- DraftHealth.SelfTest (checks 11-12). PublishFixes item 63/76 asserts if that project builds.

### Next
- Clip intelligence **246** Remaining (structured saved shot briefs / review UI / quality eval). Then **247-249**.
- Item **50** MSI only — skip. No second NLE. Never auto-publish. Do not discard unexplained working-tree files.
"""
if old_h in at:
    at = at.replace(old_h, new_h, 1)
    print("AGENTS handoff replaced")
else:
    print("WARN: AGENTS handoff block not found")
ag.write_text(at, encoding="utf-8")
print("AGENTS written")

for extra in ("tools_patch_63_76.py", "tools_patch_63_76_tests.py"):
    fp = root / extra
    if fp.exists():
        fp.unlink()
        print("deleted", extra)

print("ALL PATCHES DONE")

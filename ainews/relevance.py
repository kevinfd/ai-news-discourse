"""AI relevance filter and organisation tagging (pure regex, no model)."""
from __future__ import annotations

import re

# Matches titles/summaries that are about AI. Word-boundary anchored so
# "AI" doesn't match "said", "Claude" doesn't match "Claudette", etc.
_AI_TERMS = [
    r"\bA\.?I\.?\b", r"\bartificial intelligence\b", r"\bmachine[- ]learning\b", r"\bdeep learning\b",
    r"\bneural net\w*", r"\bLLMs?\b", r"\blarge language models?\b", r"\blanguage models?\b",
    r"\bfoundation models?\b", r"\bgenerative\b", r"\bgen[- ]?AI\b", r"\bchatbots?\b", r"\bcopilot\b",
    r"\bChatGPT\b", r"\bGPT-?\d", r"\bOpenAI\b", r"\bAnthropic\b", r"\bClaude\b", r"\bGemini\b",
    r"\bDeepMind\b", r"\bLlama\b", r"\bMistral\b", r"\bDeepSeek\b", r"\bxAI\b", r"\bGrok\b",
    r"\bHugging ?Face\b", r"\bNvidia\b", r"\bNVIDIA\b", r"\bTPU\b", r"\bGPUs?\b", r"\bAGI\b",
    r"\bsuperintelligence\b", r"\balignment\b", r"\bRLHF\b", r"\btransformers?\b", r"\bdiffusion model",
    r"\btext-to-(image|video|speech)\b", r"\bAI (safety|agents?|regulation|policy|act|chips?|startup|lab|model|models|tools?|search|assistant|boom|bubble|race|data ?centers?)\b",
    r"\bagentic\b", r"\bMCP\b", r"\bvibe coding\b", r"\bPerplexity\b", r"\bMidjourney\b", r"\bStable Diffusion\b",
    r"\bSora\b", r"\bCursor\b", r"\bCharacter\.AI\b", r"\bSam Altman\b", r"\bDario Amodei\b", r"\bDemis Hassabis\b",
    r"\bJensen Huang\b", r"\bYann LeCun\b", r"\bGeoffrey Hinton\b", r"\bSafe Superintelligence\b", r"\bScale AI\b",
    r"\bCoreWeave\b", r"\bcompute\b", r"\bmodel weights\b", r"\bopen[- ]weights?\b", r"\binference\b",
    r"\bprompt(ing| engineering)\b", r"\bhallucinat", r"\bdeepfakes?\b", r"\brobotics?\b", r"\bhumanoid\b",
    r"\bself-driving\b", r"\bautonomous (vehicles?|driving)\b", r"\bWaymo\b", r"\bTesla (FSD|Optimus)\b",
]
_WEAK_TERMS = [
    r"\bGPUs?\b", r"\bcompute\b", r"\binference\b", r"\btransformers?\b", r"\balignment\b",
    r"\brobotics?\b", r"\bgenerative\b", r"\bcopilot\b", r"\bTPU\b", r"\bhumanoid\b", r"\bCursor\b",
]
_STRONG_TERMS = [t for t in _AI_TERMS if t not in _WEAK_TERMS]
STRONG_RE = re.compile("|".join(_STRONG_TERMS), re.IGNORECASE)
WEAK_RE = re.compile("|".join(_WEAK_TERMS), re.IGNORECASE)
AI_RE = re.compile("|".join(_AI_TERMS), re.IGNORECASE)


def is_ai_relevant(*texts: str) -> bool:
    """True when the text has one strong AI term, or two or more weak ones."""
    blob = " ".join(t for t in texts if t)
    if STRONG_RE.search(blob):
        return True
    return len(WEAK_RE.findall(blob)) >= 2


# Organisations / products worth a metadata column for "who is this about".
ORG_PATTERNS: list[tuple[str, str]] = [
    ("OpenAI", r"\bOpenAI\b|\bChatGPT\b|\bGPT-?\d|\bSora\b|\bSam Altman\b"),
    ("Anthropic", r"\bAnthropic\b|\bClaude\b|\bDario Amodei\b"),
    ("Google", r"\bGoogle\b|\bDeepMind\b|\bGemini\b|\bAlphabet\b|\bDemis Hassabis\b|\bSundar Pichai\b"),
    ("Meta", r"\bMeta\b|\bLlama\b|\bZuckerberg\b|\bFacebook\b|\bInstagram\b"),
    ("Microsoft", r"\bMicrosoft\b|\bCopilot\b|\bAzure\b|\bSatya Nadella\b"),
    ("Nvidia", r"\bNvidia\b|\bNVIDIA\b|\bJensen Huang\b"),
    ("Apple", r"\bApple\b|\bSiri\b|\bApple Intelligence\b"),
    ("Amazon", r"\bAmazon\b|\bAWS\b|\bAlexa\b|\bBedrock\b"),
    ("xAI", r"\bxAI\b|\bGrok\b"),
    ("Mistral", r"\bMistral\b"),
    ("DeepSeek", r"\bDeepSeek\b"),
    ("Hugging Face", r"\bHugging ?Face\b"),
    ("Perplexity", r"\bPerplexity\b"),
    ("Tesla", r"\bTesla\b|\bElon Musk\b|\bOptimus\b"),
    ("Alibaba", r"\bAlibaba\b|\bQwen\b"),
    ("Baidu", r"\bBaidu\b|\bERNIE\b"),
    ("ByteDance", r"\bByteDance\b|\bTikTok\b"),
    ("Samsung", r"\bSamsung\b"),
    ("Intel", r"\bIntel\b"),
    ("AMD", r"\bAMD\b"),
    ("TSMC", r"\bTSMC\b"),
    ("Oracle", r"\bOracle\b"),
    ("Salesforce", r"\bSalesforce\b"),
    ("IBM", r"\bIBM\b"),
    ("Cohere", r"\bCohere\b"),
    ("Stability AI", r"\bStability AI\b|\bStable Diffusion\b"),
    ("Midjourney", r"\bMidjourney\b"),
    ("Scale AI", r"\bScale AI\b"),
    ("CoreWeave", r"\bCoreWeave\b"),
    ("SoftBank", r"\bSoftBank\b|\bMasayoshi Son\b"),
    ("Waymo", r"\bWaymo\b"),
    ("Cursor", r"\bCursor\b|\bAnysphere\b"),
    ("Safe Superintelligence", r"\bSafe Superintelligence\b|\bIlya Sutskever\b"),
    ("Thinking Machines", r"\bThinking Machines\b|\bMira Murati\b"),
    ("Character.AI", r"\bCharacter\.?AI\b"),
    ("EU", r"\bEuropean (Union|Commission)\b|\bEU AI Act\b|\bthe EU\b"),
    ("US government", r"\bWhite House\b|\bCongress\b|\bFTC\b|\bSEC\b|\bPentagon\b|\bDepartment of (Commerce|Defense|Justice)\b|\bNIST\b|\bexecutive order\b"),
    ("China", r"\bChina\b|\bChinese\b|\bBeijing\b"),
    ("UK", r"\bUK\b|\bBritain\b|\bBritish\b|\bDowning Street\b"),
]
_ORG_COMPILED = [(name, re.compile(p)) for name, p in ORG_PATTERNS]


def detect_orgs(text: str, max_orgs: int = 8) -> list[str]:
    """Return orgs mentioned, ordered by mention count (ties: pattern order)."""
    if not text:
        return []
    counts = []
    for name, rx in _ORG_COMPILED:
        n = len(rx.findall(text))
        if n:
            counts.append((n, name))
    counts.sort(key=lambda t: -t[0])
    return [name for _, name in counts[:max_orgs]]


# Coarse topic tags from keyword families (cheap, deterministic; the map's own
# topic model does the real work — these are for filtering).
TOPIC_PATTERNS: list[tuple[str, str]] = [
    ("models & research", r"\b(model|benchmark|paper|research|weights|parameters|training|reasoning|multimodal|open[- ]source)\b"),
    ("products & launches", r"\b(launch(es|ed)?|releases?|unveils?|announces?|rolls? out|new feature|app|update)\b"),
    ("business & funding", r"\b(funding|raises?|valuation|IPO|acquisition|acquires?|revenue|investors?|startup|deal|billion|million|stock|shares|earnings)\b"),
    ("policy & regulation", r"\b(regulat\w+|law|bill|legislation|policy|government|congress|senate|EU AI Act|executive order|ban|antitrust|lawsuit|court|copyright|FTC)\b"),
    ("safety & ethics", r"\b(safety|alignment|risk|bias|ethic\w*|misinformation|deepfake|harm|existential|superintelligence|AGI|guardrails?)\b"),
    ("chips & infrastructure", r"\b(chips?|GPUs?|semiconductor|data ?cent(er|re)s?|compute|TSMC|Nvidia|energy|power grid|nuclear|cloud)\b"),
    ("jobs & society", r"\b(jobs?|workers?|layoffs?|employment|labor|labour|education|students?|schools?|teachers?|society|culture|art(ists)?|writers?)\b"),
    ("agents & coding", r"\b(agents?|agentic|coding|developers?|programming|Copilot|Cursor|MCP|automation|workflow)\b"),
    ("robotics & autonomy", r"\b(robots?|robotics|humanoid|self-driving|autonomous|Waymo|drones?)\b"),
    ("health & science", r"\b(health|medical|drug|protein|biology|climate|science|scientists|hospital|patients?)\b"),
    ("search & media", r"\b(search|Google Search|news|media|publishers?|journalis\w+|advertis\w+|social media|YouTube|TikTok)\b"),
]
_TOPIC_COMPILED = [(name, re.compile(p, re.IGNORECASE)) for name, p in TOPIC_PATTERNS]


def detect_topics(text: str, max_topics: int = 4) -> list[str]:
    if not text:
        return []
    scored = []
    for name, rx in _TOPIC_COMPILED:
        n = len(rx.findall(text))
        if n >= 2:
            scored.append((n, name))
    scored.sort(key=lambda t: -t[0])
    return [name for _, name in scored[:max_topics]]

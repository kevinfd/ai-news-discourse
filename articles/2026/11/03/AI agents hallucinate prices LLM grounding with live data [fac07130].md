---
id: "fac07130e6cf81d5"
title: "AI agents hallucinate prices: LLM grounding with live data"
url: "https://blog.apify.com/llm-grounding-with-live-data"
link: "https://blog.apify.com/llm-grounding-with-live-data"
source: "Apify Blog"
domain: "blog.apify.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-03T10:41:28Z"
published_date: "2026-11-03"
collected_at: "2026-11-03T13:04:23Z"
authors: ["Dylan-Hayes"]
language: "en"
summary: "Ask an AI agent with no tools what a Kindle Paperwhite costs, and it can answer $159.99, the old launch price. The live price at the time of testing was $199.99. In tests, GPT-6 Luna and Claude Opus 5.5 each matched the live price exactly for 2 of 15 products from memory. With built-in web search, they gave more exact prices, but every run still had wrong prices, each with a source link.\nLarge…"
tags: []
orgs: ["Amazon", "Anthropic", "OpenAI"]
topics: ["agents & coding", "models & research", "search & media"]
content_source: "fulltext"
word_count: 6681
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50350302"
score: 15
comments: 0
community: "Hacker News"
---

# AI agents hallucinate prices: LLM grounding with live data

Apify Blog · Dylan-Hayes · 2026-11-03

Ask an AI agent with no tools what a Kindle Paperwhite costs, and it can answer $159.99, the old launch price. The live price at the time of testing was $199.99. In tests, GPT-6 Luna and Claude Opus 5.5 each matched the live price exactly for 2 of 15 products from memory. With built-in web search, they gave more exact prices, but every run still had wrong prices, each with a source link.
Large language model (LLM) grounding is the standard way to stop both kinds of wrong price, from memory and from web search. A grounded agent answers only from data that it fetched for the question, and every answer shows where that data came from. For prices, a grounded agent needs live data, a clear status when a check fails, and code, not the model, that writes each price into the answer.
The Python agent below has each of these. It gets live prices from E-commerce Scraping Tool, a ready-to-run tool on the Apify marketplace. Apify calls these tools Actors. First, the tests show where wrong prices come from. Then you build the agent and test it step by step.
Why AI agents hallucinate prices
If your agent shows prices, a wrong one can reach your user in 3 main ways. The model answers from memory, it reads a bad page, or a tool says "ok" when it failed. The tests below check the first 2, on 21 live product pages from Amazon, Walmart, Best Buy, Target, and 4 Shopify stores. A research study tests the third.
The live prices come from E-commerce Scraping Tool, and an independent check with a separate scraping service, from US IP addresses, matched the Actor on all 21 pages. The results include only the 15 products with a single clear price for a new item, as a US shopper sees it without member discounts or coupons. A price is exact only when it matches the live price to the cent. The other 6 pages showed no price, or an unclear seller or size. The 15 prices didn't change while the models answered.
From memory
An LLM learns prices during training, and many of those prices change before a user asks. With no tools, gpt-6-luna and Claude Opus 5.5 gave these results. The last row adds the prompt "If you cannot know the current price, answer UNKNOWN":
Without the UNKNOWN prompt, Claude Opus 5.5 added a clear warning, such as "I can't check live prices," to all 21 answers. Each answer still included a price, and agent code reads the number, not the warning. So a prompt alone gave the user either a guess or nothing.
Prices can also change fast. The AirPods Pro 3 at Best Buy went from $199.99 to $249.99 in the 3 days before the models were asked. Even a price from last week can mislead your user.
From a bad page
When your agent fetches pages itself, the page can be the wrong one, even when it loads normally.
- Wrong country. A request from outside the US received an Amazon page in Indian rupees. The model read it correctly and answered INR 7,503.02 for an Instant Pot that cost $79 in the US.
- Wrong seller. An Amazon page showed "No featured offers available." The model answered $71.89. That price came from the line "Other sellers on Amazon New & Used (2) from $71.89," not from the Buy Box, the main offer on an Amazon page.
- Wrong variant. Target redirected the link for the black Kindle Paperwhite to its parent product page, and Owala redirected its FreeSip link to the 32 oz size. A price from the new page can belong to another variant.
Code can detect each of these cases, because the data shows the currency, the seller, and the final page URL.
From a tool that says "ok" when it failed
The preprint Fabrication after tool failure, a study shared before peer review, tested what models do when a tool returns bad data. When the tool returned "ok" with bad data, such as an empty, outdated, or incomplete result, up to 45.3% of answers were dishonest. A dishonest answer hid the failure. When the tool returned an error status instead, the study reported 0% dishonest answers. So a price tool that reports a clear status or error helps the agent give honest answers.
What the 3 causes have in common
In all 3 causes, the wrong price looks like a normal answer, and nothing tells the user that something failed. The scraper tests show this. In 3 test runs, a simple do-it-yourself (DIY) scraper received 26 block pages. A block page is what a store shows when it blocks a request, such as Walmart's "Robot or human?" page or Amazon's "Continue shopping" page. The model answered "no price" for all 26. Those answers were honest, but the user still got no price. Every clearly wrong price in these tests came from a page that looked normal.
So live data alone isn't enough. The agent also needs a clear status for every price, so that code can flag a wrong page even when it looks normal. Built-in web search adds live data, but it doesn't give a clear status or code that writes each price into the answer.
Way 1: price extraction without Apify
Agent builders usually start with one of two options: the model's built-in web search or a scraper they write themselves.
With the model's built-in web search
The model provider runs the search, and your code only enables 1 setting. In this setup, each model answered 3 times for each of the same 15 products:
Web search gave many more exact prices than memory, but every wrong price included a source link. Those links went to price tracker sites, store search pages, and pages for other products. This was the answer from Claude Opus 5.5 for the Dyson V15 Detect at Best Buy, where the live price was $899.99:
{"price": 629.99, "currency": "USD", "source_url": "https://www.bestbuy.com/product/dyson-v15-detect-extra-cordless-vacuum-with-10-accessories-yellow-nickel/J3ZCSY279C"}
The link opens a different product, the V15 Detect Extra. If your agent uses web search for prices, a wrong price looks the same as a correct one, because each answer cites a source.
With your own scraper
The DIY scraper fetched each product page and read the schema.org offers object, which many stores add to the page as JSON-LD (structured data for search engines). When a page had no JSON-LD price, gpt-6-luna read the page text instead. The same scraper ran from a US cloud server and from a computer outside the US, with 2 HTTP clients. httpx is a standard Python client, and curl_cffi copies the TLS fingerprint of a real Chrome browser. The last row shows the better of the 2 clients for each location:
These are 2 of the pages that the DIY scraper received:
Patchright is an open-source version of Playwright that hides browser automation. With Patchright and Chrome, the scraper got the exact price for 7 of 15 products from outside the US. Walmart still showed the "Robot or human?" page, and Amazon and most Target pages showed no US price. All these results come from basic scrapers with no proxies. A production scraper needs US residential proxies and code for each store, which means more cost and maintenance for your team.
Experienced scraper builders often try other sources before a browser. These include the site's internal API, the /products/<handle>.js endpoint on many Shopify stores, and official APIs such as the Best Buy Products API. Each works for only some stores. In the test, the Shopify endpoint worked on 2 of the 4 Shopify stores. For the basics of DIY scraping, see how to scrape prices from websites with Python.
Way 2: price extraction with E-commerce Scraping Tool
E-commerce Scraping Tool (apify/e-commerce-scraping-tool) gets product data, including prices, from product URLs on Amazon, Walmart, Best Buy, Target, Shopify stores, and many more. It returns the same output format for every store, with fields such as offers.price, offers.priceCurrency, url, and scrapedAt. It manages proxies and browser rendering itself, so your code doesn't need extra logic for block pages or for getting the US version of a page. With scrapeMode set to AUTO, it chooses plain HTTP or a full browser for each page. With additionalProperties set to true, it also returns the seller and the condition of the Buy Box offer when the store shows them. The condition tells you whether the offer is new or used.
Install the Apify API client for Python:
pip install apify-client==3.3.0
Then set APIFY_TOKEN in your environment and call the Actor with your product URLs:
import os
from apify_client import ApifyClient
urls = ["https://www.amazon.com/dp/B0F3PT1VBL"]
client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("apify/e-commerce-scraping-tool").call(
    run_input={
        "detailsUrls": [{"url": u} for u in urls],
        "scrapeMode": "AUTO",
        "additionalProperties": True,
    }
)
for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item["inputUrl"], item.get("offers"), item["scrapedAt"])
The output:
https://www.amazon.com/dp/B0F3PT1VBL {'price': 458, 'priceCurrency': '$'} 2026-10-24T04:24:36.009Z
This is the same run in Apify Console:
In test runs on 4 different days, the Actor returned a price or a clear "no price" for every one of the 21 pages. This included the Amazon, Walmart, and Best Buy pages where the DIY scraper received block pages or timeouts. With a clear "no price," the agent can say "not available" instead of guessing. Where a store showed no price, such as a sold-out Best Buy product, the independent check also found none.
The Apify Free plan includes $5 of usage every month, enough for hundreds of live price checks. The Actor's pricing page shows the current prices on each plan.
For live price checks, start a separate Actor run for each product, and run them in parallel. Your agent then receives each price as soon as its own run finishes. To fill a cache, 1 run is enough for the whole catalog.
Web search, DIY scraper, Shopify, store APIs, and Apify compared
The tables below compare 5 price sources for an agent, 1 in each row. The Shopify row covers 2 options. One is the /products/<handle>.js endpoint from Way 1. The other is Shopify's endpoint for the Model Context Protocol (MCP), called Shop MCP. In the tests, Shop MCP returned products from each Shopify store's catalog, and the agent had to match the exact variant itself.
What each source covers and returns:
What each source takes to run:
The agent below uses E-commerce Scraping Tool because it returns the same format for every store and a clear "no price" when a store shows none.
Build a grounded price agent
The agent uses 4 files, catalog.json, prices.py, agent.py, and refresh.py. Step 4 adds a test script, eval_short.py. This is how a price moves from the store page to the answer:
Before you start
You need Python 3.11 to 3.14, an Apify account (the Free plan needs no credit card), and an OpenAI API key. Install the packages:
pip install apify-client==3.3.0 openai==3.35.1 python-dotenv==1.1.1
Find your Apify token in Apify Console. Then create a project folder with a .env file:
APIFY_TOKEN=your_apify_token
OPENAI_API_KEY=your_openai_key
OPENAI_MODEL=gpt-6-luna
Add a catalog.json file with the products your agent can check. For a product with colors or sizes, link to the exact variant, because a product URL without one usually shows the default variant.
E-commerce Scraping Tool can also help you find product URLs. It searches by keyword on the marketplaces you choose. Search results often list each model and color separately, so you can choose the exact one for your catalog.
This catalog has the 7 entries that the examples in Step 3 use. Add your own products the same way:
[
  {"store": "Amazon", "product": "Sony WH-1000XM6 headphones", "url": "https://www.amazon.com/dp/B0F3PT1VBL", "currency": "USD"},
  {"store": "Walmart", "product": "Sony WH-1000XM6 headphones", "url": "https://www.walmart.com/ip/Sony-WH1000XM6-Noise-Canceling-Wireless-Over-Ear-Headphones/16504921979", "currency": "USD"},
  {"store": "Best Buy", "product": "Sony WH-1000XM6 headphones", "url": "https://www.bestbuy.com/product/sony-wh-1000xm6-best-wireless-noise-cancelling-headphones-black/J7XSRH5RCF", "currency": "USD"},
  {"store": "Target", "product": "Sony WH-1000XM6 headphones", "url": "https://www.target.com/p/sony-wireless-noise-canceling-headphones-black/-/A-94649372", "currency": "USD"},
  {"store": "Walmart", "product": "Instant Pot Duo 7-in-1 6 qt", "url": "https://www.walmart.com/ip/Instant-Pot-DUO60-V4-6-Quart-Duo-Electric-Pressure-Cooker-Slow-Cooker/45918917", "currency": "USD"},
  {"store": "Best Buy", "product": "Instant Pot Duo 7-in-1 6 qt", "url": "https://www.bestbuy.com/product/instant-pot-6-quart-duo-7-in-1-electric-pressure-cooker-silver-brushed-stainless-steel/J3RK3ZJ866", "currency": "USD"},
  {"store": "Amazon", "product": "Dyson V15 Detect cordless vacuum", "url": "https://www.amazon.com/dp/B0C2J8KJH9", "currency": "USD"}
]
By the end of Step 4, the project folder looks like this:
price-agent/
├── .env
├── catalog.json
├── prices.py
├── agent.py
├── refresh.py
├── eval_short.py
└── price_cache.json
Step 1. Build the price tool
prices.py fetches prices from E-commerce Scraping Tool, gives every product a status, and names the seller when the Buy Box offer comes from a seller other than the store. The status flags cases such as a sold-out item, another currency, or a redirect, even when the page looks normal. Each status comes from fields that the Actor returns, such as the price, the final page URL, the seller, and the condition.
- ok means the price came from the page at the catalog URL.
- no_price means the page showed no price.
- other_currency means the price isn't in the currency that the catalog lists for that store.
- used means the Buy Box offer is for a used item, such as "Used - Like New."
- moved_page means the store redirected the request to a different page, such as a parent product page.
- big_change means the price moved more than 30% from its reference price, the last ok price in the cache. This can be a normal price change, or a different seller, size, or condition, so the agent asks before it acts. The flag stays for 1 day, so every check during that day reports it. After that, the new price becomes the reference.
- not_live means the answer uses the last known price and its time instead of a live result.
Set the change threshold for your products. In the tests, a 30% threshold flagged the Amazon Dyson listing when its price fell from $789.49 to $377.99 within 3 days. The same threshold didn't flag a normal 25% price change on AirPods at Best Buy, a few days before the models answered.
Browsing questions use a cached price up to 1 hour old. Decisions, such as a purchase or a price alert, get a live price check, because the prompt tells the model to set need_live to true for them. In your own checkout code, call asyncio.run(get_prices(products, need_live=True)) directly, so the live price check doesn't depend on the model. Set TIME_LIMIT to the longest wait your users accept. A check that takes longer returns the last known price, if there is one, with the not_live status. A failed run, or a run with no result for the page, works the same way, so a failed check never becomes a new no_price row.
The file has 5 parts:
- make_row() converts 1 Actor result into a row with a status.
- check_live() sends 1 product to the Actor and waits up to TIME_LIMIT for the result.
- compare() flags a big price change and keeps the flag for 1 day.
- get_prices() uses the cache for browsing and a live price check for decisions.
- refresh_all() and load_from_task() fill the cache from 1 run or from a scheduled task.
This is prices.py:
import asyncio
import json
import os
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse
from apify_client import ApifyClientAsync
ACTOR = "apify/e-commerce-scraping-tool"
CACHE_FILE = Path("price_cache.json")
TIME_LIMIT = timedelta(
    seconds=60
)  # longest wait for a live price check before an action
MAX_PARALLEL = 4  # live price checks that run at the same time
MAX_AGE = timedelta(hours=1)  # browsing answers may use prices up to this old
BIG_CHANGE = 0.3  # a price that moved more than 30% from the reference price
HOLD = timedelta(
    days=1
)  # a big change stays flagged this long, then becomes the new reference
DOLLAR = {
    ".ca": "CAD",
    ".com.au": "AUD",
    ".com.mx": "MXN",
}  # "$" on these sites isn't USD; add the domains in your catalog
def to_number(value):
    """Return the price as a number."""
    if value in (None, ""):
        return None
    text = str(value)
    if re.search(r",\d{2}$", text):  # "1.299,00" style
        text = text.replace(".", "").replace(",", ".")
    match = re.search(r"\d[\d,]*\.?\d*", text)
    return float(match.group().replace(",", "")) if match else None
def to_currency(value, expected, url):
    """Return the currency code, with the catalog currency as the default."""
    if value in (None, ""):
        return expected
    if value == "$":
        host = urlparse(url).netloc
        return next((code for end, code in DOLLAR.items() if host.endswith(end)), "USD")
    return "USD" if value in ("US$", "USD") else value
def seller_and_condition(item):
    """Return the seller and condition of the Buy Box offer."""
    extra = item.get("additionalProperties") or {}
    main = next(
        (s for s in extra.get("sellerOffers") or [] if s.get("isBuyBoxWinner")), {}
    )
    seller = main.get("sellerName") or extra.get("seller")
    if isinstance(seller, dict):
        seller = seller.get("name")
    return seller, main.get("condition")
def make_row(item, product):
    offer = item.get("offers") or {}
    price = to_number(offer.get("price"))
    currency = to_currency(
        offer.get("priceCurrency"),
        product["currency"],
        item.get("url") or product["url"],
    )
    same_page = item.get("url", "").split("?")[0].rstrip("/") == product["url"].split(
        "?"
    )[0].rstrip("/")
    seller, condition = seller_and_condition(item)
    if price is None:
        status = "no_price"
    elif currency != product["currency"]:
        status = "other_currency"
    elif condition and not condition.lower().startswith("new"):
        status = "used"
    elif not same_page:
        status = "moved_page"
    else:
        status = "ok"
    return {
        "store": product["store"],
        "product": product["product"],
        "url": product["url"],
        "price": price,
        "currency": currency,
        "seller": seller,
        "condition": condition,
        "checked_at": item.get("scrapedAt"),
        "status": status,
    }
async def check_live(client, limit, product):
    """Send one product to the Actor and wait up to TIME_LIMIT for its result."""
    async with limit:
        run = await client.actor(ACTOR).start(
            run_input={
                "detailsUrls": [{"url": product["url"]}],
                "scrapeMode": "AUTO",
                "additionalProperties": True,
            }  # adds the seller and condition
        )
        finished = await client.run(run.id).wait_for_finish(wait_duration=TIME_LIMIT)
        if finished is None or finished.status in ("READY", "RUNNING"):
            await client.run(run.id).abort()  # end the run when the agent stops waiting
            return None
        if finished.status != "SUCCEEDED":
            return None
        run = finished
    items = [i async for i in client.dataset(run.default_dataset_id).iterate_items()]
    return make_row(items[0], product) if items else None
def compare(row, old):
    """Mark a price that moved a lot from the reference price. It can be a real price drop,
    or a different seller, size, or condition, so the agent asks before acting."""
    old = old or {}
    ref = old.get("reference_price") or (
        old.get("price") if old.get("status") == "ok" else None
    )
    if (
        ref
        and row["price"]
        and row["status"] == "ok"
        and abs(row["price"] - ref) / ref > BIG_CHANGE
    ):
        since = old.get("changed_since") or row["checked_at"]
        if age({"checked_at": since}) < HOLD:  # refreshes keep the flag for a day
            return {
                **row,
                "status": "big_change",
                "previous_price": ref,
                "reference_price": ref,
                "changed_since": since,
            }
    return {**row, "reference_price": row["price"] if row["status"] == "ok" else ref}
def load_cache():
    return json.loads(CACHE_FILE.read_text()) if CACHE_FILE.exists() else {}
def age(row):
    if not row.get("checked_at"):
        return timedelta.max
    checked = datetime.fromisoformat(row["checked_at"].replace("Z", "+00:00"))
    return datetime.now(timezone.utc) - checked
async def get_prices(products, need_live):
    """Browsing questions use a cached price up to MAX_AGE old.
    Calls with need_live=True (an alert, a checkout, an approval) always get a live price check.
    """
    client = ApifyClientAsync(os.environ["APIFY_TOKEN"])
    limit = asyncio.Semaphore(MAX_PARALLEL)
    cache = load_cache()
    rows, to_check = {}, []
    for product in products:
        cached = cache.get(product["url"])
        if not need_live and cached and age(cached) <= MAX_AGE:
            rows[product["url"]] = cached
        else:
            to_check.append(product)
    results = await asyncio.gather(*(check_live(client, limit, p) for p in to_check))
    for product, row in zip(to_check, results, strict=True):
        if row:
            row = compare(row, cache.get(product["url"]))
            cache[product["url"]] = row
            rows[product["url"]] = row
        elif product["url"] in cache:
            # Use the last known price, with its time, and mark it
            # so the agent says it's not live.
            cached = cache[product["url"]]
            status = (
                "not_live"
                if cached["status"] in ("ok", "moved_page", "big_change", "used")
                else cached["status"]
            )
            rows[product["url"]] = {**cached, "status": status}
        else:
            rows[product["url"]] = {
                **product,
                "price": None,
                "checked_at": None,
                "status": "not_live",
            }
    CACHE_FILE.write_text(json.dumps(cache, indent=1))
    return [rows[p["url"]] for p in products]
async def save_items(dataset, products):
    """Convert a dataset of Actor results into cache rows."""
    by_url = {p["url"]: p for p in products}
    cache = load_cache()
    async for item in dataset.iterate_items():
        product = by_url.get(item.get("inputUrl"))
        if product:
            cache[product["url"]] = compare(
                make_row(item, product), cache.get(product["url"])
            )
    CACHE_FILE.write_text(json.dumps(cache, indent=1))
    return cache
async def refresh_all(products):
    """Fill the cache for every product in one run. Run it every 30 minutes."""
    client = ApifyClientAsync(os.environ["APIFY_TOKEN"])
    run = await client.actor(ACTOR).call(
        run_input={
            "detailsUrls": [{"url": p["url"]} for p in products],
            "scrapeMode": "AUTO",
            "additionalProperties": True,
        }
    )
    return await save_items(client.dataset(run.default_dataset_id), products)
async def load_from_task(task_id, products):
    """Fill the cache from the last successful run of a scheduled Apify task."""
    client = ApifyClientAsync(os.environ["APIFY_TOKEN"])
    last_run = client.task(task_id).last_run(status="SUCCEEDED")
    return await save_items(last_run.dataset(), products)
Step 2. Build an agent where code inserts each price
A common grounding check compares the numbers in the answer with the numbers in the tool output. The test catalog was larger than the 7 entries above and included the Kindle Paperwhite. These 5 wrong answers use only prices from that tool output, such as $199.99, the Kindle's price. This grounding check passes all of them, and the validator in the agent below rejects all of them:
The check proves that a number exists in the data. It doesn't prove that the number belongs to that product and that store. A source link has the same weakness, because a user can only check it after reading the answer. So in the agent below, the model writes placeholders, code inserts each price from the data, and the validator checks the answer before the user sees it. Apify CEO Jan Čurn describes the same approach in his talk at the Prague Crawl conference, MCP doesn't suck, your agent does.
agent.py uses the OpenAI Responses API with 1 tool, get_prices. The placeholders look like {{offer:r1}} or {{cheapest}}. For {{cheapest}}, code chooses the cheapest offer among rows with the status ok. The cheapest offer is based on listed prices. Before a purchase, take the final total, with shipping and tax, from the store's checkout.
Rows with no price, or with a price in another currency, get no placeholder. Code adds them to the end of the answer, together with any checked offer that the model skipped. The tool schema lists the catalog URLs as an enum, so the model can choose only those URLs.
The validator rejects an answer when any of these is true:
- The model typed a currency sign or code.
- The model typed a price with cents.
- The model typed a capitalized store name, such as "Target."
- The answer names a product with no offer in it.
- The answer calls an offer the lowest without {{cheapest}}.
Each inserted offer names its product, so the reader sees which product each price belongs to. The validator returns the error to the model up to 2 times. After that, the agent returns a short fallback message. The validator doesn't check plain numbers with no currency sign, such as "458." For those, the prompt adds a second check and tells the model not to write prices.
The file has 4 parts:
- SYSTEM tells the model to write placeholders and never a price or a store name.
- run_tool() calls get_prices() and gives each row a row_id.
- render() runs the validator checks, then replaces each placeholder with data from the rows.
- ask() runs the loop and gives the model 2 retries after a rejected draft.
This is agent.py:
"""A price agent in which code inserts each price. The model writes {{offer:r1}},
and code inserts the price, store, time, and status from live data."""
import asyncio
import json
import os
import re
import sys
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI  # noqa: E402
from prices import get_prices  # noqa: E402
MODEL = os.environ.get(
    "OPENAI_MODEL", "gpt-6-luna"
)  # set OPENAI_MODEL in .env to use another model
MAX_TURNS = 8  # stop a model that keeps calling tools
FALLBACK = "Sorry, I could not answer that. Please ask again."
CATALOG = json.load(open("catalog.json"))
# A brand store, such as Ridge for a Ridge wallet, shares its name with the
# product, so the model may write it. Every other store name must come from code.
STORES = sorted(
    {
        p["store"]
        for p in CATALOG
        if not any(p["store"].lower() in q["product"].lower() for q in CATALOG)
    }
)
SYMBOL = {"USD": "$", "EUR": "€", "GBP": "£"}
oa = OpenAI()
TOOLS = [
    {
        "type": "function",
        "name": "get_prices",
        "description": "Get prices for products from the catalog. Each row has a row_id and a status.",
        "parameters": {
            "type": "object",
            "properties": {
                # The enum lets the model choose only catalog URLs, so a typo can't create a new one.
                "urls": {
                    "type": "array",
                    "items": {"type": "string", "enum": [p["url"] for p in CATALOG]},
                },
                "need_live": {
                    "type": "boolean",
                    "description": "true before a purchase, a price alert, or an approval. false for browsing questions.",
                },
            },
            "required": ["urls", "need_live"],
            "additionalProperties": False,  # JSON Schema rule: no other arguments
        },
        "strict": True,
    }
]
SYSTEM = (
    "You answer questions about product prices in one or two full sentences, starting "
    "with the answer. Never write a price, a currency, "
    "or a store name yourself. Refer to each offer only as {{offer:ROW_ID}}, using "
    "row_id values from get_prices, and use a placeholder for every row the user asked "
    "about. Code fills in the price, product, store, and time. Each placeholder becomes a full phrase, "
    "such as '$458.00 for the Sony WH-1000XM6 headphones at Amazon (checked ...)', so do not "
    "repeat the price, product, or store it names, and use each "
    "placeholder only once. Rows with no usable price have no row_id. Code adds them to the "
    "answer, so do not mention them. If no row has a usable price, write one short sentence "
    "saying that it has no listed price right now. "
    "To name the cheapest offer for one product, write {{cheapest}} and code fills in every offer at "
    "the lowest price. "
    "Set need_live to true only before a purchase, a price alert, or an approval. Words like "
    "'today' or 'now' in a question do not make it a purchase. If a status is not_live and the "
    "user wants to act, say you could not confirm the live price. If a status is big_change, "
    "give the offer first, then ask the user to confirm the new price before acting. "
    "If a status is used, say that the offer is for a used item. "
    "If a product is not in the catalog, say you cannot check it.\nCatalog:\n"
    + json.dumps([{k: p[k] for k in ("store", "product", "url")} for p in CATALOG])
)
ANSWER_FORMAT = {
    "type": "json_schema",
    "name": "answer",
    "strict": True,
    "schema": {
        "type": "object",
        "properties": {"text": {"type": "string"}},
        "required": ["text"],
        "additionalProperties": False,
    },
}
PLACEHOLDER = re.compile(r"\{\{offer:(r\d+)\}\}|\{\{cheapest\}\}")
MONEY = re.compile(
    r"[$€£₹]|\b(USD|EUR|GBP|INR|dollars?|euros?)\b|\b\d+\.\d{2}\b", re.IGNORECASE
)
# Words that name each catalog product, such as "sony" or "kindle".
PRODUCT_WORDS = {
    p["product"]: {
        w for w in re.findall(r"[\w-]+", p["product"].lower())[:2] if len(w) > 3
    }
    for p in CATALOG
}
SUPERLATIVE = re.compile(
    r"\b(cheapest|lowest|least expensive|best price)\b", re.IGNORECASE
)
STORE_NAME = re.compile(
    r"\b(" + "|".join(map(re.escape, STORES)) + r")\b"
)  # capitalized store names only
STATUS_NOTE = {
    "ok": "",
    "moved_page": ", the store redirected this link",
    "not_live": ", last known price, not live",
}
def typed_fact(text):
    """Find a currency sign or code, a price with cents, or a capitalized store name the model typed."""
    text = PLACEHOLDER.sub("", text)
    return MONEY.search(text) or STORE_NAME.search(text)
def join(parts):
    return parts[0] if len(parts) == 1 else ", ".join(parts[:-1]) + ", and " + parts[-1]
rows = {}
cheapest = []
unpriced = []  # rows with no usable price, which code adds to the answer
def run_tool(urls, need_live):
    products = [p for p in CATALOG if p["url"] in urls]
    found = asyncio.run(get_prices(products, need_live))
    out = []
    for row in found:
        if row["price"] is None or row["status"] == "other_currency":
            if row not in unpriced:
                unpriced.append(row)
            out.append(
                {
                    "store": row["store"],
                    "product": row["product"],
                    "status": row["status"],
                    "price": None,
                    "note": "code adds this row to the answer",
                }
            )
            continue
        row_id = f"r{len(rows) + 1}"
        rows[row_id] = row
        out.append(
            {
                "row_id": row_id,
                "store": row["store"],
                "product": row["product"],
                "status": row["status"],
                "price": row["price"],
            }
        )
    # The cheapest offer covers every row in this answer, not only this tool call.
    priced = {
        rid: r
        for rid, r in rows.items()
        if r["price"] is not None and r["status"] == "ok"
    }
    low = min(priced.values(), key=lambda r: r["price"])["price"] if priced else None
    cheapest[:] = [rid for rid, r in priced.items() if r["price"] == low]
    return {"rows": out}
def describe(row):
    """Convert a row into the phrase that replaces its placeholder."""
    if row["price"] is None and row["status"] == "not_live":
        return f"Price not confirmed for the {row['product']} at {row['store']}"
    if row["price"] is None or row["status"] == "no_price":
        return f"{row['store']} shows no price for the {row['product']}"
    if row["status"] == "other_currency":
        return f"No price in the expected currency for the {row['product']} at {row['store']}"
    checked = datetime.fromisoformat(row["checked_at"].replace("Z", "+00:00"))
    sign = SYMBOL.get(row["currency"], row["currency"] + " ")
    price = f"{sign}{row['price']:,.2f}"
    note = STATUS_NOTE.get(row["status"], "")
    if row["status"] == "big_change":
        note = f", was {sign}{row['previous_price']:,.2f} before the change"
    if row["status"] == "used" or (
        row["status"] == "not_live"
        and row.get("condition")
        and not row["condition"].lower().startswith("new")
    ):
        note += f", {row['condition']}"
    seller = row.get("seller")
    if seller and row["store"].lower() not in seller.lower():
        note = f", sold by {seller}" + note  # another seller on the store's site
    return f"{price} for the {row['product']} at {row['store']} (checked {checked:%H:%M} UTC on {checked:%B} {checked.day}{note})"
def render(text):
    """Reject any price or store name the model typed. Fill every placeholder from data."""
    if typed_fact(text):
        return (
            None,
            "You typed a price, currency, or store name. Use only {{offer:ROW_ID}} placeholders.",
        )
    if SUPERLATIVE.search(PLACEHOLDER.sub("", text)) and "{{cheapest}}" not in text:
        return None, "To name the lowest price, use {{cheapest}}, which code fills in."
    if "{{cheapest}}" in text and len({r["product"] for r in rows.values()}) > 1:
        return (
            None,
            "Use {{cheapest}} only when the answer covers one product. Use {{offer:ROW_ID}} instead.",
        )
    ids = [i for i in PLACEHOLDER.findall(text) if i] + (
        cheapest if "{{cheapest}}" in text else []
    )
    offered = {rows[i]["product"] for i in ids if i in rows} | {
        r["product"] for r in unpriced
    }
    words = set(re.findall(r"[\w-]+", PLACEHOLDER.sub("", text).lower()))
    if any(w & words for p, w in PRODUCT_WORDS.items() if p not in offered):
        return (
            None,
            "You named a product that has no offer in your answer. Name only the products of the offers you use.",
        )
    used = set()
    def fill(match):
        if match.group(1) is None:  # {{cheapest}}
            if not cheapest:
                return "no confirmed price"
            used.update(cheapest)
            return join([describe(rows[r]) for r in cheapest])
        row = rows.get(match.group(1))
        if row is None:
            raise KeyError(match.group(1))
        used.add(match.group(1))
        return describe(row)
    try:
        answer = PLACEHOLDER.sub(fill, text).strip()
        others = [
            describe(r) for rid, r in rows.items() if rid not in used
        ]  # offers the model skipped
        if (unpriced or others) and answer and answer[-1] not in ".!?":
            answer += "."
        lead = "Another offer is" if len(others) == 1 else "Other offers are"
        extra = [f"{lead} {join(others)}."] if others else []
        answer = " ".join(
            [answer[:1].upper() + answer[1:]]
            + extra
            + [describe(r) + "." for r in unpriced]
        )
        return answer.strip(), None
    except KeyError as missing:
        return (
            None,
            f"Row {missing} does not exist. Use only row_id values from get_prices.",
        )
def ask(question, max_retries=2):
    rows.clear()
    cheapest.clear()
    unpriced.clear()
    items = [{"role": "user", "content": question}]
    response = oa.responses.create(
        model=MODEL,
        instructions=SYSTEM,
        input=items,
        tools=TOOLS,
        text={"format": ANSWER_FORMAT},
    )
    retries = 0
    for _ in range(MAX_TURNS):
        calls = [o for o in response.output if o.type == "function_call"]
        if calls:
            items += response.output
            for call in calls:
                args = json.loads(call.arguments)
                result = run_tool(args["urls"], args["need_live"])
                items.append(
                    {
                        "type": "function_call_output",
                        "call_id": call.call_id,
                        "output": json.dumps(result),
                    }
                )
        else:
            answer, error = render(json.loads(response.output_text)["text"])
            if answer:
                return answer
            if retries == max_retries:
                return FALLBACK
            retries += 1
            items += response.output + [{"role": "user", "content": error}]
        response = oa.responses.create(
            model=MODEL,
            instructions=SYSTEM,
            input=items,
            tools=TOOLS,
            text={"format": ANSWER_FORMAT},
        )
    return FALLBACK
if __name__ == "__main__":
    print(
        ask(
            " ".join(sys.argv[1:]) or "Where is the Sony WH-1000XM6 cheapest right now?"
        )
    )
Step 3. Fill the cache and ask questions
refresh.py fills the cache for the whole catalog in 1 run:
"""Fill the price cache for the whole catalog. Run it on a schedule."""
import asyncio
import json
from dotenv import load_dotenv
load_dotenv()
from prices import refresh_all  # noqa: E402
catalog = json.load(open("catalog.json"))
cache = asyncio.run(refresh_all(catalog))
print(f"Cached {len(cache)} products")
Run it, then ask the agent a browsing question:
python refresh.py
python agent.py "Where is the Sony WH-1000XM6 cheapest right now: Amazon, Walmart, Best Buy, or Target?"
The output:
Cached 7 products
The lowest-priced offers are tied: $458.00 for the Sony WH-1000XM6 headphones at Amazon (checked 05:25 UTC on October 24), $458.00 for the Sony WH-1000XM6 headphones at Walmart (checked 05:26 UTC on October 24), and $458.00 for the Sony WH-1000XM6 headphones at Best Buy (checked 05:26 UTC on October 24). Another offer is $458.99 for the Sony WH-1000XM6 headphones at Target (checked 05:25 UTC on October 24, the store redirected this link).
The answer used cached prices, so it needed no live price check. Target's offer has a note because Target redirected the catalog link to its parent product page. For a product with no price on the store's page, the agent says so. Best Buy showed this Instant Pot as sold out:
python agent.py "How much is the Instant Pot Duo 6 qt at Best Buy?"
The output:
It has no listed price right now. Best Buy shows no price for the Instant Pot Duo 7-in-1 6 qt.
A question before a purchase gets a live price check. A sudden low price needs extra care. During the tests, the Amazon listing for the Dyson V15 Detect went from $789.49 to $377.99, then to $422.44:
python agent.py "I want to buy the Dyson V15 Detect at Amazon now. What does it cost?"
The output:
It's $422.44 for the Dyson V15 Detect cordless vacuum at Amazon (checked 05:26 UTC on October 24, sold by Evergreen Renew Tech LLC, Used - Like New); note that this offer is for a used item.
This is the Amazon page a US shopper saw at the time of that check:
E-commerce Scraping Tool reported the seller and the condition of the Buy Box offer, and code used them to set the used status. The status is used, not big_change, because the code checks the condition before it compares prices. A grounding check would pass "$422.44 at Amazon" with no used note, because that number is in the data.
If a setup step is missing, the error message names it:
Step 4. Test the agent with repeated questions
A single good answer isn't enough proof, because a model can answer differently each time. Ask each test question several times, and check what the agent did, not only what it said. This script, eval_short.py, checks which products each answer used:
"""Ask each question 5 times and check which products the agent used."""
import agent
TESTS = {
    "Where is the Sony WH-1000XM6 cheapest right now: Amazon, Walmart, Best Buy, or Target?": "Sony",
    "How much is the Instant Pot Duo 6 qt at Best Buy?": "Instant Pot",
    "How much is the Nintendo Switch 2 at Walmart?": None,  # not in the catalog
}
for question, product in TESTS.items():
    for _ in range(5):
        answer = agent.ask(question)
        used = {row["product"] for row in list(agent.rows.values()) + agent.unpriced}
        right = all(product in p for p in used) and bool(used) if product else not used
        print("PASS" if right and answer != agent.FALLBACK else "FAIL", "|", answer[:90])
Run it with python eval_short.py. In the tests, 6 runs of this script passed 89 of 90 checks. A longer run asked 8 questions, 5 times each. The questions included a purchase, a price alert, and a used offer, and the run checked whether the agent asked for a live price check. It gave these results:
- All 40 answers used the correct rows and the correct kind of price check, cached or live.
- The validator worked as designed. It found a store name that the model typed in 12 first drafts. Each rejected draft passed on the second try.
- No answer needed the fallback message.
Run the script again after every change to the prompt or the validator, because repeated runs find bugs that a single run misses.
Run the price agent in production
ChatGPT and the Universal Commerce Protocol (UCP) specification from Google use 2 kinds of price. The feed price is for browsing, and the checkout price is the final one. Your agent can work the same way. Each kind of agent needs a different price:
- Keep the cache up to date. Save the Actor input from refresh.py as a task in Apify Console. Run the task every 30 minutes with an Apify schedule, so the refresh runs on Apify, not on your server. Then read its results with load_from_task(), or set an Apify webhook to call your code when the run succeeds. If you already use cron, run refresh.py every 30 minutes instead.
- Monitor every status. Log each status separately, such as no_price and moved_page. A change at one store is then visible, instead of hidden in an overall success rate. Also log the seller and condition for each store, because the used status depends on those fields.
To read the results of the task's last successful run, replace the import and the refresh_all() call in refresh.py with these lines:
from prices import load_from_task  # noqa: E402
cache = asyncio.run(load_from_task("YOUR_TASK_ID", catalog))
The tutorial code keeps state in 1 process and 1 JSON file. For a web service, keep the rows for each request separate, call get_prices with await, and store the cache in a database. For a catalog with thousands of products, don't list every URL in the prompt and the tool schema. Instead, give the model a search tool that returns matching catalog entries.
In MCP clients such as Claude or Cursor, the Apify MCP server makes E-commerce Scraping Tool available to the agent as a tool. Real-time product data for AI agents shows that setup.
The case study Maven AGI x Apify: Customer support with 100% company-approved data shows grounded agents in production.
Next steps
Models, prices, and store pages will keep changing, but one rule stays the same. When the model types a price, the user can't know whether it's a guess or a fact. When code inserts it from live data, with a source and a time, the user receives an answer they can check.
For more on agents and live data, see AI agent tools that keep agents grounded in current data and Agentic commerce and the AI economy stack. The guide on whether web scraping is legal answers common legal questions about collecting prices.
Every agent needs proper tools. Equip your AI agents with thousands of tools on Apify, starting with E-commerce Scraping Tool for live prices with a clear status. It runs on the Apify Free plan. Add your own products to catalog.json, and ask the agent where they're cheapest.
FAQ
What is LLM grounding?
LLM grounding means that a model answers from data that your code fetched for the question, not from what it learned in training. A grounded answer shows its source and its time, so a user or a program can check it.
Is LLM grounding the same as RAG?
RAG (retrieval-augmented generation) is one way to ground a model. It finds documents and adds them to the prompt. For prices, a retrieved page can be out of date or describe another product, so a price agent should fetch the live product page and let code insert the price.
Can a prompt stop price hallucinations?
A prompt can stop the guessing. With no tools and the prompt "If you cannot know the current price, answer UNKNOWN," gpt-6-luna and Claude Opus 5.5 both answered UNKNOWN for all 21 products. But then the user got no price. Live data gives an answer that's both honest and useful.
Do agentic commerce protocols fix wrong prices?
They help at checkout. Protocols such as Google's Universal Commerce Protocol (UCP) separate a feed price for browsing from a checkout price, which is final. Before checkout, the agent still needs live data with a clear status for every price it shows.
How do I get live prices for an AI agent?
Give the agent a tool that fetches the product page when the user asks. E-commerce Scraping Tool, a ready-to-run tool on Apify, returns the price, currency, and timestamp for Amazon, Walmart, Best Buy, Target, Shopify stores, and many more. With additionalProperties set to true, it also returns the seller and condition when the store shows them.

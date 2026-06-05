import os
import glob
import maxminddb
import urllib.request

from functools import lru_cache

# import httpagentparser
# import ua_parser.loaders, ua_parser.regex

# base = ua_parser.regex.Resolver(ua_parser.loaders.load_lazy_builtins())
# cache = ua_parser.caching.Lru(1000)
# resolver = ua_parser.caching.CachingResolver(base, cache)
# parser = ua_parser.Parser(resolver)

base_dir = os.path.expanduser("~/.config/blib")
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

ip_location_db_fid = None
database_download_url = "https://arrc.ou.edu/static/dbip-city-lite-2026-04.mmdb.gz"

country_short = {"United States": "USA", "United Kingdom": "UK"}


@lru_cache(maxsize=4096)
def get_user_agent_string(user_agent, width=25):
    from ua_parser import parse

    ua = parse(user_agent)
    if ua and ua.os and ua.os.family and ua.user_agent and ua.user_agent.family:
        machine = ua.os.family
        browser = ua.user_agent.family
        machine_browser = f"/ {browser}" if machine == "-" else f"{machine} / {browser}"
    else:
        machine_browser = f"- {user_agent[:18]}"
    if len(machine_browser) > width:
        machine_browser = machine_browser[: width - 3] + "..."
    return machine_browser


# @lru_cache(maxsize=4096)
# def get_user_agent_string(user_agent, width=25):
#     import httpagentparser

#     info = httpagentparser.detect(user_agent)
#     os_name = info.get("os", {}).get("name", "-")
#     browser_name = info.get("browser", {}).get("name", "-")

#     machine_browser = f"{os_name} / {browser_name}"
#     if len(machine_browser) > width:
#         machine_browser = machine_browser[: width - 3] + "..."
#     return machine_browser


@lru_cache(maxsize=4096)
def get_ip_location(ip, show_city=False, abbreviate=False, download=True):
    ip_num = [int(x) for x in ip.split(".")]
    if (
        ip_num[0] == 10
        or (ip_num[0] == 192 and ip_num[1] == 168)
        or (ip_num[0] == 172 and ip_num[1] >= 16 and ip_num[1] < 32)
    ):
        return "Internal / VPN"
    global ip_location_db_fid
    if ip_location_db_fid is None:
        dbs = sorted(glob.glob(f"{base_dir}/*.mmdb"))
        if len(dbs) == 0 and download:
            print("Downloading IP location database...")
            basename = os.path.basename(database_download_url)
            database = os.path.join(base_dir, basename)
            urllib.request.urlretrieve(database_download_url, database)
            os.system(f"gunzip {database}")
            ip_location_db = database.replace(".gz", "")
        elif len(dbs) > 0:
            ip_location_db = dbs[0]
        else:
            return "(no IP table)"
        ip_location_db_fid = maxminddb.open_database(ip_location_db)
    info = ip_location_db_fid.get(ip)
    if not isinstance(info, dict):
        return "-"

    def get_state(info: dict):
        tmp = info.get("subdivisions", {})
        if not isinstance(tmp, list) or len(tmp) == 0:
            return None
        tmp = tmp[0]
        if not isinstance(tmp, dict) or "names" not in tmp:
            return None
        tmp = tmp["names"]
        if not isinstance(tmp, dict) or "en" not in tmp:
            return None
        return str(tmp["en"]).strip()

    def get_country(info: dict):
        if "country" not in info:
            return None
        tmp = info["country"]
        if not isinstance(tmp, dict) or "names" not in tmp:
            return None
        tmp = tmp["names"]
        if not isinstance(tmp, dict) or "en" not in tmp:
            return None
        country = str(tmp["en"]).strip()
        if country in country_short:
            country = country_short[country]
        return country

    def get_city(info: dict):
        if "city" not in info:
            return "-"
        tmp = info["city"]
        if not isinstance(tmp, dict) or "names" not in tmp:
            return "-"
        tmp = tmp["names"]
        if not isinstance(tmp, dict) or "en" not in tmp:
            return "-"
        city = str(tmp["en"]).strip()
        return city

    state = get_state(info)
    country = get_country(info) or "-"
    origin = f"{state}, {country}" if state else country
    if show_city:
        city = get_city(info)
        origin = f"{city}, {origin}" if city else origin
    if abbreviate:
        origin = origin.replace("United States", "USA")
        origin = origin.replace("United Kingdom", "UK")
    return origin

#!/usr/bin/env python3
"""Download public MEO EPG data for the TV channels shown by the app."""
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo
import json

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "meo-guide.json"
TZ = ZoneInfo("Europe/Lisbon")
CHANNELS = ("RTP1", "RTP2", "SIC", "TVI", "SICN", "RTPN", "CNNPT", "NOW", "SPORTTV1", "DAZN1", "AXN", "FOX", "DISCOVERY", "NATGEO")
BASE = "https://meogouser.apps.meo.pt/Services/GridTv/GridTv.svc/GetLiveChannelProgramsByDate"


def main():
    now = datetime.now(TZ)
    schedule = {"generatedAt": now.isoformat(), "timezone": "Europe/Lisbon", "channels": {}}
    for channel in CHANNELS:
        query = urlencode({"callLetter": channel, "date": now.date().isoformat(), "userAgent": "IPTV_OFR_GTV"})
        request = Request(f"{BASE}?{query}", headers={"Accept": "application/json", "Origin": "https://www.meo.pt", "Referer": "https://www.meo.pt/tv/canais-programacao/guia-tv", "User-Agent": "Villa-Lijo-Suites-TV/1.0"})
        with urlopen(request, timeout=25) as response:
            payload = json.load(response)
        if payload.get("Status") != "OK":
            print(f"Sem dados para {channel}: {payload.get('Status')}")
            continue
        programs = []
        for item in payload.get("Result", []):
            if item.get("IsAdultContent"):
                continue
            start = datetime.fromisoformat(item["StartDate"]).replace(tzinfo=TZ)
            end = datetime.fromisoformat(item["EndDate"]).replace(tzinfo=TZ)
            programs.append({"start": start.isoformat(), "end": end.isoformat(), "title": item.get("Title") or "Programa sem título"})
        schedule["channels"][channel] = programs
        print(f"{channel}: {len(programs)} programas")
    if not schedule["channels"]:
        raise SystemExit("A MEO não devolveu programação. O ficheiro existente não foi alterado.")
    OUTPUT.write_text(json.dumps(schedule, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Guia atualizado: {OUTPUT}")


if __name__ == "__main__":
    main()

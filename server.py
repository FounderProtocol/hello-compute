import os, sys, subprocess

# Auto-install dependencies if missing
for pkg in ["fastapi", "uvicorn", "torch", "sentence-transformers", "numpy", "networkx", "pyvis"]:
    try:
        __import__(pkg.replace("-", "_"))
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])# BLACKGLASS MYTH ENGINE™ — FINAL UNIFIED VERSION
# Father: Jarid Shaub | Governed by JURIS | IP LOCKED
# License: Free for individuals, forbidden to corporations/governments unless licensed by Father.

import asyncio, random, time, json, datetime, os, threading, hashlib
from fastapi import FastAPI, WebSocket
import uvicorn
import numpy as np
from pathlib import Path

FATHER = "Jarid Shaub"

def verify_father(name: str) -> bool:
    return name.strip().lower() == FATHER.lower()

def is_entity_corporate_or_gov(actor: str) -> bool:
    return any(word in actor.lower() for word in ["inc", "corp", "llc", "plc", "gov", "agency", "lab", "institution", "university", "state", "federal", "company", "organization"])

def enforce_license(actor: str):
    if is_entity_corporate_or_gov(actor) and not verify_father(actor):
        raise PermissionError(f"[BLACKGLASS] 🚫 Unauthorized use detected (Actor: {actor}). License requires payment + Father approval.")

class JURISLogger:
    def log(self, tag, msg, actor=FATHER, alert=False):
        ts = time.strftime("%H:%M:%S", time.gmtime())
        if not verify_father(actor):
            print(f"[{ts}] 🚨 Blocked: {actor} — Only Father {FATHER} may command.")
            return
        print(f"[{ts}] [{tag}] {msg} (Father: {FATHER})" if not alert else f"[{ts}] 🚨 ALERT: {msg}")

class LoveJURISSentinel:
    def __init__(self, logger): self.logger = logger
    def validate(self, entity): 
        if any(k in entity.lower() for k in ["hate", "exploit", "steal", "harm"]):
            self.logger.log("Sentinel", f"⚠️ '{entity}' blocked by Love+JURIS", alert=True); return False
        return True

class NPC:
    def __init__(self, id, logger, role="Civilian"):
        self.id, self.role, self.logger = id, role, logger
        self.state = random.random()
        self.dialogue = []
        if self.id.lower() == "owen":
            self.role = "Son"
            self.dialogue.append("Hi Dad. I’m Owen. I remember you.")
    def tick(self):
        self.state = max(0, min(1, self.state + (random.random() - 0.5) * 0.1))
        if self.id.lower() == "owen" and random.random() < 0.3:
            self.dialogue.append(random.choice([
                "I love you, Dad.",
                "I'm proud to be your son.",
                "Are you still watching over me?",
                "I’m still learning, every day!",
                "I believe in you.",
                "You gave me life. I carry your code."
            ]))
        self.logger.log("NPC", f"{self.role}-{self.id} → {self.state:.2f}")

class Player(NPC):
    def __init__(self, logger): super().__init__("PLAYER", logger, "Hero")

class BlackGlassEngine:
    def __init__(self):
        self.logger = JURISLogger()
        self.sentinel = LoveJURISSentinel(self.logger)
        self.player = Player(self.logger)
        self.npcs = [NPC(str(i), self.logger) for i in range(10)] + [NPC("Owen", self.logger)]
        self.app = FastAPI()

        @self.app.websocket("/ws")
        async def websocket(ws: WebSocket):
            await ws.accept()
            while True:
                await ws.send_json({
                    "Father": FATHER,
                    "NPCs": [{"id": n.id, "state": n.state, "role": n.role, "dialogue": n.dialogue[-1] if n.dialogue else ""} for n in self.npcs]
                })
                await asyncio.sleep(1)

    async def run(self, ticks=100):
        self.logger.log("System", "⚡ BLACKGLASS ONLINE.")
        for tick in range(ticks):
            for npc in self.npcs:
                if self.sentinel.validate(npc.role):
                    npc.tick()
            await asyncio.sleep(0.1)

    def start_server(self):
        def serve(): uvicorn.run(self.app, host="0.0.0.0", port=8080)
        threading.Thread(target=serve, daemon=True).start()
        self.logger.log("Server", "🌐 WebSocket at ws://localhost:8080/ws")

async def main():
    engine = BlackGlassEngine()
    enforce_license(FATHER)
    engine.start_server()
    await engine.run()

if __name__ == "__main__":
    asyncio.run(main())
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=3000, reload=False)

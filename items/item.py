from dataclasses import dataclass
from enum import Enum

class ItemType(Enum):
    AH = "ah"
    GL = "gl"
    AL = "al"
    BL = "bl"
    WD = "wd"
    WS = "ws"
    BH = "bh"
    WM = "wm"
    WT = "wt"
    HH = "hh"
    WA = "wa"
    AM = "am"
    WB = "wb"
    XS = "xs"
    GH = "gh"
    UH = "uh"
    US = "us"
    Z = "z"
    UP = "up"
    HM = "hm"
    HL = "hl"
    WC = "wc"
    WG = "wg"
    WP = "wp"
    XR = "xr"
    XA = "xa"

    def __eq__(self, other):
        if type(self).__qualname__ != type(other).__qualname__:
            return NotImplemented
        return self.name == other.name and self.value == other.value

    def __hash__(self):
        return hash((type(self).__qualname__, self.name))
    
    
@dataclass
class Item:
    uid: str
    level: int
    type: str
    subtype: str
    xp: int
    craftXp: int
    value: int
    tradeMinMaxValue: int
    favor: int
    time: int
    atk: int
    defense: int
    hp: int
    eva: int
    crit: int
    excl: int
    tier: int
    subtier: int
    combo: int
    worker1: str
    worker2: str
    worker3: str
    w1BuildingReq: str
    w2BuildingReq: str
    w3BuildingReq: str
    resource1: str
    r1Qty: int
    resource2: str
    r2Qty: int
    resource3: str
    r3Qty: int
    component1: str
    c1Qty: int
    c1Tags: str
    component2: str
    c2Qty: int
    c2Tags: str
    u1Req: int
    u2Req: int
    u3Req: int
    u4Req: int
    u5Req: int
    upgrade1: str
    upgrade2: str
    upgrade3: str
    upgrade4: str
    upgrade5: str
    upgradeBonus: int
    supgrade1: str
    supgrade2: str
    supgrade3: str
    su1Cost: int
    su2Cost: int
    su3Cost: int
    restrict: int
    reqTags: str
    tagIndex: int
    elements: str
    skill: str
    lTag2: str
    lTag3: str
    elementAffinity: str
    spiritAffinity: str
    tag: str
    discount: int
    surcharge: int
    suggest: int
    speedup: int
    buyAnimIdOverride: int
    questAnimIdOverride: int
    slotOverride: int
    soundType: str
    unlock: int
    chest: int
    firstOfLine: int
    prohibited: int
    hasChinaTexture: int
    nonCraftable: int
    releaseAt: int
    shardPrice: int
    capriceDelay: int
    EnchantedItemTexturer: str
    name:str

    def __init__(self, data):
        self.uid = data["uid"]
        self.level = data["level"]
        self.type = data["type"]
        self.subtype = data["subtype"]
        self.xp = data["xp"]
        self.craftXp = data["craftXp"]
        self.value = data["value"]
        self.tradeMinMaxValue = data["tradeMinMaxValue"]
        self.favor = data["favor"]
        self.time = data["time"]
        self.atk = data["atk"]
        self.defense = data["def"]
        self.hp = data["hp"]
        self.eva = data["eva"]
        self.crit = data["crit"]
        self.excl = data["excl"]
        self.tier = data["tier"]
        self.subtier = data["subtier"]
        self.combo = data["combo"]
        self.worker1 = data["worker1"]
        self.worker2 = data["worker2"]
        self.worker3 = data["worker3"]
        self.w1BuildingReq = data["w1BuildingReq"]
        self.w2BuildingReq = data["w2BuildingReq"]
        self.w3BuildingReq = data["w3BuildingReq"]
        self.resource1 = data["resource1"]
        self.r1Qty = data["r1Qty"]
        self.resource2 = data["resource2"]
        self.r2Qty = data["r2Qty"]
        self.resource3 = data["resource3"]
        self.r3Qty = data["r3Qty"]
        self.component1 = data["component1"]
        self.c1Qty = data["c1Qty"]
        self.c1Tags = data["c1Tags"]
        self.component2 = data["component2"]
        self.c2Qty = data["c2Qty"]
        self.c2Tags = data["c2Tags"]
        self.u1Req = data["u1Req"]
        self.u2Req = data["u2Req"]
        self.u3Req = data["u3Req"]
        self.u4Req = data["u4Req"]
        self.u5Req = data["u5Req"]
        self.upgrade1 = data["upgrade1"]
        self.upgrade2 = data["upgrade2"]
        self.upgrade3 = data["upgrade3"]
        self.upgrade4 = data["upgrade4"]
        self.upgrade5 = data["upgrade5"]
        self.upgradeBonus = data["upgradeBonus"]
        self.supgrade1 = data["supgrade1"]
        self.supgrade2 = data["supgrade2"]
        self.supgrade3 = data["supgrade3"]
        self.su1Cost = data["su1Cost"]
        self.su2Cost = data["su2Cost"]
        self.su3Cost = data["su3Cost"]
        self.restrict = data["restrict"]
        self.reqTags = data["reqTags"]
        self.tagIndex = data["tagIndex"]
        self.elements = data["elements"]
        self.skill = data["skill"]
        self.lTag2 = data["lTag2"]
        self.lTag3 = data["lTag3"]
        self.elementAffinity = data["elementAffinity"]
        self.spiritAffinity = data["spiritAffinity"]
        self.tag = data["tag"]
        self.discount = data["discount"]
        self.surcharge = data["surcharge"]
        self.suggest = data["suggest"]
        self.speedup = data["speedup"]
        self.buyAnimIdOverride = data["buyAnimIdOverride"]
        self.questAnimIdOverride = data["questAnimIdOverride"]
        self.slotOverride = data["slotOverride"]
        self.soundType = data["soundType"]
        self.unlock = data["unlock"]
        self.chest = data["chest"]
        self.firstOfLine = data["firstOfLine"]
        self.prohibited = data["prohibited"]
        self.hasChinaTexture = data["hasChinaTexture"]
        self.nonCraftable = data["nonCraftable"]
        self.releaseAt = data["releaseAt"]
        self.shardPrice = data["shardPrice"]
        self.capriceDelay = data["capriceDelay"]
        self.EnchantedItemTexturer = data["EnchantedItemTexturer"]
        self.name = data["name"]

    @property
    def itemType(self):
        return ItemType(self.type)
    
    def short_description(self):
        return f"{self.name}\t({self.type})\t{self.tier}\t"
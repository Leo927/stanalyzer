from enum import Enum
from dataclasses import dataclass

class Currency(Enum):
    GOLD = 'gold'
    GEMS = 'gems'
    def __str__(self):
        return str(self.value)
    def __eq__(self, other):
        if type(self).__qualname__ != type(other).__qualname__:
            return NotImplemented
        return self.name == other.name and self.value == other.value

    def __hash__(self):
        return hash((type(self).__qualname__, self.name))
class ListingType(Enum):
    OFFER = "o"
    REQUEST = "r"
    def __str__(self):
        return str(self.value)
    def __eq__(self, other):
        if type(self).__qualname__ != type(other).__qualname__:
            return NotImplemented
        return self.name == other.name and self.value == other.value

    def __hash__(self):
        return hash((type(self).__qualname__, self.name))
class Quality(Enum):
    COMMON = 'common'
    UNCOMMON = 'uncommon'
    FLAWLESS = 'flawless'
    EPIC = 'epic'
    LEGENDARY = 'legendary'
    def __str__(self):
        return str(self.value)
    @classmethod
    def ranking_to_rarity(cls, ranking):
        if ranking == 0:
            return Quality.COMMON
        elif ranking == 1:
            return Quality.UNCOMMON
        elif ranking == 2:
            return Quality.FLAWLESS
        elif ranking == 3:
            return Quality.EPIC
        elif ranking == 4:
            return Quality.LEGENDARY
    
    @classmethod
    def get_ranking(cls, rarity):
        if rarity == Quality.COMMON:
            return 0
        elif rarity == Quality.UNCOMMON:
            return 1
        elif rarity == Quality.FLAWLESS:
            return 2
        elif rarity == Quality.EPIC:
            return 3
        elif rarity == Quality.LEGENDARY:
            return 4
    def __eq__(self, other):
        if type(self).__qualname__ != type(other).__qualname__:
            return NotImplemented
        return self.name == other.name and self.value == other.value

    def __hash__(self):
        return hash((type(self).__qualname__, self.name))
    
    @classmethod
    def add_one(cls, rarity):
        value = cls.get_ranking(rarity) + 1
        if(value > 4):
            raise ValueError("Rarity cannot exceed LEGENDARY")
        return cls.ranking_to_rarity(value)
    
    def __eq__(self, other):
        if type(self).__qualname__ != type(other).__qualname__:
            return NotImplemented
        return self.name == other.name and self.value == other.value

    def __hash__(self):
        return hash((type(self).__qualname__, self.name))

# Rest of the code...

@dataclass
class Listing:
    id: int
    tType: str
    uid: str
    tag1: str
    tag2: str
    tag3: str
    goldQty: int
    gemsQty: int
    created: int
    tier: int
    order: int
    cityId: str
    goldPrice: int
    gemsPrice: int
    requestCycleLast: int
    createdAt: int
    updatedAt: int
    
    def __init__(self, id=None, tType=None, uid=None, tag1=None, tag2=None, tag3=None, goldQty=None, gemsQty=None, created=None, tier=None, order=None, cityId=None, goldPrice=None, gemsPrice=None, requestCycleLast=None, createdAt=None, updatedAt=None):
        self.id = id
        self.tType = tType
        self.uid = uid
        self.tag1 = tag1
        self.tag2 = tag2
        self.tag3 = tag3
        self.goldQty = goldQty
        self.gemsQty = gemsQty
        self.created = created
        self.tier = tier
        self.order = order
        self.cityId = cityId
        self.goldPrice = goldPrice
        self.gemsPrice = gemsPrice
        self.requestCycleLast = requestCycleLast
        self.createdAt = createdAt
        self.updatedAt = updatedAt
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get('id'),
            tType=data.get('tType'),
            uid=data.get('uid'),
            tag1=data.get('tag1'),
            tag2=data.get('tag2'),
            tag3=data.get('tag3'),
            goldQty=data.get('goldQty'),
            gemsQty=data.get('gemsQty'),
            created=data.get('created'),
            tier=data.get('tier'),
            order=data.get('order'),
            cityId=data.get('cityId'),
            goldPrice=data.get('goldPrice'),
            gemsPrice=data.get('gemsPrice'),
            requestCycleLast=data.get('requestCycleLast'),
            createdAt=data.get('createdAt'),
            updatedAt=data.get('updatedAt')
        )

    
    @property
    def quality(self):
        if self.tag1 == None:
            return Quality.COMMON
        else:
            return Quality(self.tag1)
        
    @property
    def type(self):
        if self.tType == "o":
            return ListingType.OFFER
        elif self.tType == "r":
            return ListingType.REQUEST
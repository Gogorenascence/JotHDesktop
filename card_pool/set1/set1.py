from card_pool.set1.i01pm1 import pantheraman
from card_pool.set1.i02gw1 import golden_wall
from card_pool.set1.i03bw1 import bone_whisperer
from card_pool.set1.i04fb1 import flamebell
from card_pool.set1.i05bm1 import blast_mouth
from card_pool.set1.i06rf1 import red_fist
from card_pool.set1.i07be1 import burst_esper
from card_pool.set1.i08bga1 import battle_girl_alice
from card_pool.set1.i09dw1 import jet_and_climber
from card_pool.set1.i10h01 import hive
from card_pool.set1.i11hs1 import hammerspace
from card_pool.set1.i12bb1 import bolt_blossom
from card_pool.set1.i13bn1 import black_note
from card_pool.set1.i14p01 import portal
from card_pool.set1.i15cp1 import ceifeira_preta
from card_pool.set1.i16ge1 import gravity_enforcer
from card_pool.set1.gen1 import generic1


set1 =[
    pantheraman,
    golden_wall,
    bone_whisperer,
    flamebell,
    blast_mouth,
    red_fist,
    burst_esper,
    battle_girl_alice,
    jet_and_climber,
    hive,
    hammerspace,
    bolt_blossom,
    black_note,
    portal,
    ceifeira_preta,
    gravity_enforcer,
    generic1,
]

card_pool_set1 = []
for series in set1:
    for card in series:
        card_pool_set1.append(card)

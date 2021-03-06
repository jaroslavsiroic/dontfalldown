
# LEVEL DESIGN ELEMENTS:

# U - User (player)
# E - Enemy
# R - Rock (solid block)
# P - Platform (with random time [1,9])
# [number] - Platform with this much time
# V, ^, >, < - Spike (and direction its facing)
# W - Water
# F - Finish

levels = [
    [
    "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",
    "R>                                   R",
    "R>                                  FR",
    "R44444RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",
    "R    RR                              R",
    "R                                    R",
    "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR    <R",
    "R                                 R  R",
    "RU                                 ^^R",
    "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",],
    [
    "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",
    "R          V      V                  R",
    "R                                    R",
    "RU                                E  R",
    "RRRR      E     P         PPPPPPPPPPPR",
    "RPPPPPPPPPPPPPPPP                    R",
    "R^^^^^^^^^^^^^^^P               E    R",
    "RRRRRRRRRRRRRRRRPPPPPPPPPPPPPPPPPPPPPR",
    "R  V                                 R",
    "R                                    R",
    "R                                    R",
    "RF      P  E P     P    E  P         R",
    "RRR    <PPPPPP>   <PPPPPPPPP> <PPP>  R",
    "R                                    R",
    "R^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^R",
    "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",],
    [
    "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",
    "R P      P      P       U       P      P      P R",
    "RPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPR",
    "R   P      P      P           P      P      P   R",
    "R    P      P^^^^^^P    E    P^^^^^^P      P    R",
    "RPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPR",
    "R      P      P      P     P      P      P      R",
    "RWWWWWWWP      P  E   P E P   E  P      PWWWWWWWR",
    "RPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPR",
    "R       P      P      P   P      P      P       R",
    "R      P^^^^^^P    E P  E  P   E  P^^^^^^P      R",
    "RPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPR",
    "R    P      P      P         P      P      P    R",
    "R   P      P      P     F     P      P      P   R",
    "RPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPR",
    "R^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^R",
    "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",],
    [
    "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",
    "R     R               VV  V   V  VVVVR",
    "R     R                              R",
    "R  0R   R      0  R                  R",
    "R   R   R   0  0  R> P     E     P   R",
    "R0  R000R   0     R> PPPPPPPPPPPPP   R",
    "RU  R^^^R^^^^^^^^^R^^^^^^^^^^^^^^R  FR",
    "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",],
    [
    "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",
    "R                                  R",
    "R                                  R",
    "R                                  R",
    "R                P  E    P         R",
    "R           ^    PPPPPPPPP         R",
    "R F   RWWWWWR    VVVVVVV    4R     R",
    "RRRRRRRRRRRRR              33RR    R",
    "R                         222RRR   R",
    "R               ^        1111RRRR  R",
    "R  U            R    E  00000RRRRR R",
    "RRRRRRRR     RRRRRRRRRRRRRRRRRRRRRRR",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"],
    [
    "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",
    "R         V                   V                                  R",
    "R                                                                R",
    "R                                                                R",
    "RR   R    R    R    R    R    R    R    R    R    R    R    R    RR",
    "R                                                                R",
    "R  F                                                            RR",
    "RRRRRR                                                           R",
    "R                                                           R    R",
    "R                                                                R",
    "R                P  E    P                                      RR",
    "R           ^    PPPPPPPPP                                       R",
    "RWWWWWWWWWWWR    VVVVVVV    4R                              R    R",
    "RRRRRRRRRRRRR              33RR                                  R",
    "R                         222RRR                                RR",
    "R               ^        1111RRRR                           R    R",
    "R  U            R    E  00000RRRRR                               R",
    "RRRRRRRR     RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"],
    [
    "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",
    "R            VVVVVVVVVV    V                                     R",
    "R                                                                R",
    "R      0R               E                    E                   R",
    "R      <RPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPR",
    "RPP     R                                                        R",
    "R       R       P^P        E           P^P       E               R",
    "R      PRPPPPPPPPRPPPPPPPPPPPPPPPPPPPPPPRPPPPPPPPPPPPPPPPPPPPPPPPR",
    "R       R                                                        R",
    "RP      R        E         P^P               E                   R",
    "R>      RPPPPPPPPPPPPPPPPPPPRPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPR",
    "R>     PR                                                        R",
    "R>      R       P^P          E               E                   R",
    "R     PPRPPPPPPPPRPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPR",
    "R       R                                                        R",
    "RP     PRRRRRRRRPPPPPPPPPPRRRRRRRRRRPPPPPPPPPPPPPRRRRRRRRRRRRPPPPR",
    "RU      RF                                                       R",
    "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"],
    [
    "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",
    "R        V                 V                 VVV                 R",
    "R                                                                R",
    "R                                                                R",
    "RU                                                               R",
    "RRRRRRR    RRRRRR    RRR    RRRRRR     R   RRRRR    R  RR  RRRRRRR",
    "R                                                                R",
    "R   E            E    E       E  0            E                E R",
    "R0000000000000000000000000000000000000000000000000000000000000000R",
    "R                                                                R",
    "R                                                                R",
    "R0    0    0    0    0    0    0    0    0    0    0    0    0   R",
    "R0    0    0    0    0    0    0    0    0    0            ^     R",
    "R^^^^^0WWWW0 E  0  E 0WWWW0^ ^^0    E     E   0WWWWWWWP^^^^P  E  R",
    "RPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPR",
    "R                                                               <R",
    "RF                                                              <R",
    "RPP>   <PP>    <PP>    <PP>    <PP>    <PP>    <PP>    <PP> P  <PR",
    "R                                                                R",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"],
    [
    "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",
    "RF       R                                                       R",
    "RRR      R000000000000000000000000000000000000000R               R",
    "R  0     R V VV   VVVVVVVVVVVVVVV                    P           R",
    "R        R                                          P            R",
    "R       0R     E   R                  E   PE      P              R",
    "R       <RRRPRRRRRRR              PPPPPPPPPPPPPPPP               R",
    "R0       R         R          P      VVVVVV                      R",
    "R>       R         R      P                                      R",
    "R       0R         R      P       R                              R",
    "R       <R       E R      PPPPPPPPRR  E          R^^^^^          R",
    "R0       R000000000R              RPPPPPPPPPPPPPPPPPPPPPPPPPP    R",
    "R>                 R                                           U R",
    "R0000000000                                                   RRRR",
    "R^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^R",
    "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",
    "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"],
]

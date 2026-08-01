# CoreProtect-Blacklist-Settings
Entities take up the most database space in CoreProtect, around 5 times more than blocks. This is an optimal CoreProtect plugin blacklist.txt that can be easily copied for servers, that is easily configurable, allowing the removal of mobs cluttering your database from farms while keeping named mobs tracked.

Copy this into your `blacklist.txt`

<!-- START_BLACKLIST_DEREXXD -->
```
#dispenser
#hopper
#guardian
#cramming
DerexXD
#bonemeal
#gravity

; --- FALL DAMAGE (Drop Farms) ---
minecraft:glow_squid@#fall
minecraft:slime@#fall
minecraft:spider@#fall
minecraft:zombie@#fall
minecraft:skeleton@#fall
minecraft:creeper@#fall
minecraft:enderman@#fall
minecraft:witch@#fall
minecraft:zombie_villager@#fall
minecraft:drowned@#fall
minecraft:husk@#fall
minecraft:stray@#fall
minecraft:pillager@#fall
minecraft:cave_spider@#fall
minecraft:sulfur_cube@#fall
minecraft:axolotl@#fall

; --- LAVA KILLS ---
minecraft:axolotl@#lava
minecraft:bat@#lava
minecraft:cave_spider@#lava
minecraft:chicken@#lava
minecraft:cod@#lava
minecraft:creeper@#lava
minecraft:drowned@#lava
minecraft:enderman@#lava
minecraft:evoker@#lava
minecraft:glow_squid@#lava
minecraft:husk@#lava
minecraft:iron_golem@#lava
minecraft:magma_cube@#lava
minecraft:phantom@#lava
minecraft:pillager@#lava
minecraft:pufferfish@#lava
minecraft:ravager@#lava
minecraft:salmon@#lava
minecraft:silverfish@#lava
minecraft:skeleton@#lava
minecraft:slime@#lava
minecraft:spider@#lava
minecraft:stray@#lava
minecraft:sulfur_cube@#lava
minecraft:tropical_fish@#lava
minecraft:vindicator@#lava
minecraft:witch@#lava
minecraft:zombie@#lava
minecraft:zombie_villager@#lava

; --- FIRE KILLS ---
minecraft:axolotl@#fire
minecraft:bat@#fire
minecraft:cave_spider@#fire
minecraft:chicken@#fire
minecraft:cod@#fire
minecraft:creeper@#fire
minecraft:drowned@#fire
minecraft:enderman@#fire
minecraft:evoker@#fire
minecraft:glow_squid@#fire
minecraft:husk@#fire
minecraft:iron_golem@#fire
minecraft:magma_cube@#fire
minecraft:phantom@#fire
minecraft:pillager@#fire
minecraft:pufferfish@#fire
minecraft:ravager@#fire
minecraft:salmon@#fire
minecraft:silverfish@#fire
minecraft:skeleton@#fire
minecraft:slime@#fire
minecraft:spider@#fire
minecraft:stray@#fire
minecraft:sulfur_cube@#fire
minecraft:tropical_fish@#fire
minecraft:vindicator@#fire
minecraft:witch@#fire
minecraft:zombie@#fire
minecraft:zombie_villager@#fire

; --- CAMPFIRE KILLS ---
minecraft:guardian@#campfire
minecraft:cod@#campfire
minecraft:salmon@#campfire
minecraft:zombie@#campfire
minecraft:skeleton@#campfire
minecraft:creeper@#campfire
minecraft:spider@#campfire
minecraft:pillager@#campfire
minecraft:witch@#campfire
minecraft:silverfish@#campfire
minecraft:cave_spider@#campfire
minecraft:slime@#campfire
minecraft:magma_cube@#campfire
minecraft:zombified_piglin@#campfire
minecraft:enderman@#campfire
minecraft:blaze@#campfire
minecraft:wither_skeleton@#campfire
minecraft:wandering_trader@#campfire
minecraft:snow_golem@#campfire
minecraft:bat@#campfire
minecraft:hoglin@#campfire
minecraft:zoglin@#campfire

; --- OTHER FARM TYPES ---
minecraft:guardian@#suffocation
minecraft:shulker@#shulker_bullet
minecraft:glow_squid@#glow_squid
minecraft:zombie@#zombie

; --- WITHER EFFECTS (Wither Rose/Wither Farms) ---
minecraft:zombie@#wither_effect
minecraft:skeleton@#wither_effect
minecraft:creeper@#wither_effect
minecraft:spider@#wither_effect
minecraft:enderman@#wither_effect
minecraft:husk@#wither_effect
minecraft:stray@#wither_effect
minecraft:shulker@#wither_effect

minecraft:enderman@#iron_golem
minecraft:axolotl@#drowned
minecraft:axolotl@#axolotl

; Suffocation
minecraft:iron_golem@#suffocation
minecraft:zombie@#suffocation
minecraft:skeleton@#suffocation
minecraft:creeper@#suffocation
minecraft:spider@#suffocation
minecraft:enderman@#suffocation
minecraft:witch@#suffocation
minecraft:drowned@#suffocation
minecraft:salmon@#suffocation
minecraft:cod@#suffocation
minecraft:pufferfish@#suffocation
minecraft:tropical_fish@#suffocation
minecraft:pillager@#suffocation
minecraft:evoker@#suffocation
minecraft:vindicator@#suffocation
minecraft:ravager@#suffocation

; --- DROWNING KILLS ---
minecraft:zombie@#drowning
minecraft:skeleton@#drowning
minecraft:creeper@#drowning
minecraft:spider@#drowning
minecraft:enderman@#drowning
minecraft:witch@#drowning
minecraft:husk@#drowning
minecraft:stray@#drowning
minecraft:cave_spider@#drowning
minecraft:pillager@#drowning
minecraft:evoker@#drowning
minecraft:vindicator@#drowning
minecraft:ravager@#drowning
minecraft:iron_golem@#drowning
minecraft:glow_squid@#drowning
minecraft:slime@#drowning
minecraft:squid@#drowning
minecraft:squid@#dryout
minecraft:glow_squid@#dryout
minecraft:bat@#drowning
minecraft:sulfur_cube@#drowning
nautilus@#dryout

; --- CONTACT KILLS (Cactus/Dripstone) ---
minecraft:guardian@#contact
minecraft:cod@#contact
minecraft:salmon@#contact
minecraft:zombie@#contact
minecraft:skeleton@#contact
minecraft:creeper@#contact
minecraft:spider@#contact
minecraft:pillager@#contact
minecraft:witch@#contact
minecraft:silverfish@#contact
minecraft:cave_spider@#contact
minecraft:slime@#contact
minecraft:magma_cube@#contact
minecraft:zombified_piglin@#contact
minecraft:enderman@#contact
minecraft:blaze@#contact
minecraft:wither_skeleton@#contact
minecraft:wandering_trader@#contact
minecraft:snow_golem@#contact
minecraft:glow_squid@#contact
minecraft:drowned@#contact
minecraft:sulfur_cube@#contact
minecraft:squid@#contact
nautilus@#contact

; --- VOID DAMAGE (End/Perimeter Farms) ---
minecraft:enderman@#void
minecraft:zombie@#void
minecraft:skeleton@#void
minecraft:creeper@#void
minecraft:spider@#void
minecraft:witch@#void
minecraft:zombie_villager@#void
minecraft:drowned@#void
minecraft:husk@#void
minecraft:stray@#void
minecraft:pillager@#void
minecraft:cave_spider@#void
minecraft:glow_squid@#void
minecraft:slime@#void
minecraft:magma_cube@#void
minecraft:silverfish@#void
minecraft:evoker@#void
minecraft:vindicator@#void
minecraft:ravager@#void

; --- ZOMBIE ORE & DRIPLEAF SPAM ---
minecraft:deepslate_redstone_ore@#zombie
minecraft:redstone_ore@#zombie
minecraft:big_dripleaf@#zombie
minecraft:big_dripleaf_stem@#zombie

; --- FREEZE DAMAGE (Powder Snow / Snow Farms) ---
minecraft:zombie@#freeze
minecraft:skeleton@#freeze
minecraft:creeper@#freeze
minecraft:spider@#freeze
minecraft:cave_spider@#freeze
minecraft:enderman@#freeze
minecraft:witch@#freeze
minecraft:zombie_villager@#freeze
minecraft:drowned@#freeze
minecraft:husk@#freeze
minecraft:stray@#freeze
minecraft:pillager@#freeze
minecraft:evoker@#freeze
minecraft:vindicator@#freeze
minecraft:ravager@#freeze
minecraft:phantom@#freeze
minecraft:slime@#freeze
minecraft:magma_cube@#freeze
minecraft:silverfish@#freeze
```
<!-- END_BLACKLIST_DEREXXD -->

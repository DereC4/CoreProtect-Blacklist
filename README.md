# CoreProtect-Blacklist-Settings
Entities take up the most database space in CoreProtect, around 5 times more than blocks. This is an optimal CoreProtect plugin blacklist.txt that can be easily copied for servers, that is easily configurable, allowing the removal of mobs cluttering your database from farms while keeping named mobs tracked.

Copy this into your `blacklist.txt`

```
#dispenser
#hopper
#guardian
#cramming
DerexXD
#bonemeal
#gravity
#glow_squid
#squid

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

; --- LAVA & FIRE (Iron/Mob Farms) ---
minecraft:spider@#lava
minecraft:enderman@#lava
minecraft:witch@#lava
minecraft:zombie_villager@#lava
minecraft:drowned@#lava
minecraft:husk@#lava
minecraft:stray@#lava
minecraft:pillager@#lava
minecraft:cave_spider@#lava
minecraft:glow_squid@#lava
minecraft:slime@#lava
minecraft:magma_cube@#lava
minecraft:silverfish@#lava
minecraft:evoker@#lava
minecraft:vindicator@#lava
minecraft:ravager@#lava
minecraft:bat@#lava
minecraft:cod@#lava
minecraft:salmon@#lava
minecraft:pufferfish@#lava
minecraft:tropical_fish@#lava
minecraft:chicken@#lava
minecraft:axolotl@#lava
minecraft:spider@#fire
minecraft:zombie@#fire
minecraft:skeleton@#fire
minecraft:creeper@#fire
minecraft:enderman@#fire
minecraft:witch@#fire
minecraft:pillager@#fire

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

; --- OTHER FARM TYPES ---
minecraft:guardian@#suffocation
minecraft:shulker@#shulker_bullet
minecraft:glow_squid@#glow_squid
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
minecraft:witch@#suffocation

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

; --- BIG DRIPLEAF TILT ---
minecraft:zombie@big_dripleaf
minecraft:skeleton@big_dripleaf
minecraft:creeper@big_dripleaf
minecraft:spider@big_dripleaf
minecraft:cave_spider@big_dripleaf
minecraft:enderman@big_dripleaf
minecraft:witch@big_dripleaf
minecraft:drowned@big_dripleaf
minecraft:husk@big_dripleaf
minecraft:stray@big_dripleaf
minecraft:pillager@big_dripleaf
minecraft:evoker@big_dripleaf
minecraft:vindicator@big_dripleaf
minecraft:ravager@big_dripleaf
minecraft:zombified_piglin@big_dripleaf
minecraft:piglin@big_dripleaf
minecraft:wither_skeleton@big_dripleaf
minecraft:slime@big_dripleaf
minecraft:magma_cube@big_dripleaf

; --- REDSTONE ORE LIGHTING SPAM ---
minecraft:zombie@redstone_ore
minecraft:zombie@deepslate_redstone_ore
minecraft:skeleton@redstone_ore
minecraft:skeleton@deepslate_redstone_ore
minecraft:creeper@redstone_ore
minecraft:creeper@deepslate_redstone_ore
minecraft:spider@redstone_ore
minecraft:spider@deepslate_redstone_ore
minecraft:cave_spider@redstone_ore
minecraft:cave_spider@deepslate_redstone_ore
minecraft:enderman@redstone_ore
minecraft:enderman@deepslate_redstone_ore
minecraft:witch@redstone_ore
minecraft:witch@deepslate_redstone_ore
minecraft:drowned@redstone_ore
minecraft:drowned@deepslate_redstone_ore
minecraft:husk@redstone_ore
minecraft:husk@deepslate_redstone_ore
minecraft:stray@redstone_ore
minecraft:stray@deepslate_redstone_ore
minecraft:pillager@redstone_ore
minecraft:pillager@deepslate_redstone_ore
minecraft:evoker@redstone_ore
minecraft:evoker@deepslate_redstone_ore
minecraft:vindicator@redstone_ore
minecraft:vindicator@deepslate_redstone_ore
minecraft:ravager@redstone_ore
minecraft:ravager@deepslate_redstone_ore
minecraft:zombified_piglin@redstone_ore
minecraft:zombified_piglin@deepslate_redstone_ore
minecraft:slime@redstone_ore
minecraft:slime@deepslate_redstone_ore
```

# Jakob Sailer BSP Deobfuscator

This tool aims to reverse the obfuscation done to BSPs by Jakob Sailer's tool.  

Below is a list of the protections that can be put onto a BSP and this tool's ability to reverse them. 

| Method               | Reversed? | Notes                                                                                           |
|----------------------|-----------|-------------------------------------------------------------------------------------------------|
| Brush Obfuscation    | ✅         | Some brushes don't have textures, that links to the next one.                                   |
| Texture Obfuscation  | ❌         | This one takes a little more work, I actually have a few ideas that I need to try.              |
| Entity Extraction    | ❌         | This one will not be implemented at all, as it is impossible to reverse.                        |
| Entity Relocation    | ❌         | Again, another one that cannot be reversed.                                                     |
| Entity Garbage/Crash | ✅         | If the command flag is specified, then it just removes the entity lump and puts a blank one in. |

## How the protections work

### Brush Obfuscation
Any brush that has 6 sides (a cuboid) has the number of sides replaced with a 0.  
Yeah, it's that easy.

### Texture Obfuscation
Now, obviously the textures look fine in game, so what gives?  
Well this is because it randomises the texinfo value in LUMP_BRUSHSIDES which isn't used by the game.

As there is no direct way to link brushes and brushsides and the face array entries that are used to render the brush, this cannot easily be reversed.  
I think I see a possible way, but possibly not. A crazy idea I had was to completely dump the map from in game but that doesn't seem very feasible.

### Entity Extraction
This one is not new and has been used by servers for ages now. It removes LUMP_ENTITIES from the BSP (or replaces it with a blank one) which can be loaded by a server.

### Entity Relocation
Any entities that's position isn't critical to it's operation e.g. logic entities are moved to some position (probably the origin).

### Entity Garbage/Crash
If entities have been extracted, this just adds some text, a klaxon, and manhacks (or sometimes crashing!).

## Notes
Something seems to be changed in LUMP_GAME_LUMP (35, and it's two values), it doesn't seem important and I think it's just some offsets being changed because Jakob added text into the BSP.

A note to Jakob: It took me about 10 minutes to get a basic deobfuscator working a few months back. You can change that claim on your website now.

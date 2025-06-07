## Macropad for CAD
----
```
Title: CAD-PAD (it sucks i know)

Author: ryan d

Description: A macropad with all of the shortcuts that I need for my CAD work.

Created: 6-6-2025
```
----
# 6-6-2025 - 6 hours

## Planninmg

I spent the first little bit just doing a bit of reserch into what I want to have my layout be, and I have decided to have 12 keys, and 3 leds. This is so that I can have three settings on the pad, with 11 keys each, giving me 33 shortcuts in total. There will be one switch to cycle through the modes, Sketch, Part Studio, and Assembly. The LEDs are there to indicate which mode is currently activated.

This is the layout and list of shortcuts that I settled on, with a main 5x2 grid, and an upper row for the last switches and LED indicators. It isnt anything artistic, but more suits my aesthetic of nice blocky chunks that I seem to aquire, and if I leave the microcontroller exposed, I thinkl that could look realy good.

![image](https://github.com/user-attachments/assets/9d017bba-e9dd-44fb-b9a6-1c294e0a7d1c)

(Pardon the bad handwritting, here is everything I wrote down)

| Part Studio | Sketch | Assembly |
|-------------|--------|----------|
| Extrude | Line | Mate |
| Loft | Circle | Revolute Mate |
| Fillet | Coincident | Group |
| Mirror | Parallel | Relations (Gear) |
| Boolean | Tangent | Relations (Rack & Pinnion) | 
| Plane | Equal | Relations (Screw) |
| Split | Midpoint | Relations (Linear) |
| Transform | Perpendicular | Replace Instance |
| Scetch | Mirror | Part Studio in Context |
| TBD | TBD | Import |

This was all that I had the forsight to do, so after skimming some yutube tutorials (https://www.youtube.com/watch?v=8WXpGTIbxlQ&t=737s) I decided to get into KiCAD

## KiCAD Setup

This part was mixed into my time acctualy cadding, but for simplicities sake, ill lump it all here

I had a rough start with libraries because for the first haour I was importing them wrong, so they reported as loaded, but showed no files, but after much futile troubleshooting and unzipping, I mannaged to get all of the assorted libraries that I had downloaded onto KiCAD, and in the end I had something like 6 redundant libraries, but it was worth it in the end.

## Schematic

This part was the least frustrating, but also the leas fun in my oppinion, as it was pretty uneventful, and just a bunch of layout and making sure everything conneted well.

![image](https://github.com/user-attachments/assets/fb20f33d-2dfe-4983-abf7-e188a1229d3e)

The layout that I came up with is nothing fancy, just the standard grid of swiches and diodes to fit more switches on a sicgle controller board, plus some led wiring.

## PCB

This was the fun part for me, as it was a fun puzzle to route all of the wires well, and also to make as few crossing paths as possible, which involved switching the order of some wiring elements, but that was about it for that. The real pain was figuring out what was wrong with my diode footprint, because it summarily refused to connect to anything else. I eventualy fixed it by using a generic diode footprint, but that only worked after 30 minutes of trouble shooting and scrolling on old forums. However, after that it was all smooth and i ended up with this pcb.

![image](https://github.com/user-attachments/assets/c1fefec3-8ac1-4420-a4ea-b4257a7a9b29)

I couldnt get any of my components to render on it, but it should be fine to start cadding a case around

## Case

I cadded the case in Onshape, which works the best on linux for me, and I gave it a cantaleavered base so that it would be more comfortable to rest my hand on, and an open top to show all the electronics.

![image](https://github.com/user-attachments/assets/3e817a60-0c42-4e0f-aae6-d77c80af4d39)

The base PCB also came togeather quite well once I got the parts on it, and it was super easy to model everything to spec around it.

![image](https://github.com/user-attachments/assets/0895efd6-6f5f-49f2-99ff-1468760a5a98)

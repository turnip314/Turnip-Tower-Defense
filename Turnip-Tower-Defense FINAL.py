#Turnip Tower Defense
#A game where turnips fight against math problems
#Written by Andrew Luo

#Imports modules required
import simplegui
import math
import random

#Images will all be uploaded here
#Background images
menu_image = simplegui.load_image("http://i.imgur.com/Cj1Ye66.png")
menu_chalkboard_image = simplegui.load_image("http://i.imgur.com/guJqiqG.png")
chalkboard_image = simplegui.load_image("http://i.imgur.com/tpvzUbd.jpg")
field_image = simplegui.load_image("http://i.imgur.com/PDRSzw3.jpg")
wood_texture_image = simplegui.load_image("http://i.imgur.com/wQB57cN.jpg")
roots_image = simplegui.load_image("http://i.imgur.com/HiChqsE.jpg")
board_image = simplegui.load_image("http://i.imgur.com/dgBBmem.png")

#Button images and frame images
normie_start_button = simplegui.load_image("http://i.imgur.com/cZjWCh1.jpg")
nontrivial_start_button = simplegui.load_image("http://i.imgur.com/uQ4VrWL.jpg")
deep_start_button = simplegui.load_image("http://i.imgur.com/EiTJ5KO.jpg")
help_button = simplegui.load_image("http://i.imgur.com/QB0g3HF.jpg")
about_button = simplegui.load_image("http://i.imgur.com/KrwKz1j.jpg")
start_image = simplegui.load_image("http://i.imgur.com/v2jILrO.jpg")
home_image = simplegui.load_image("http://i.imgur.com/4NdWXyZ.png")

#All image frames are 70 by 60
speed1_image_frame = simplegui.load_image("http://i.imgur.com/sQymyqb.jpg")
speed2_image_frame = simplegui.load_image("http://i.imgur.com/dBGeqNd.jpg")
speed3_image_frame = simplegui.load_image("http://i.imgur.com/dOjA5kI.jpg")
shield_image_frame = simplegui.load_image("http://i.imgur.com/bJPImRn.jpg")

#Icons are 20 by 20
speed1_icon = simplegui.load_image("http://i.imgur.com/OtooLAh.png")
speed2_icon = simplegui.load_image("http://i.imgur.com/VBx0wpC.png")
speed3_icon = simplegui.load_image("http://i.imgur.com/TCKaAVi.png")
shield_icon = simplegui.load_image("http://i.imgur.com/fqBHZDn.png")

#Tower selection is 60 by 60
normie_image_frame = simplegui.load_image("http://i.imgur.com/zQ7uRyI.jpg")
permuturnip_image_frame = simplegui.load_image("http://i.imgur.com/9hCo0su.jpg")
illuminati_image_frame = simplegui.load_image("http://i.imgur.com/fbVLg7R.jpg")
multitasker_image_frame = simplegui.load_image("http://i.imgur.com/QHfMc3D.jpg")
procrastinator_image_frame = simplegui.load_image("http://i.imgur.com/FJunFNZ.jpg")
modular_image_frame = simplegui.load_image("http://i.imgur.com/YihIQfm.jpg")
fp_image_frame = simplegui.load_image("http://i.imgur.com/hZdI55s.jpg")
farm_image_frame = simplegui.load_image("http://i.imgur.com/DX8Wlzp.jpg")

#These are 200 by 100
freeplay_image = simplegui.load_image("http://i.imgur.com/LuJL1Zf.png")
leave_image = simplegui.load_image("http://i.imgur.com/tCPcCbm.png")
win_image = simplegui.load_image("http://i.imgur.com/WERcij2.png")
lose_image = simplegui.load_image("http://i.imgur.com/AryP0u9.png")

#Sprite images
#Turnip images are 100 by 100
hero_turnip = simplegui.load_image("http://i.imgur.com/ef7w0cW.png")
hero_turn_sprite = simplegui.load_image("http://i.imgur.com/0jDmxIo.png")
normie_sprite = simplegui.load_image("http://i.imgur.com/HsUjPNo.png")
permuturnip_sprite = simplegui.load_image("http://i.imgur.com/InobXW9.png")
illuminati_sprite = simplegui.load_image("http://i.imgur.com/I9BhUEx.png")
multitasker_sprite = simplegui.load_image("http://i.imgur.com/quis9cK.png")
procrastinator_sprite = simplegui.load_image("http://i.imgur.com/IVvh9Ne.png")
modular_sprite = simplegui.load_image("http://i.imgur.com/ef7w0cW.png")

#Projectile images are 20 by 20
potato_sprite = simplegui.load_image("http://i.imgur.com/tvjP8N4.png")
orb_sprite = simplegui.load_image("http://i.imgur.com/3an2tKW.png")
pascal_sprite = simplegui.load_image("http://i.imgur.com/N5mjwM9.png")
eye_sprite = simplegui.load_image("http://i.imgur.com/Y2EwFMB.png")
mod_sprite = simplegui.load_image("http://i.imgur.com/6Iv1KAI.png")
#60 by 60
ball_sprite = simplegui.load_image("http://i.imgur.com/TL0fDbL.png")
#Rings are 200 by 200
sun_ring = simplegui.load_image("http://i.imgur.com/51eQsth.png")
water_ring = simplegui.load_image("http://i.imgur.com/IjwYeKI.png")
fire_ring = simplegui.load_image("http://i.imgur.com/HTQqcLd.png")
energy_ring = simplegui.load_image("http://i.imgur.com/qajspRc.png")

#Drops are 20 by 20
health_drop = simplegui.load_image("http://i.imgur.com/VMxs7yz.png")
money_drop = simplegui.load_image("http://i.imgur.com/Pefye0R.png")
speed_drop = simplegui.load_image("http://i.imgur.com/IXNAnCx.png")

#Pose images are 200 by 200
normie_pose = simplegui.load_image("http://i.imgur.com/32kgUIh.png")
permuturnip_pose = simplegui.load_image("http://i.imgur.com/aAy0Wxo.png")
illuminati_pose = simplegui.load_image("http://i.imgur.com/DroDZzj.png")
multitasker_pose = simplegui.load_image("http://i.imgur.com/uSyvcPD.png")
procrastinator_pose = simplegui.load_image("http://i.imgur.com/CDRy3ZY.png")
modular_pose = simplegui.load_image("http://i.imgur.com/YDHSUsV.png")
fp_pose = simplegui.load_image("http://i.imgur.com/3sSP9sF.png")
farm_pose = simplegui.load_image("http://i.imgur.com/RmvdBVT.png")

#Support images are 50 by 50
fp_sprite = simplegui.load_image("http://i.imgur.com/Cz6zxKA.png")
farm_sprite = simplegui.load_image("http://i.imgur.com/lHCed4R.png")


#Math image sprites. All these images are 50 by 50
arith1_sprite = simplegui.load_image("https://i.imgur.com/oHcNyvH.png")
arith2_sprite = simplegui.load_image("https://i.imgur.com/oV313rr.png")
arith3_sprite = simplegui.load_image("https://i.imgur.com/x0bhrZz.png")
arith4_sprite = simplegui.load_image("https://i.imgur.com/jt8jEsp.png")
combo_sprite = simplegui.load_image("https://i.imgur.com/BRmSuAE.png")
geometry_sprite = simplegui.load_image("https://i.imgur.com/2m0mQkR.gif")
algebra_sprite = simplegui.load_image("https://i.imgur.com/7VrFDAX.png")
rates_sprite = simplegui.load_image("https://i.imgur.com/M7lQE32.png")
theory_sprite = simplegui.load_image("https://i.imgur.com/5Bt8O1Z.png")
mental_sprite = simplegui.load_image("https://i.imgur.com/4CcjRBh.png")
proof_sprite = simplegui.load_image("https://i.imgur.com/ugTa2G7.png")
math_sprites = {'arithmetic':[arith1_sprite,arith1_sprite,arith1_sprite,arith1_sprite],
                'combo':[combo_sprite],
                'geometry':[geometry_sprite],
                'rates':[rates_sprite],
                'number theory':[theory_sprite],
                'mental':[mental_sprite],
                'proof':[proof_sprite],
                'algebra':[algebra_sprite]}

#Help text are stored here, page number then position, followed by text
#used for the help menu
help_text = {1:[[1, 0,"Welcome to Turnip Tower Defense!"],
                   [3, 0, "Your game objective is to help your turnip solve math problems. Turnips"],
                   [4, 0, "are friendly but easily stressed out - they can't let a math problem get"],
                   [5, 0, "too close to them or they will start losing health from anxiety. You're"],
                   [6, 0, "trying to solve math problems before they catch up to you. "],
                   [8, 0, "Luckily, turnips have friends who can come to their help in exchange for"],
                   [9, 0, "IQ points. Each turnip friend has unique strengths and weaknesses, and"],
                   [10, 0, "are required to get you far into the game. Here they are:"],
                   [14.5, 0, "          Normie Turnip          Permuturnip          Illuminati Turnip "],
                   [19, 0, "          Multitasker         Procrastinator     Genetically Modular Turnip"]],
             2:[[1, 0,"                        Normie Turnip"],
                [2, 0,"                        Intel: Low"],
                [3, 0,"                        Speed: Medium-Fast"],
                [4, 0,"                        Cost: Very Cheap"],
                [5, 0,"                        Vision: Medium-Low"],
                [7, 0,"A cheap starting tower with very cost-efficient upgrades"],
                [8.7, 0,"Upgrade Path 1"],
                [10, 0,"1) Turnip Glasses"],
                [11, 0,"Better turnip vision means it can"],
                [12, 0,"shoot further."],
                [13.3, 0,"2) Ambidexterity"],
                [14.3, 0,"Turnip can work with both hands,"],
                [15.3, 0,"doubling the productivity."],
                [16.6, 0,"3) Terence Tao Fan Club"],
                [17.6, 0,"Having a positive role model strongly"],
                [18.6, 0,"improves speed and intelligence."],
                [8.7, 7.6,"Upgrade Path 2"],
                [10, 7.6,"1) Smarter Turnip"],
                [11, 7.6,"Greater attack power."],
                [12, 7.6, ""],
                [13.3, 7.6,"2) Reliable Knowledge"],
                [14.3, 7.6,"Confident turnip shoots large"],
                [15.3, 7.6,"projectiles that miss less often."],
                [16.6, 7.6,"3) Faceoff Training"],
                [17.6, 7.6,"Fast doesn't mean smart. Greater"],
                [18.6, 7.6,"attack speed but at the cost of intel."]],
                
                3:[[1, 0,"                        Permuturnip"],
                [2, 0,"                        Intel: Medium"],
                [3, 0,"                        Speed: Medium"],
                [4, 0,"                        Cost: Cheap"],
                [5, 0,"                        Vision: Medium"],
                [7, 0,"A medium intel turnip that specializes in combinatorics."],
                [8.7, 0,"Upgrade Path 1"],
                [10, 0,"1) Factorial!!!"],
                [11, 0,"Excited turnip shoots much faster"],
                [12, 0,""],
                [13.3, 0,"2) Lucky Charm"],
                [14.3, 0,"Effective casework allows turnip to"],
                [15.3, 0,"work faster and smarter."],
                [16.6, 0,"3) Triangle Obsession"],
                [17.6, 0,"Strong worship of Pascal has the "],
                [18.6, 0,"turnip working harder and faster."],
                [8.7, 7.6,"Upgrade Path 2"],
                [10, 7.6,"1) Efficiency"],
                [11, 7.6,"Triangles have one extra pierce."],
                [12, 7.6, ""],
                [13.3, 7.6,"2) Pi-Mutation"],
                [14.3, 7.6,"Mutation process allows turnip"],
                [15.3, 7.6,"to be smarter, but inconsistent."],
                [16.6, 7.6,"3) Per-mutation"],
                [17.6, 7.6,"Mutated turnip is much smarter."],
                [18.6, 7.6,"Better vision and intel."]],
                
                4:[[1, 0,"                        Illuminati Turnip"],
                [2, 0,"                        Intel: High"],
                [3, 0,"                        Speed: Very Low"],
                [4, 0,"                        Cost: High"],
                [5, 0,"                        Vision: High"],
                [7, 0,"Only the turnip with the all-seeing eye can masterfully do geometry."],
                [8.7, 0,"Upgrade Path 1"],
                [10, 0,"1) Improved Art Skills"],
                [11, 0,"Better diagrams allows turnip to do"],
                [12, 0,"geometry much faster."],
                [13.3, 0,"2) Keen Eyesight"],
                [14.3, 0,"Turnip shoots further. Also gives"],
                [15.3, 0,"intel boost."],
                [16.6, 0,"3) Wrecking Ball"],
                [17.6, 0,"Adds a powerful wrecking ball attack "],
                [18.6, 0,"to crush all math in its path."],
                [8.7, 7.6,"Upgrade Path 2"],
                [10, 7.6,"1) Geometry Kit"],
                [11, 7.6,"Better tools allows turnip to work."],
                [12, 7.6, "on problems faster."],
                [13.3, 7.6,"2) All Seeing Eye"],
                [14.3, 7.6,"Projectiles chase after their"],
                [15.3, 7.6,"target."],
                [16.6, 7.6,"3) Turnip God"],
                [17.6, 7.6,"Sacrifices all turnips in its"],
                [18.6, 7.6,"range but takes in their power."]],
                
                5:[[1, 0,"                        Multitasker"],
                [2, 0,"                        Intel: Low"],
                [3, 0,"                        Speed: Fast"],
                [4, 0,"                        Cost: Medium"],
                [5, 0,"                        Vision: Low"],
                [7, 0,"A hard working turnip that can work on 8 things at a time!"],
                [8.7, 0,"Upgrade Path 1"],
                [10, 0,"1) Isolation"],
                [11, 0,"Fewer distractions allows turnip to"],
                [12, 0,"work faster and effectively."],
                [13.3, 0,"2) Improved Work Space"],
                [14.3, 0,"Turnip can reach much further."],
                [15.3, 0,"Distance boost to all attacks."],
                [16.6, 0,"3) Crystal Math"],
                [17.6, 0,"High turnip shoots super fast "],
                [18.6, 0,"and up to 12 projectiles!"],
                [8.7, 7.6,"Upgrade Path 2"],
                [10, 7.6,"1) Focused Attacks"],
                [11, 7.6,"Projectiles fly out much further."],
                [12, 7.6, ""],
                [13.3, 7.6,"2) Concentration"],
                [14.3, 7.6,"Turnip is less likely to miss"],
                [15.3, 7.6,"thanks to larger projectiles."],
                [16.6, 7.6,"3) Ring Theory"],
                [17.6, 7.6,"Replaces orbs with rings because"],
                [18.6, 7.6,"who doesn't love rings?"]],
                
                6:[[1, 0,"                        Procrastinator"],
                [2, 0,"                        Intel: Low"],
                [3, 0,"                        Speed: Slow"],
                [4, 0,"                        Cost: Very Cheap"],
                [5, 0,"                        Vision: Low"],
                [7, 0,"Laziness isn't bad if used correctly.. this turnip slows incoming math!"],
                [8.7, 0,"Upgrade Path 1"],
                [10, 0,"1) Turnip Discipline"],
                [11, 0,"Lazy turnip must work harder at"],
                [12, 0,"being lazy. Gives a speed boost."],
                [13.3, 0,"2) Minecraft Distraction"],
                [14.3, 0,"Distracted turnip procrastinates"],
                [15.3, 0,"even more."],
                [16.6, 0,"3) Time Dilation"],
                [17.6, 0,"All problems in a small range of "],
                [18.6, 0,"the turnip will move much slower."],
                [8.7, 7.6,"Upgrade Path 2"],
                [10, 7.6,"1) Facebook"],
                [11, 7.6,"Social influence of laziness over."],
                [12, 7.6, "a larger area."],
                [13.3, 7.6,"2) Stalin'"],
                [14.3, 7.6,"Will sometimes stall and inflict"],
                [15.3, 7.6,"damage to math."],
                [16.6, 7.6,"3) Greater Influence"],
                [17.6, 7.6,"Slow effect lasts much longer, but"],
                [18.6, 7.6,"you have to solve them eventually!"]],
                
                7:[[1, 0,"                        Genetically Modular Turnip (GMT)"],
                [2, 0,"                        Intel: Medium"],
                [3, 0,"                        Speed: Very Fast"],
                [4, 0,"                        Cost: High"],
                [5, 0,"                        Vision: Very High"],
                [7, 0,"A turnip that you can aim... the second closest turnip to being human"],
                [8.7, 0,"Upgrade Path 1"],
                [10, 0,"1) Bull's Eye Practice"],
                [11, 0,"Better precision of shots."],
                [12, 0,""],
                [13.3, 0,"2) Genetic Alertness"],
                [14.3, 0,"Shoots even faster than it already"],
                [15.3, 0,"does!"],
                [16.6, 0,"3) Fermat's Last Theorem"],
                [17.6, 0,"This space is too small to contain"],
                [18.6, 0,"a proper upgrade description."],
                [8.7, 7.6,"Upgrade Path 2"],
                [10, 7.6,"1) Mod-ified Shots"],
                [11, 7.6,"Projectiles fly out even further!"],
                [12, 7.6, ""],
                [13.3, 7.6,"2) Modulo Search Algorithm"],
                [14.3, 7.6,"Some projectiles will search for"],
                [15.3, 7.6,"math problems themselves."],
                [16.6, 7.6,"3) 91 Degree Potatoes"],
                [17.6, 7.6,"Shoots exploding potatoes baked at"],
                [18.6, 7.6,"91 degrees Celsius, 'cuz why not?"]],
                
                8:[[1, 0,"Well, that's all of them. Got 'em memorized? I don't think so. Don't"],
                [2, 0, "worry, you get used to what each one does as you play the game. Towers"],
                [3, 0, "come in many forms and not just turnips. There are two additional towers"],
                [4, 0, "you should familiarze yourself with. They don't help attack but they are"],
                [5, 0, "useful in other ways, by helping nearby towers or providing income. "],
                [7, 0, "Well... here they are:"],
                [17, 0, "                      Fleetwood Park                       Turnip Farm"]],
                
                9:[[1, 0,"                        Fleetwood Park"],
                [2, 0,"                        Intel: N/A"],
                [3, 0,"                        Speed: N/A"],
                [4, 0,"                        Cost: Medium-High"],
                [5, 0,"                        Vision: High"],
                [7, 0,"This support tower provides a 15% intel boost to all turnips in its range."],
                [8.7, 0,"Upgrade Path 1"],
                [10, 0,"1) Enriched Courses"],
                [11, 0,"Gives an additional 20% intel boost"],
                [12, 0,"to all nearby turnips"],
                [13.3, 0,"2) Later Classes"],
                [14.3, 0,"More sleep means more alert turnip."],
                [15.3, 0,"Grants a 10% speed boost."],
                [8.7, 7.6,"Upgrade Path 2"],
                [10, 7.6,"1) PE Dept Funding Cut"],
                [11, 7.6,"All nearby turnips and their "],
                [12, 7.6, "upgrades cost 10% less."],
                [13.3, 7.6,"2) Planning"],
                [14.3, 7.6,"Improves each turnip's vision. "],
                [15.3, 7.6,"Grants a 15% vision boost."]],
                
                10:[[1, 0,"                        Turnip Farm"],
                [2, 0,"                        Intel: N/A"],
                [3, 0,"                        Speed: N/A"],
                [4, 0,"                        Cost: High"],
                [5, 0,"                        Vision: Medium"],
                [7, 0,"Produces 3 turnips each round, worth $20 each in IQ points."],
                [8.7, 0,"Upgrade Path 1"],
                [10, 0,"1) Turnip plantation"],
                [11, 0,"Produces 5 turnips per round instead"],
                [12, 0,"of 3."],
                [13.3, 0,"2) Turnip University"],
                [14.3, 0,"Produces 12 tunips per round"],
                [15.3, 0,""],
                [8.7, 7.6,"Upgrade Path 2"],
                [10, 7.6,"1) Turnip Labour Agency"],
                [11, 7.6,"Will help you collect IQ points "],
                [12, 7.6, "within its range"],
                [13.3, 7.6,"2) Healthier Turnips"],
                [14.3, 7.6,"Collects health drops and "],
                [15.3, 7.6,"turnips are worth $100 in IQ."]],
                
                11:[[1, 0,"Let's not forget about the most important turnip in the game... the Hero!"],
                [2, 0, "Your purpose of the game is to protect the Hero - if the Hero dies, it's"],
                [3, 0, "game over. You can move your hero using WS, turn it using AD, "],
                [4, 0, "shoot using Spacebar, and activate shield by holding W and S together."],
                [5, 0, "The Hero won't get far alone, so be sure to buy towers as well!"],
                [7, 0, "In addition, you have 4 sets of boosts that can be purchased for the Hero."],
                [8,0, "Here they are:"],
                [14, 0, "There are two options for each: A short and long duration. The first three"],
                [15, 0, "boosts are speed boosts of varying degree of effectiveness, and the last one"],
                [16, 0, "increases your Hero's resistance, so it takes much less damage. These "],
                [17, 0, "boosts are expensive but can get you out of tricky situations!"],
                [19, 0, "You can hold down W and S at the same time to activate a weak shield."]],
                
                12:[[1, 0, "Last but not least, different towers are strong and weak against different"],
                [2,0, "types of math problems. These strengths and weaknesses are up to you to "],
                [3,0, "find out, but we will show you each type of math problem here:"],
                [6, 0, "Arithmetic:"],
                [10,0, "Combinatorics:"],
                [14, 0, "Mental Math:"],
                [18, 0, "Algebra:"],
                [6, 7, "Rates:"],
                [10, 7, "Number Theory:"],
                [14, 7, "Geometry"],
                [18, 7, "Proof:"]],
                
                13:[[4, 0, "     Well, that's all you need to know. Good luck. We're rooting for you!"]]
             }
#About text, same format but only one page
about_text = [[1, 0, "This game was created by the members of Turnip Productions 2017..."],
              [2, 0, "Just kidding it was a project for Programming 11. Special thanks"],
              [3, 0, "to these people:"],
              [5, 0, "Kayla Estacio:"],
              [6, 0, "For helping make the turnip sprites and images"],
              [8, 0, "Jonathan Wang:"],
              [9, 0, "For contributing ideas and for the programming help"],
              [11, 0, "Jason Mao, Terence Sun, Arti Shridhar, and Sarah Mae:"],
              [12, 0, "For test playing the game"],
              [14, 0, "And of course, Ms. Stusiak for helping out every step along the way!"],
              [16, 0, "The game wouldn't have been possible without you!"]]
#0/1 for image/sprite, sprite, center, image_size, size
#                      image, pos1, pos2, scale
help_image = {1:[[1, normie_pose, [170, 335], 200, 80],[1, permuturnip_pose, [365, 335], 200, 80],[1, illuminati_pose, [565, 335], 200, 80],
                [1, multitasker_pose, [165, 445], 200, 80],[1, procrastinator_pose, [340, 445], 200, 80],[1, modular_pose, [560, 445], 200, 80]],
              2:[[0, normie_pose, [10, 15],[210, 215], 0.6]],
              3:[[0, permuturnip_pose, [10, 15],[210, 215], 0.6]],
              4:[[0, illuminati_pose, [10, 15],[210, 215], 0.6]],
              5:[[0, multitasker_pose, [10, 15],[210, 215], 0.6]],
              6:[[0, procrastinator_pose, [10, 15],[210, 215], 0.6]],
              7:[[0, modular_pose, [10, 15],[210, 215], 0.6]],
              8:[[0, fp_pose, [165, 250], [365, 450],0.8],[0, farm_pose, [425, 250], [625, 450],0.8]],
              9:[[0, fp_pose, [10, 15], [210, 215],0.6]],
              10:[[0, farm_pose, [10, 15], [210, 215],0.6]],
              11:[[0, speed1_image_frame, [100, 280],[170, 340], 1.6], [0, speed2_image_frame, [250, 280],[320,340], 1.6], 
                  [0, speed3_image_frame, [400, 280],[470, 340], 1.6], [0, shield_image_frame, [550, 280],[620,340], 1.6]],
              12:[[1,arith2_sprite, [280, 190], 50, 35], [1,rates_sprite, [630, 190], 50, 35],
                  [1,combo_sprite, [280, 286], 50, 35], [1,theory_sprite, [630, 286], 50, 35],
                  [1,mental_sprite, [280, 382], 50, 35], [1,geometry_sprite, [630, 382], 50, 35],
                  [1,algebra_sprite, [280, 478], 50, 35], [1,proof_sprite, [630, 478], 50, 35]],
              13:[[0, roots_image, [150, 200], [650, 485], 1]]
              }

#Comment will be displayed after respective level
comment = {0:["Welcome to Turnip Tower Defense!"],
           1:["Pretty easy so far, huh? Don't worry, it gets harder."],
           2:["Don't forget to buy towers. You're gonna need them next level."],
           3:["I don't know about you, but this is the only game I've ever played", "featuring turnips and math."],
           4:["Unlike most tower defense games, your reflexes have to be sharp in", "this one. One problem can spawn into many faster ones."],
           5:["Every tower has its strengths and weakness, but none of them are", "useless. It all depends on your preferred strategy."],
           6:["The normie tower is extremely cost efficient. It just won't last you", "long later on."],
           7:["Illuminati, GMT, and Permuturnip have the strongest upgrades. They're", "expensive though, so save them for late game."],
           8:["You might find the Procrastinator or a fast-firing tower useful for", "next round. Seriously. Don't say I didn't warn you."],
           9:["Next level is the first challenge level - you will be taking on the", "COMC. Be ready for the harder than normal math that's coming."],
           10:["That was just a warmup. Have you not seen the later levels?"],
           11:["The Procrastinator does not seem very useful but will become a", "necessity for the later levels."],
           12:["The last upgrade of each path is generally very powerful.", "Don't hold back because of the price tag!"],
           13:["The Turnip Farm can make you some good money if used correctly,", "but it's the IQ-collecting upgrade that makes it so useful."],
           14:["The Fleetwood Park tower is really useful - but only if you're", "planning to put many towers beside it."],
           15:["Be careful when buying the Temple upgrade for the Illuminati","Turnip. It will sacrifice all nearby turnips."],
           16:["How are you holding out? Pretty impressive to be getting this", "far... if you're on Deep difficulty, that is."],
           17:["Besides getting stronger, the math problems also get faster.", "If you're fortunate enough to see level 100... you won't.", "That's how fast it is."],
           18:["If you haven't noticed already, the levels tend to repeat in", "style every 10 rounds. *hint hint*"],
           19:["Next level is the CMO boss. Good luck!"],
           20:["I'm impressed. But no way are you beating level 30."],
           21:["If you're playing on Nontrivial or Deep, the problems actually", "speed up over time to a logistic curve. Wait... there's math", "in a math-themed game? I'd never guess."],
           22:["How are you enjoying these sarcastic and TOTALLY useful", "comments?"],
           23:["This game actually works out pretty well as a 2-player game.", "Just have one person buying towers while the other does", "the controls."],
           24:["The X-2 farm upgrade can collect health crates too!"],
           25:["Congrats on getting this far."],
           29:["Well.. this is it. It's every mathematician's dream. Do you", "dare press play?"],
           30:["I'm not sure what to say. Looks like you mastered this game.", "I bet you were playing on Normie weren't you? Anyways,", "have fun in freeplay mode!"]
          }

# Global variables
error_message = [None, 0]
game_difficulty = None
page_number = 1
spin_timer = 0
#Buttons!!
start_buttons = [] #For game start menu
turnip_buttons = [] #For the turnip selection menu
tower_buttons = [] #For a tower upgrade
hero_buttons = [] #For hero boosts
scroll_buttons = []
confirm_buttons = []
play_button = None
quit_button = None
#These are the key controls
mouse_position = 0
up = False
down = False
left = False
right = False
space = False
#Spawn timers and shooting timers
wait_time = 0
spawn_timer = 0
level_up = True
#Hero will be created as instance of Hero class when game begins
hero = None
playing = "Start"
pause = True
level = 0
#Item selected
selection = None
#List of turnips, problems, and projectiles in a round. All instances of classes.
iq = 0
turnips = []
math_problems = []
projectiles = []
splash_attacks = []
supports = []
item_drops = []

#Dictionaries storing strength/weakness pairs
#Turnip types are neutral, permuturnip, illuminati, multitasker, procrastinator
#Math types are arithmetic, geometry, combo, mental (math), algebra, rates, number theory, and proof
strengths = {'neutral':['algebra', 'rates', 'arithmetic'], 'combo':['combo', 'arithmetic'],
            'procrastinator':['mental'], 'geometry':['geometry'],
            'multitasker':['arithmetic', 'mental', 'rates', 'algebra'],
            'number theory':['number theory', 'proofs'],
            'polymath':['algebra', 'rates', 'arithmetic', 'combo', 'mental', 'geometry', 'number theory', 'proofs']}

weaknesses = {'procrastinator':['proof', 'algebra'], 'neutral':['proof'],
             'multitasker':['geometry', 'combo'], 'combo':['geometry', 'rates'],
             'geometry':['combo', 'rates'], 'number theory':['combo', 'geometry'],
             'polymath':[]}

#Speed conditions
conditions = {'slow1':0.6, 'slow2': 0.4, 'slow3':0.25, 'speed1':2, 'speed2':2.8, 'speed3':3.5}

#Stores upgrade values for turnips
#Upgrade values are in order: [power, radius, vision, pierce,   intel, wait, tower size, COST]
#Vision, intel, wait are multiplicative, not additive
#Support upgrades work differently so only cost is stored
upgrade = {'neutral':{1:[0,0,1.5,0,1,1,0, 50], 2:[0,0,1,0,1,1,0, 300], 3:[8, 1,1,0,1,0.6,2,1000],
                      4:[5,0.5,1,0,1,1,0, 125], 5:[0,3,1,0,1,1,0,75], 6:[0,0,1,0,0.8,0.6,0, 250]},
           
           'combo':{1:[0,0,1,0,1,0.8,0, 100], 2:[0,0,1,0,1.5,0.9,0, 300], 3:[0,0,1,0,1,0.6,0, 1500],
                    4:[0,0,0.9,1,1,1,0, 40], 5:[0,0,1,0,1,1,0, 350], 6:[0,2,1.2,0,5,1,5,2500]},
           
           'geometry':{1:[0,0,1,0,1,0.7, 0, 350], 2:[0,0,1.3,0,1,1.25, 0.8, 0, 500], 3:[0,0,1,0,1,1,0,850],
                      4:[8,0,1,0,1,0.8,0,400], 5:[0,0,1,0,1,1,0,800], 6:[0,0,1.5,1,1,1,0,65000]},
           
           'polymath':{1:[0,0,1,0,1,0.7, 0, 250], 2:[0,0,1.3,0,1,1.25, 0.8, 0, 500], 3:[0,0,1,0,1,1,0,850],
                      4:[8,0,1,0,1,0.8,0,300], 5:[0,0,1,0,1,1,0,800], 6:[0,0,1.5,1,1,1,0,65000]},
           
           'multitasker':{1:[3,0,1,0, 1,0.9,0,200], 2:[0,0,1.4,0,1,1,0,250], 3:[0,0,1,2,2, 0.75,0,1750],
                          4:[1,0,1,0,1,1,0,75], 5:[2,4,1,0,1,1,0,250], 6:[0,0,1,50,3, 0.7,5,3500]},
           
           'procrastinator':{1:[0,0,1,0,1,1,6,0,100], 2:[0,0,1,0,1,1,0,250], 3:[0,0,1,5,1,1,5,1500],
                             4:[0,0,1.7,3,1,1,0,150], 5:[0,0,1,0,1,1,0,300], 6:[0,0,1,0,1,1,5,750]},
           
           'number theory':{1:[0,0,1,0,1,1,0,200],2:[0,0,1,0,1,0.7,1,0,500],3:[2, 1, 1.1, 0, 5, 0.8, 0,4000],
                            4:[0,0,1.3,0,1,1,0,300],5:[0,0,1,0,1,1,0,500],6:[5,1,1,0,2,1,0,8000]},  
           
           'Fleetwood Park':{1:[750], 2:[1000],
                             3:[500], 4:[1000]},
           
           'Turnip Farm':{1:[300], 2:[1000],
                         3:[400], 4:[5000]}
          }
#Put this in separate dictionary to avoid clutter
upgrade_names = {'neutral':{1:"Turnip Glasses", 2:"Ambidexterity", 3:"Terence Tao Fan Club",
                         4:"Smarter Turnip", 5:"Reliable Knowledge", 6:"Faceoff Training"},
                 
                'combo':{1:"Factorial!!!", 2:"Lucky Charm", 3:"Triangle Obsession",
                         4:"Efficiency", 5:"Pi-mutation", 6:"Per-mutation"},
                 
                'geometry':{1:"Improved Art Skills", 2:"Keen Eyesight", 3:"Wrecking Ball",
                            4:"Geometry Kit", 5:"All Seeing Eye", 6:"Turnip God"},
                 
                'polymath':{1:"Improved Art Skills", 2:"Keen Eyesight", 3:"Wrecking Ball",
                            4:"Geometry Kit", 5:"All Seeing Eye", 6:"Turnip God"},
                 
                'multitasker':{1:"Isolation", 2:"Improved Work Space", 3:"Crystal Math",
                                4:"Focused Attack", 5:"Concentration", 6:"Ring Theory"},
                 
                'procrastinator':{1:"Turnip Discipline", 2:"Minecraft Distraction", 3:"Time Dilation",
                                  4:"Facebook Distraction", 5:"Stalin'", 6:"Greater Influence"},
                 
                'number theory':{1:"Bull's Eye Practice", 2:"Genetic Alertness", 3:"Fermat's Last Theorem",
                                 4:"Mod-ified Shots", 5:"Modulo Search Algorithm", 6:"91 Degree Potatoes"},
                 
                'Fleetwood Park':{1:"Enriched Courses", 2:"Later Classes",
                                  3:"PE Dept Funding Cut", 4:"Planning"},
                 
                'Turnip Farm':{1:"Turnip Plantation", 2:"Turnip University",
                               3:"Turnip Labour Agency", 4:"Healthier Turnips"}
                }

#Again, separate to avoid clutter
#How the upgrade will be described in game
upgrade_descriptions = {'neutral':{1:["Gives better vision."], 2: ["Turnip works with two hands."], 3:["Improved attack speed and", "power."],
                                   4:["Greater power."], 5:["Orbs are larger."], 6:["Shoots faster but less", "powerfully."]},
                        
                        'combo':{1:["Excited turnip shoots faster."], 2:["Faster speed and better intel."], 3:["Shoots in the shape of a", "triangle with improved attack", "speed."],
                                 4:["Shots have extra pierce."], 5:["Inconsistent but powerful", "shots."], 6:["Master of effiency and", "intelligence."]},
                        
                        'geometry':{1:["Shoots significantly faster."], 2:["Shots are more powerful and", "go further."], 3:["Adds a powerful wrecking ball", "attack to crush those math", "problems."],
                                    4:["This kit will maximize", "productivity with a speed", "and power boost."], 5:["Only a true Illuminati can", "pass their foresight onto", "the projectiles themselves."], 6:["This turnip demands sacrifice,", "and in return will bring", "upon the ultimate weapon of", "math destruction."]},
                        
                        'polymath':{1:["Shoots significantly faster."], 2:["Shots are more powerful and", "go further."], 3:["Adds a powerful wrecking ball", "attack to crush those math", "problems."],
                                    4:["This kit will maximize," "productivity with a speed", "and power boost."], 5:["Only a true Illuminati can", "pass their foresight onto", "the projectiles themselves."], 6:["This turnip demands sacrifice,", "and in return will bring", "upon the ultimate weapon of", "math destruction."]},
                        
                        'multitasker':{1:["Isolated turnip works faster", "and harder."], 2:["Turnip projectiles reach out", "much further."], 3:["Don't do meth, do math.","It's the only way to shoot", "12 projectiles at once!"],
                                        4:["Projectiles fly out much", "further."], 5:["Shoots larger orbs that miss", "less often."], 6:["Shoots a large ring around", "the turnip that deals", "area damage."]},
                        
                        'procrastinator':{1:["Even a lazy turnip can work", "faster with some discipline."], 2:["More distraction = slower", "math problems."], 3:["The best way to procrastinate.", "All problems in short range of", "turnip will move very slowly."],
                                          4:["Influences laziness over a", "larger area."], 5:["Stalls nearby math problems.", "I apologize for the pun,","comrade."], 6:["Problems are affected by", "slow for much longer."]},
                        
                        'number theory':{1:["Greater accuracy of shots."], 2:["Turnip shoots faster"], 3:["I have discovered a truly", "remarkable way to solve", "problems, for which the length", "of this upgrade description", "is too small to contain."],
                                         4:["Shots fly out further."], 5:["Every few shots will target","a problem themselves."], 6:["A fresh potato baked at 91", "degrees Celsius, perfect for", "blowing up your math", "homework."]},
                        
                        'Fleetwood Park':{1:["Grants an additional 20%","intel boost to turnips."], 2:["More sleep = better", "productivity. Turnips work", "faster"],
                                          3:["All turnips in range will", "cost 10% less. Also applies", "to their upgrades."], 4:["Turnips can better foresee", "the future... at least they", "can see further."]},
                        
                        'Turnip Farm':{1:["Produces 5 IQ points instead", "of 3."], 2:["Produces up to 12 IQ points", "per round."],
                                       3:["Will automatically collect", "nearby IQ points."], 4:["IQ points are worth 50%", "more."]}
                       }
                                   

#Stores initial attack conditions
#Format - [group, radius, sprite, pierce]
#Will be modified according to upgrade of tower
init_attack = {'neutral': ['neutral', 1, orb_sprite, 1],
              'combo': ['combo', 2.5, pascal_sprite, 2],
              'geometry': ['geometry', 5, eye_sprite, 1],
              'multitasker':['multitasker', 1, orb_sprite, 1],
              'procrastinator': ['procrastinator', 75, water_ring, 2],
              'number theory':['number theory', 1, mod_sprite, 1],
              'polymath':['polymath', 10, eye_sprite, 3]}


#Stores attributes of math: strength, difficulty, speed, spawn timer, max_spawn
#These are meant to be ratios to give an idea of what each type is like
math_types = {'arithmetic':[7, 6, 0.4, 300, 2],
                 'geometry':[20, 24, 0.3, 350, 3],
                 'combo':[15, 16, 0.5, 250, 2],
                 'mental':[5, 5, 0.7, 150, 1],
                 'algebra':[10, 10, 0.5, 200, 3],
                 'rates':[15, 12, 0.6, 300, 2],
                 'proof':[25, 50, 0.2, 500, 5],
                'number theory':[15, 20, 0.4, 300, 3]}
                 
#Function for generating levels through a certain level interval (1-30 for most cases)
def generate_level(start, end):
    global levels
    #m is multiplier for auto-generated levels
    #and speed multiplier for manual levels
    #k is multiplier for manual levels
    if game_difficulty == 'Normie':
        m = 1.12 
        k = 1
    elif game_difficulty == 'Nontrivial':
        m = 1.15
        k = 1.25
    else:
        m = 1.18
        k = 1.5
    for x in range(start,end+1):
        if True:
            levels[x] = []
            for i in range(min(x+3, 100)):
                group = random.choice(['arithmetic', 'arithmetic', 'geometry', 'combo', 'mental', 'algebra', 'rates', 'proof', 'number theory'])
                math_type = []
                math_type.extend(math_types[group])
                strength, difficulty, speed, spawn_timer, max_spawn = math_type[0], math_type[1], math_type[2], math_type[3], math_type[4]
                levels[x].append([strength*m**x,difficulty*m**x, min(speed*m**(0.25*x),25), group, int(math.sqrt(x)), max_spawn, max(spawn_timer-5*x,10)])
    
    #Manual levels
    #Levels are [strength, difficulty, speed, group, tier, max_spawn, timer]
    levels[3] = [[10, 6, 0.5*m, 'arithmetic', 1, 1, 20],[20, 24, 0.4, 'geometry',1, 1, 25],[15, 16, 0.6,'combo',1, 1, 15],[10, 10, 0.6,'algebra',1,1, 20],[15, 12, 0.8,'rates',1, 1, 10]]*3
    
    levels[6] = []
    for i in range(10):
        levels[6].append([25, 70*k, 0.5*m, 'geometry', 1, 1, 150])
    
    levels[9] = []
    for i in range(35):
        levels[9].append([10, 15, 2*m, 'mental', 1, 1, 100-i])   
    
    levels[10] = []
    for i in range(6):
        group = ['algebra', 'rates', 'combo', 'number theory', 'geometry', 'proof']
        levels[10].append([30*(i+1), 60*(i+1)*k, math_types[group[i]][2]*1.5*m, group[i], 2+i/3, 4, 350])

    levels[13] = [[20, 18, 0.7, 'arithmetic', 2, 2, 30],[40, 70, 0.5, 'geometry',2, 2, 35],[30, 50, 0.7,'combo',2, 2, 25],[20, 35, 0.7,'algebra',2,2, 30],[30, 40, 1,'rates',2, 2, 20]]*4
    
    levels[16] = []
    for i in range(15):
        levels[16].append([100, 300*k, m, 'combo', 4, 4, 150])
    
    levels[19] = []
    for i in range(50):
        levels[19].append([30, 50, 3*m, 'arithmetic', 2, 2, 90-i])                
    
    levels[20] = [[1000, 800*k, 0.3*m, 'proof', 6,6,100]]*2

    levels[23] = [[80, 60, 1, 'arithmetic', 3, 3, 40],[150, 200, 0.7, 'geometry',3, 3, 45],[100, 120, 0.9,'combo',3, 3, 35],[70, 100, 1,'algebra',3,3, 40],[80, 90, 1.3,'rates',3, 3, 30]]*5
    
    levels[26] = []
    for i in range(20):
        levels[26].append([300, 1000*k, 1.5*m, 'number theory', 5, 6, 100])
    
    levels[29] = []
    for i in range(80):
        levels[29].append([100, 200, 5*m, 'arithmetic', 3, 3, 80-i])                
    
    levels[30] = [[2000, 10000*k, 0.4*m, 'proof', 7,6,100]]


#Useful in game functions

#Draws image, usually for buttons and stuff
#pos1 and pos2 are top left and bottom right corners
def draw_image(canvas, image, pos1, pos2, scale, rotation):
    WIDTH = math.fabs(pos1[0] - pos2[0])
    HEIGHT = math.fabs(pos1[1] - pos2[1])
    canvas.draw_image(image, (WIDTH/2, HEIGHT/2), (WIDTH,HEIGHT), ((pos1[0]+pos2[0])/2, (pos1[1]+pos2[1])/2), (WIDTH*scale, HEIGHT*scale), rotation)

#Draws sprite - sprites are always square in dimensions, so pos1, pos2 are not needed
def draw_sprite(canvas, sprite, center, image_size, size, direction): #All sprites will be squares, image_size is side length of image file
    #negative direction so it fits in with math
    canvas.draw_image(sprite, (image_size/2, image_size/2), (image_size,image_size), (center[0], center[1]), (size*2, size*2), direction)
    

def magnitude(vector): #Gives the magnitude of a vector
    return math.sqrt(vector[0]**2 + vector[1]**2)

def distance(a,b): #Gives the distance of two position vectors
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def direc(pos1, pos2): #Gives direction of pos2 with respect to pos1, decides where pos1 will point
    dx = pos2[0]-pos1[0]
    dy = pos2[1]-pos1[1]
    d = distance(pos1, pos2)
    if d > 0:
        return [dx/d, dy/d] #Returns direction of projectile as a vector
    else:
        return [1,0]

#Returns a vector 90 degrees clockwise
def perpendicular(vector):
    return [-vector[1], vector[0]]

#Converts a vector to one of magnitude 1
def unit(vector):
    d = distance([0,0], vector)
    return [vector[0]/d, vector[1]/d]

#Rotates a vector by i degrees clockwise
def rotate(vector, rad, i): #i is how many times it will perform that rotation
    return [math.cos(i*rad)*vector[0] - math.sin(i*rad)*vector[1], math.sin(i*rad)*vector[0] + math.cos(i*rad)*vector[1]]

#Gives the angle of a vector going clockwise from [0,-1]
def get_angle(vector):
    #UP is zero degrees in this case
    if magnitude(vector) == 0:
        return 0
    else:
        init_angle = math.asin(vector[0]/magnitude(vector))
        if vector[1] > 0:
            return math.pi - init_angle
        else:
            return init_angle
        
#Goes through position grid and checks to see if any towers have already been placed
#Position grid is [x, y, tower or 0]
#Size is size of tower, the two for loops represent the number of grids being
#covered by the tower
def has_space(position, size): #Will check if tower has space in positions list
    x,y = position[0], position[1]
    for i in range(x/5-size/5, x/5+size/5 + 1):
        for j in range((y-120)/5-size/5, (y-120)/5+size/5 + 1):
            if i >= 0 and j >= 0 and positions[i][j][-1] != 0:
                return False
    else:
        return True

#When a problem spawns this function will decide what the problem's drop is
def drop_randomizer(rand, strength, tier): #Strength is strength of problem
    #Drops can be money (iq), health, or speed potion
    if rand < 3:
        drop = Drops([0,0], [0,0], min(1+strength/10.0, 15.0), 40, money_drop, "iq", 2*strength, 1250)
    elif rand < 10:
        drop = Drops([0,0], [0,0], 7, 40, health_drop, "health", min(strength*0.5, 1000), 1500)
    elif rand < 15:
        drop = Drops([0,0], [0,0], 5, 30, speed_drop, "speed1", random.randint(200, 400), 1500)
    else:        
        drop = Drops([0,0], [0,0], min(1+math.sqrt(strength/10.0), 15.0), 40, money_drop, "iq", 7*math.sqrt(strength/2), 1250)
    return drop
 
#defeat_spawn is when a larger tier problems splits into smaller ones
#It takes on attributes of its spawner
def defeat_spawn(problem):
    spawn_num = random.randint(problem.max_spawn/2, problem.max_spawn)
    for spawn in range(spawn_num):
        group = random.choice(['arithmetic', 'arithmetic', 'geometry', 'combo', 'mental', 'algebra', 'rates', 'proof', 'number theory'])
        math_type = []
        math_type.extend(math_types[group])
        
        #Multiplier will be amount multiplied to attributes
        #of math_type list mentioned earlier
        multiplier = (problem.strength/math_type[0])*float(problem.tier-1)/problem.tier
        speed_multiplier = float(problem.tier+2)/(problem.tier+1)*math_types[group][2]/math_types[problem.group][2]
        
        #See math types list
        strength, difficulty, max_spawn = \
            math_type[0]*multiplier, math_type[1]*multiplier, math_type[4]
        speed = problem.speed*speed_multiplier
        
        #Spawns new problem in the position of its spawner
        x, y = problem.position[0], problem.position[1]
        drop = drop_randomizer(random.randint(1,100),strength, problem.tier)
        math_problems.append(Math(strength, [x,y], difficulty, speed, group, problem.tier-1, max_spawn,drop))
    
#Spawns stuff at beginning of level, different from defeat_spawn
def spawn(problem): #Input problem will be smt sorted in dictionary levels
    rand_side = float(random.choice([0,600, 120, 601]))
    strength, difficulty, speed, group, tier, max_spawn = problem[0], problem[1], problem[2], problem[3], problem[4], problem[5]
    #Will choose a position near the walls to spawn a problem
    if  rand_side == 600:
        rand_pos = float(random.randint(120,600))
        x,y = rand_side, rand_pos
    elif rand_side == 0:
        rand_pos = float(random.randint(120,600))
        x,y = rand_side, rand_pos             
    elif rand_side == 120:
        rand_pos = float(random.randint(0,500))
        y,x = rand_side, rand_pos
    else:
        rand_pos = float(random.randint(0,500))
        y,x = rand_side, rand_pos
    #strength, position, difficulty, speed, group, tier
    drop = drop_randomizer(random.randint(1,100),strength, tier)
    problem = Math(problem[0], [x,y], problem[1], problem[2], problem[3], problem[4], problem[5], drop)
    math_problems.append(problem)

#Determines how a condition affects something
#Will add a condition based on these choices:
# 1) If no condition of the type exists
# 2) If it exists but the new one is stronger
# 3) if they are the same strength but new one lasts longer
#Conditions are stored like [condition_strength, duration, inital duration (for hero only)]
#eg. [speed2, 50, 50]
#[speed2, 50, 50] > [speed1, 500, 500] > [speed1, 100, 100]
def add_condition(new, conditions):
    for condition in conditions:
        if new[0][0:-1] == condition[0][0:-1]:
            if new[0][-1] > condition[0][-1]:
                conditions.remove(condition)
                conditions.append(new)
            elif new[0][-1] == condition[0][-1]:
                if new[1] > condition[1]:
                    conditions.remove(condition)
                    conditions.append(new)
                else:
                    return False
            else:
                return False #This is if no new conditions are added
            break #Break if they do find same condition, to avoid else loop below
    else:
        conditions.append(new)

#Discounts a tower based off of how many X-1 fp supports are in range of tower
def discount(cost, tower):
    new_cost = cost
    for support in supports:
        if support.group == "Fleetwood Park" and support.upgrade[1] >= 1 and distance(support.position, tower.position) <= support.vision:
            new_cost *= 0.85
    if new_cost < 0.5*cost:
        return 0.5*cost
    else:
        return new_cost
        
#Upgrade tower function will check which path is selected
#Most upgrades will increase a tower's attributes, which the
#values being called from the upgrade dictionary, but
#a select few upgrades work differently
def upgrade_tower(path):
    global selection
    global iq
    global error_message
    group = selection.group
    if str(type(selection)) == "<class '__main__.Turnip'>":
        #PYRAMID OF THE TURNIP GOD upgrade
        if path == 1 and selection.upgrade[path] == 2 and selection.group == "geometry" and iq >= discount(upgrade['geometry'][6][-1],selection):
            turnips_copy = []
            turnips_copy.extend(turnips)
            selection.sacrifice_count = 0
            #Will sacrifice nearby turnips and take in their power
            #Will increase pierce and speed of god if the turnip sacrificed
            #is worth more than $2500
            for turnip in turnips_copy:
                if distance(turnip.position, selection.position) <= selection.vision and selection != turnip:
                    selection.intel += turnip.intel
                    if turnip.cost >= 2500:
                        selection.wait *= 0.9
                        selection.sacrifice_count += 1
                    
                    x,y = turnip.position[0], turnip.position[1]
                    size = turnip.init_radius
                    
                    #Removes the sacrificed turnips from positions
                    for i in range(x/5-size/5 + 1, x/5+size/5):
                        for j in range((y-120)/5-size/5 + 1, (y-120)/5+size/5 ):
                            if positions[i][j][-1] != 0:
                                positions[i][j][-1] = 0
                    turnips.remove(turnip)
                    
            #Its group changes to polymath        
            selection.group = 'polymath'
            selection.vision *= 1.5
            selection.radius *= 2
            selection.reload_time *= 0.5
            selection.intel *= 2
            cost = discount(upgrade['geometry'][6][-1], selection)
            selection.cost += cost
            iq -= cost
            selection.upgrade[path] += 1  
        
        #Will change a turnip's vision based off of the path you upgraded
        #See upgrade dictionary for values
        if selection.upgrade[path] < 3:
            cost = discount(upgrade[group][3*path + selection.upgrade[path] + 1][-1], selection)
            if iq >= cost: #Checks if you can afford
                selection.vision *= upgrade[group][3*path + selection.upgrade[path] + 1][2]
                selection.intel *= upgrade[group][3*path + selection.upgrade[path] + 1][4]
                selection.reload_time *= upgrade[group][3*path + selection.upgrade[path] + 1][5]
                selection.radius += upgrade[group][3*path + selection.upgrade[path] + 1][6]
                selection.cost += cost
                iq -= cost
                selection.upgrade[path] += 1
            else:
                error_message = ["Not enough IQ points.", 120]
            
            
    #If this is upgraded, must check all turnips to see if it's in range
    #If so, those towers will get a boost based off of what upgrade
    #you bought for Fleetwood Park
    elif selection.group == "Fleetwood Park":
        if path == 0 and selection.upgrade[0] < 2:
            if iq >= upgrade[group][selection.upgrade[0] + 1][-1]:
                selection.upgrade[0] += 1
                for turnip in turnips:
                    if distance(selection.position, turnip.position) <= selection.radius:
                        if selection.upgrade[0] == 1:
                            turnip.intel *= 1.2
                        elif selection.upgrade[0] == 2:
                            turnip.reload_time *= 0.9
                selection.cost += upgrade[group][selection.upgrade[0]][-1]
                iq -= upgrade[group][selection.upgrade[0]][-1]
            else:
                error_message = ["Not enough IQ points.", 120]
        elif path == 1 and selection.upgrade[1] < 2:
            if iq >= upgrade[group][2 + selection.upgrade[1] + 1][-1]:
                selection.upgrade[1] += 1
                for turnip in turnips:
                    if distance(selection.position, turnip.position) <= selection.radius:
                        if selection.upgrade[1] == 2:
                            turnip.vision *= 1.15
                selection.cost += upgrade[group][2 + selection.upgrade[0]][-1]
                iq -= upgrade[group][2 + selection.upgrade[1]][-1]
            else:
                error_message = ["Not enough IQ points.", 120]

    
    #These upgrades will change a farm's production rate
    #max_production is stored as [amount, time to produce, value, duration]
    elif selection.group == "Turnip Farm":
        if path == 0 and selection.upgrade[0] < 2:
            if iq >= upgrade[group][selection.upgrade[0] + 1][-1]:
                selection.upgrade[0] += 1
                if selection.upgrade[0] == 1:
                    selection.max_production[0] += 2
                    selection.max_production[1] *= 3.0/5.0
                elif selection.upgrade[0] == 2:
                    selection.max_production[0] += 7
                    selection.max_production[1] *= 0.4
                selection.cost += upgrade[group][selection.upgrade[0]][-1]
                iq -= upgrade[group][selection.upgrade[0]][-1]
            else:
                error_message = ["Not enough IQ points.", 120]
        elif path == 1 and selection.upgrade[1] < 2:
            if iq >= upgrade[group][2 + selection.upgrade[1] + 1][-1]:
                selection.upgrade[1] += 1
                if selection.upgrade[1] == 1:
                    selection.vision *= 1.25
                elif selection.upgrade[1] == 2:
                    selection.max_production[2] = 100
                    selection.max_production[3] = 1500
                selection.cost += upgrade[group][2 + selection.upgrade[0]][-1]
                iq -= upgrade[group][2 + selection.upgrade[1]][-1]
            else:
                error_message = ["Not enough IQ points.", 120]
                    

#Searches attacks for each type of turnip through upgrade path
#When a turnip attacks, its init_attack is modified based on what
#upgrades it has. init_attack is the unupgraded attack.
#See upgrade dictionary for values of how power, radius, and pierce
#of upgraded projectiles are affected
def increment_attack(turnip):
    group = turnip.group
    power, group, radius, sprite, distance, pierce = \
    turnip.intel, init_attack[group][0], init_attack[group][1], init_attack[group][2],turnip.vision*1.05, init_attack[group][3]
    for i in range(1,turnip.upgrade[0]+1):
        power += upgrade[group][i][0]
        radius += upgrade[group][i][1]
        pierce += upgrade[group][i][3]
    for i in range(4, turnip.upgrade[1]+4):
        power += upgrade[group][i][0]
        radius += upgrade[group][i][1]
        pierce += upgrade[group][i][3]
    return [power, group, radius, sprite, distance, pierce]

#This function determines how a tower will aim
#based off of the direction of the target with
#respect to the turnip
#pencil_position is where projectile leaves the turnip
def attack_motion(turnip, other): 
    direction = direc(turnip.position, other.position)
    position = [turnip.position[0], turnip.position[1]]
    pencil_position = [turnip.position[0] + direction[0]*turnip.radius, turnip.position[1]+direction[1]*turnip.radius]
    velocity = [2.5*direction[0],2.5*direction[1]]
    return [velocity, position, pencil_position, direction] 
 
#The next following set of functions are the attack functions
#for each different turnip
#Again, it will check how much each turnip has been upgraded
#to determine what it will shoot
#Then it will append a projectile or splash to their lists
#For loops are used for turnips that shoot >1 projectiles at once
#NOTE: X-Y means a tower has been upgraded X times on path 1
#Y times on path 2
def normie_attack(turnip, other):
    attack = increment_attack(turnip)
    motion = attack_motion(turnip, other)
    power, group, radius, sprite, distance, pierce = attack[0], attack[1], attack[2], attack[3], attack[4], attack[5]
    
    #Ambidexterity upgrade adds 2 projectiles
    if turnip.upgrade[0] >= 2:
        for i in [-2,2]:
            x,y = motion[2][0] + i*perpendicular(motion[0])[0], motion[2][1] + i*perpendicular(motion[0])[1]
            projectiles.append(Projectile(power, group, radius,sprite,distance,pierce, [x,y], [motion[0][0],motion[0][1]], None, None))
    #Fan club upgrade
    if turnip.upgrade[0] >= 3:
        power += random.randint(1,4)
        radius += 2*random.random()
    else:
        projectiles.append(Projectile(power, group, radius,sprite,distance,pierce,[motion[2][0], motion[2][1]], [motion[0][0],motion[0][1]], None, None))
        
def permuturnip_attack(turnip, other):
    attack = increment_attack(turnip)
    motion = attack_motion(turnip, other)
    power, group, radius, sprite, distance, pierce = attack[0], attack[1], attack[2], attack[3], attack[4], attack[5]
    
    #Pimutation upgrade
    if turnip.upgrade[1] == 2:
        power += random.randint(-5,15)
        radius += random.randint(-1,3)
    #Triangle obsession upgrade shoots 3 projectiles
    if turnip.upgrade[0] >= 3:
        for i in [0,2,4]:
            v1 = rotate(motion[0], math.pi/3, i)
            projectiles.append(Projectile(power, group, radius,sprite,distance,pierce, [motion[2][0], motion[2][1]], [v1[0],v1[1]], None, None))
    else:
        projectiles.append(Projectile(power, group, radius,sprite,distance,pierce, [motion[2][0], motion[2][1]], [motion[0][0],motion[0][1]], None, None))
        
def multitasker_attack(turnip):
    attack = increment_attack(turnip)
    power, group, radius, sprite, distance, pierce = attack[0], attack[1], attack[2], attack[3], attack[4], attack[5]
    
    #0-1 is the faster projectiles upgrade
    if turnip.upgrade[1] < 1:
        velocity = [0.8,0.8]
    else:
        velocity = [1.6, 1.6]
    #Ring theory upgrade
    if turnip.upgrade[1] >= 3:
        splash_attacks.append(Splash(power, group, distance, [turnip.position[0], turnip.position[1]], pierce, None, sun_ring))
    elif turnip.upgrade[0] < 3:
        for i in range(8):
            v1 = rotate(velocity, math.pi/4, i)
            x,y = turnip.position[0] + unit(v1)[0]*turnip.radius, turnip.position[1] + unit(v1)[1]*turnip.radius
            projectiles.append(Projectile(power, group, radius, sprite, distance, pierce, [x,y], [v1[0],v1[1]], None, None))
    #Crystal math upgrade
    else:
        for i in range(12):
            v1 = rotate(velocity, math.pi/6, i)
            x,y = turnip.position[0] + unit(v1)[0]*turnip.radius, turnip.position[1] + unit(v1)[1]*turnip.radius
            projectiles.append(Projectile(power, group, radius, sprite, distance, pierce, [x,y], [v1[0],v1[1]], None, None))
            
def geometry_attack(turnip, other):
    attack = increment_attack(turnip)
    motion = attack_motion(turnip, other)
    power, group, radius, sprite, distance, pierce = attack[0], attack[1], attack[2], attack[3], attack[4], attack[5]
    target = None
    
    #Turnip God upgrade
    if turnip.upgrade[1] >= 3:
        pierce += turnip.sacrifice_count
        for i in range(16):
            velocity = [1.6, 1.6]
            v1 = rotate(velocity, math.pi/8, i)
            x,y = turnip.position[0] + unit(v1)[0]*turnip.radius, turnip.position[1] + unit(v1)[1]*turnip.radius
            projectiles.append(Projectile(power/4, group, radius/2, orb_sprite, distance, pierce/2, [x,y], [v1[0],v1[1]], None, None))
    #Seeking upgrade
    if turnip.upgrade[1] >= 2: 
        target = other
    if turnip.upgrade[0] >= 3 and random.randint(1,4) == 4:
        projectiles.append(Projectile(50+power, 'geometry', 30, ball_sprite,450, 99, [motion[2][0], motion[2][1]], [motion[0][0],motion[0][1]], target, None))
    else:
        projectiles.append(Projectile(power, group, radius,sprite,distance,pierce, [motion[2][0], motion[2][1]], [motion[0][0],motion[0][1]], target, None))
    
def procrastinator_attack(turnip):
    attack = increment_attack(turnip)
    power, group, radius, sprite, distance, pierce = attack[0], attack[1], attack[2], attack[3], attack[4], attack[5]
    
    #Stalin' upgrade gives stall effect
    if turnip.upgrade[1] >= 2 and random.randint(1,5) > 3:
        splash_attacks.append(Splash(turnip.intel, group, distance, [turnip.position[0], turnip.position[1]], pierce, ['stall0',50], water_ring))
    #Greater influence upgrade increases duration of slow
    if turnip.upgrade[1] >= 3:
        effect_time = 10000
    else:
        effect_time = 500
    #0-2 upgrade changes slow 1 effect to slow 2
    if turnip.upgrade[0] >= 2:
        splash_attacks.append(Splash(0, group, distance, [turnip.position[0], turnip.position[1]], pierce, ['slow2',effect_time], water_ring))
    else:
        splash_attacks.append(Splash(0, group, distance, [turnip.position[0], turnip.position[1]], pierce, ['slow1',effect_time], water_ring))
    
def modular_attack(turnip):
    attack = increment_attack(turnip)
    direction = direc(turnip.position, mouse_position)
    pencil_position = [turnip.position[0]+direction[0]*turnip.radius, turnip.position[1]+direction[1]*turnip.radius]
    power, group, radius, sprite, distance, pierce = attack[0], attack[1], attack[2], attack[3], attack[4], attack[5]
    target = None
    v = [2.5*direction[0], 2.5*direction[1]]
    
    #1-X upgrade is meant to decrease spread for increased accuracy
    if turnip.upgrade[0] >= 1:
        v = rotate(v,0.05*(random.random()-1),1)
    else:
        v = rotate(v, 0.5*(random.random()-1),1)
    #X-2 tower seeks for targets occasionally
    if turnip.upgrade[1] >= 2 and len(math_problems) > 0 and random.randint(1,10) > 6:
        target = math_problems[0]
    #90 degree potatoes :)
    if turnip.upgrade[1] >= 3:
        projectiles.append(Projectile(power, group, radius,potato_sprite,distance,pierce, [pencil_position[0], pencil_position[1]], [v[0], v[1]], target, 'mod splash'))
        v1 = rotate(v, -math.pi/12, 1)
        projectiles.append(Projectile(power, group, radius,potato_sprite,distance,pierce, [pencil_position[0], pencil_position[1]], [v1[0], v1[1]], target, 'mod splash'))
        v2 = rotate(v, math.pi/12, 1)
        projectiles.append(Projectile(power, group, radius,potato_sprite,distance,pierce, [pencil_position[0], pencil_position[1]], [v2[0], v2[1]], target, 'mod splash'))
    else:
        projectiles.append(Projectile(power, group, radius,sprite,distance,pierce, [pencil_position[0], pencil_position[1]], [v[0], v[1]], target, None))

#All info about button positions, appearance, and actions
#are stored here
class Button:
    def __init__(self, pos1, pos2, colour, outline_colour, text, text_pos, image, link, display):
        self.pos1 = pos1 #Top left
        self.pos2 = pos2 #Bottom right
        self.colour = colour
        self.outline_colour = outline_colour
        self.text = text
        self.text_pos = text_pos
        self.image = image
        self.link = link
        self.display = display
        self.clicked = False
        
    def draw(self, canvas):
        #Display image for button
        if self.image != None:
            draw_image(canvas, self.image, self.pos1, self.pos2,1, 0)
        elif self not in confirm_buttons and self not in scroll_buttons:
            canvas.draw_polygon(
            [[self.pos1[0], self.pos1[1]], [self.pos1[0], self.pos2[1]], [self.pos2[0], self.pos2[1]], [self.pos2[0], self.pos1[1]]],
            2, self.outline_colour, self.colour)
        
        #If clicked, highlight the button lime
        if self.clicked:
            canvas.draw_polygon(
                [[self.pos1[0], self.pos1[1]], [self.pos1[0], self.pos2[1]], [self.pos2[0], self.pos2[1]], [self.pos2[0], self.pos1[1]]],
                2, "lime") 
        
        #The next set of text are the 
        #labels for different types of buttons
        #Eg, upgrade name if it's an upgrade button
        
        #Displays name of tower under tower selection
        if self in turnip_buttons:
            canvas.draw_text("$" + str(towers[self.link][-1]), [self.pos1[0]+10, 110], 20, "white")
            if self.link == "Genetically Modular Turnip":
                canvas.draw_text("GMT", [self.pos1[0]+20, 90], 10, "white")
            else:
                canvas.draw_text(self.link, [self.pos1[0]-(len(self.link)-15)/2, 90], 10, "white")
        
        elif self in tower_buttons:
            if self.link == "sell":
                canvas.draw_text("Sell for $" + str(int(selection.cost*.85)), [self.pos1[0] + 10, self.pos1[1] + 27], 25, "white")
            #Will check selected tower's upgrade and search
            #through upgrade_names and upgrade_descriptions
            #for the text to display on upgrade button
            #Will display Max Upgrades if fully upgraded
            elif self.link == "upgrade1" or self.link == "upgrade2":
                path = int(self.link[-1]) - 1
                if selection in turnips:
                    if selection.upgrade[path] < 3:
                        canvas.draw_text(upgrade_names[selection.group][path*3+selection.upgrade[path] + 1], [self.pos1[0] + 5, self.pos1[1] + 20], 14.5, "white")
                        for i in range(len(upgrade_descriptions[selection.group][path*3+selection.upgrade[path] + 1])):
                            canvas.draw_text(upgrade_descriptions[selection.group][path*3+selection.upgrade[path] + 1][i], [self.pos1[0] + 5, self.pos1[1] + 36 + 11*i], 12, "white")
                        canvas.draw_text("$" + str(upgrade[selection.group][path*3+selection.upgrade[path] + 1][-1]), [self.pos1[0] + 5, self.pos2[1] - 5], 20, "white")
                    else:
                        canvas.draw_text("Max Upgrades", [self.pos1[0] + 5, self.pos1[1] + 25], 15, "white")
                elif selection in supports:
                    if selection.upgrade[path] < 2:
                        canvas.draw_text(upgrade_names[selection.group][path*2+selection.upgrade[path] + 1], [self.pos1[0] + 5, self.pos1[1] + 20], 14.5, "white")
                        for i in range(len(upgrade_descriptions[selection.group][path*2+selection.upgrade[path] + 1])):
                            canvas.draw_text(upgrade_descriptions[selection.group][path*2+selection.upgrade[path] + 1][i], [self.pos1[0]+5, self.pos1[1] + 36 + 11*i], 12, "white")
                        canvas.draw_text("$" + str(upgrade[selection.group][path*2+selection.upgrade[path] + 1][-1]), [self.pos1[0] + 5, self.pos2[1] - 5], 20, "white")
                    else:
                        canvas.draw_text("Max Upgrades", [self.pos1[0] + 5, self.pos1[1] + 25], 15, "white")
        
        #Display cost of tower boosts, based on algorithm n * duration / 3
        #Where n is cost multiplier
        elif self in hero_buttons: #self.link[0] is the boost type "speed1", self.link[1] is duration
            if self.link[0] == "shield": 
                canvas.draw_text(str(5*self.link[1]/3), [self.pos1[0] + 1, self.pos2[1] + 12], 15, "white")
            else:
                canvas.draw_text(str(int(self.link[0][-1])**2*self.link[1]/3), [self.pos1[0] + 1, self.pos2[1] + 12], 15, "white")
        
        #Displays yes or no to confirm something
        elif self in confirm_buttons:
            canvas.draw_text(self.link, [self.pos1[0] + 4, self.pos2[1] - 4], 20, "black")
        
        #Displays Next or Back
        elif self in scroll_buttons:
            canvas.draw_text(self.link[0].upper() + self.link[1:], [self.pos1[0]+2, self.pos2[1]-5], 22, "black")
                    
    def click(self):
        global selection
        global iq
        global pause
        global playing
        global page_number
        global error_message
        #Check if the clicked position is within the region of the button
        if self.pos1[0] < mouse_position[0] < self.pos2[0] and self.pos1[1] < mouse_position[1] < self.pos2[1]:
            self.clicked = True
            #Will check what the button is, and will perform the action necessary
            #Will return True if clicked
            
            #Upgrade buttons for when a tower is selected
            if self.link == 'upgrade1':
                upgrade_tower(0)
            elif self.link == 'upgrade2':
                upgrade_tower(1)
            elif self.link == 'sell':
                sell()
                for button in tower_buttons:
                    button.display = False
                    button.clicked = False
                selection = None
                
            #Starts game each round
            elif self.link == "play":
                pause = False
             
            #The following two are for buying hero boosts
            #I wasn't able to find a better place to put them
            #And it doesn't take up too many lines anyways
            elif self.link[0][:-1] == "speed":
                if iq >= int(self.link[0][-1])**2 * self.link[1] / 3:
                    if add_condition([self.link[0],self.link[1], self.link[1]], hero.conditions) != False:
                        iq -= int(self.link[0][-1])**2 * self.link[1] / 3
                else:
                    error_message = ["Not enough IQ points.", 120]
            elif self.link[0] == "shield":
                if iq >= 5 * self.link[1] / 3:
                    if add_condition([self.link[0],self.link[1], self.link[1]], hero.conditions) != False:
                        iq -= 5 * self.link[1] / 3
                else:
                    error_message = ["Not enough IQ points.", 120]
            
            #Start game menu buttons
            elif self.link in ["Normie", "Nontrivial", "Deep"]:
                start_game(self.link)
            elif self.link == "Help":
                playing = "Help"
            elif self.link == "About":
                playing = "About"
                
            #Next or back scroll buttons
            elif self.link == "next":
                if page_number < 13:
                    page_number += 1
                else:
                    page_number = 1
                    playing = "Start"
            elif self.link == "back":
                if playing == "Help":
                    if page_number > 1:
                        page_number -= 1
                    else:
                        playing = "Start"
                else:
                    playing = "Start"
                    
            #Leave game button will open
            #confirmation screen
            elif self.link == "quit":
                for button in confirm_buttons:
                    button.display = True
            #Opened up by quit button        
            elif self in confirm_buttons:
                if self.link == "Yes":
                    quit()
                for button in confirm_buttons:
                    button.display = False
                    
            #These buttons are displayed when game over
            #or game win (freeplay is game win only)
            elif self.link == "leave":
                quit()
            elif self.link == "freeplay":
                playing = "In Game"
                
            #These are the tower button that will make
            #selection equal to name of tower. See 
            #add tower function 
            else:
                selection = self.link
            return True
        else:
            return False #To check if button has been clicked
            pass
                                                                                                      
#Class of things dropped by math problems when they are solved
class Drops:
    def __init__(self, position, velocity, radius, collect_radius, sprite, group, value, span):
        self.position = position
        self.velocity = velocity
        self.radius = radius   
        self.collect_radius = collect_radius
        self.sprite = sprite
        self.group = group
        self.value = value
        self.span = span
        
    def update(self):
        #Span is how long the drop will last before disappearing
        self.span -= 1
        
        #Will move towards hero if hero is within its collect radius
        if distance(self.position, hero.position) <= self.collect_radius:
            x,y = direc(self.position, hero.position)[0], direc(self.position, hero.position)[1]
            self.velocity[0] += 0.05*x
            self.velocity[1] += 0.05*y
        else:
            self.velocity[0] *= 0.9
            self.velocity[1] *= 0.9
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        
    def collect(self, collector):
        global iq
        #This is called when the drop is collected
        if self.group == "iq":
            iq += self.value
        elif self.group == "health":
            hero.health += self.value
        elif self.group == "speed1":
            add_condition(["speed1", self.value, self.value], hero.conditions)
        elif self.group == "speed2":
            add_condition(["speed2", self.value, self.value], hero.conditions)
            
    def draw(self, canvas):
        draw_sprite(canvas, self.sprite, self.position, 20, self.radius + 3, 0)
        
#Projectile class is for objects shot out by turnips
class Projectile:
    def __init__(self, power, group, radius, sprite, distance, pierce, position, velocity, target, animation):
        self.power = power
        self.group = group
        self.position = position
        self.velocity = velocity #This will be updated later      
        self.radius = radius
        self.sprite = sprite
        self.distance = distance
        self.pierce = pierce
        self.target = target
        self.hits = []
        self.animation = animation
        
    def update(self):
        #If it has target, move towards target
        #Otherwise, travel in its velocity in a straight line
        if self.target != None and self.target in math_problems:
            v = direc(self.position, self.target.position)
            self.velocity = [2.5*v[0], 2.5*v[1]]
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.distance -= math.sqrt(self.velocity[0]**2 + self.velocity[1]**2) #Distance left to travel
    
    def draw(self, canvas):
        if self.sprite == ball_sprite:
            draw_sprite(canvas, self.sprite, self.position, 60, 1.4*self.radius, spin_timer*0.03)
        else:
            draw_sprite(canvas, self.sprite, self.position, 20, 1.4*self.radius, spin_timer*0.03)

#Splash attacks that form a ring around attacker
class Splash:
    def __init__(self, power, group, max_radius, position, pierce, effect, sprite):
        self.power = power
        self.group = group
        self.position = position
        self.max_radius = max_radius
        self.radius = 1
        self.pierce = pierce
        self.effect = effect
        self.sprite = sprite
        
    def update(self):
        #Increase in size until it reaches its max radius
        if self.radius < self.max_radius:
            self.radius += 2.5
            
    def draw(self, canvas):
        draw_sprite(canvas, self.sprite, self.position, 200, self.radius*1.1, spin_timer*0.03)

#Turnip class
#intel = intelligence
#vision is turnip's range
#The group is the name of the tower as well. I used group so I can sort by attack type
class Turnip:
    def __init__(self, intel, wait, vision, group, position, direction, radius):
        self.intel = intel
        self.wait = wait #This is the reload time
        self.reload_time = wait
        self.vision = vision
        self.group = group
        self.position = position
        self.direction = direction
        self.upgrade = [0, 0]
        self.radius = radius
        self.init_radius = radius #Upgrades that affect size don't take up more space
        self.conditions = [] #[condition,timer, init_time]
        
    def search(self, other):
        #Looks for math problems nearby
        for problem in math_problems:
            if distance(self.position,other.position) <= self.vision + other.radius:
                return True
            
    def attack(self, other):
        #Will call attack function of respective group of tower
        if self.group == "number theory":
            self.direction = direc(self.position, other)
        else:
            self.direction = direc(self.position, other.position)
        if self.group == 'neutral':
            normie_attack(self,other)
        elif self.group == 'combo':
            permuturnip_attack(self, other)
        elif self.group == 'multitasker':
            multitasker_attack(self)
        elif self.group == 'geometry' or self.group == 'polymath':
            geometry_attack(self, other)
        elif self.group == 'procrastinator':
            procrastinator_attack(self)
        elif self.group == 'number theory':
            modular_attack(self)
            
    def draw(self, canvas):
        canvas.draw_circle(self.position, self.radius, 1, 'Blue', 'Blue')
        draw_sprite(canvas, self.sprite, self.position, 100, 1.4*self.radius, math.pi + get_angle(self.direction))
        if self == selection:
            canvas.draw_circle(selection.position, 1.4*selection.radius, 1, "cyan")
            canvas.draw_circle(selection.position, selection.vision, 1, "lime")
                       
#Turnip that you control         
class Hero(Turnip):
    def __init__(self, wait, vision, group, position, direction, speed, health, intel, radius):
        Turnip.__init__(self,intel, wait, vision, group, position, direction, radius)
        self.speed = speed
        self.health = health
        self.intel = intel
        self.conditions = []
        self.direction = [0, 1]
        
    def damage(self,attack):
        #Called when math collides with hero
        #damage_taken can be reduced by shield condition
        #if W and S keys are held at same time
        damage_taken = attack
        for condition in self.conditions:
            if condition[0] == "shield":
                damage_taken *= 0.4
                break
        if up and down:
            damage_taken *= 0.75
        self.health -= damage_taken
        
    def update(self):
        global error_message
        
        #Adjusts speed of hero based on its conditions
        speed = self.speed
        for condition in self.conditions:
            if condition[1] <= 0:
                self.conditions.remove(condition)
            if condition[0][0:-1] == 'speed':
                speed*=conditions[condition[0]]
            condition[1] -= 1
            
        #A key (left) turns counter-clockwise
        #D key (right) turns clockwise
        if left:
            self.direction = rotate(self.direction, -0.07, 1)
        if right:
            self.direction = rotate(self.direction, 0.07, 1)
        
        #Up is to move forwards
        #Down is backwards
        #Checks too see if turnip is moving off screen, display 
        #error message if so
        if up:
            if (self.position[0] <= 0 and self.direction[0] < 0) or (self.position[0] >= 600 and self.direction[0] > 0):
                error_message = ["Can't move off the screen.", 120]
            else:
                self.position[0] += 1.1*self.direction[0] * speed
            if (self.position[1] <= 120 and self.direction[1] < 0) or (self.position[1] >= 600 and self.direction[1] > 0):
                error_message = ["Can't move off the screen.", 120]
            else:
                self.position[1] += 1.1*self.direction[1] * speed
        if down:
            if (self.position[0] <= 0 and self.direction[0] > 0) or (self.position[0] >= 600 and self.direction[0] < 0):
                error_message = ["Can't move off the screen.", 120]
            else:
                self.position[0] -= 0.8*self.direction[0] * speed
            if (self.position[1] <= 120 and self.direction[1] > 0) or (self.position[1] >= 600 and self.direction[1] < 0):
                error_message = ["Can't move off the screen.", 120]
            else:
                self.position[1] -= 0.8*self.direction[1] * speed

    def attack(self):
        #Press spacebar to shoot
        pencil_position = [self.position[0]+1.2*self.radius*self.direction[0],self.position[1]+1.2*self.radius*self.direction[1]]
        projectile_velocity = [5*self.direction[0],5*self.direction[1]]
        projectiles.append(Projectile(self.intel*math.sqrt(level), 'neutral', 4, orb_sprite, 200, 1, [pencil_position[0],pencil_position[1]],projectile_velocity, None, None))
    
    def draw(self, canvas):
        draw_sprite(canvas, hero_turnip, self.position, 100, 1.4*self.radius, math.pi+get_angle(self.direction))
        if up and down and pause == False: #This activates shield
            draw_sprite(canvas, energy_ring, self.position, 400, 45, spin_timer*0.01)
            
#Support towers are fp and turnip farm                
class Support:
    def __init__(self, vision, position, radius, group, sprite):
        self.vision = vision
        self.position = position
        self.radius = radius
        self.init_radius = radius
        self.group = group
        self.upgrade = [0,0]
        self.sprite = sprite
        
    def draw(self, canvas):
        if self == selection:
            canvas.draw_circle(selection.position, selection.radius, 1, "cyan")
            canvas.draw_circle(selection.position, selection.vision, 1, "lime")
        draw_sprite(canvas, self.sprite, self.position, 50, self.radius, 0)
        
    def produce(self): #For turnip farm only
        if self.production[0] >= 1:
            if self.production[1] <= 0:
                #Spit out money in a random direction when produce timer hits 0
                angle = rotate([0,1],random.random()*2*math.pi,1)
                item_drops.append(Drops([self.position[0]+angle[0]*self.radius, self.position[1]+angle[1]*self.radius],\
                                        [angle[0]*10, angle[1]*10],\
                                        3, 40, money_drop, "iq", self.production[2], self.production[3]))
                if self.production[0] >= 1:
                    #Lowers the number left to be produced by 1 when one gets produced
                    x = self.production[0]
                    self.production = [x-1, self.max_production[1], self.production[2], self.production[3]]
            else:
                #If nothing is produced, decrease production timer by 1
                self.production[1] -= 1
#Math class
#he "enemies" that come at you during the game
class Math:
    def __init__(self, strength, position, difficulty, speed, group, tier, max_spawn, drop):
        self.strength = strength #Strength is how many lives you lose if the math problems come to you
        self.position = position
        self.health = difficulty
        self.difficulty = difficulty #Difficulty doesn't go down while health does
        self.speed = speed
        self.init_speed = speed
        self.group = group
        self.tier = tier
        self.radius = 10*math.sqrt(self.tier)
        self.immunity = []
        self.conditions = []
        self.max_spawn = max_spawn
        self.drop = drop
        self.velocity = rotate([0.6*speed,0.8*speed], random.random()*2*math.pi, 1)
        self.colour = random.choice(["red","orange","yellow","green","blue","purple","pink"])
        self.vision = random.randint(50, 200)
        
    def update(self):
        #In trivial mode, the speed is constant unless affected by slow
        #In nontrivial and deep, the speed increases according to a logistic curve
        if game_difficulty == "Nontrivial":
            self.speed += 0.001*self.speed*(1-self.speed/(3*self.init_speed)) #ds/dt = 0.001*s*(1-s/(3*s_0))
        elif game_difficulty == "Deep":
            self.speed += 0.0008*self.speed*(1-self.speed/(5*self.init_speed)) #ds/dt = 0.0008*s*(1-s/(3*s_0))
            
        speed = self.speed
        moving = True
        
        #Searches through list of conditions to see if it is affected by slow
        for condition in self.conditions:
            if condition[1] <= 0:
                self.conditions.remove(condition)
            if condition[0][0:-1] == 'stall':
                moving = False
            elif condition[0][0:-1] == 'slow' or condition[0][0:-1] == 'speed':
                speed = self.speed*conditions[condition[0]]
                if self.group == strengths['procrastinator']:
                    speed //= 1.25
                elif self.group in weaknesses['procrastinator']:
                    speed = (self.speed + speed)/2.2
            condition[1] -= 1 
        
        if moving:
            #Slow math problems and ones close to the hero will chase hero
            if distance(self.position, hero.position) < self.vision or self.init_speed < 1:
                x = (hero.position[0]-self.position[0])
                y = (hero.position[1]-self.position[1])
                d = distance(self.position,hero.position)
                self.velocity = [x*speed/d, y*speed/d]
            #Others will move in straight line until it hits a wall, then bounce off
            else:
                if self.position[0] <= 0:
                    self.velocity[0] = math.fabs(self.velocity[0])
                elif self.position[0] >= 600:
                    self.velocity[0] = -math.fabs(self.velocity[0])
                if self.position[1] <= 120:
                    self.velocity[1] = math.fabs(self.velocity[1])
                elif self.position[1] >= 600:
                    self.velocity[1] = -math.fabs(self.velocity[1])
            self.position[0] += self.velocity[0]
            self.position[1] += self.velocity[1]
            
    def damage(self, other): #Other is projctile
        if other not in self.immunity:
            #Deals damage according to respective strength and weakness groups
            if  self.group in strengths.get(other.group):
                self.health -= 2.0*other.power
            elif self.group in weaknesses.get(other.group):
                self.health -= 0.3 * other.power
            else:
                self.health -= 0.8*other.power
    
    def draw(self, canvas):
       
        canvas.draw_circle((self.position[0], self.position[1]), self.radius, 1, self.colour, self.colour)
        draw_sprite(canvas, random.choice(math_sprites[self.group]), self.position, 50, self.radius/2, get_angle(self.velocity))
        
        #Prints own health bar by ratio of current health to initial health
        bar = self.health/self.difficulty
        x, y = self.position[0], self.position[1] 
        r = self.radius
        if bar > 0:
            canvas.draw_line([x - 0.9*r, y-1.3*r],[x - 0.9*r + 1.8*r*bar, y-1.3*r],2,self.colour)
        #Projectile will be [x,y,power,group]
        
#Stores the initial stuff for all turnips 
#intel, wait, vision, group, direction, size, sprite, COST
towers = {"Normie Turnip":[5, 200, 70, 'neutral',[0,1], 10, normie_sprite, 100],
          "Permuturnip":[15, 250, 100, 'combo',[0,-1], 15, permuturnip_sprite, 150],
         "Illuminati Turnip":[50, 600, 150, 'geometry', [1,0], 25, illuminati_sprite, 500],
         "Multitasker": [5, 150, 50, 'multitasker', [-1,0],15, multitasker_sprite, 300],
         "Procrastinator": [6, 500, 60, 'procrastinator',[-0.8,0.6], 15, procrastinator_sprite, 100],
         "Genetically Modular Turnip":[8,100,250,'number theory', [0.6, -0.8], 20, modular_sprite, 450],
         "Fleetwood Park": [0,0,200, 'fleetwood', 0, 30, 400],
         "Turnip Farm": [0,0,120, 'farm', 9, 25, 600]}

#When a tower is being placed, this function will check
#if you have space and money, then place tower, subtract
#tower cost from your iq, and store tower information in
#positions grid
def add_tower(position):
    #Note when making new tower: update towers and init attack
    global selection
    global iq
    global error_message
    #Selected tower is the TOWER INFORMATION from the dictionary
    #above, it is NOT the object of the tower's class
    selected_tower = towers[selection]
    x, y = position[0], position[1]
    size = selected_tower[5]
    cost = selected_tower[-1]
    placed = False
    #If enough space and money
    if has_space([x,y], size) and iq >= cost:
        if selection == "Fleetwood Park":
            #Counts how many fp towers there are
            #Maxed at 5 to prevent extreme stacking
            count = 0
            for support in supports:
                if support.group == "Fleetwood Park":
                    count += 1
            if count < 5:
                tower = Support(selected_tower[2], [x,y], selected_tower[5], "Fleetwood Park", fp_sprite)
                tower.cost = cost
                iq -= cost
                supports.append(tower)
                #Gives the 25% intel boost to turnips
                for turnip in turnips:
                    if distance(turnip.position, tower.position) < tower.vision:
                        turnip.intel *= 1.25            
                selection = None  
                placed = True
            else:
                #Message shows up at bottom of screen
                error_message = ["Can only have 5 Fleetwood Park towers.", 120]

            
        elif selection == "Turnip Farm":
            #Production list contains number of turnips, time to produce, value, how long they last
            tower = Support(selected_tower[2], [x,y], selected_tower[5], "Turnip Farm", farm_sprite)
            tower.max_production = [3, 400, 30, 750]
            tower.production = [3, 400, 30, 750]
               
            tower.cost = cost
            iq -= cost
            supports.append(tower)
            selection = None
            placed = True
            
        else:
            tower = Turnip(selected_tower[0],selected_tower[1],selected_tower[2],\
                           selected_tower[3],[x,y],selected_tower[4],selected_tower[5])
            tower.sprite = selected_tower[6] #I forgot to put this as an init, oops
            for support in supports:
                #Checks if there are any fp towers that can give boosts to tower
                if distance(support.position, tower.position) <= support.vision:
                    tower.intel *= 1.25
                    if support.upgrade[0] >= 1:
                        tower.intel *= 1.2
                    if support.upgrade[0] >= 2:
                        tower.reload_time *= 0.9
                    if support.upgrade[1] >= 2:
                        tower.vision *= 1.15
            #Subtracts cost as appropriate
            cost = discount(cost, tower)
            tower.cost = cost
            iq -= cost
            turnips.append(tower)
            selection = None
            placed = True
        
        #These spaces will be taken up in "positions"    
        if placed:
            for i in range(x/5-size/5 + 1, x/5+size/5):
                for j in range((y-120)/5-size/5 + 1, (y-120)/5+size/5 ):
                    if positions[i][j][-1] != 1:
                        positions[i][j][-1] = tower
    #Displays appropriate error message if tower can't be bought for whatever reason
    elif iq < cost:
        error_message = ["Not enough IQ points.", 120]
    elif has_space([x,y], size) == False:
        error_message = ["Not enough space.", 120]

#Does the reverse of the previous function
#Returns 85% the cost of the tower and clears
#up space in positions
def sell():
    global iq, selection
    iq += selection.cost*0.85
    x,y = selection.position[0], selection.position[1]
    size = selection.init_radius
    #Clears up the space that the tower originally took up
    for i in range(x/5 - size/5 + 1, x/5 + size/5):
        for j in range((y-120)/5 - size/5 + 1, (y-120)/5 + size/5 ):
            if positions[i][j][-1] != 0:
                positions[i][j][-1] = 0
    #Removes turnip 
    if selection in turnips:
        turnips.remove(selection)
    #If selling support, remove all the boosts provided by the support originally
    elif selection in supports:
        supports.remove(selection)
        if selection.group == "Fleetwood Park":
            for turnip in turnips:
                if distance(turnip.position, selection.position) <= selection.vision:
                    turnip.intel //= 1.25
                    if selection.upgrade[0] >= 1:
                        turnip.intel //= 1.2
                    if selection.upgrade[0] >= 2:
                        turnip.wait *= 1.1
                    if selection.upgrade[1] >= 2:
                        turnip.vision //= 1.15
    selection = None

# Handler for key up and key down
# Pretty self explanatory (too lazy to comment)
# left and right were originally move buttons
# but got changed to turn buttons
# left is counter-clockwise, right is clockwise
def key_down(key):
    global up, down, left, right
    global space
    if key == simplegui.KEY_MAP['w']:
        up = True
    elif key == simplegui.KEY_MAP['s']:
        down = True
    elif key == simplegui.KEY_MAP['a']:
        left = True
    elif key == simplegui.KEY_MAP['d']:
        right = True
    elif key == simplegui.KEY_MAP['space']:
        space = True
        
def key_up(key):
    global up, down, left, right
    global space
    if key == simplegui.KEY_MAP['w']:
        up = False
    elif key == simplegui.KEY_MAP['s']:
        down = False
    elif key == simplegui.KEY_MAP['a']:
        left = False
    elif key == simplegui.KEY_MAP['d']:
        right = False
    elif key == simplegui.KEY_MAP['space']:
        space = False
        
#Handler for mouse click
def mouse_handler(position):
    global selection
    global mouse_position
    mouse_position = position
    
    #Starts out by unclicking all buttons 
    for button in scroll_buttons:
        button.clicked = False
    for button in start_buttons:
        button.clicked = False
    for button in hero_buttons:
        button.clicked = False
    for button in tower_buttons:
        button.clicked = False
    for button in turnip_buttons: 
        button.clicked = False
    for button in confirm_buttons:
        if button.display == True:
            if button.click() == True:
                button.clicked = False
                
    #Each button and what they do are explained in the start function
    #but basically, the playing variable tells you where you are in the
    #game, ie menu screen or in game, to determine which buttons can be clicked
    #The button will check if it was actually clicked within the click method
    if playing == "Start":
        for button in start_buttons:
            button.click()
    elif playing == "Help":
        for button in scroll_buttons:
            button.click()
    elif playing == "About":
        scroll_buttons[1].click()
    elif playing == "Win":
        freeplay_button.click()
        leave_button.click()
    elif playing == "Game Over":
        leave_button.click()
    else:
        if pause:
            if play_button.click(): #button.clicked == True will highlight a button
                play_button.clicked = False #These buttons are one-time and should not be highlighted
                for button in confirm_buttons:
                    button.display = False
            if quit_button.click():
                quit_button.clicked = False
                
        #Checks click position if in game screen (not menu)
        x = 10*(position[0]/10)+5
        y = 10*(position[1]/10)+5    
        
        #If clicked on a tower
        if (position[0]<=600 and position[1] >= 120) and positions[x/5][(y-120)/5][-1] != 0: #if clicked on tower (to upgrade)
            selection = positions[x/5][(y-120)/5][-1]
            for button in tower_buttons:
                button.display = True
                #Display upgrade buttons
            for button in hero_buttons:
                button.display = False
                #Hero buttons are also boost buttons, that take up the same space
        
        #If buying a tower
        elif position[0] <= 600 and position[1] >= 120 \
        and selection in ["Normie Turnip", "Permuturnip", "Illuminati Turnip", "Multitasker", "Procrastinator", "Genetically Modular Turnip", "Fleetwood Park", "Turnip Farm"]:
            add_tower([10*(position[0]/10)+5,10*(position[1]/10)+5])
            #selection = None 
            #This is already in add tower function but might be needed later
        
        #If buying an upgrade, selection will be an object in turnip or support class
        elif str(type(selection)) == "<class '__main__.Turnip'>" or str(type(selection)) == "<class '__main__.Support'>":
            for button in tower_buttons:
                if button.click() and button.link != "sell":
                    button.clicked = True
                    break
            else:
                #If clicked elsewhere, or clicked sell button, get rid of upgrade buttons
                for button in tower_buttons:
                    button.display = False
                for button in hero_buttons:
                    button.display = True #Either tower or hero buttons will display
                selection = None #Button disappears after click
        else:
            #Tower selection and boost buttons
            for button in turnip_buttons:
                if button.click():
                    button.clicked = True
            for button in hero_buttons:
                if button.click():
                    button.clicked = True

#Handler for init canvas
def start():
    global start_buttons, turnip_buttons, tower_buttons, play_button, quit_button, confirm_buttons, leave_button, freeplay_button
    
    #Buttons for start selection menu
    start_buttons.append(Button([300, 160], [500, 240], 'blue','blue',None, None, normie_start_button, 'Normie', False))
    start_buttons.append(Button([300, 260], [500, 340], 'blue','blue',None, None, nontrivial_start_button, 'Nontrivial', False))
    start_buttons.append(Button([300, 360], [500, 440], 'blue', 'blue', None, None, deep_start_button, 'Deep', False))
    start_buttons.append(Button([300, 460], [390, 520], 'blue', 'blue', None, None, about_button, 'About', False))
    start_buttons.append(Button([410, 460], [500, 520], 'blue', 'blue', None, None, help_button, 'Help', False))
    
    #Buttons for help and about, that navigate the page number
    scroll_buttons.append(Button([715, 510], [765, 540], 'blue','blue', None, None, None, 'next', False))
    scroll_buttons.append(Button([35, 510], [85, 540], 'blue','blue', None, None, None, 'back', False))
    
    #Buttons for turnip selection
    towers = ["Normie Turnip", "Permuturnip", "Illuminati Turnip", "Multitasker", "Procrastinator", "Genetically Modular Turnip", "Fleetwood Park", "Turnip Farm"]
    images = [normie_image_frame, permuturnip_image_frame, illuminati_image_frame, multitasker_image_frame, procrastinator_image_frame, modular_image_frame, fp_image_frame, farm_image_frame]
    for i in range(8): #8 tower buttons
        k = 75*i
        turnip_buttons.append(Button([10+k, 10], [70+k, 70], 'blue', 'blue', None, None, images[i], towers[i], True))
    
    #2 upgrade buttons and a sell button for towers
    tower_buttons.append(Button([620, 140], [780, 260], 'brown','tan',None, None, None, 'upgrade1', False))
    tower_buttons.append(Button([620, 280], [780, 400], 'brown','tan',None, None, None, 'upgrade2', False))
    tower_buttons.append(Button([620, 420], [780, 460], 'brown','tan', None, None, None, 'sell', False))
    
    #Button for starting round
    play_button = Button([620, 520], [780, 580], 'blue', 'blue', None, None, start_image, 'play', False)
    quit_button = Button([550, 550], [580, 580], 'blue', 'blue', None, None, home_image, 'quit', False)
    
    #Confirmation to quit
    confirm_buttons.append(Button([250, 320],[290,345], 'blue', 'blue', None, None, None, 'Yes', False))
    confirm_buttons.append(Button([310, 320],[350,345], 'blue', 'blue', None, None, None, 'No', False))
    
    #Leave and freeplay buttons
    freeplay_button = Button([200, 250], [400, 350], 'tan', 'brown', None, None, freeplay_image, 'freeplay', False)
    leave_button = Button([200, 370], [400, 470], 'tan', 'brown', None, None, leave_image, 'leave', False)
    
    #Button for hero boosts
    hero_boosts = ["speed1", "speed2", "speed3", "shield"]
    frame_images = [speed1_image_frame, speed2_image_frame, speed3_image_frame, shield_image_frame]
    for i in range(8):
        boost = hero_boosts[i/2]
        duration = 300+750*(i%2)
        hero_buttons.append(Button([620+90*(i%2), 140+90*int(i/2)], [690+90*(i%2), 200+90*(i/2)], 'blue', 'blue', None, None, frame_images[i/2], [boost, duration], True))
        
# For initializing new game conditions, clears all in-game lists
# And sets starting game conditions based on difficulty
# Generates levels
def start_game(difficulty):
    global turnips, supports, projectiles, math_problems, item_drops, splash_attacks
    global playing
    global level, levels
    global hero
    global game_difficulty
    global iq
    global comment
    global positions
    global level_up
    global pause
    
    level_up = True
    pause = True
    #Places where towers can be placed
    #Creates a position map where towers fit on a 5 by 5 grid
    positions = []
    for x in range(125): #120 but extra space for towers that go slightly off map
        positions.append([])
        for y in range(102): #96 but extra for towers that go slightly off map
            positions[x].append([5*x, 120+5*y,0])
    
    #Clears local in game lists
    turnips, supports, projectiles, math_problems, item_drops, splash_attacks = [], [], [], [], [], []
    game_difficulty = difficulty
    
    #Initializes game conditions and generates levels
    iq = {"Normie":2500, "Nontrivial":2000, "Deep":1500}[difficulty]
    health = {"Normie":500, "Nontrivial":250, "Deep":100}[difficulty]
    levels = {}
    generate_level(1,30) 
    level = 0
    hero = Hero(10,1500,'neutral',[300.0,360.0,0],0, 1, health, 5, 25)
    playing = "In Game"

#Handler for quitting game
#Although not 100% necessary, I kept it so it would
#be easier to change the quit game action later
def quit():
    global playing
    playing = "Start"
     
# Handler to draw on canvas
def draw(canvas):
    global playing, pause
    global levels, level
    global math_problems
    global wait_time, hero
    global problems_spawned, level_timer #level_timer starts next wave automatically
    global selection
    global level_up
    global iq
    global comment
    global page_number
    global spin_timer
    
    if playing == "Start": #Start is game selection menu
        canvas.draw_image(menu_image, (400, 300), (800, 600), (400, 300), (800, 600))
        for button in start_buttons:
            button.draw(canvas)
            
    elif playing == "Help": #When help button is clicked
        canvas.draw_image(menu_chalkboard_image, (400, 300), (800, 600), (400, 300), (800, 600))
        
        if page_number == 12: #This was only needed once so I didn't bother store it elsewhere
            for i in range(8):
                canvas.draw_circle([280 + 350*(i/4), 190 + 96*(i%4)], 30, 2, "cyan", "cyan")
                
        for button in scroll_buttons: #Back and next page buttons
            button.draw(canvas)
            
        for text in help_text[page_number]: #See help text dictionary
            canvas.draw_text(text[2], [45+50*text[1], 50+24*text[0]], 24, "Black")
            
        for image in help_image[page_number]: #canvas, sprite, center, image_size, size, direction
            if image[0] == 0:
                draw_image(canvas, image[1], image[2], image[3], image[4],0)
            else:
                draw_sprite(canvas, image[1], image[2], image[3], image[4]/2, 0)
                
    elif playing == "About": #When about button is clicked
        canvas.draw_image(menu_chalkboard_image, (400, 300), (800, 600), (400, 300), (800, 600))
        scroll_buttons[1].draw(canvas)
        for text in about_text: #See about_text list
            canvas.draw_text(text[2], [45+50*text[1], 50+24*text[0]], 24, "Black")
     
    #Only difference between Game Over and Win is that
    #there is no freeplay option for Game Over
    elif playing == "Game Over": #Game over screen
        canvas.draw_image(field_image, (300, 240), (600, 480), (300, 360), (600, 480))
        canvas.draw_image(wood_texture_image, (400, 60), (800, 120), (400, 60), (800, 120))
        for i in range(4):
            canvas.draw_image(wood_texture_image, (700-200*i, 60), (200, 120), (700, 180+120*i), (200, 120))
        leave_button.draw(canvas)
        draw_image(canvas, lose_image, [150, 150], [450, 220], 1, 0)
        
    elif playing == "Win": #Win screen
        canvas.draw_image(field_image, (300, 240), (600, 480), (300, 360), (600, 480))
        canvas.draw_image(wood_texture_image, (400, 60), (800, 120), (400, 60), (800, 120))
        for i in range(4):
            canvas.draw_image(wood_texture_image, (700-200*i, 60), (200, 120), (700, 180+120*i), (200, 120))
        freeplay_button.draw(canvas)
        leave_button.draw(canvas)
        draw_image(canvas, win_image, [150, 150], [450, 220], 1, 0)
            
    elif playing == "In Game":
        canvas.draw_image(field_image, (300, 240), (600, 480), (300, 360), (600, 480))
        
        #If game is not paused (if in middle of a round)
        if pause == False:
            #Timer for spin of projectiles
            if spin_timer < 2094: 
                spin_timer += 1
            else:
                spin_timer = 0
            
            #level_up is True whenever the start round button is clicked
            if level_up:
                level += 1
                
                if level > 30: #After level 30 is freeplay, must generate levels as needed
                    generate_level(level, level)

                #The spawn counter
                #I may not have a need for this anymore but I kept
                #it just in case it was actually used somewhere
                problems_spawned = 0
                level_up = False
                
                #Reloads production of turnip farms
                for support in supports:
                    if support.group == "Turnip Farm":
                        p = support.max_production
                        support.production = [p[0], p[1], p[2], p[3]]
            
            #Spawns problems as necessary
            if len(levels[level]) > 0: #If list of problems to be spawned is not empty
                levels[level][0][-1] -= 1 #levels[level][0] is first problem of the list                    
                if levels[level][0][-1] <= 0:  #levels[level][0][-1] is the spawn_timer
                    spawn(levels[level][0])
                    levels[level].remove(levels[level][0])
                    problems_spawned += 1
            
            #Level 30 is last boss level
            if len(levels[level]) == 0 and len(math_problems) == 0:
                if level == 30:
                    playing = "Win"
                    
                #Level bonus and comment
                iq += 100 + level
                "Level " + str(level) + " passed. " + str(100+level) + " IQ awarded." #add level quote
                level_up = True
                pause = True         
                    
            #Each turnip searches for a math problem and will attack if it is nearby
            for turnip in turnips:
                #Number theory attacks based on mouse position, whether or not 
                #Math problem is nearby
                if turnip.group == "number theory" and turnip.wait <= 0:
                    turnip.attack(mouse_position)
                    turnip.wait = turnip.reload_time
                else:
                    turnip.wait -= 3 #Should be -1 but I got used to its firing speed
                counter = 0       
                for problem in math_problems:
                    #Time dilation effect for procrastinator turnip
                    if turnip.group == 'procrastinator' and turnip.upgrade[0] >= 3 and distance(turnip.position, problem.position) <= 75 and counter <= 15:
                        counter += 1
                        add_condition(['slow3', 1], problem.conditions) 
                    #All other turnips will attack if they see math problem
                    #as usual
                    if turnip.wait <= 0 and turnip.search(problem) and turnip.group != "number theory":
                        turnip.attack(problem)
                        turnip.wait = turnip.reload_time
                        break
                else:
                    turnip.wait -= 1 #Attack timer

            #Checks if hero is alive, if not go to game over screen
            if hero.health > 0:    
                hero.update()
                #Hero attack timer
                if space and wait_time < 0:
                    hero.attack()
                    wait_time = hero.wait
                else:
                    wait_time -= 1
            else:
                playing = "Game Over"


            #Iterates through problems to check its proximity to a projectile, splash, or the hero
            for problem in math_problems:
                #Checks if is in close proximity of projectile. If so, take damage.
                for projectile in projectiles:
                    if projectile.pierce <= 0: #If projectile is out of pierce, remove it
                        if projectile.animation == "mod splash": #Mod splash is the explosion effect
                            splash_attacks.append(Splash(projectile.power, projectile.group,30,\
                                                  [projectile.position[0], projectile.position[1]],
                                                  5, None, fire_ring))
                        projectiles.remove(projectile)
                    #If pierce is not 0, see if projectile is touching a problem
                    #If it is and it hasn't dealt damage to that problem before
                    #then damage it
                    elif distance(problem.position, projectile.position) < problem.radius + projectile.radius + 1 and projectile not in problem.immunity:
                        problem.damage(projectile)
                        projectile.pierce -= 1
                        problem.immunity.append(projectile)
                        projectile.hits.append(problem)
                        #This is for the projectiles that target math problems
                        #searching through list for new target
                        if len(math_problems) > len(projectile.hits) and projectile.target != None:
                            for i in range(10):
                                next_target = random.choice(math_problems)
                                if next_target not in projectile.hits:
                                    projectile.target = next_target
                        else:
                            projectile.target = None
                
                #Same as before but with splash attacks
                for splash in splash_attacks:
                    if splash.pierce <= 0:
                        splash_attacks.remove(splash)
                    elif distance(problem.position, splash.position) <= splash.radius + problem.radius + 1 and splash not in problem.immunity:
                        if splash.effect != None:
                            add_condition(splash.effect, problem.conditions)
                        problem.damage(splash)
                        splash.pierce -= 1
                        problem.immunity.append(splash)

                #Checks if is in close proximity to hero
                #If so, deal damage to hero equal to its strength
                if distance(problem.position, hero.position) < hero.radius + problem.radius - 2:
                    hero.damage(problem.strength)
                    math_problems.remove(problem)
            
            #Moves projectiles and sees if it has travelled its maximum distance
            for projectile in projectiles: 
                projectile.update()
                
                if projectile.distance <= 0:
                    projectiles.remove(projectile)  
                    
            #Same as before but with splash       
            for splash in splash_attacks:
                splash.update()
                if splash.radius >= splash.max_radius:
                    splash_attacks.remove(splash)   
                    
            #Turnip farm produce money (iq) method
            for support in supports:
                if support.group == "Turnip Farm":
                    support.produce()
                    
            #Updates problem and checks if alive, prints health bar
            for problem in math_problems:
                if problem.health <= 0:
                    if problem.tier > 1: #Problems greater than tier 1 will split
                        defeat_spawn(problem)
                    math_problems.remove(problem)
                    drop = problem.drop
                    drop.position = [problem.position[0], problem.position[1]]
                    item_drops.append(drop)
                else:
                    problem.update()
                    
            remove_list = []
            #Sees if drop is collected, if it is being collected, or if it has expired
            for drop in item_drops:
                drop.update()    
                #Hero can collect drops
                if distance(drop.position, hero.position) < drop.radius + hero.radius:
                    drop.collect(hero)
                    remove_list.append(drop)
                #Remove drop if it has been around too long
                elif drop.span <= 0:
                    remove_list.append(drop)
                #Turnip farms can collect drops if upgraded
                #0-1 turnip farm collects IQ
                #0-2 turnip farm collects IQ and health
                for support in supports:
                    if support.group == "Turnip Farm" and distance(drop.position, support.position) <= support.vision:
                        if support.upgrade[1] >= 2:
                            drop.velocity[0] += 0.4*direc(drop.position, support.position)[0]
                            drop.velocity[1] += 0.4*direc(drop.position, support.position)[1]
                            if distance(drop.position, support.position) <= 6:
                                drop.collect(support)
                                remove_list.append(drop)
                        elif support.upgrade[1] >= 1 and drop.group == "iq":
                            drop.velocity[0] += 0.4*direc(drop.position, support.position)[0]
                            drop.velocity[1] += 0.4*direc(drop.position, support.position)[1]
                            if distance(drop.position, support.position) <= 6:
                                drop.collect(support)
                                remove_list.append(drop)
                            break
                            
            for item in remove_list:
                for drop in item_drops:
                    if item == drop and item in item_drops:
                        item_drops.remove(item)
        
        #Draws everything after all the actions have been performed with them
        #The order at which they are drawn depends on the layering
        for turnip in turnips:
            turnip.draw(canvas)
        for support in supports:
            support.draw(canvas)
        for problem in math_problems:
            problem.draw(canvas)
        for projectile in projectiles:
            projectile.draw(canvas)
        for splash in splash_attacks:
            splash.draw(canvas)
        hero.draw(canvas)  
        for drop in item_drops:
            drop.draw(canvas)
        
        #Prints bar for how long hero's boosts will last
        for condition in hero.conditions:
            if condition[0] == "speed1":
                draw_sprite(canvas, speed1_icon, [50, 140], 20, 15, 0)
                canvas.draw_line([65, 140], [65+float(condition[1])/condition[2]*80,140], 5, 'green')
            elif condition[0] == "speed2":
                draw_sprite(canvas, speed2_icon, [175, 140], 20, 14, 0)
                canvas.draw_line([195, 140], [195+float(condition[1])/condition[2]*80,140], 5, 'green')
            elif condition[0] == "speed3":
                draw_sprite(canvas, speed3_icon, [300, 140], 20, 15, 0)
                canvas.draw_line([315, 140], [315+float(condition[1])/condition[2]*80,140], 5, 'green')
            elif condition[0] == "shield":
                draw_sprite(canvas, shield_icon, [425, 140], 20, 13, 0)
                canvas.draw_line([445, 140], [445+float(condition[1])/condition[2]*80,140], 5, 'green')
        
        canvas.draw_image(wood_texture_image, (400, 60), (800, 120), (400, 60), (800, 120))
        for i in range(4):
            canvas.draw_image(wood_texture_image, (700-200*i, 60), (200, 120), (700, 180+120*i), (200, 120))    
        
        #Displays difficulty, level, health, IQ
        draw_image(canvas, board_image, [600, 0], [800, 120], 0.91, 0)
        canvas.draw_text("Difficulty: " + game_difficulty, [623, 32], 20, "black", 'sans-serif')
        canvas.draw_text("Wave: " + str(int(level)), [623,53], 20, "black", 'sans-serif')
        canvas.draw_text("Health: " + str(int(hero.health)), [623,74], 20, "black", 'sans-serif')
        canvas.draw_text("IQ: $" + str(int(iq)), [623,95], 20, "black", 'sans-serif')
        
        #Displays appropriate tower buttons
        for button in turnip_buttons:
            button.draw(canvas)
        for button in tower_buttons:
            if button.display == True:
                button.draw(canvas)
        for button in hero_buttons:
            if button.display == True:
                button.draw(canvas)
        
        #Displays error message if its time span is greater than 0
        if error_message[1] > 0:
            canvas.draw_text(error_message[0], [40, 500], 18, 'White')
            error_message[1] -= 1
            
        #Displays the buttons that are only there when game is paused
        #such as level comment (see comment dictionary)
        #and start and quit buttons
        #Confirm buttons display if quit button is clicked
        if pause:
            if level > 0:
                canvas.draw_text("Level " + str(level) + " passed. " + str(100+level) + " IQ awarded.", [40, 520], 18, 'White')
            if comment.has_key(level):
                for i in range(len(comment[level])):
                    canvas.draw_text(comment[level][i], [40, 540+20*i], 18, "White")
            play_button.draw(canvas)
            quit_button.draw(canvas)
            if confirm_buttons[0].display == True:
                canvas.draw_polygon([[225, 270], [375,270], [375,360], [225, 360]], 1, "blue", "white")
                canvas.draw_text("Are you sure you", [234, 298], 20, 'Black')
                canvas.draw_text("want to quit?", [246, 318], 20, 'Black')
                for button in confirm_buttons:
                    button.draw(canvas)
        else:
            #If game not paused, a hero image will take place of start level button
            draw_sprite(canvas, hero_turn_sprite, [700, 550], 400, 40, math.pi+get_angle(hero.direction))
                                               
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 800, 600)
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
frame.set_mouseclick_handler(mouse_handler)

# Start the frame animation
frame.start()
start()




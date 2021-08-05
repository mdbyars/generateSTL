# randomSTL
How can you immortalize music?
In several million years, all of our buildings, coke bottles, and monuments will be dilapidated leaving almost nothing behind. How can we immortalize our humanity here on earth? Should we even try? The golden record was sent out to space in 1977 and included popular songs from around the world to show aliens who we are. However, I feel as though this keyhole view excludes so many voices that were pivotal to the human experience.
This semester, I spent 100+ hours creating a program that turns music into sculpture. I poured my heart into this piece. I used python code that I wrote myself that takes the Fourier Transform, meshLab to calculate normals and fusion360 for rendering.
I have always believed that we should care about the suffering of others, not just the oppression we face. As a white, queer person assigned female at birth, I wish to use my expertise and privilege to raise oppressed voices. My voice. Your voice. BIPOC voices. Trans voices. Feminist voices. Everyone who was excluded from the golden record in 1977.
So, here is my version of the golden record! The... Silver Blobs!!... Okay the title needs work. Not silver because it's second place; I just think it's prettier! But here are some sounds that exemplify the human experience, advocated for unheard voices and expressed extreme suffering through music.
Below we have: Pussy Riot's Organs which put the band in Russian prison for perpetuating the "Gay Agenda",
The first Phone call made EVER (don’t get me started on the patent theft though), and
Stonewall Nation (The First Gay Liberation Record)!
I posted the first song I added to this collection on social media. Strange fruit by Billie Holiday. The fact that this song was not included in the golden record was not entirely surprising. However, I feel like no other song better exemplifies humanity. It is well known to be a masterfully beautiful song about the lynching of black people in America. As time has passed, the song remains devastatingly relevant. I started this project with this song in mind. I still believe that Strange Fruit should be the first addition to any new golden record to immortalize the suffering of black people in America and the all too human tendency to oppress. We cannot let time erase these crimes and black music needs the amplification it deserves as the basis of most modern music. So many popular white artists simply appropriated the style and ingenuity of black artists. However, because of the negative response I received, I won't be posting those models on social media. Only including them here for my assignment. Some people were uncomfortable with me using a black woman’s voice for my art. Because of this morbid historic relationship of white artists using black art, I understand the discomfort. I do not want to be a source of pain, only of joy and support! I hope, through this full explanation, you understand my intentions were ally-ship. As always, I am open to feedback on this matter! I am a better person because of all of you. Thank you for supporting my lifelong goal of activism through science and art. 
For FINAL readme/write up: https://prezi.com/view/BwtK1iFhxj3G3af9baxE/

To run random STL Generator: 
$pip install numpy-stl 
$python genStl.py
Then the STL will appear in the foler. 

To generate a song based model:
You must edit the line in fft.py to put in your own file name. Only accepts WAV files. 
$python fft.py > yourFileName.xyz 
Then, follow the instructions in the prezi above. 

Midway Project checkpoint writeup: 
Produces a randomized STL. 
For this project I will use python from personal preference and its nice stl handling. I will begin with a list of possible vertices and planes. Then, I will use math.random to randomize the exact points that will be used. Next, I will need to implement some simple version of convex hull to ensure that the final stl is 3dprintable and not infinately small or thin in any area. Additions may include adding several randomized stls together in a mathematically random fashion or using data from mp3 files to have a controled randomness based on music. After I have generated several different files, I will pick my favorite to 3d print. Mostly the compelx part is having the vertices and planes match even when randomized and convex hull is alittle bit of an obsticle. However, there are plenty of solutions. to the concave issue such as adding multiple stls together. 

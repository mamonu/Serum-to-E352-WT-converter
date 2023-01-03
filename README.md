#  A Serum to E352 Wavetable converter


## 1. What Are Wavetables & How Do They Work?


`“Wavetable Synthesis”` is a technique used to generate unique and evolving waveforms from a series of frames (waveforms) stored within the wavetable. 
This technology has been in use since the 70’s but has gained popularity and been expanded upon in recent years. 
One analogy to understand wavetables would be a flip-book. 

![image](https://gravitascreate.com/wp-content/uploads/2021/01/flipbook-gif.gif)

The flip-book would be the wavetable, and each page within that book would be a waveform. 
Flipping through the book (wavetable) at a fast pace would produce a morphing or evolving waveform.




## 2 What is the E352?


![image](https://user-images.githubusercontent.com/3820011/210415586-1f957da1-4702-4733-96d9-438fef5e729f.png)


### 2.1 Details

The Synthesis Technology E352 combines the latest 200MHz 32-bit ARM DSP with SynthTech's Cloud and Morphing algorithms 
found in the legendary E340 Cloud Generator and the E350 Morphing Terrarium.



Some important features:

User-defined wavetables loaded via microSD card
Color 240 x 320 TFT LCD display
Grayhill mil-spec optical encoder for data entry
16-bit wavetables (versus 8-bit for the E350) for 5x lower noise & THD
Contains all 192 of the original E350 wavetables
LFO mode, variable Glitch Energy and other added features
VCO Architecture
The E352 has a single VCO, but 2 seperate audio outputs. The outputs are determined by the VCO Mode setting. They do not necessarily have to be the same pitch (Detuning Mode).

The VCO is based upon a unique implementation of wavetable synthesis using 256 fixed-sample-length tables of 16-bit values. Each bank in memory consists of 64 wavetables, in an 8x8 array (like a chessboard). Our proprietary DSP algorithms then allow either smooth or 'glitched' morphing between the wavetables in various ways. The E352 comes with 3 factory banks (192 total waves) and internal FLASH memory to hold 26 user-defined banks. This allows over 1,650 individual wavetables to be accessible. The free, cross-platform WaveEdit program is used to generate and import WAV files to user Banks.

Each VCO has 3 CV inputs (called Parameters or PARMs) which the VCO mode assigns to functions within that algorithm. In addition, there is a hard SYNC input, and the FM can be set to exponential or 3 ranges of TZFM (Thru-Zero FM).


### 3 What is Serum


![image](https://user-images.githubusercontent.com/3820011/210420174-bdb19ebf-4607-4fe0-b91e-4c28a1e31117.png)


Serum is a wavetable synthesizer plugin created by Xfer Records that has completely taken over the music production world as the most used synth plugin.






# 🌿 Deprowave
A minimal dark Pop OS based rice

<img src="https://media.discordapp.net/attachments/1115614887658410085/1128824822059778049/Mono.png?width=864&height=652" />

<center> <h1 align="left" id="">Tables</h1> </center>
<summary>Table of Contents</summary>
  <ol>
    <li><a href="#about">About</a></li>
    <li><a href="#keybinds">Keybinds</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>


<center> <h1 align="left" id="about">About</h1> </center>

<center> <p align="left" >Deprowave is a minimalist Pop OS rice that boasts lightning-fast performance and a clean, uncluttered interface designed to enhance productivity and streamline workflow. With bspwm as its window manager and sxhkd for binds, PurpMal delivers an intuitive user experience that is both efficient and customizable. Remarkably, this rice is capable of running smoothly on a mere 1GB of RAM, even with all applications open. PurpMal is an ideal choice for professionals seeking a fast and minimalistic operating system that can handle daily use with ease. </p></center

<center> <h1 align="left" id="keybinds">Keybinds</h1> </center>


1. Applications

   ```
   LAlt + T = Alacritty
   LAlt + S = Theme Changer
   LAlt + SPACE = Rofi
   ```
   
2. Window Manager

   ```
   WinKey + LAlt + R = Restart BSPWM
   WinKey + LAlt + Q = Exit BSPWM
   ```

3. Window States

   ```
   WinKey + S = Floating Window
   WinKey + T = Tiling Window
   WinKey + F = Fullscreen Window
   WinKey + LShift + T = Pseudo Tiling Window
   ```
   
4. Window Move & Resize

   ```
   WinKey + MBLClick = Move Window
   WinKey + MBRClick = Resize Window
   ```


<center> <h1 align="left" id="firefox">Firefox</h1> </center>

1. Rice Firefox ( Manuall )
  
    * Enabling the Modules
   
      Firstly you need to visit `about:config` by puting it in your URL Bar and Clicking Enter. It will display a Popup with the message I accept the risk, click yes and then search for these but one at a time and set everything to **True** by double Clicking them!
      
      `toolkit.legacyUserProfileCustomizations.stylesheets` <br />
      `layers.acceleration.force-enabled` <br />
      `gfx.webrender.all` <br />
      `svg.context-properties.content.enabled` <br />
       <br />
      
    * Creating the Folder and Files
    
      You need to open Alacritty and execute `cd .mozilla/firefox/` then you can list the files by doing `ls`.
      After that you have to find the folder that has `.default-release` at the end of it and then cd inside it.
      If youre inside the profile Directory you can now execute `mkdir chrome && cd chrome` after that you can move the files from the [Firefox Files](https://github.com/0romos/Deprowave/tree/main/Firefox) inside the chrome folder! When you're done close Firefox using ctrl + q!<br />
   
<center> <h1 align="left" >Contributing</h1> </center>

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

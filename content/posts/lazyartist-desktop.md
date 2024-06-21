---
title: 'Content creation is boring as hell, so I built an app'
summary: "Project showcase for a desktop app I built to help with my painting hobby"
date: 2024-06-21T20:23:51+08:00
---

## Problem
I keep forgetting to take pictures of the process whenever I paint. Work in progress (WIP) pics are such an easy way to squeeze out more value out of a painting - you just have to remember to shake yourself out of the artist daze enough to remember to actually do it.

{{<img src="/images/Screenshot%202024-06-21%20202710.png" caption="This took me more than a month to make" >}}

## Solution
Well, whenever I do get in the mood to paint it's almost impossible to shake myself out of it until I finish unless there's an earthquake or something -- so I made an app do it for me.

## Solution; How does it work?: 
Clip Studio Paint has a feature where it can automatically save the WIP video for you. 

That in itself is already amazing enough, but it can be as long as just a few minutes to HOURS. When I'm done painting I usually don't have the energy to sift through all that footage anymore LMAO. 

So this desktop app (LazyArtist -- name not final) basically just looks at the directory where the videos are stored, and automatically gets snapshots for me -- automatically resized to be good enough for most social media platforms. 


{{<img src="/images/Pasted%20image%2020240621113437.png" caption="Desktop notifications" >}}
{{<img src="/images/Pasted%20image%2020240621112515.png" caption="Closeups on random regions of the painting" >}}
{{<img src="/images/Pasted%20image%2020240621112457.png" caption="Snapshots of regular intervals of the painting" >}}


That's it. Dead simple, no AI or whatever. To make things even lazier, the app automatically runs on the background on startup. Once I'm done configuring the app, I really don't have to think about it anymore. 


{{<img src="/images/Pasted%20image%2020240621112411.png" caption="The user interface" >}}

(caption: I literally just used [Custom Tkinter](https://pypi.org/project/customtkinter/) for the UI. Not my best work, but this app will be in the background 95% of the time anyway 💀)

## Challenges
This entire thing was mostly a personal challenge where I wanted to see how general purpose Python really is. I have experience with [Electron JS](https://www.electronjs.org/) and [WPF](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/getting-started/introduction-to-wpf-in-vs?view=netframeworkdesktop-4.8) -- but at the time I was looking for an easy way to utilize [OpenCV](https://pypi.org/project/opencv-python/). I chose OpenCV over something like [FFMPEG](https://ffmpeg.org/) since I'm hoping to add more intensive postprocessing steps later on.

Sure enough, getting OpenCV to work was easy -- but I ran into way more gotchas than expected just building and packaging the application. Here's a few tips from the top of my head:

- For Python projects I usually use [WSL](https://ubuntu.com/desktop/wsl) by default -- it's just a muscle memory thing, everything is way easier on Linux. But I got way too many cryptic errors before I realized that building a desktop application for Windows on Linux ...was a pretty stupid decision.
- With WPF and Electron, I don't remember ever having any issues with creating an installer. At some point, I just got the MSI installer as soon as I built the project and it was over. For this toolset the best I could get was a .exe of the application. It works for me since this is just a personal project anyway -- but the next thing I have to work on now would be to build that installer myself so that (1) Windows doesn't flag this as a virus and (2) Users can just check a box to run the app on startup instead of going through [this whole process](https://www.dell.com/support/kbdoc/en-us/000124550/how-to-add-app-to-startup-in-windows-10)

# Closing
Regardless, the main point of side projects is really just to learn new things about my preferred toolkit and this really served its purpose -- commercializing this would be a fun next step but for now, I'll leave that to future me. Will update this article as I go. Cheers!
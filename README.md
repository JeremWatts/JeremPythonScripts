# Script Collection

A set of useful scripts with descriptions, usage instructions, and example use-cases. More scripts will be added over time.

---

### ❗ `groupcrop.py` 🎨
**Purpose:** 

   Crop all images in the same folder as the script. Overwrites the original files.  

**How to Use:**  
   1. Place `groupcrop.py` in the folder containing your images.  
   2. Edit the crop values directly in the script.  
   3. Run the script:  
      - On Windows: Open the folder, type `cmd` in the address bar, press Enter.  
      - Type `python groupcrop.py` and press Enter.  
      
**Use-Case Example:** Preparing Blender sprites for Zandronum without having to install gimp.

---

### ❗ `45RGBA.py` 🎨
**Purpose:** 

   Recolour all images in the same folder as the script down to 45 colours + transparency. 

**How to Use:**  
   1. Place `45RGBA.py` in the folder containing your images.  
   2. Run the script:  
      - On Windows: Open the folder, type `cmd` in the address bar, press Enter.  
      - Type `python 45RGBA.py` and press Enter.  
      
**Use-Case Example:** Optimizing art for games.

---

### ❗ `time.py` ⏰
**Purpose:** 

   Display system time. 

**How to Use:**  
   1. Open command prompt, type `taskschd.msc`, press enter.  
   2. Have this script open in a cmd window on startup. I might detail the steps for this here one day. Use an LLM in the mean time.
   
**Use-Case Example:** You're seethingly sick of windows' explorer.exe and you still want to see the time.

---



### ❗ `t+v.py` ⏰+🔊
**Purpose:** 

   Display system time in 5min increments, and let you input a float for volume control or even simply press enter to receive time again. 

**How to Use:**  
   1. Open command prompt, type `taskschd.msc`, press enter.  
   2. Have this script open in a cmd window on startup. I might detail the steps for this here one day. Use an LLM in the mean time.
   
**Use-Case Example:** You're seethingly sick of windows' explorer.exe and you still want to see the time and set your volume.

---

### ❗ `convert all subfolder images to 4bit.py` 🎨
**Purpose:** 

   Save you disk space via reducing many images to 4bit. This script looks through the root folder that it is placed in, and all subfolders, then creates an output with the same folder structure where it converts any PNGs found inside into 4bit to give your disk a rest.
This does not touch images with transparency, because 4bit does not blend transparency. there is definitely a way to deal with that that i've done in the past. transparent iamges, though not 4bit, will still be copied into the output of course.

**How to Use:**  
   1. Place `convert all subfolder images to 4bit.py` in the folder containing your image folders.
   2. Open command prompt, type `python "convert all subfolder images to 4bit.py"`, press enter.  
   
**Use-Case Example:** Your PNGs are too fat.


---


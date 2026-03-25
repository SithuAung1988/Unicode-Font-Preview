# Myanmar Unicode Font Previewer
One of my hobbies is collecting Myanmar Unicode fonts. I have a huge collection dating back to the early days of Burmese unicode. 
Have you ever used or heard of 'Myanmar1'?

One of the problems font collectors face is that not every font is for everyone. As a writer who usually spends hours before actually writing 
anything to check which fonts will be the best for a particular piece of text, I’ve noticed that the fonts that writers love aren't necessarily 
liked by others, and vice versa. For us writers, a proper Burmese font needs to be rounded, simple, clean, and look good on the printed page. On 
the other hand, programmers prefer monospaced fonts—something that looks crisp and isn't taxing on the eyes.

## The Problem with Font Management
The real headache starts when you get a new font collection. If you install around 100 fonts just to see how they look in Microsoft Word or Notepad 
or TextEdit, it becomes a total mess. It’s a huge chore to go back and delete the ones you don't like.

While there are websites like [font.saturngod.net](https://font.saturngod.net/) and [Myanmar Unicode Fonts Preview](https://myanmar-unicode-fonts.pages.dev/) 
where you can preview 30 or 40+ Burmese unicode fonts, they have limitations. Being websites, you can’t use them offline, and you can only view 
what is hosted on their server. There are many "cool" and "fancy" Myanmar Unicode fonts out there that aren't available on these sites.

Recently, **NatPanchi** has been giving away many fonts for free of charge; I’ve already downloaded about 20. I also really like the fonts by **Ko Zin Bo**—he has 
both free and paid ones. I’ve personally bought several of his, like "Z02-Typewriter", and "Z03-Press".

## The Solution: A "Vibe Coding" Project
With so many fonts, deciding which one to use before I start writing becomes a task in itself. Constantly installing, deleting, searching, and buying fonts is exhausting.
To solve this, I wrote this app using **"Vibe Coding"** so I can easily preview everything from the latest NatPanchi fonts to ancient ones like "Parabaik" without the hassle.

## Technical Details:
* **The Journey:** I initially tried **Tkinter**, but previewing uninstalled fonts required complex workarounds with `ctypes`, which didn't work at all on macOS. Then I tried **NiceGUI** using CSS `@font-face`; the UI was beautiful, but packaging it with `Pywebview` was a nightmare.
* **The Result:** I settled on **Flet**, a relatively new GUI library I had never used before.
* **Development:** I thought it would take 15 minutes, but it took 3 days because I wanted to create a proper package. The logic and GUI code aren't complex. Using **Felt** was not quite as easy as HTML/CSS/Tailwind, 
but it’s far less finicky than **PySide** or **wxPython**. It's robust and has plenty of widgets. 
* **Performance:** Since `PyInstaller` and `NiceGUI Pack` have issues on macOS, I built this using **Nuitka**. It’s not my usual workflow, but the performance is great.

## How to Use It
- **For Python Users:** 
    - Set up your Python virtual environment first. You should have at least version 3.12.x to use the **Unicode Font Previewer**.
    - Activate your virtual environment. Then install **Flet** by ruuning `pip install flet`.
    - Then enter into the directory where you placed the `main.py` file.
    - Then simply run `python main.py` or `python3 main.py`.
- **For Apple Silicon Users:** I’ve provided a pre-built App. It’s under 60MB.
- **Coming Soon:** I will package versions for Intel-based Macs and x86_64 Windows and Linux machines soon.

**Key Features:**
- Preview Myanmar Unicode fonts **without installing** them on your system.
- Adjustable font sizes via a slider.
- Toggle between Dark and Light modes.
- **License:** Open source under GPLv3.

## Latest Release
- **v0.0.1** - Apple Silicon - Nuitka - **[DOWNDLOAD](https://github.com/SithuAung1988/Unicode-Font-Preview/releases/tag/v0.0.1)**

## Who is this for?
This is perfect for font creators, designers, typists, AI researchers, video editors, and writers like myself. Instead of cluttering your OS with hundreds of fonts you might not even use, you can preview them first and only install the ones you love. It’s a clean, dedicated Desktop App—not a browser-based app or PWA—so you don't have to deal with Node servers or backend/frontend communication lag.

**Note for macOS (Arm64) Users:**
If you run the app and your font files are stored in protected folders like Desktop, Downloads, or Documents, you will need to grant the app permission to access those directories. It requires Python 3.10+ if you are running from source.

Enjoy!


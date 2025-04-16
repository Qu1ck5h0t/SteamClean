# We all know that Steam doesn't do the best job of cleaning up your uninstalled games. Hopefully this tool helps you with fixing Valve's mess like it did for me.
## Function
This script will check your installed games and compare them to the folder names of your steamapps/common folder, and then present the folders whose names are not in your installed games list as well as their filesizes to help you clean any residue from your previously uninstalled games. **It works on both Windows and Linux!** 

Here's what it looks like:
![image](https://github.com/user-attachments/assets/7b741b43-4082-4bcc-9b12-abc5ffde8840)

## Context
The day prior to writing the script, I had discovered that even though I've uninstalled Cyberpunk 2077 and PUBG through steam, the folders still remained on my machine and were hogging 100GB of my disk space for nothing. I knew that steam was terrible at uninstalling games, but I never thought it'd be this bad. Thus, I took matters into my own hands and got to coding this tool ASAP.

## How it works
First it scans your appdata directory for the .acf files, which correspond to your currently "installed" Steam games. It stores all the AppIDs in a list, which is then requested to Steam's API for their corresponding appnames, which are also appended to a list. Then it compares the appnames to the folder names in your steamapps/common folder, and it identifies the folders whose names are not in the installed games name list. It then gets the folder size of each of those folders, and prints them. Lastly it will delete ```steamapps/common/[foldername]``` for a given user input, or exit the script if the user chooses to do so.

It is compatible with both Linux and Windows because it detects your OS, and uses the corresponding forward/back slashes when constructing paths for file deletion.

## License
I don't care how you use it as long as it's legal and you give me credit. Note that I am not responsible for any misuse of this utility, and by downloading this you acknowledge that there will be no guarantee of support beyond bugs with the code.

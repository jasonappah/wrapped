# wrapped

Spotify Wrapped, but for your beats. See what VSTs you use most, what samples you use most, and more.

# Notes

another winter, another attempt at this project - open source this time, for accountability

* stats that would be interesting to pull:
  * most used sample
    * most used overall, then break down by sample type (bass, snare, etc)
    * maybe use gm drum list to 'categorize' samples
    * how does fl/ableton categorize files
  * most used vst
  * how many projects
  * average length (in bars and in ms)
  * average bpm
  * fl includes the time spent in a project, that's an interesting stat to show
  * would be cool if we could analyze midi patterns to determine categories but that is a long way away idk much about data analysis stuff lol
* use the pudding/spotify wrapped for inspiration
* for now i want to support fl and ableton
  * ableton is probably higher priority given thats what i use and als files are so much easier to parse (just gzipped xml lol)
  * a lot of ppl also use fl so i def want to get that working at some point, later tm
* def should be a desktop app - i imagine people would be sus if a web app asked you to upload all your projects 🤔
  * qt? flutter? tauri? electron? idk aaa
    * i've done a good bit of electron stuff recently so that would definitely be easy... but this fl parsing library that would make my life so so so much easier is in python so...
      * ffi? lmao

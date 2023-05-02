# Monte-Carlo-Project
This includes a python library with a simple monte carlo simulator. It includes three classes: Die, Game, and Analyzer that accomplish various tasks by Isidro Pride

# Installation and Usage
## Via Github
1. Go to Github repository main page, [link](https://github.com/Isidro5004/casino).
2. At the top right of the page, click Fork.
3. Review the options and change to your liking.
4. click create fork.
5. Run the following code in local command line:
```
$pip install git+<url>.git#egg=casino
```
## Using it
In preferred python workspace, use the from and import functions to bring in module(s)
```python
from casino import montecarlo 
```
### Code Example
For this example, we will make a coin with faces 'H' (heads) and 'T' (Tails). The Game class only requires one die to initialize, but for this example, we will pass five dice. Note that we can pass the same die multiple times. We will also play the game 1,000 times. Afterwards, we can analyize statistics of the game we played. Let's get the number of jackpots or number of times that all five dice have the same face.
```
from casino import montecarlo as mc
die = mc.Die(['H','T'])
game = mc.Game([die,die,die,die,die])
game.play(1000)
analysis = mc.Analyzer([game])
jackpots = analysis.jackpot()
```

## API Description
### Die
A die has N sides, or “faces”, and W weights, and can be rolled to select a face. To create a die/dice, create an array of face elements that can be either a numeric or string. Weights do not need to be input to run as it defaults to 1.0.

#### change weight


### Game Class

```
game = Game([die,die,die])
```

## License 
MIT License

Copyright (c) 2023 Isidro Pride 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

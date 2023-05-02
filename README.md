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
### Die Class
A die has N sides, or “faces”, and W weights, and can be rolled to select a face. To create a die/dice, create an array of face elements that can be either a numeric or string. Weights do not need to be input to run as it defaults to 1.0. This class creates any discrete random variable associated with a stochastic process, such as using a deck of cards or flipping a coin or speaking a language.
#### Methods
__change_weight(face,new_weight)__
<br>    Allows user to change weight on a given face from the default initialized value of 1.0. 
<br>__roll(num_rolls = 1)__
<br>    Returns a list of random weighted faces with n-length determined by the user.
<br>__show()__
<br>    returns the most recent face and weight values as a dataframe.<br>__Returns__
<br>The return will be a dataframe with the user defined faces and weights defaulted to 1.0.        
#### Attributes
__N__: array, dtype = numbers or strings
<br>        array of number or strings used to represent variable.
<br>__W__: array, dtype = floats
<br>      fl it defaults to 1.0.

### Methods

#### change weight
Allows user to change weight on a given face from the default initialized value of 1.0.
<br> __Parameters__
<br> __face__: array, dtype = numbers or strings
<br> array of number or strings used to reference weight value to change. 
<br>__new_weight__: float
<br> user defined float value to affect probability of face being selected different from default value of 1.0. 

#### roll
Returns a list of random weighted faces with n-length determined by the user.
<br>__Parameters__
<br>__num_rolls__: numeric,optional
<br> indicates the number of face values that will randomly selected influenced by weight.Default is 1.
<br>__Returns__
<br> a list of random face values.

#### show
Returns the most recent face and weight values as a dataframe.
__Returns__
<br>The return will be a dataframe with the user defined faces and weights defaulted to 1.0.


### Game Class
A game consists of rolling of one or more dice of the same kind one or more times.

#### Methods
__play(num_rolls)__
<br> Takes a parameter to specify how many times the dice should be rolled. Saves the result of the play to a private dataframe of shape N rolls by M dice. The private dataframe should have the roll number is a named index. This results in a table of data with columns for roll number, the die number (its list index), and the face rolled in that instance.
<br>__show(form = 'W')__
<br> Returns the most recent face and weight values as a dataframe.
#### Attributes
__dice__: die class object
<br> die or dice created of equal length 
<br>__form__: string, optional
<br> user defined value determines the dimensions of the returned private dataframe. 'N' will return a narrow dataframe while 'W' will return wide dataframe.

#### play
Takes a parameter to specify how many times the dice should be rolled. Saves the result of the play to a private dataframe of shape N rolls by M dice. The private dataframe should have the roll number is a named index. This results in a table of data with columns for roll number, the die number (its list index), and the face rolled in that instance.
<br>__Parameters__
<br>__num_rolls__: numeric
<br>Number of times that die/dice should be rolled.

#### show 
This method just passes the private dataframe to the user.
<br>__Paramaters__:
<br> __form__: string, optional
<br>User defined value determines the dimensions of the returned private dataframe. 'N' will return a narrow dataframe  while 'W' will return wide dataframe. 

### Analyzer Class
An analyzer takes the results of a single game and computes various descriptive statistical properties about it. These properties results are available as attributes of an Analyzer object.

#### Methods
__jackpot()__
<br>method to compute how many times the game resulted in all faces being identical.  
<br>__combo()__
<br> method to compute the distinct combinations of faces rolled, along with their counts.
<br>__face_count()__
<br> method to compute how many times a given face is rolled in each event.
        
#### Attributes
<br>__datatype__: dtype
<br>will ascertain the datatype of variables.
<br>__game__: game class object
<br>Game that will statistics will be derived from.
<br>__jackpott__: dataframe
<br> how many times a roll resulted in all faces being the same.
<br>__combodata__: dataframe
<br>how many combination types of faces were rolled and their counts  
<br>__facecountdata__: datataframe
<br> the number of times a given face appeared in each roll

#### jackpot
Method to compute how many times the game resulted in all faces being identical. returns an integer count of times all faces were identical.

#### combo
Method to compute the distinct combinations of faces rolled, along with their counts. Returns dataframe of these values.

#### face count
Method to compute how many times a given face is rolled in each event. Returns these values as dataframe.

## Manifest
- LICENSE
+ README
* casino
  - init.py
  - montecarlo.py
* tests
  - init.py
  - montecarlo_tests.py
* montecarlo_results.txt
* setup.py
* monte.ipnyb

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

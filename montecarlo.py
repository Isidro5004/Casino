import numpy as np
import pandas as pd

class Die:
    '''
    Purpose:
    ---------
    This class creates any discrete random variable associated with a stochastic process, 
    such as using a deck of cards or flipping a coin or speaking a language.
    
    Methods:
    ---------
    change_weight(face,new_weight)
        Allows user to change weight on a given face from the default initialized value of 1.0. 
    roll(num_rolls = 1)
        Returns a list of random weighted faces with n-length determined by the user.
    show()
        returns the most recent face and weight values as a dataframe.
        
    Attributes:
    ------------
    N: array, dtype = numbers or strings
        array of number or strings used to represent variable.
    W: array, dtype = floats
        float values to affect probability of face being selected.      
    '''
    def __init__(self,faces,weight = 1.0):
        '''
        Parameters
        -----------
        faces: array, dtype = numbers or strings
            array of number or strings used to represent variable.
        weight: float, optional
            float value to affect probability of face being selected.Default 1.0.     
        '''
        
        self.N = np.array(faces)
        self.W = np.repeat(weight,len(self.N))
        self.__datastore = pd.DataFrame({'faces':self.N,'weight':self.W})
 
    def change_weight(self,face,new_weight):
        ''' Allows user to change weight on a given face from the default initialized value of 1.0.
        
        Parameters
        -----------
        face: array, dtype = numbers or strings
            array of number or strings used to reference weight value to change. 
        new_weight: float
            user defined float value to affect probability of face being selected different from default value of 1.0. 
            
        Flags/Exceptions
        -----------------
        will test if the face value is actually in the array.
        will test if the new weight is a float or can be converted into one.
        '''
        
        #Check to see if face is in array
        if face not in self.N:
            print('Face value not present in array!')
            return
        
        #Check if weight is a float
        if new_weight is not float: 
            try: 
                float(new_weight) 
            
            except: 
                print('Invalid format for weight. Cannot be converted to float.')
                return 
        
        #change values 
        idx = list(self.N).index(face)
        self.W[idx] = new_weight
        self.__datastore['weight'] = self.W
        
    def roll(self,num_rolls = 1):
        ''' Returns a list of random weighted faces with n-length determined by the user.
        
        Parameters
        -----------
       num_rolls: numeric
            dictates the number of face values that will randomly selected influenced by weight.   
        '''
        
        weighted_dist = self.__datastore['weight']/sum(self.__datastore['weight'])
        randomizer = lambda a: np.random.choice(a['faces'],1, p = weighted_dist)
        return np.concatenate([randomizer(self.__datastore) for x in range(0,num_rolls)]).tolist()

    def show(self):
        ''' returns the most recent face and weight values as a dataframe.'''
        return self.__datastore
      
class Game:
    '''
    Purpose:
    ---------
    A game consists of rolling of one or more dice of the same kind one or
    more times.
    
    Methods:
    ---------
    play(num_rolls)
        Takes a parameter to specify how many times the dice should be rolled. Saves the result of the play to a private dataframe
        of shape N rolls by M dice. The private dataframe should have the roll number is a named index. This results in a table of 
        ata with columns for roll number, the die number (its list index), and the face rolled in that instance.
    roll(num_rolls = 1)
        Returns a list of random weighted faces with n-length determined by the user.
    show(form = 'W')
        returns the most recent face and weight values as a dataframe.
        
    Attributes:
    dice: die class object
        die or dice created of equal length 
    form: string, optional
            user defined value determines the dimensions of the returned private dataframe. 'N' will return a narrow dataframe 
            while 'W' will return wide dataframe. 
    ------------
    '''
    def __init__(self,die):
        '''
        die: die class object
            If multiple die - must have the same number of faces and values, but may adopt different weights.
        '''
        
        #for x in range(1,len(die)):
        #    if np.array_equal(die[x].N,die[x-1].N) is False:
        #        print(f"Dice {x} and {x+1} are not of the same type")
        #        return
        #    else:
        self.dice = die 
    
    def play(self,num_rolls):
        ''' Takes a parameter to specify how many times the dice should be rolled. Saves the result of the play to a private 
        dataframe of shape N rolls by M dice. The private dataframe should have the roll number is a named index. This results in 
        a table of data with columns for roll number, the die number (its list index), and the face rolled in that instance.
        Parameters
        -----------
        num_rolls: numeric
            Number of times that die/dice should be rolled.
        '''
        
        self.__playdata = pd.DataFrame(index = range(1,len(self.dice)+1), columns = range(num_rolls))
        for i in range(0,len(self.dice)):
            self.__playdata.iloc[i] =  self.dice[i].roll(num_rolls)
        self.__playdata = self.__playdata.transpose()
        self.__playdata.index = range(1,num_rolls+1,1)
        self.__playdata.index.name = 'Roll'
        
    def show(self,form = 'W'):
        '''This method just passes the private dataframe to the
        user.
        Paramaters:
        ------------
        form: string, optional
            user defined value determines the dimensions of the returned private dataframe. 'N' will return a narrow dataframe 
            while 'W' will return wide dataframe. 
        '''
        
        self.form = form
        if form.upper() != 'W' and form.upper() != 'N': 
            raise ValueError('Invalid Input: must be W or N')
        elif form.upper() == 'N':
            self.__playdata = self.__playdata.stack().to_frame()
            self.__playdata.index.names = ['Roll','Dice']
            self.__playdata.columns = ['Face']
            return self.__playdata
        elif form.upper() == 'W':
            self.__playdata.index.name = None
            self.__playdata = self.__playdata.T
            return self.__playdata
            
            
class Analyzer:
    '''
     Purpose:
    ---------
    An analyzer takes the results of a single game and computes various
    descriptive statistical properties about it. These properties results are
    available as attributes of an Analyzer object.
    
    Methods:
    ---------
    jackpot()
        method to compute how many times the game resulted in all faces being identical.  
    combo()
        method to compute the distinct combinations of faces rolled, along with their counts.
    face_count()
        method to compute how many times a given face is rolled in each event.
        
    Attributes:
    datatype: dtype
        will ascertain the datatype of variables.
    game: game class object
        Game that will statistics will be derived from.
    jackpott: dataframe
        how many times a roll resulted in all faces being the same.
    combodata: dataframe
        how many combination types of faces were rolled and their counts  
    facecountdata: datataframe
        the number of times a given face appeared in each roll.
    '''
    
    def __init__(self,game): 
        '''
        Paramaters
        -----------
        game: game class object
            Game that will statistics will be derived from.     
        '''
        
        self.datatype = type(game._Game__playdata.values[0,0])
        self.game = game
        
    def jackpot(self):
        '''method to compute how many times the game resulted in all faces being identical'''
        
        if self.game.form == 'W':
            self.jackpott = self.game._Game__playdata.eq(self.game._Game__playdata.iloc[0,:],axis = 1).all().to_frame()
        else:
            self.game._Game__playdata = self.game._Game__playdata.unstack()
            self.jackpott = self.game._Game__playdata.eq(self.game._Game__playdata.iloc[:,0],axis = 0).all(1).to_frame()
        return int(self.jackpott.sum())
    
    def combo(self):
        '''method to compute the distinct combinations of faces rolled, along with their counts. '''
        
        if self.game.form == 'W':
            self.game._Game__playdata = self.game._Game__playdata.T
            
        df = pd.DataFrame({'Combinations':[]})
        for i in range(0,self.game._Game__playdata.shape[0]):
            df.loc[i+1,'Combinations'] = self.game._Game__playdata.iloc[i,:].map(str).str.cat(sep = ' ')      
            df2 = df['Combinations'].value_counts(ascending = True)
            self.combodata = df2.to_frame()
        return self.combodata
    
    def face_count(self):
    ''' method to compute how many times a given face is rolled in each event. '''
    
        if self.game.form == 'W':
            self.game._Game__playdata = self.game._Game__playdata.T
            self.facecountdata = self.game._Game__playdata.apply(pd.value_counts).T
      
        else:
            self.facecountdata = game._Game__playdata.apply(pd.value_counts,axis = 1)
        
        return self.facecountdata

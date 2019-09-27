# Recurrent Neural Nets
## (well, and LSTMs)
My distilled notes from various sources including Christopher Olah's explanations [here](http://colah.github.io/posts/2015-08-Understanding-LSTMs/) and Andrej Karpathy's [here](http://karpathy.github.io/2015/05/21/rnn-effectiveness/). These are my transliterations doing a level 3 read (see Mortimer J. Adler's "How to Read a Book", summary [here](https://fastertomaster.com/how-to-read-a-book-mortimer-j-adler/)).

This is an RNN:
<p align="center">
  <img width="125" src="http://colah.github.io/posts/2015-08-Understanding-LSTMs/img/RNN-rolled.png">
  RNN rolled up
<img width="125" src="http://colah.github.io/posts/2015-08-Understanding-LSTMs/img/RNN-unrolled.png" caption="This is a Recurrent Neural Network, hear it roar." >
  RNN unrolled
</p>

An RNN is copies of the same network passing messages forward form the prior RNN. Kind of like an amnesiac who can only inform the next version of themselves through a single sticky note.

The forward pass of the RNN:
`class RNN:
  def step(self, x):
    # update the hidden state
    self.h = np.tanh(np.dot(self.W_hh, self.h) + np.dot(self.W_xh, x))
    # compute the output vector
    y = np.dot(self.W_hy, self.h)
    return y`


## LSTMs: Chained RNNs with Special Structure

LSTMs have modules with four layers. These layers also have specific interactions to accomplish needed functions like memory, attention, and forgetting.

<p align="center">
  <img width="300" src="http://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-chain.png">
<img width="250" src="http://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM2-notation.png">
  Repeating module in an LSTM. Note the four specially structured layers.
</p>


### Cell States
Information is passed through these modules via the "**cell state**." It interacts with the modules' networks through special linear gating functions or "gates." These assure that the information flowing through the LSTM is changed only when it potentially improves our loss function's objective.

<p align="center">
  <img width="150" src="http://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-C-line.png">
</p>
<p align="center">
  Cell state. This is the note that each version of the amnesiac passes forward to the next module.
</p>

### Gates
**Gates** are a sigmoid layer and a pointwise multiplication operator. The sigmoid layer squashes the output to \[0, 1\]. This means that only a certain proportion of each component of the input to the gate will make it through to the **cell state**. The pointwise multiplication operator simply applies those proportions to the incoming weights. There are three gates in the LSTM providing this filtering function.

<p align="center">
  <img width="125" src="http://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-gate.png">
</p>
<p align="center">
  Gate. This filters out stuff.
</p>

## LSTMs One Step at a Time
### Layer 1: Forget Gate Layer
This layer decides what information to remove from the [cell state](#cell-states). Here's what that layer looks like more closely

<p align="center">
  <img width="200" src="http://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-focus-f.png">
</p>
<p align="center">
  Forget gate. This is the note that each version of the amnesiac passes forward to the next module.
</p>

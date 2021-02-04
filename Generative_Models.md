[Home](index.md)
# Generative Models
**Resources**
Great medium article [here](https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f70510919f73).

## Generative Adversarial Networks (GANs)

## Variational Autoencoders (AEs)

For context, encoders are used for dimensionality reduction, the process of creating a smaller, condensed data set to represent a larger dataset. Typically using fewer features which may be a distilled representation of the larger dataset. Principal Component Analysis is a canonical method used to achieve this and is a paricular type of matrix factorization method. 
- **encoder** - process that produces the new feature representation; a kind of data compression
- **decoder** - process that takes reduced feature set and creates features akin to the original dataset; a kind of data decompression
- **encoded or latent space** - the reduced dimensional space into which the original data has been encoded
- **lossy vs lossless encoding** lossy encoding loses some information in the encoding, lossless does not
- **Encoder objective**: maximize information retention in latent space in order to minimize the reconstruction error when decoding. ![objective_of_dim_redux](https://miro.medium.com/max/1096/1*9_DFaRan_hX9xMZldVGNjg@2x.png)
![encoder](https://miro.medium.com/max/2000/1*UdOybs9wOe3zW8vDAfj9VA@2x.png)

**autoencoder** - encoder and decoder scheme where the encoder and decoders are both neural networks. The objective is the same as above, where the learned weights are the encoder and decoders. The encoding happens because the network creates a bottleneck, forcing the autoencoder to pass through only the most vital information for decoding.
If the encoder and decoders were only 1-layer each, then we would be asking the autoencoder to create the best *linear* representation of the original data, like PCA (though without the orthonormal constraint). Adding more layers allows for more dimensions to represent the data.
![autoencoder](https://miro.medium.com/max/1400/1*bY_ShNK6lBCQ3D9LYIfwJg@2x.png)

### Points to Consider
- too many layers reduces the practical and interpretable latent space—it's filled with extra fluff and noise and isn't as compact as it could be. In other words, we could create an eutoencoder so deep that each object gets its own latent space. This isn't useful, we want it compact enough that general features get shared amongst objects as appropriate.
- **regularizing** or the act of constraining the network size and using loss that achieves the goal of the netowork
![goldilocks_encoding](https://miro.medium.com/max/2000/1*F-3zbCL_lp7EclKowfowMA@2x.png)

### Adding the Variational to Autoencoders
Regularized versions of Autoencoders making generating new data possible. 

Standard autoencoders have no constraints on their layers so we have no guarantee that the way they were created will give us meaningful information if we use particular layers of the decoder.

Variational autoencoders encode inputs as distributions over the latent space, as opposed to the typical single point.
Steps:
1) encode the input as a distribution (in practice it's Gaussian)
2) sample from that distribution
3) decode the *sampled point*
4) calculate reconstruction error
5) backpropogate reconstruction error through the network
![autoencoder_vs_variational_autoencoder](https://miro.medium.com/max/2000/1*ejNnusxYrn1NRDZf4Kg2lw@2x.png)


The inputs are ~Gaussian because we can then use a Gaussian-based term in the loss function. In this case it is the Kulback-Leibler divergence between the returned distribution and the inputted distribution. There's a nice closed-form solution to the KL divergence making it easier to compute.
![VAE_loss_function](https://miro.medium.com/max/1400/1*Q5dogodt3wzKKktE0v3dMQ@2x.png)

### Properties Sought Via Regularization
- **continuity** the latent space should have a sense of continuity in its representation of the underlying concepts. In other words, "close" points in the latent space should have "close" interpretations in the original space.
- **completeness** - latent space should give meaningful content when decoded
![encoded_space_properties_sought](https://miro.medium.com/max/2000/1*83S0T8IEJyudR_I5rI9now@2x.png)

**VAEs could easily become plain ol' autoencoders if not regularized with the right loss function.** VAE could return distributions with *tight* variances and/or means that are very far from the original. So we have to penalize both in our loss function by regularizing the covariance matrix and the means of the returned distributions.

Thus we chose standard Gaussian representations of our inputs, so we could enforce this in the loss function. 

This tends to create a "gradient" over the information encoded in the latent space; i.e., points between two known points are "between" the points in the original space.


### Architecture of VAEs
The architecture of VAEs has a theoretical basis derived from Bayes' Theorem along with assumptions necessary to make the problem tractable and implementation practical. The blog linked to above goes through it nicely, I'll just put the pretty pictures here. :)
![encoder_vae](https://miro.medium.com/max/1400/1*XYyWimolMhPDMg8qCNlcwg@2x.png)
![decoder_vae](https://miro.medium.com/max/1400/1*1n6HwjwUWbmE9PvCzOVcbw@2x.png)
![reparameterization_trick](https://miro.medium.com/max/2000/1*S8CoO3TGtFBpzv8GvmgKeg@2x.png)
This is the final architecture and associate loss function. The architecture is based on replacing a probabilistic model with neural nets to approximate the underlying distributions. It also enforces the nice properties we discussed previously. 
- When deriving the loss function shows there's a nice place that shows the direct tradeoff between maximizing the liklihood of the observations and staying close to the prior; in other words, the tradeoff between representing the data well and keeping the representation general enough.
![loss_function_tradeoff](https://miro.medium.com/max/1400/1*v56YF5KqZk35r85EZBZuAQ@2x.png)


# Meta—SDNE:some loss function change for SDNE

## data information

### formula data

number of different symptom:189

number of different herb:357

### edgelist

the first 189 nodes are symptom
the other nodes are herb

## Usage

There are 3 model:SDNE, SDNE_Binary_Loss,SDNE_Meta_path

### Example

python __main__.py --input data\s_h.edgelist --method sdne_meta_path --graph-format edgelist --output embedding.vec

### Specific Options

- --encoder-list, a list of numbers of the neuron at each encoder layer, the last number is the dimension of the output node representation, the default is [1000, 128]
- --alpha, alpha is a hyperparameter in SDNE that controls the first order proximity loss, the default is 1e-6
- --beta, beta is used for construct matrix B, the default is 5
- --nu1, parameter controls l1-loss of weights in autoencoder, the default is 1e-5
- --nu2, parameter controls l2-loss of weights in autoencoder, the default is 1e-4
- --bs, batch size, the default is 200
- --lr, learning rate, the default is 0.01
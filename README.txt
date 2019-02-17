Welcome to the Neuroecon lab!

This is meant to be a brief intro to training word embedding models.
Word embeddings are powerful models of natural language that map words
like "cat", "running", "Obama", etc... to vectors in a high-dimensional
vector space. These vectors preserve information about the words they
represent. For example, the vector for 'car' can be expected to be
similar to the vectors for 'truck', 'vehicle', 'minivan', etc...

A more astonishing quality is that certain vector operations can be used
to complete analogies. For example, subtracting the vector for "man" from
the vector of "king", and adding in the vector for "woman" gives us a 
vector similar to that for "queen".

king - man + woman ~= queen

This might be a lot to take in, so to start try running train.py and build
your own word embedding model. Afterwards, run explore.py in interactive
mode (python -i explore.py) and mess around with some of the methods
listed, or try some of your own. The model may take a while to train
(On average it takes ~20 minutes on my machine) so feel free to browse
through the code while it does so and get a feel for whats going on.

Also considering skimming through the following paper:
    - https://arxiv.org/pdf/1301.3781.pdf
    - https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf

Thankfully, we're not in the
business of designing algorithms to generate word embeddings, just
analyzing patterns in existing models. However, it's important to get
a feeling for how these models are actually generated to understand
why and what kind of information they encode. Don't get too bogged down
in the details, but feel free to come back to me with any questions.

Once you've explored the model, try to answer some of the following
questions:

What data type are the vectors corresponding to each word stored as?
(Hint: try using the builtin function `type`)

How many dimensions do these vectors have?

What sorts of operations can we use on these vectors?

How does the model deal with homophones? i.e. the string 'orange' could
refer to either a fruit or a color.

Does the model contain any multi-word strings? i.e. 'New York', 'Barack Obama',
'San Francisco Giants'

Does the model distinguish between capitalized and uncapitalized words?
For example, are there seperate entries for 'the' and 'The'?

(You don't have to send the answers to me or anyone or anything, just keep
these questions and their answers in mind.)

import os
import tensorflow as tf
import numpy as np

path_to_file = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')

text = open(path_to_file, 'rb').read().decode(encoding='utf-8')

# print(len(text))

vocab = sorted(set(text))
# print(len(vocab))

char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

text_as_int = np.array([char2idx[char] for char in text])

# print(text_as_int)

print('{')
for char, _ in zip(char2idx, range(20)):
    print('     {:4s}:  {:3d},'.format(repr(char), char2idx[char]))
print('...\n')

print('{} ----> characters mapped to int ----> {}'.format(repr(text[:13]), text_as_int[:13]))

seq_length = 100
examples_per_epoch = len(text) // (seq_length + 1)

char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

# for i in char_dataset.take(5):
#     print(idx2char[i.numpy()])

sequences = char_dataset.batch(seq_length+1, drop_remainder=True)

# for item in sequences.take(5):
#     print(repr(''.join(idx2char[item.numpy()])))

def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text

dataset = sequences.map(split_input_target)

# for input_example, target_example in dataset.take(1):
#     print('input data: ', repr(''.join(idx2char[input_example.numpy()])))
#     print('\n')
#     print('taregt data: ', repr(''.join(idx2char[target_example.numpy()])))


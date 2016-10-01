import ParsingText  as pt


datasets=pt.read_data_sets()

batch_images, batch_labels, batch_size=datasets.train.next_batch(10)

print batch_size[0], batch_size[1], batch_size[2], len(batch_size)


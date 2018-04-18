import tensorflow as tf
import numpy as np

# def parse_record(serialized_example, num_classes, channels):
#     keys_to_features = {
#         'image': tf.FixedLenFeature([], tf.string),
#         'label': tf.FixedLenFeature([], tf.int64)
#     }
#     features = tf.parse_single_example(serialized_example, keys_to_features)
	
#     image = tf.image.decode_jpeg(features['image'], channels=channels)
#     image = tf.cast(image, tf.float32)
#     label = tf.cast(features['label'], tf.int32)
#     return image, label

# def resize_image(image, height, width):
#     return tf.image.resize_image_with_crop_or_pad(image, height, width)

# def standardize(image):
#     return tf.image.per_image_standardization(image)

# def preprocess_image(image, params, is_training=False):
#     image = resize_image(image, params['image_height'], params['image_width'])
#     image = standardize(image)
#     return image

# def input_fn(file_names, params, mode=tf.estimator.ModeKeys.EVAL):
#     dataset = tf.data.TFRecordDataset(filenames=file_names)

#     is_training = (mode == tf.estimator.ModeKeys.TRAIN)
#     if is_training:
#         buffer_size = params['batch_size'] * 2 + 1
#         dataset = dataset.shuffle(buffer_size=buffer_size)

#     dataset = dataset.map(lambda example: parse_record(example, params['num_classes'], channels=params['image_channels']))
#     dataset = dataset.map(lambda image, label: (preprocess_image(image, params, is_training), label))

#     dataset = dataset.repeat(None)
#     dataset = dataset.batch(params['batch_size'])
#     dataset = dataset.prefetch(2 * params['batch_size'])

#     images, labels = dataset.make_one_shot_iterator().get_next()

#     features = {'images': images}
#     return features, labels

def resize_image(image, height, width):
	return tf.image.resize_image_with_crop_or_pad(image, height, width)

def standardize(image):
	return tf.image.per_image_standardization(image)

def preprocess_image(image, params):
	image = resize_image(image, params['image_height'], params['image_width'])
	image = standardize(image)
	return image

def parse_record(serialized_example, params):
	keys_to_features = {
		'image': tf.FixedLenFeature((), tf.string, default_value=""),
		'label': tf.FixedLenFeature((), tf.int64, default_value=tf.zeros([], dtype=tf.int64))
	}
	features = tf.parse_single_example(serialized_example, keys_to_features)
	image = tf.image.decode_jpeg(features['image'], channels=params['image_channels'])
	image = tf.image.convert_image_dtype(image, dtype=tf.float32)

	label = tf.cast(features['label'], tf.int32)

	return image, label

def input_fn(file_names, params):
	dataset = tf.data.TFRecordDataset(filenames=file_names)
	dataset = dataset.map(lambda value: parse_record(value, params))
	dataset = dataset.map(lambda image, label: (preprocess_image(image, params), label))

	buffer_size = params['batch_size'] * 2 + 1
	dataset = dataset.shuffle(buffer_size=buffer_size)
	dataset = dataset.batch(params['batch_size'])
	dataset = dataset.repeat(None)
	iterator = dataset.make_one_shot_iterator()
	images, labels = iterator.get_next()
	return {'images': images}, labels
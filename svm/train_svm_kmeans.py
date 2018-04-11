from common import load_images
import numpy as np
from sklearn.preprocessing import normalize
import cv2
import os

# IF_BINARY_FEATURES = bool(os.environ.get('IF_BINARY_FEATURES', False))
KMEANS_CLUSTERS = int(os.environ.get('KMEANS_CLUSTERS', 128))
# IF_SQRT_KEYPOINTS_KMEANS_CLUSTERS = bool(os.environ.get('IF_SQRT_KEYPOINTS_KMEANS_CLUSTERS', False))

from .train_and_test_svm import train_and_test_svm

def train_svm_sift_kmeans():
  (images, image_labels) = load_images(if_grayscale=True)
  X = extract_sift_kmeans_feature_vectors(images)
  y = image_labels
  train_and_test_svm(X, y)

def train_svm_orb_kmeans():
  (images, image_labels) = load_images(if_grayscale=True)
  X = extract_orb_kmeans_feature_vectors(images)
  y = image_labels
  train_and_test_svm(X, y)

def train_svm_colour_orb_kmeans():
  (images, image_labels) = load_images()
  X_blue = extract_orb_kmeans_feature_vectors([[[pixel[0] for pixel in row] for row in image] for image in images])
  X_green = extract_orb_kmeans_feature_vectors([[[pixel[1] for pixel in row] for row in image] for image in images])
  X_red = extract_orb_kmeans_feature_vectors([[[pixel[2] for pixel in row] for row in image] for image in images])
  X = [np.concatenate((b, g, r)) for (b, g, r) in zip(X_blue, X_green, X_red)]
  y = image_labels
  train_and_test_svm(X, y)

def train_svm_colour_sift_kmeans():
  (images, image_labels) = load_images()
  X_blue = extract_sift_kmeans_feature_vectors([[[pixel[0] for pixel in row] for row in image] for image in images])
  X_green = extract_sift_kmeans_feature_vectors([[[pixel[1] for pixel in row] for row in image] for image in images])
  X_red = extract_sift_kmeans_feature_vectors([[[pixel[2] for pixel in row] for row in image] for image in images])
  X = [np.concatenate((b, g, r)) for (b, g, r) in zip(X_blue, X_green, X_red)]
  y = image_labels
  train_and_test_svm(X, y)

# Ref: https://dsp.stackexchange.com/questions/5979/image-classification-using-sift-features-and-svm
def extract_sift_kmeans_feature_vectors(images_gray):
  print('Extracting SIFT features...')
  sift = cv2.xfeatures2d.SIFT_create()

  def to_sift_desc(image):
    (kps, image_sift_desc) = sift.detectAndCompute(np.array(image), None)
    if image_sift_desc is None:
      return []
    return image_sift_desc

  image_sifts = [to_sift_desc(image) for image in images_gray]
  # cluster_vectors = compute_kmeans_cluster_vectors(image_sifts)
  # return cluster_vectors
  return image_sifts

def extract_orb_kmeans_feature_vectors(images_gray):
  print('Extracting ORB features...')
  orb = cv2.ORB_create()

  def to_orb_desc(image):
    (kps, image_orb_desc) = orb.detectAndCompute(np.array(image), None)
    if image_orb_desc is None:
      return []
    return image_orb_desc

  image_orbs = [to_orb_desc(image) for image in images_gray]
  # cluster_vectors = compute_kmeans_cluster_vectors(image_orbs)
  # return cluster_vectors
  return image_orbs


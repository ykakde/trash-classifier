# Results of SVM training V2

SVM_C_PARAM=4 KMEANS_BOW_FEATURES_NORMALIZATION=binary KMEANS_CLUSTERS=sqrt_keypoints KMEANS_JOBS=1 IMAGE_COUNT_PER_CLASS=50 IF_VISUALIZE_FEATURES=True python . svm_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting SIFT features...
Computing KMeans clusters with n_clusters=289...
Converting to binary BoW features...
Converting to binary BoW features...
Running PCA on (X, y)...
Displaying dataset on scatterplot...
Train accuracy: 0.88
Train confusion matrix:
[[29  3  0  5  4]
 [ 0 32  1  0  0]
 [ 0  0 27  0  0]
 [ 0  1  3 34  1]
 [ 1  0  2  0 32]]
Test accuracy: 0.38666666666666666
Test confusion matrix:
[[8 4 1 1 2]
 [3 6 6 2 3]
 [2 2 4 0 1]
 [7 0 3 6 2]
 [0 2 3 2 5]]

SVM_C_PARAM=4 KMEANS_CLUSTERS=sqrt_keypoints KMEANS_JOBS=1 IMAGE_COUNT_PER_CLASS=50 IF_VISUALIZE_FEATURES=True python . svm_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting SIFT features...
Computing KMeans clusters with n_clusters=289...
Running PCA on (X, y)...
Displaying dataset on scatterplot...
Train accuracy: 0.9714285714285714
Train confusion matrix:
[[32  0  0  0  0]
 [ 1 38  0  4  0]
 [ 0  0 36  0  0]
 [ 0  0  0 33  0]
 [ 0  0  0  0 31]]
Test accuracy: 0.24
Test confusion matrix:
[[ 2  1  2  2  2]
 [ 2  2  0  1  5]
 [10  9 12  9 11]
 [ 3  0  0  1  0]
 [ 0  0  0  0  1]]

IF_NORMALIZE_IMAGES=True SVM_C_PARAM=4 KMEANS_BOW_FEATURES_NORMALIZATION=binary KMEANS_CLUSTERS=sqrt_keypoints KMEANS_JOBS=1 IMAGE_COUNT_PER_CLASS=50 IF_VISUALIZE_FEATURES=True python . svm_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting SIFT features...
Computing KMeans clusters with n_clusters=299...
Converting to binary BoW features...
Running PCA on (X, y)...
Displaying dataset on scatterplot...
Train accuracy: 0.9257142857142857
Train confusion matrix:
[[33  0  0  1  3]
 [ 0 34  2  0  0]
 [ 0  1 31  0  0]
 [ 1  0  3 30  1]
 [ 1  0  0  0 34]]
Test accuracy: 0.41333333333333333
Test confusion matrix:
[[10  2  0  9  1]
 [ 0  5  4  0  1]
 [ 2  5  2  1  1]
 [ 2  1  4  7  2]
 [ 1  2  4  2  7]]

IF_NORMALIZE_IMAGES=True SVM_C_PARAM=100 KMEANS_BOW_FEATURES_NORMALIZATION=l1 KMEANS_CLUSTERS=sqrt_keypoints  KMEANS_JOBS=1 IMAGE_COUNT_PER_CLASS=10 IF_VISUALIZE_FEATURES=True python . svm_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting SIFT features...
Computing KMeans clusters with n_clusters=138...
L1 normalizing BoW features...
Running PCA on (X, y)...
Displaying dataset on scatterplot...
Train accuracy: 0.8571428571428571
Train confusion matrix:
[[7 0 0 2 0]
 [1 7 0 1 1]
 [0 0 7 0 0]
 [0 0 0 2 0]
 [0 0 0 0 7]]
Test accuracy: 0.3333333333333333
Test confusion matrix:
[[0 0 0 3 0]
 [1 3 1 1 2]
 [1 0 2 0 0]
 [0 0 0 0 0]
 [0 0 0 1 0]]

IF_NORMALIZE_IMAGES=True SVM_C_PARAM=100 KMEANS_BOW_FEATURES_NORMALIZATION=l1 KMEANS_CLUSTERS=instances_count  KMEANS_JOBS=1 IMAGE_COUNT_PER_CLASS=10 IF_VISUALIZE_FEATURES=True python . svm_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting SIFT features...
Computing KMeans clusters with n_clusters=35...
L1 normalizing BoW features...
Running PCA on (X, y)...
Displaying dataset on scatterplot...
Train accuracy: 0.6571428571428571
Train confusion matrix:
[[5 1 0 1 0]
 [2 7 2 1 4]
 [0 0 2 0 0]
 [0 0 0 6 0]
 [0 0 1 0 3]]
Test accuracy: 0.26666666666666666
Test confusion matrix:
[[1 0 0 1 0]
 [2 2 3 1 2]
 [0 0 0 0 0]
 [0 0 1 0 0]
 [0 0 1 0 1]]

IF_NORMALIZE_IMAGES=True SVM_C_PARAM=4 KMEANS_BOW_FEATURES_NORMALIZATION=binary KMEANS_CLUSTERS=sqrt_keypoints KMEANS_JOBS=1 IMAGE_COUNT_PER_CLASS=50 IF_VISUALIZE_FEATURES=True python . svm_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting SIFT features...
Computing KMeans clusters with n_clusters=299...
Converting to binary BoW features...
Running PCA on (X, y)...
Displaying dataset on scatterplot...
Train accuracy: 0.9371428571428572
Train confusion matrix:
[[33  1  0  2  1]
 [ 0 37  0  0  0]
 [ 0  0 33  0  0]
 [ 2  0  2 32  2]
 [ 1  0  0  0 29]]
Test accuracy: 0.44
Test confusion matrix:
[[10  4  1  5  2]
 [ 1  7  4  1  5]
 [ 0  1  5  0  2]
 [ 2  0  3  7  5]
 [ 1  0  2  3  4]]

IF_NORMALIZE_IMAGES=True SVM_C_PARAM=100 KMEANS_BOW_FEATURES_NORMALIZATION=l1 KMEANS_CLUSTERS=sqrt_keypoints  KMEANS_JOBS=1 IMAGE_COUNT_PER_CLASS=50 IF_VISUALIZE_FEATURES=True python . svm_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting SIFT features...
Computing KMeans clusters with n_clusters=294...
L1 normalizing BoW features...
Running PCA on (X, y)...
Displaying dataset on scatterplot...
Train accuracy: 0.5714285714285714
Train confusion matrix:
[[16  0  1  4  0]
 [19 34 14 16 13]
 [ 0  0 14  0  0]
 [ 1  0  1 13  0]
 [ 2  2  2  0 23]]
Test accuracy: 0.38666666666666666
Test confusion matrix:
[[ 5  0  0  1  0]
 [ 7 11  9  9  6]
 [ 0  0  3  0  1]
 [ 0  0  3  3  0]
 [ 0  3  3  4  7]]

IF_NORMALIZE_IMAGES=True SVM_C_PARAM=4 KMEANS_BOW_FEATURES_NORMALIZATION=binary KMEANS_CLUSTERS=sqrt_keypoints KMEANS_JOBS=1 IMAGE_COUNT_PER_CLASS=50 IF_VISUALIZE_FEATURES=True python . svm_rgb_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting RGB-SIFT features...
Computing KMeans clusters with n_clusters=294...
Converting to binary BoW features...
Running PCA on (X, y)...
Displaying dataset on scatterplot...
Train accuracy: 0.92
Train confusion matrix:
[[27  3  0  3  1]
 [ 0 25  0  0  0]
 [ 1  0 42  0  1]
 [ 2  0  2 33  1]
 [ 0  0  0  0 34]]
Test accuracy: 0.4533333333333333
Test confusion matrix:
[[10  5  0  2  3]
 [ 1  4  0  0  0]
 [ 3  8  5  1  2]
 [ 4  3  0  9  2]
 [ 2  2  1  2  6]]


IF_NORMALIZE_IMAGES=True SVM_C_PARAM=4 KMEANS_BOW_FEATURES_NORMALIZATION=binary KMEANS_CLUSTERS=sqrt_keypoints KMEANS_JOBS=1 IMAGE_COUNT_PER_CLASS=50 IF_VISUALIZE_FEATURES=True python . svm_rgb_gray_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting RGB-Gray-SIFT features...
Computing KMeans clusters with n_clusters=290...
Converting to binary BoW features...
Running PCA on (X, y)...
Displaying dataset on scatterplot...
Train accuracy: 0.9371428571428572
Train confusion matrix:
[[36  2  0  2  2]
 [ 0 34  0  0  1]
 [ 0  0 34  0  0]
 [ 1  1  2 32  0]
 [ 0  0  0  0 28]]
Test accuracy: 0.49333333333333335
Test confusion matrix:
[[11  5  0  5  1]
 [ 0  3  2  1  2]
 [ 0  3  8  2  3]
 [ 0  0  2  7  5]
 [ 2  2  2  1  8]]

IF_NORMALIZE_IMAGES=True SVM_C_PARAM=4 KMEANS_BOW_FEATURES_NORMALIZATION=binary KMEANS_CLUSTERS=sqrt_keypoints KMEANS_JOBS=1 IMAGE_COUNT_PER_CLASS=50 IF_VISUALIZE_FEATURES=True python . svm_rgb_gray_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting RGB-Gray-SIFT features...
Computing KMeans clusters with n_clusters=290...
Converting to binary BoW features...
Running PCA on (X, y)...
Displaying dataset on scatterplot...
Train accuracy: 0.8914285714285715
Train confusion matrix:
[[32  3  0  4  4]
 [ 0 31  0  0  0]
 [ 0  0 29  0  0]
 [ 1  1  3 34  1]
 [ 0  0  2  0 30]]
Test accuracy: 0.4266666666666667
Test confusion matrix:
[[ 9  6  1  1  0]
 [ 1  4  6  1  2]
 [ 0  2  1  0  1]
 [ 6  0  5  8  2]
 [ 1  3  3  2 10]]

IF_NORMALIZE_IMAGES=True SVM_C_PARAM=1 KMEANS_BOW_FEATURES_NORMALIZATION=binary KMEANS_CLUSTERS=sqrt_keypoints KMEANS_JOBS=1 IMAGE_COUNT_PER_CLASS=50 IF_VISUALIZE_FEATURES=True python . svm_rgb_gray_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting RGB-Gray-SIFT features...
Computing KMeans clusters with n_clusters=295...
Converting to binary BoW features...
Running PCA on (X, y)...
Displaying dataset on scatterplot...
Train accuracy: 0.4857142857142857
Train confusion matrix:
[[29 18  5 11  8]
 [ 0  1  0  0  0]
 [ 3  7 24  0 12]
 [ 6  4  9 27  7]
 [ 0  0  0  0  4]]
Test accuracy: 0.18666666666666668
Test confusion matrix:
[[ 6  5  5  7  2]
 [ 0  0  0  0  0]
 [ 0 10  3  0  9]
 [ 6  5  4  5  8]
 [ 0  0  0  0  0]]

IF_NORMALIZE_IMAGES=True SVM_C_PARAM=3 KMEANS_BOW_FEATURES_NORMALIZATION=binary KMEANS_CLUSTERS=sqrt_keypoints KMEANS_JOBS=1 IMAGE_COUNT_PER_CLASS=50 IF_VISUALIZE_FEATURES=True python . svm_rgb_gray_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting RGB-Gray-SIFT features...
Computing KMeans clusters with n_clusters=288...
Converting to binary BoW features...
Running PCA on (X, y)...
Displaying dataset on scatterplot...
Train accuracy: 0.8685714285714285
Train confusion matrix:
[[27  2  0  4  5]
 [ 1 36  2  0  0]
 [ 0  0 24  0  0]
 [ 2  1  4 33  0]
 [ 1  0  0  1 32]]
Test accuracy: 0.36
Test confusion matrix:
[[10  4  1  4  1]
 [ 2  6  9  3  2]
 [ 0  0  1  0  0]
 [ 4  0  3  5  5]
 [ 3  1  6  0  5]]

SVM_C_PARAM=4
IF_NORMALIZE_IMAGES=True
IMAGE_COUNT_PER_CLASS=100
KMEANS_BOW_FEATURES_NORMALIZATION=binary
KMEANS_CLUSTERS=sqrt_keypoints
python . svm_rgb_gray_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting RGB-Gray-SIFT features...
Computing KMeans clusters with n_clusters=414...
Converting to binary BoW features...
[0.66617838 0.84849515 0.51017284 0.508542   0.80471368 0.59112398
 0.80865697 0.58803515 0.70220535 0.49817674 0.72545433 0.56444829
 0.63205103 0.63057809 0.77945491 0.78324429 0.74013036 0.67043407
 0.64012556 0.38765293 0.56897652 0.65050585 0.41538875 0.71194606
 0.768881   0.53246364 0.74319592 0.74908379 0.71948105 0.65374725
 0.61801401 0.7999512  0.63382141 0.64075504 0.71895621 0.48380635
 0.60763731 0.57240953 0.76086801 0.71973363 0.76384865 0.60939031
 0.75660311 0.54399251 0.66955644 0.76818681 0.43015293 0.56905257
 0.67733384 0.86177441 0.619295   0.7441313  0.41362512 0.6601421
 0.6714104  0.52304953 0.48929964 0.40335083 0.59062452 0.76128967
 0.77590037 0.40345435 0.74508361 0.63205795 0.76646437 0.68349992
 0.77379791 0.5874265  0.63624656 0.26318973 0.48055664 0.74368221
 0.76458162 0.70912237 0.78672514 0.68926898 0.76376884 0.84585979
 0.67995887 0.74551939 0.75919852 0.67974748 0.62388628 0.78293533
 0.67539354 0.62701363 0.61502086 0.69791071 0.66299541 0.67572074
 0.77771603 0.5791068  0.76832245 0.6211808  0.68739715 0.68618709
 0.74551552 0.50995188 0.73836545 0.73401345 0.72372097 0.760064
 0.71591216 0.58927449 0.79039248 0.67285405 0.63617995 0.38034345
 0.76025182 0.7437084  0.50416389 0.7785527  0.75334683 0.69205547
 0.81348688 0.69256619 0.77467657 0.7473624  0.62010978 0.70067967
 0.77526392 0.75886353 0.75389373 0.61998445 0.54669031 0.73651921
 0.66738606 0.76152688 0.60741975 0.68675547 0.67265192 0.77834893
 0.4877048  0.40515595 0.62257276 0.78135508 0.61659268 0.77451073
 0.68932003 0.76086182 0.7578716  0.69711916 0.8384873  0.58715141
 0.51643029 0.57859    0.77128371 0.74472295 0.64594714 0.748917
 0.78230688 0.67004775 0.81442623 0.74347418 0.74421129 0.51964081
 0.79560638 0.77374962 0.75813706 0.79379612 0.6166968  0.3630328
 0.73715053 0.69083431 0.66848289 0.40579596 0.81144425 0.79632606
 0.71316074 0.76155681 0.67041743 0.73724987 0.62588712 0.74540419
 0.68779514 0.71229681 0.62404748 0.39058142 0.75686351 0.66815179
 0.39849809 0.61997004 0.80997639 0.36300089 0.6273068  0.73039538
 0.61798911 0.54346792 0.61637128 0.77771068 0.7737114  0.62739224
 0.7516436  0.73430077 0.75666023 0.73039699 0.67130689 0.75641747
 0.63542289 0.73114429 0.43524193 0.77275848 0.61968728 0.58716464
 0.66893483 0.68862792 0.74211375 0.46987174 0.52457351 0.47904078
 0.80490866 0.69682102 0.72923382 0.80658933 0.75194365 0.63263667
 0.68660817 0.38079009 0.63753152 0.88896703 0.76234392 0.73750332
 0.61311002 0.65937838 0.46184495 0.60962918 0.61229507 0.79009097
 0.58923018 0.63062558 0.52130292 0.84948642 0.62897584 0.84939091
 0.74720946 0.773801   0.84845039 0.73903617 0.51536661 0.6283878
 0.6743532  0.73844281 0.63719132 0.74950485 0.42994372 0.75424792
 0.66428845 0.59580162 0.69193193 0.75098358 0.76786051 0.7029322
 0.74396051 0.28857805 0.77192043 0.77262175 0.7740711  0.45341816
 0.55078607 0.54572525 0.60954269 0.78496381 0.77065532 0.72018021
 0.52620642 0.51804198 0.76658226 0.76459891 0.60722603 0.76035989
 0.74874386 0.44927066 0.6626271  0.88649245 0.76843153 0.75237233
 0.75118163 0.72461292 0.68339841 0.37142779 0.6014845  0.6520145
 0.74793104 0.6948675  0.54215206 0.57159601 0.77352889 0.71662745
 0.7108511  0.76671113 0.7456726  0.74749306 0.56795219 0.7537285
 0.61582639 0.56512108 0.6959225  0.36738681 0.58035618 0.68356686
 0.68073536 0.74060676 0.75875552 0.75023055 0.51224047 0.26549431
 0.61888484 0.62282448 0.72424187 0.77358893 0.77264245 0.6156522
 0.52314381 0.72501307 0.84696118 0.59316301 0.73870178 0.6623406
 0.46889655 0.76322892 0.6698399  0.74730837 0.76934785 0.70049808
 0.76423104 0.55824251 0.77402509 0.75417267 0.70222936 0.34317413
 0.76041951 0.5851101  0.64345493 0.41417915 0.78286667 0.59550449
 0.67840347 0.70715499 0.66558942 0.75149037 0.61705819 0.62363612
 0.43676211 0.69009992 0.61951943 0.74404942 0.74647559 0.33959932
 0.64911428 0.79266584]
Train accuracy: 0.9514285714285714
Train confusion matrix:
[[67  0  0  1  0]
 [ 0 66  0  0  0]
 [ 1  0 66  1  0]
 [ 1  0  0 67  1]
 [ 2  4  3  3 67]]
Test accuracy: 0.47333333333333333
Test confusion matrix:
[[15  7  3  5  2]
 [ 4  8  2  1  8]
 [ 2  7 16  0  3]
 [ 6  0  4 16  3]
 [ 2  8  6  6 16]]

SVM_C_PARAM=2
IF_NORMALIZE_IMAGES=True
IMAGE_COUNT_PER_CLASS=200
KMEANS_BOW_FEATURES_NORMALIZATION=binary
KMEANS_CLUSTERS=sqrt_keypoints
python . svm_rgb_gray_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting RGB-Gray-SIFT features...
Computing KMeans clusters with n_clusters=577...
Converting to binary BoW features...
[0.84926647 0.59640571 0.93415018 0.77153343 0.44220216 0.73218523
 0.46728493 0.63774209 0.73143764 0.67578754 0.85130243 0.55212914
 0.48013146 0.83823799 0.81128819 0.55133127 0.50663091 0.68489591
 0.35773408 0.77991068 0.69141975 0.52560077 0.49109706 0.77706991
 0.29426449 0.88484591 0.46181672 0.664293   0.64246377 0.35610149
 0.68595895 0.72893847 0.5629259  0.94362626 0.86621111 0.7573822
 0.84285181 0.83379828 0.8617042  0.92769507 0.47348727 0.74313273
 0.66583789 0.50652443 0.86684056 0.83632773 0.42592429 0.71168403
 0.37832902 0.56751848 0.5464432  0.38569727 0.37670858 0.86653087
 0.39247295 0.80710576 0.48310586 0.67095497 0.52458739 0.41842643
 0.75051756 0.81027206 0.78004375 0.73685631 0.45678716 0.94433979
 0.66034709 0.59695435 0.59259181 0.83044955 0.77883379 0.59135503
 0.83428864 0.71826733 0.59992818 0.71813756 0.55917507 0.43342655
 0.72655714 0.71610619 0.32859633 0.44676194 0.66960247 0.46241596
 0.7922747  0.90970209 0.93764353 0.51356824 0.61444089 0.44677599
 0.70932311 0.71911694 0.51687199 0.52714809 0.83168729 0.76420491
 0.43792273 0.70440812 0.66744236 0.78107805 0.84819607 0.71968367
 0.39770586 0.48790799 0.53906132 0.65337805 0.63618969 0.64334081
 0.71726429 0.57171912 0.84414411 0.43454138 0.569632   0.75837184
 0.45882101 0.40186209 0.38586431 0.60717187 0.87485903 0.46051476
 0.45888584 0.52315972 0.43249111 0.71123295 0.38410544 0.32780493
 0.58352227 0.81132759 0.68880655 0.86532371 0.72984812 0.57457246
 0.64171283 0.52529521 0.93152716 0.52173116 0.79308568 0.61428495
 0.55995209 0.80768761 0.50286066 0.81716481 0.82896536 0.68632523
 0.65917328 0.72340742 0.62587403 0.81546811 0.83209704 0.36292498
 0.62716403 0.83290289 0.49052176 0.50726509 0.5950525  0.81112055
 0.67347396 0.83826483 0.44318853 0.65426152 0.54073961 0.8852427
 0.72994919 0.49772786 0.73283229 0.81459341 0.9088262  0.79279532
 0.7081119  0.5493456  0.41178332 0.65643216 0.38702648 0.75673459
 0.48290983 0.56225015 0.36866373 0.69633155 0.82181864 0.34192264
 0.5059988  0.76937766 0.7754648  0.72661038 0.47146491 0.35407087
 0.62784177 0.94435395 0.46712949 0.48756757 0.66013336 0.43905887
 0.70334526 0.69655465 0.73874035 0.42045166 0.79959589 0.44598925
 0.44332461 0.70742149 0.5176481  0.78102971 0.39678037 0.58908181
 0.89030205 0.85965711 0.48724808 0.88527188 0.76545429 0.39361524
 0.43984537 0.62489864 0.81440483 0.59968197 0.59007719 0.79613211
 0.60499613 0.57220535 0.45639499 0.88426557 0.71139316 0.56613988
 0.60937869 0.68861419 0.63285682 0.63426023 0.71921203 0.71690296
 0.5989638  0.80015627 0.37777732 0.49915215 0.92842863 0.74598456
 0.84167027 0.57917349 0.85280794 0.4355402  0.86631328 0.6435634
 0.47923889 0.90714346 0.7821755  0.89209767 0.60309934 0.81031378
 0.4210457  0.60790313 0.49011307 0.48788427 0.8363771  0.84783324
 0.6629822  0.56275969 0.66054729 0.67213081 0.61918363 0.92099094
 0.77656355 0.82805    0.69641654 0.54833563 0.56627724 0.85219359
 0.61286051 0.82529963 0.83724212 0.83800357 0.60184028 0.50803241
 0.41465949 0.75668977 0.60906691 0.32825311 0.5210333  0.41004409
 0.62706932 0.43653    0.86057911 0.81929204 0.61482192 0.6619805
 0.34838277 0.46289811 0.81144651 0.82443    0.75486781 0.45059758
 0.91238411 0.76079248 0.74874844 0.81371637 0.3573082  0.75959661
 0.78678644 0.44784672 0.75387071 0.70613802 0.83588396 0.48397115
 0.54146454 0.39820301 0.78380012 0.75675627 0.766835   0.70740296
 0.81293431 0.80399258 0.52010665 0.67898324 0.71285455 0.63649195
 0.44260324 0.67769997 0.63043407 0.6046308  0.58516124 0.57083414
 0.63043052 0.79498703 0.31079313 0.65540799 0.65307329 0.8298415
 0.63193384 0.57132038 0.81652054 0.85615743 0.6322902  0.42922312
 0.44995402 0.64770889 0.43193358 0.78752588 0.56595116 0.6089112
 0.65154493 0.64453802 0.53307231 0.61470593 0.5444946  0.52778905
 0.82945246 0.44777067 0.84148877 0.6498149  0.78170231 0.80561485
 0.74755493 0.90464565 0.72608055 0.60859958 0.46993825 0.7745607
 0.80039422 0.47246594 0.63258656 0.68275796 0.40060233 0.84594241
 0.80210277 0.90350313 0.40320984 0.53633272 0.68198367 0.51303956
 0.69204146 0.95293467 0.74079907 0.43242923 0.94303885 0.76189313
 0.78688483 0.35705448 0.53950662 0.63747805 0.43746121 0.46966356
 0.92293975 0.46730144 0.92729106 0.33869768 0.35613214 0.43887744
 0.85479037 0.60652557 0.64175369 0.60257815 0.88258734 0.82179277
 0.52278841 0.42578911 0.55613034 0.65871657 0.41775095 0.60769461
 0.44005174 0.74158847 0.8744588  0.47119028 0.45468895 0.86879232
 0.83707638 0.33471685 0.39517815 0.55318357 0.4036053  0.5710997
 0.79028317 0.62597971 0.81034652 0.38132699 0.40358007 0.71162294
 0.58114644 0.47763492 0.36902456 0.62367687 0.83822569 0.42363115
 0.63361053 0.66340419 0.84503245 0.87192735 0.33838599 0.80171435
 0.75157991 0.73283486 0.30012097 0.8055426  0.69380487 0.43641238
 0.72556189 0.86698512 0.85619001 0.30901089 0.42970697 0.70658903
 0.58787711 0.49624478 0.69717814 0.72074494 0.74468085 0.51676613
 0.81307065 0.91815819 0.48025847 0.57292532 0.64490623 0.90301877
 0.69801054 0.73059217 0.80161575 0.78245378 0.54346814 0.75684999
 0.86169701 0.30780937 0.84343684 0.45922508 0.82275175 0.62955686
 0.66890291 0.79533248 0.59813962 0.50279843 0.32427704 0.56204881
 0.56283094 0.86287286 0.46467879 0.74128406 0.71532302 0.5008869
 0.35586859 0.90906468 0.70145069 0.86864334 0.73059217 0.45179813
 0.6768992  0.53398078 0.49787057 0.641162   0.80540546 0.89803829
 0.91462905 0.5935742  0.87898159 0.50691682 0.84832395 0.61757884
 0.41596946 0.36254346 0.65584249 0.53240492 0.79003711 0.56581324
 0.61387118 0.51107679 0.64670428 0.73464347 0.64302944 0.80774365
 0.67779825 0.83395243 0.50572418 0.34828706 0.41163336 0.56521901
 0.88012041 0.70768142 0.75527577 0.75878362 0.78867221 0.65060412
 0.80845024 0.49959542 0.80260252 0.85901738 0.36708562 0.54168318
 0.77140193 0.81767594 0.52172018 0.60074797 0.45874312 0.43090531
 0.8386842  0.51851571 0.53215127 0.54539465 0.82702179 0.45240578
 0.59825962 0.84876232 0.5399645  0.31724568 0.80405821 0.43011943
 0.36803757 0.75819671 0.55701281 0.47194677 0.90309144 0.50145937
 0.46350801 0.54266544 0.59903904 0.66622917 0.85546344 0.91790522
 0.87168643 0.55497963 0.60856397 0.36719235 0.55450836 0.79887279
 0.49522894 0.51270632 0.3309661  0.67930282 0.37711632 0.89306571
 0.80241057 0.82489481 0.85901866 0.72733274 0.36396548 0.71253856
 0.4548336  0.56372849 0.37178277 0.52659631 0.85280906 0.72327458
 0.49132392 0.93018255 0.37392359 0.39104548 0.76333226 0.81960754
 0.81587111 0.37656423 0.44212284 0.63102888 0.43649144 0.49283618
 0.81594635 0.78552985 0.43764089 0.851413   0.82336424 0.66161948
 0.45418301 0.66344939 0.50574485 0.54381875 0.37741513 0.5825568
 0.54825546 0.56169375 0.39287455 0.59698408 0.83384524 0.39277362
 0.50658763 0.86424215 0.5572055  0.74026411 0.58464266 0.57883081
 0.72819212 0.82455728 0.42483199 0.59477415 0.65901609 0.44053537
 0.51105567 0.64768881 0.67811961 0.6875384  0.66899861 0.83615629
 0.86433534 0.77839411 0.81235861 0.33862347 0.62752341 0.87880209
 0.48089706 0.64309069 0.49431921 0.63709661 0.61156306 0.78789122
 0.5252687  0.79246621 0.82879058 0.75451175 0.58345453 0.82419431
 0.82599365 0.43455597 0.58742782 0.41770594 0.84586147 0.5316289
 0.84141818 0.47055498 0.63234062 0.4511353  0.85719714 0.28050066
 0.74773533 0.34018845 0.71057529 0.64074372 0.53787853 0.73639101
 0.44401127 0.62838409 0.8607795  0.81235625 0.61423464 0.58798957
 0.66648809 0.51644219 0.46734268 0.79091429 0.59667364 0.40810981
 0.74370643 0.61070538 0.84140969 0.82564932 0.7835946  0.45922132
 0.87063579 0.8574589  0.5296772  0.92548677 0.82579738 0.91774985
 0.46126446 0.87174486 0.85361684 0.69568372 0.55111045 0.44212805
 0.43483525 0.61722785 0.68431245 0.86017333 0.8086994  0.72459773
 0.65911102 0.77423832 0.38798156 0.41516155]
Train accuracy: 0.85
Train confusion matrix:
[[130   1   3  13   1]
 [  6 130  13  10  16]
 [  4   6 113   1   5]
 [  2   1   2 106   1]
 [  9   3   3   5 116]]
Test accuracy: 0.5433333333333333
Test confusion matrix:
[[31  4  3 11  2]
 [ 5 35 18  6 16]
 [ 5 14 35  4 11]
 [ 5  0  4 35  5]
 [ 3  6  6  9 27]]

SVM_C_PARAM=2
IF_NORMALIZE_IMAGES=True
IMAGE_COUNT_PER_CLASS=200
KMEANS_BOW_FEATURES_NORMALIZATION=binary
KMEANS_CLUSTERS=sqrt_keypoints
python . svm_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting SIFT features...
Computing KMeans clusters with n_clusters=591...
Converting to binary BoW features...
DescribeResult(nobs=700, minmax=(0.2842296531187909, 0.9491344574040599), mean=0.6429581014860696, variance=0.026353655107807027, skewness=-0.11100497354266134, kurtosis=-1.0446009955165148)
Train accuracy: 0.8471428571428572
Train confusion matrix:
[[118   0   1   9   1]
 [ 10 128  15   7  20]
 [  5   4 118   0   2]
 [  2   0   2 106   3]
 [  8   4   4  10 123]]
Test accuracy: 0.5066666666666667
Test confusion matrix:
[[36  7  2 11  1]
 [ 5 27 20  4 15]
 [ 4 18 28  4  9]
 [ 7  3  4 42  7]
 [ 5  9  6  7 19]]

SVM_C_PARAM=1
IF_NORMALIZE_IMAGES=True
IMAGE_COUNT_PER_CLASS=200
KMEANS_CLUSTERS=200
KMEANS_BOW_FEATURES_NORMALIZATION=binary
python . svm_rgb_gray_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting RGB-Gray-SIFT features...
Computing KMeans clusters with n_clusters=200...
Converting to binary BoW features...
DescribeResult(nobs=700, minmax=(0.24097719748069774, 0.7819928528175433), mean=0.457951701149121, variance=0.011879299082192716, skewness=0.4838794904877015, kurtosis=-0.45426310602642506)
Train accuracy: 0.6042857142857143
Train confusion matrix:
[[83  4  4 14  7]
 [ 3 83  8  7  8]
 [16 24 88  4 29]
 [16 14 31 92 28]
 [20 13 11 16 77]]
Test accuracy: 0.38666666666666666
Test confusion matrix:
[[27  9  4 17  1]
 [12 10  4  4  9]
 [ 8 15 30  4 16]
 [12  9 17 36 12]
 [ 3 19  3  6 13]]

SVM_C_PARAM=1
IF_NORMALIZE_IMAGES=True
IMAGE_COUNT_PER_CLASS=200
KMEANS_CLUSTERS=sqrt_keypoints
KMEANS_BOW_FEATURES_NORMALIZATION=binary
python . svm_rgb_gray_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting RGB-Gray-SIFT features...
Computing KMeans clusters with n_clusters=580...
Converting to binary BoW features...
DescribeResult(nobs=700, minmax=(0.21969091947850092, 0.9217861473391137), mean=0.5164538972847144, variance=0.022548019871611955, skewness=0.7066258004324343, kurtosis=-0.1406416835818569)
Train accuracy: 0.6528571428571428
Train confusion matrix:
[[ 97   5   3  26   1]
 [ 26 104  31  23  51]
 [ 12  22 108   5  11]
 [  6   3   3  80   6]
 [  1   3   1   4  68]]
Test accuracy: 0.51
Test confusion matrix:
[[37  6  1  7  2]
 [ 9 37 11 10 29]
 [ 7 14 34 12 16]
 [ 2  1  8 32  3]
 [ 3  5  0  1 13]]

SVM_C_PARAM=1
IF_NORMALIZE_IMAGES=True
IMAGE_COUNT_PER_CLASS=400
KMEANS_CLUSTERS=sqrt_keypoints
KMEANS_BOW_FEATURES_NORMALIZATION=binary
KMEANS_MINI_BATCH_SIZE=100
python . svm_rgb_gray_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting RGB-Gray-SIFT features...
Running Mini-batch KMeans with n_clusters=825, batch_size=100...
C:\Users\yunch\Documents\projects\trash-classifier\.env\lib\site-packages\sklearn\cluster\k_means_.py:1418: RuntimeWarning: init_size=300 should be larger than k=825. Setting it to 3*k
  init_size=init_size)
Converting to binary BoW features...
DescribeResult(nobs=1400, minmax=(0.24591865862411988, 0.9821626941648179), mean=0.5625832537238165, variance=0.029880184453500862, skewness=0.4856967297303908, kurtosis=-0.6869811993990429)
Train accuracy: 0.6942857142857143
Train confusion matrix:
[[217  44  26  51  55]
 [ 20 191  28  18  32]
 [ 13  26 201   5  16]
 [ 12   5  11 193   7]
 [ 13  20  12  14 170]]
Test accuracy: 0.5283333333333333
Test confusion matrix:
[[84 27  8 28 28]
 [18 44 26  5 19]
 [ 3 18 61  7 11]
 [10  6 17 71  5]
 [10 19 10  8 57]]

SVM_C_PARAM=1
IF_NORMALIZE_IMAGES=True
IMAGE_COUNT_PER_CLASS=400
KMEANS_CLUSTERS=sqrt_keypoints
KMEANS_BOW_FEATURES_NORMALIZATION=binary
KMEANS_MINI_BATCH_SIZE=1000
python . svm_rgb_gray_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting RGB-Gray-SIFT features...
Running Mini-batch KMeans with n_clusters=846, batch_size=1000...
Converting to binary BoW features...
DescribeResult(nobs=1400, minmax=(0.23808998455720792, 0.9901313492448762), mean=0.6868624473527686, variance=0.0330888617313824, skewness=-0.3549139270128284, kurtosis=-1.0359023482320038)
Train accuracy: 0.8235714285714286
Train confusion matrix:
[[251  12   6  40  29]
 [ 14 247  33  13  37]
 [  7  15 237   4   8]
 [  4   4   1 227   5]
 [  6   1   3   5 191]]
Test accuracy: 0.6
Test confusion matrix:
[[88  9  7 26 11]
 [15 77 34 10 41]
 [ 4 21 68  5 15]
 [ 7  3  5 67  3]
 [ 4 11  6  3 60]]

SVM_C_PARAM=1
IF_NORMALIZE_IMAGES=True
IMAGE_COUNT_PER_CLASS=400
KMEANS_CLUSTERS=sqrt_keypoints
KMEANS_BOW_FEATURES_NORMALIZATION=binary
KMEANS_MINI_BATCH_SIZE=10000
python . svm_rgb_gray_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting RGB-Gray-SIFT features...
Running Mini-batch KMeans with n_clusters=834, batch_size=10000...
Converting to binary BoW features...
DescribeResult(nobs=1400, minmax=(0.2523811587439512, 0.9920379206180834), mean=0.6983521919347657, variance=0.03401277103415359, skewness=-0.36931999467844795, kurtosis=-1.0069815019282493)
Train accuracy: 0.8342857142857143
Train confusion matrix:
[[262  17   5  48  34]
 [  7 249  23  10  34]
 [  5  10 236   3   5]
 [  6   1   4 234   4]
 [  6   2   5   3 187]]
Test accuracy: 0.6066666666666667
Test confusion matrix:
[[86 11  4 22 16]
 [ 9 77 27  8 38]
 [ 6 20 77  5 16]
 [10  3  9 63  5]
 [ 3 10 10  4 61]]

SVM_C_PARAM=100
IF_NORMALIZE_IMAGES=True
IMAGE_COUNT_PER_CLASS=400
KMEANS_CLUSTERS=sqrt_keypoints
KMEANS_BOW_FEATURES_NORMALIZATION=l1
KMEANS_MINI_BATCH_SIZE=10000
python . svm_rgb_gray_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting RGB-Gray-SIFT features...
Running Mini-batch KMeans with n_clusters=838, batch_size=10000...
L1 normalizing BoW features...
DescribeResult(nobs=1400, minmax=(0.21286870969935912, 0.9999998008039654), mean=0.4535569317566832, variance=0.03400515231441816, skewness=1.6316241447709987, kurtosis=1.904880215190829)
Train accuracy: 0.48428571428571426
Train confusion matrix:
[[ 92   0   2  18   2]
 [158 247 167 122 148]
 [  5   8  90   8   5]
 [ 12   3  10 126   2]
 [  5  15  19  13 123]]
Test accuracy: 0.43666666666666665
Test confusion matrix:
[[ 33   0   0   5   0]
 [ 84 105  71  49  70]
 [  1   7  28   6   2]
 [  3   1   2  48   0]
 [  7  14  11   5  48]]

SVM_C_PARAM=500
IF_NORMALIZE_IMAGES=True
IMAGE_COUNT_PER_CLASS=400
KMEANS_CLUSTERS=sqrt_keypoints
KMEANS_BOW_FEATURES_NORMALIZATION=l1
KMEANS_MINI_BATCH_SIZE=10000
python . svm_rgb_gray_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting RGB-Gray-SIFT features...
Running Mini-batch KMeans with n_clusters=841, batch_size=10000...
L1 normalizing BoW features...
DescribeResult(nobs=1400, minmax=(0.24157343237380421, 0.9999999497099284), mean=0.6041095490550177, variance=0.0459123573937432, skewness=0.44237746868858685, kurtosis=-1.0919161230408452)
Train accuracy: 0.665
Train confusion matrix:
[[179   1   4  36  10]
 [ 84 263 103  67 104]
 [  9   8 164   5   5]
 [  3   3   4 171   3]
 [  4   6   9   1 154]]
Test accuracy: 0.5766666666666667
Test confusion matrix:
[[79  4  4 24  9]
 [31 99 55 29 51]
 [ 3  7 53  3  4]
 [ 4  0  0 57  2]
 [ 4  9  4  7 58]]

SVM_C_PARAM=1000
IF_NORMALIZE_IMAGES=True
IMAGE_COUNT_PER_CLASS=400
KMEANS_CLUSTERS=sqrt_keypoints
KMEANS_BOW_FEATURES_NORMALIZATION=l1
KMEANS_MINI_BATCH_SIZE=10000
python . svm_rgb_gray_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting RGB-Gray-SIFT features...
Running Mini-batch KMeans with n_clusters=837, batch_size=10000...
L1 normalizing BoW features...
DescribeResult(nobs=1400, minmax=(0.2572687353942731, 0.9999999652704074), mean=0.672564398322111, variance=0.04388613593904426, skewness=-0.010450639209364329, kurtosis=-1.3078856780709853)
Train accuracy: 0.755
Train confusion matrix:
[[216   5   5  23  13]
 [ 57 250  73  52  74]
 [  5   8 196   0   5]
 [  2   4   3 215   4]
 [  2   5   2   1 180]]
Test accuracy: 0.6
Test confusion matrix:
[[68  3  2 14  5]
 [38 97 42 24 46]
 [ 4 14 68  1 11]
 [ 4  1  2 69  4]
 [ 4 13  7  1 58]]

SVM_C_PARAM=1500
IF_NORMALIZE_IMAGES=True
IMAGE_COUNT_PER_CLASS=400
KMEANS_CLUSTERS=sqrt_keypoints
KMEANS_BOW_FEATURES_NORMALIZATION=l1
KMEANS_MINI_BATCH_SIZE=10000
python . svm_rgb_gray_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting RGB-Gray-SIFT features...
Running Mini-batch KMeans with n_clusters=836, batch_size=10000...
L1 normalizing BoW features...
DescribeResult(nobs=1400, minmax=(0.2620480402379643, 0.9999999358328169), mean=0.6620634064872339, variance=0.03880644729485464, skewness=0.004694050819582416, kurtosis=-1.148620203043049)
Train accuracy: 0.7871428571428571
Train confusion matrix:
[[241   9   8  31   8]
 [ 45 262  59  35  75]
 [  3   5 201   2   3]
 [  2   2   0 213   0]
 [  1   3   6   1 185]]
Test accuracy: 0.61
Test confusion matrix:
[[75  6  4 22  8]
 [20 98 43 17 52]
 [ 4  9 69  6 10]
 [ 7  1  4 71  6]
 [ 2  5  6  2 53]]

SVM_C_PARAM=1000
SVM_GAMMA_PARM=0.0001
IF_NORMALIZE_IMAGES=True
IMAGE_COUNT_PER_CLASS=400
KMEANS_CLUSTERS=sqrt_keypoints
KMEANS_BOW_FEATURES_NORMALIZATION=l1
KMEANS_MINI_BATCH_SIZE=10000
python . svm_rgb_gray_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting RGB-Gray-SIFT features...
Running Mini-batch KMeans with n_clusters=831, batch_size=10000...
L1 normalizing BoW features...
DescribeResult(nobs=1400, minmax=(0.21851515831474258, 0.9999999128438503), mean=0.4577472850416494, variance=0.03488983670108095, skewness=1.599781594649459, kurtosis=1.7278384511191645)
Train accuracy: 0.44857142857142857
Train confusion matrix:
[[ 83   0   2  16   0]
 [184 261 179 123 165]
 [  1   4  48   6   0]
 [ 11   2  10 125   4]
 [  9  19  25  12 111]]
Test accuracy: 0.3983333333333333
Test confusion matrix:
[[32  0  0  3  5]
 [72 98 83 62 71]
 [ 0  1 21  2  1]
 [ 2  1  6 45  0]
 [ 6 14 26  6 43]]

SVM_C_PARAM=1000 
KMEANS_BOW_FEATURES_NORMALIZATION=l1 
KMEANS_CLUSTERS=average_keypoints 
KMEANS_JOBS=2 
SVM_GAMMA_PARAM=0.5 
IMAGE_COUNT_PER_CLASS=400 
python . svm_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting SIFT features...
Computing KMeans clusters with n_clusters=485...
L1 normalizing BoW features...
DescribeResult(nobs=1400, minmax=(0.25930951615299619, 0.99870143885131224), mean=0.53991512673170716, variance=0.027832634951104305, skewness=1.0078105795605872, kurtosis=0.1699703057177544)
Train accuracy: 0.990714285714
Train confusion matrix:
[[278   0   0   0   0]
 [  0 282   1   0   0]
 [  0   0 277   0   0]
 [  1   0   0 268   0]
 [  5   1   0   5 282]]
Test accuracy: 0.568333333333
Test confusion matrix:
[[73 13  6 25 12]
 [12 65 24 19 25]
 [ 7 15 74  7 14]
 [10  6  7 68  6]
 [14 18 11  8 61]]

IF_NORMALIZE_IMAGES=True 
SVM_C_PARAM=4 
KMEANS_BOW_FEATURES_NORMALIZATION=binary 
KMEANS_CLUSTERS=sqrt_keypoints 
KMEANS_JOBS=2 
IMAGE_COUNT_PER_CLASS=400 
python . svm_rgb_gray_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting RGB-Gray-SIFT features...
Computing KMeans clusters with n_clusters=841...
Converting to binary BoW features...
DescribeResult(nobs=1400, minmax=(0.26740413767517063, 0.98881311788332082), mean=0.77270414876479943, variance=0.026516751129717162, skewness=-1.1713420141195199, kurtosis=0.5017481081389699)
Train accuracy: 0.933571428571
Train confusion matrix:
[[276  10   3  17  13]
 [  2 260   9   1   9]
 [  1   3 261   2   1]
 [  1   0   1 265   1]
 [  7   3   2   7 245]]
Test accuracy: 0.563333333333
Test confusion matrix:
[[80 18 11 19 10]
 [ 7 56 22  6 30]
 [ 9 17 70  9 16]
 [ 9 11 10 69 12]
 [ 8 22 11  5 63]]

SVM_C_PARAM=4 
KMEANS_BOW_FEATURES_NORMALIZATION=binary 
KMEANS_CLUSTERS=sqrt_keypoints 
KMEANS_JOBS=2 
IMAGE_COUNT_PER_CLASS=400  
python . svm_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting SIFT features...
Computing KMeans clusters with n_clusters=842...
Converting to binary BoW features...
DescribeResult(nobs=1400, minmax=(0.26808637758243131, 0.98793204191823347), mean=0.74423334077537906, variance=0.028821079174821452, skewness=-0.978301186868331, kurtosis=-0.09285262362595814)
Train accuracy: 0.907857142857
Train confusion matrix:
[[266   9   6  19  11]
 [  9 228  11  10  20]
 [  6   4 271   1   3]
 [  1   3   0 261   2]
 [  4   5   2   3 245]]
Test accuracy: 0.596666666667
Test confusion matrix:
[[83 18  9 22 11]
 [10 74 16  3 27]
 [ 4 26 69  3 13]
 [ 9 12  4 69  5]
 [ 8 21 12  9 63]]


SVM_C_PARAM=4 
KMEANS_BOW_FEATURES_NORMALIZATION=binary 
KMEANS_CLUSTERS=400 
KMEANS_JOBS=2 
IMAGE_COUNT_PER_CLASS=400 
python . svm_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting SIFT features...
Computing KMeans clusters with n_clusters=400...
Converting to binary BoW features...
DescribeResult(nobs=1400, minmax=(0.27703471857845896, 0.98172015131567636), mean=0.69780074682575566, variance=0.023149063313400629, skewness=-0.6639056303767775, kurtosis=-0.38520833020510636)
Train accuracy: 0.893571428571
Train confusion matrix:
[[247   5   2   8   9]
 [ 11 268  10  13  27]
 [  5  15 256   1   5]
 [  9   2   8 254   3]
 [  7   3   3   3 226]]
Test accuracy: 0.583333333333
Test confusion matrix:
[[75 10  4 14 13]
 [18 59 28 12 35]
 [ 4 16 69  3  8]
 [18  7 11 82  9]
 [ 6 15  9 10 65]]

SVM_C_PARAM=4 
KMEANS_BOW_FEATURES_NORMALIZATION=binary 
KMEANS_CLUSTERS=average_keypoints 
KMEANS_JOBS=2 
IMAGE_COUNT_PER_CLASS=400 
python . svm_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting SIFT features...
Computing KMeans clusters with n_clusters=489...
Converting to binary BoW features...
DescribeResult(nobs=1400, minmax=(0.28584953410236019, 0.98279416008255094), mean=0.71707721772122668, variance=0.024508736887037235, skewness=-0.8315879097497484, kurtosis=-0.1689629865631419)
Train accuracy: 0.896428571429
Train confusion matrix:
[[259   7   3  18  13]
 [ 12 262  16   8  27]
 [  3  10 251   3   4]
 [  4   6   0 253   2]
 [  5   1   2   1 230]]
Test accuracy: 0.596666666667
Test confusion matrix:
[[81  9 10 16  9]
 [ 7 59 22  4 31]
 [ 8 19 76  8 13]
 [11  8  4 81 10]
 [10 19 16  8 61]]


SVM_C_PARAM=1 
KMEANS_BOW_FEATURES_NORMALIZATION=binary 
KMEANS_CLUSTERS=average_keypoints 
KMEANS_JOBS=2 
IMAGE_COUNT_PER_CLASS=400 
python . svm_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting SIFT features...
Computing KMeans clusters with n_clusters=472...
Converting to binary BoW features...
DescribeResult(nobs=1400, minmax=(0.25405286751896428, 0.96763170165477541), mean=0.5996452045101841, variance=0.027979054052683291, skewness=0.1245238646126458, kurtosis=-1.046742266971236)
Train accuracy: 0.702142857143
Train confusion matrix:
[[250  28  20  66  40]
 [ 12 213  38  13  49]
 [ 11  26 188   9  10]
 [ 16  11  14 161  13]
 [  8  12  10  11 171]]
Test accuracy: 0.538333333333
Test confusion matrix:
[[75 12  9 35 22]
 [14 61 28 10 25]
 [ 5 20 63 12 12]
 [ 5  4 19 71  5]
 [ 4 13 11 12 53]]

SVM_C_PARAM=1000 
IF_NORMALIZE_IMAGES=True 
KMEANS_CLUSTERS=sqrt_keypoints 
KMEANS_JOBS=2 
KMEANS_BOW_FEATURES_NORMALIZATION=l1 
IMAGE_COUNT_PER_CLASS=400 
python . svm_rgb_gray_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting RGB-Gray-SIFT features...
Computing KMeans clusters with n_clusters=834...
L1 normalizing BoW features...
DescribeResult(nobs=1400, minmax=(0.24156007784547562, 0.99999996230060073), mean=0.65577758240895456, variance=0.04519302041632664, skewness=0.10376775277068029, kurtosis=-1.3061819551698441)
Train accuracy: 0.736428571429
Train confusion matrix:
[[209   4   2  27  10]
 [ 59 267  82  51  88]
 [  4   7 183   2   4]
 [  3   1   5 207   5]
 [  3   8   3   1 165]]
Test accuracy: 0.591666666667
Test confusion matrix:
[[71  1  2 13 11]
 [35 92 46 27 42]
 [ 5 11 70  5  8]
 [ 9  4  2 65 10]
 [ 2  5  5  2 57]]

SVM_C_PARAM=1500 
SVM_GAMMA_PARAM=0.5 
KMEANS_CLUSTERS=sqrt_keypoints 
KMEANS_JOBS=4 
KMEANS_BOW_FEATURES_NORMALIZATION=l1 
IMAGE_COUNT_PER_CLASS=400 
python . svm_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting SIFT features...
Computing KMeans clusters with n_clusters=831...
L1 normalizing BoW features...
DescribeResult(nobs=1400, minmax=(0.27963990963860746, 0.9966370944742583), mean=0.57788656461224042, variance=0.021361074655666466, skewness=0.8496573111878325, kurtosis=-0.015913216411859832)
Train accuracy: 0.997142857143
Train confusion matrix:
[[286   0   0   0   0]
 [  0 276   1   0   0]
 [  0   0 273   0   0]
 [  0   0   0 276   0]
 [  2   1   0   0 285]]
Test accuracy: 0.531666666667
Test confusion matrix:
[[68 12 10 25 12]
 [11 52 26 13 23]
 [13 28 77 14 17]
 [11  7  2 67  8]
 [ 9 24 11  5 55]]

SVM_C_PARAM=1000
SVM_GAMMA_PARAM=0.5
KMEANS_BOW_FEATURES_NORMALIZATION=l1
KMEANS_CLUSTERS=sqrt_keypoints
KMEANS_JOBS=2
IMAGE_COUNT_PER_CLASS=400
python . svm_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting SIFT features...
Computing KMeans clusters with n_clusters=822...
L1 normalizing BoW features...
DescribeResult(nobs=1400, minmax=(0.29561439202474732, 0.9945528778580508), mean=0.58602761104296175, variance=0.020524884953576246, skewness=0.8031675778075706, kurtosis=-0.13170298071266817)
Train accuracy: 0.995714285714
Train confusion matrix:
[[270   0   0   0   0]
 [  0 287   0   0   0]
 [  0   0 293   0   0]
 [  0   0   0 259   0]
 [  3   0   0   3 285]]
Test accuracy: 0.556666666667
Test confusion matrix:
[[65  8 11 17  7]
 [21 59 10 13 29]
 [10 19 65 10 19]
 [16  8  6 89  4]
 [15 19 15  9 56]]

SVM_C_PARAM=4
SVM_GAMMA_PARAM=0.5
KMEANS_BOW_FEATURES_NORMALIZATION=l1
KMEANS_CLUSTERS=sqrt_keypoints
KMEANS_JOBS=2
IMAGE_COUNT_PER_CLASS=400
python . svm_sift_kmeans
Loading image data...
Splitting dataset to train & test set with test_set_ratio=0.3...
Extracting features for train & test set...
Extracting SIFT features...
Computing KMeans clusters with n_clusters=821...
L1 normalizing BoW features...
DescribeResult(nobs=1400, minmax=(0.28602250649969252, 0.99878520981211405), mean=0.7066022446895841, variance=0.038814829435717887, skewness=-0.25492593091827304, kurtosis=-1.248511435986818)
Train accuracy: 0.805
Train confusion matrix:
[[231   2   2  13   6]
 [ 49 275  62  46  67]
 [  6   1 208   3   2]
 [  0   0   0 209   3]
 [  2   4   5   0 204]]
Test accuracy: 0.588333333333
Test confusion matrix:
[[75  6  5 15  4]
 [21 82 41 29 46]
 [ 3 11 67  8  9]
 [10  1  6 72  2]
 [ 3 18  4  5 57]]
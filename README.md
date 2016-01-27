# Goal

- proof of concept to solve a Captcha which seems to be very easy
- properties of the Captcha
  - fixed number of letters
  - noise in a different color
  - letters are well separated

# Steps

## Download catpchas

## Segmentation of captchas

view:
bin/segment.py file1 file2 ...

batch processing:
bin/segment.py --out data/segmentations/ data/captchas/*

## Solve captchas manually

Start server: `python3 bin/solve.py --segmentations data/segmentations/ --db data/solutions.txt`

Open web browser: `http://localhost:8000`

Solve the captchas...

## Create a dataset from the labeled captchas

bin/build_dataset.py --labeled data/solutions.txt --captchapath data/captchas/ --out-labels data/labels.txt --out-matrix data/features.txt --out-labelmap data/labelmap.txt

## Cross validation on dataset

bin/knn.py -i data/features.txt --labels data/labels.txt

## One captcha

bin/captcha_as_matrix.py data/captchas/captcha.1437908702.31160.jpg > m.txt
cat m.txt | bin/predict.py --features data/features.txt --labels data/labels.txt --labelmap data/labelmap.txt

# Data

- data/captchas: Captchas downloaded via a script
- data/selected_captchas: some Captchas from data/captchas for testing
- TODO

# Tasks

- [x] get captchas
- [ ] image segmentation
  - [x] implement segmentation algorithm
  - [x] reorganize the code
  - [ ] estimate the accuracy of segmentation
- [x] webserver
  - [x] one URL which delivers captchas
  - [x] one URL to post the solutions to the captchas
- [ ] do manual labeling via webserver
- [x] build a dataset from the labeled captchas
  - for each labeled image
    - [x] extract letters
    - [x] normalize the letters (i.e. fixed width and height)
    - [x] build a feature vector
  - [x] create a matrix of feature vectors
- [x] implement a classification algorithm
- [x] implement cross validation
- [ ] optimize the parameters with cross validation
- [ ] online attack! ;)

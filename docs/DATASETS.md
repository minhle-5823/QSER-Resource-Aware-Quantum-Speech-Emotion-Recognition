# Datasets and redistribution

This repository **does not** redistribute original audio files or `.npy` feature caches.

## RAVDESS

Official archive: https://zenodo.org/records/1188976

The dataset creators license RAVDESS under **CC BY-NC-SA 4.0**; review the source and its license before downloading, modifying, or redistributing the content. The manuscript uses a deduplicated set of 1,440 speech utterances. The main experiment uses speaker-independent (actor-disjoint) splits.

## CMU-MOSEI

Official page: https://multicomp.cs.cmu.edu/resources/cmu-mosei-dataset/  
SDK: https://github.com/CMU-MultiComp-Lab/CMU-MultimodalSDK

The accepted manuscript's supplementary cross-corpus arm maps six emotions (happy, sad, anger, surprise, disgust, fear) and preserves source-video separation; these are audio-only derived comparisons, **not a claim about end-to-end multimodal performance**. Follow the CMU dataset's access and redistribution terms.

## Feature extraction

The manuscript describes 206 acoustic descriptors built with `librosa`, 16-kHz mono conversion, and 4-second pad/crop. Full extraction and model-training implementation is **not present** in the supplied archive and is **not reproduced** in this repository. See `REPRODUCIBILITY.md`.

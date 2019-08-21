# library.qai.spacy
Customized SpaCy pipeline

## Installing
```sh
$ pip install -e git+https://github.com/Qordobacode/library.qai.spacy.git@master#egg=en_qai_sm
> installs the package and deps from master branch of qai.spacy
```
## Usage
```python
import spacy
nlp = spacy.load('en_qai_sm')
```
## About SpaCy pipelines:

Default spaCy pipeline consists of 4 steps (components):

![spaCy pipeline](img/pipeline.png)

- `tokenizer` - splits text into tokens
- `tagger` - assigns part-of-speech tags
- `parser` - assigns dependency labels
- `ner` - detects and label named entities

Custom components (ex. any functions on `doc`) can be inserted into the pipeline (at any place after the `tokenizer`. For simplicity, `tokenizer` is not listed in pipelines descriptions.)

Reference: [spaCy docs](https://spacy.io/usage/processing-pipelines).

## Pipeline components:

### v1.0.0

The pipeline consists of:
```python
pipeline = [
    "merge_matcher",
    "tagger",
    "parser",
    "ner"
    ]
```
where ```merge_matcher``` matches and merges into 1 token spans of type:
- connected by 1 hyphen ex.  ```rock-hard```
- contractions ex. ```don't```
- special (informal) short forms ex. ```gonna```

## Todo:
- export merging patterns to ```patterns.json``` (currently in ```__init__.py```)

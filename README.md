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
- connected by hyphens ex.  ```state-of-the-art```
- contractions ex. ```don't```
- special (informal) short forms ex. ```gonna```

## Todo:
- export merging patterns to ```patterns.json``` (currently in ```__init__.py```)

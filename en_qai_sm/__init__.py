from __future__ import unicode_literals

from pathlib import Path
from spacy.util import load_model_from_init_py, get_model_meta
from spacy.language import Language
from spacy.tokens import Span
from spacy.matcher import Matcher


__version__ = get_model_meta(Path(__file__).parent)['version']


def load(**overrides):
    Language.factories['merge_matcher'] = lambda nlp, **cfg: MergeMatcher(nlp, **cfg)
    return load_model_from_init_py(__file__, **overrides)


class MergeMatcher(object):
    name = 'merge_matcher'

    def __init__(self, nlp, **cfg):
        self.matcher = Matcher(nlp.vocab)
        self.matcher.add('HYPENS', None, [{'IS_ALPHA': True},{'ORTH': '-'},{'IS_ALPHA': True}])
        self.matcher.add('CONTR1', None, [{'PRON': True},{'ORTH': '\'m'}])
        self.matcher.add('CONTR2', None, [{'PRON': True},{'ORTH': '\'s'}])
        self.matcher.add('CONTR3', None, [{'PRON': True},{'ORTH': '\'d'}])
        self.matcher.add('CONTR4', None, [{'PRON': True},{'ORTH': '\'ve'}])
        self.matcher.add('CONTR5', None, [{'PRON': True},{'ORTH': '\'re'}])
        self.matcher.add('CONTR6', None, [{'PRON': True},{'ORTH': '\'ll'}])
        self.matcher.add('CONTR7', None, [{'VERB': True},{'ORTH': 'n\'t'}])
        self.matcher.add('CONTR8', None, [{'IS_ALPHA': True},{'ORTH': 'n\'t'}, {'ORTH': '\'ve'}])
        self.matcher.add('CONTR9', None, [{'IS_ALPHA': True},{'ORTH': '\'d'}, {'ORTH': '\'ve'}])
        self.matcher.add('SPECIAL1', None, [{'ORTH': 'gon'}, {'ORTH': 'na'}])
        self.matcher.add('SPECIAL2', None, [{'ORTH': 'got'}, {'ORTH': 'ta'}])
        self.matcher.add('SPECIAL3', None, [{'ORTH': 'y\''}, {'ORTH': 'all'}])

    def __call__(self, doc):
        matched_spans = []
        matches = self.matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            matched_spans.append(span)
        for span in matched_spans:
            span.merge()
        return doc
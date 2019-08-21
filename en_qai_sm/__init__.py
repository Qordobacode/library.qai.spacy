from __future__ import unicode_literals

import json
from pathlib import Path

from spacy.language import Language
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy.util import get_model_meta, load_model_from_init_py

__version__ = get_model_meta(Path(__file__).parent)["version"]


def load(**overrides):
    Language.factories["merge_matcher"] = lambda nlp, **cfg: MergeMatcher(nlp, **cfg)
    return load_model_from_init_py(__file__, **overrides)


class MergeMatcher(object):
    name = "merge_matcher"

    def __init__(self, nlp, **cfg):
        self.patterns_file = "patterns.json"
        self.matcher = Matcher(nlp.vocab)

    def __call__(self, doc):
        matched_spans = []
        matches = self.matcher(doc)
        for _, start, end in matches:
            span = doc[start:end]
            matched_spans.append(span)
        for span in matched_spans:
            span.merge()
        return doc

    def from_disk(self, path, **cfg):
        patterns_path = path / self.patterns_file
        with open(patterns_path, "r", encoding="utf8") as f:
            self.patterns = json.load(f)
            for label, pattern in self.patterns.items():
                self.matcher.add(label, None, pattern)
        return self

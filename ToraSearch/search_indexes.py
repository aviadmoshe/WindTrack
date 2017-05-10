import datetime
from haystack import indexes
from ToraSearch.models import UpLoadToraText


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='yeshiva')
    pub_date = indexes.DateTimeField(model_attr='date')
    # We add this for autocomplete.
    title_auto = indexes.EdgeNgramField(model_attr='title')
    text_auto = indexes.EdgeNgramField(model_attr='text')

    def get_model(self):
        return UpLoadToraText

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
        #filter(pub_date__lte=datetime.datetime.now())
import typecheck
import fellow


@fellow.app.task(name="mr.top100_words_simple_plain")
@typecheck.returns("100 * (string, count)")
def top100_words_simple_plain():
    return [("the", 1586419)] * 100

@fellow.app.task(name="mr.top100_words_simple_text")
@typecheck.returns("100 * (string, count)")
def top100_words_simple_text():
    return [("the", 1577579)] * 100

@fellow.app.task(name="mr.top100_words_simple_no_metadata")
@typecheck.returns("100 * (string, count)")
def top100_words_simple_no_metadata():
    return [("the", 1427342)] * 100


languages = ["simple", "thai"]
ngrams = [1, 2, 3]
keys = [language + str(ngram) for language in languages
                              for ngram in ngrams]  # noqa

@fellow.app.task(name="mr.wikipedia_entropy")
@typecheck.returns_dict("number", keys)
def wikipedia_entropy():
    return {"simple1": 1.,
            "simple2": 1.,
            "simple3": 1.,
            "thai1": 1.,
            "thai2": 1.,
            "thai3": 1.}

keys = ["count", "mean", "stdev", "25%", "median", "75%"]
@fellow.app.task(name="mr.link_stats_simple")
@typecheck.returns_dict("number", keys)
def link_stats_simple():
    return {"count": 0.,
            "mean": 0.,
            "stdev": 0.,
            "25%": 0.,
            "median": 0.,
            "75%": 0.}

@fellow.app.task(name="mr.link_stats_english")
@typecheck.returns_dict("number", keys)
def link_stats_english():
    return {"count": 0.,
            "mean": 0.,
            "stdev": 0.,
            "25%": 0.,
            "median": 0.,
            "75%": 0.}

@fellow.app.task(name="mr.double_link")
@typecheck.returns("100 * ((string, string), number)")
def double_link_stats():
    return [(("idaho", "list of cities in idaho"), 0.055922694796753325)] * 100

def search_till(to_search_from, to_search_for, to_return_till):
    words = to_search_from.split()
    try:
        return " ".join(words[words.index(to_search_for) : words.index(to_return_till)])
    except:
        return None
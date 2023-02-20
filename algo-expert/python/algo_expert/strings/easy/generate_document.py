def generate_document(characters: str, document: str) -> bool:
    if len(characters) < len(document):
        return False
    array = [x for x in characters]
    for c in document:
        try:
            array.remove(c)
        except ValueError:
            return False
    return True

def transposeDictionary(scriptByExtension):
    return [*zip(sorted(scriptByExtension.values()),sorted(scriptByExtension,key=scriptByExtension.get))]

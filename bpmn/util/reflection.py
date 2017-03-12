

def get_all_subclasses_for_class(cls):
    direct_subclasses = cls.__subclasses__()
    all_subclasses = direct_subclasses
    map(lambda subclass_list: all_subclasses.extend(subclass_list)
        , [get_all_subclasses_for_class(subclass) for subclass in direct_subclasses])
    ret = []
    map(lambda c: ret.append(c) if c not in ret else None, all_subclasses)
    return ret
